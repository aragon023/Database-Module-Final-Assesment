import os
import random
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

# Flask Admin Setup
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from markupsafe import Markup


# Load environment variables
load_dotenv()

app = Flask(__name__)

if os.getenv("FLASK_ENV") == "production" or os.getenv("RENDER"):
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )

# Prefer DATABASE_URL (Render), fallback to LOCAL_DATABASE_URL (Local)
db_url = os.getenv("DATABASE_URL") or os.getenv("LOCAL_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev")

# Initialize DB
db = SQLAlchemy(app)

# Enable Alembic/Flask-Migrate
migrate = Migrate(app, db)

# Import models after db is created
from models import Article, Comment, User

# ---- Auth & CSRF setup ----
login_manager = LoginManager(app)
login_manager.login_view = "login"

csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def inject_csrf():
    return dict(csrf_token=generate_csrf)

# ---- Login Form ----
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])  # template will render as password field


# Flask-Admin setup
class SecureModelView(ModelView):
    # gate admin behind login; keep public site untouched
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin 
    def inaccessible_callback(self, name, **kwargs):
        from flask import redirect, url_for
        return redirect(url_for("login"))

class ArticleAdmin(SecureModelView):
    # show useful columns + a tiny image preview (URL-based)
    column_list = ["title", "tag", "published_on", "author", "slug", "image_preview"]
    column_searchable_list = ["title", "summary", "content", "slug", "tag", "author"]
    column_filters = ["tag", "published_on"]
    form_excluded_columns = ["comments"]  # relationship

    # simple preview column (doesn't alter your public templates)
    def _image_preview(view, context, model, name):
        if not model.image:
            return ""
        src = model.image
        # works with both full URLs and static-relative paths
        if not src.startswith("http"):
            from flask import url_for
            src = url_for("static", filename=src)
        return Markup(f'<img src="{src}" style="height:40px;object-fit:cover;border-radius:4px;">')
    column_formatters = {"image_preview": _image_preview}

    # auto-slug if empty
    def on_model_change(self, form, model, is_created):
        import re
        if (not getattr(model, "slug", None)) and getattr(model, "title", None):
            s = re.sub(r"[^\w\s-]", "", model.title).strip().lower()
            model.slug = re.sub(r"[-\s]+", "-", s)

admin = Admin(app, name="Admin", template_mode="bootstrap4", url="/admin")
admin.add_view(ArticleAdmin(Article, db.session))
admin.add_view(SecureModelView(Comment, db.session))
admin.add_view(SecureModelView(User, db.session))


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

# ---- Admin Auth Routes ----
@app.route("/admin/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.index"))  # go to Flask-Admin dashboard
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data.strip()).first()
        if u and u.check_password(form.password.data):
            login_user(u)
            return redirect(url_for("admin.index"))
        return render_template("admin/login.html", form=form, error="Invalid credentials")
    return render_template("admin/login.html", form=form)

@app.route("/admin/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# ------------- ENTRYPOINT -----------------
if __name__ == "__main__":
    app.run(debug=True)
