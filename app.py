from flask import Flask, render_template, request, redirect, url_for
from project_data import projects_list  # This imports the projects list
from articles_data import db, Article, Comment
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

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
    return render_template("projects.html", projects=projects_list)

# Tools Page
@app.route("/tools")
def tools():
    return render_template("tools.html")

# Articles List Page
@app.route("/articles")
def articles():
    articles_list = Article.query.all()
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
    return render_template('article_detail.html', article=article, comments=comments)


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Run App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
