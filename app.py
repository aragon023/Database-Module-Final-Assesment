import os
import random
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Prefer DATABASE_URL (Render), fallback to LOCAL_DATABASE_URL (local dev)
db_url = os.getenv("DATABASE_URL") or os.getenv("LOCAL_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev")

# Initialize DB
db = SQLAlchemy(app)

# Enable Alembic/Flask-Migrate
migrate = Migrate(app, db)

# Import models after db is created
from models import Article, Comment


# ----------------- ROUTES -----------------

# Home Page
@app.route('/')
def index():
    all_articles = Article.query.all()
    featured_articles = random.sample(all_articles, min(3, len(all_articles)))
    return render_template("index.html", featured_articles=featured_articles)

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Projects Page
@app.route("/projects")
def projects():
    from project_data import projects_list   # still static data for now
    return render_template("projects.html", projects=projects_list)

# Tools Page
@app.route("/tools")
def tools():
    return render_template("tools.html")

# Articles List Page
@app.route("/articles")
def articles():
    articles_list = Article.query.order_by(Article.published_on.desc()).all()
    return render_template("articles.html", articles=articles_list)

# Single Article + Comments
@app.route('/articles/<slug>', methods=['GET', 'POST'])
def article_detail(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()

    # Handle comment submission
    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']

        new_comment = Comment(
            article_id=article.id,
            name=name,
            content=content
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('article_detail', slug=slug))

    comments = Comment.query.filter_by(article_id=article.id).order_by(Comment.created_at.desc()).all()
    return render_template("article_detail.html", article=article, comments=comments)

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# ------------- ENTRYPOINT -----------------
if __name__ == "__main__":
    app.run(debug=True)
