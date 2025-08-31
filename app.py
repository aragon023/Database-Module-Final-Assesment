# --- Core imports ---
import os, random
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv


# --- Admin / Auth / Forms ---
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink  
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf import CSRFProtect, FlaskForm
from flask_wtf.csrf import generate_csrf
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from markupsafe import Markup

# --- Load env ---
load_dotenv()
app = Flask(__name__)

# --- Secure cookies in prod ---
if os.getenv("FLASK_ENV") == "production" or os.getenv("RENDER"):
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )

# --- DB setup ---
db_url = os.getenv("DATABASE_URL") or os.getenv("LOCAL_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# --- Import models (AFTER db is ready) ---
from models import Article, Comment, User

# --- Auth & CSRF setup ---
login_manager = LoginManager(app)
login_manager.login_view = "login"

csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def inject_csrf():
    return dict(csrf_token=generate_csrf)

# --- Forms ---
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

# --- Flask-Admin setup ---
class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))

class ArticleAdmin(SecureModelView):
    column_list = ["title", "tag", "published_on", "author", "slug", "image_preview"]
    column_searchable_list = ["title", "summary", "content", "slug", "tag", "author"]
    column_filters = ["tag", "published_on"]
    form_excluded_columns = ["comments"]

    def _image_preview(view, context, model, name):
        if not model.image: return ""
        src = model.image
        if not src.startswith("http"):
            src = url_for("static", filename=src)
        return Markup(f'<img src="{src}" style="height:40px;object-fit:cover;border-radius:4px;">')
    column_formatters = {"image_preview": _image_preview}

    def on_model_change(self, form, model, is_created):
        import re
        if not model.slug and model.title:
            s = re.sub(r"[^\w\s-]", "", model.title).strip().lower()
            model.slug = re.sub(r"[-\s]+", "-", s)

admin = Admin(app, name="Admin", template_mode="bootstrap4", url="/admin")

# Exempt Flask-Admin blueprint from CSRF (its forms don't include Flask-WTF tokens)
admin_bp = app.blueprints.get("admin")  # blueprint name is "admin" by default
if admin_bp:
    csrf.exempt(admin_bp)

admin.add_view(ArticleAdmin(Article, db.session))
admin.add_view(SecureModelView(Comment, db.session))
admin.add_view(SecureModelView(User, db.session))
admin.add_link(MenuLink(name="Logout", category="", url="/admin/logout"))


# --- Routes ---
@app.route("/")
def index():
    all_articles = Article.query.all()
    featured_articles = random.sample(all_articles, min(3, len(all_articles)))
    return render_template("index.html", featured_articles=featured_articles)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    from project_data import projects_list
    return render_template("projects.html", projects=projects_list)

@app.route("/tools")
def tools():
    return render_template("tools.html")

@app.route("/articles")
def articles():
    articles_list = Article.query.order_by(Article.published_on.desc()).all()
    return render_template("articles.html", articles=articles_list)

@app.route("/articles/<slug>", methods=["GET", "POST"])
def article_detail(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()
    if request.method == "POST":
        name = request.form["name"]
        content = request.form["content"]
        db.session.add(Comment(article_id=article.id, name=name, content=content))
        db.session.commit()
        return redirect(url_for("article_detail", slug=slug))
    comments = Comment.query.filter_by(article_id=article.id).order_by(Comment.created_at.desc()).all()
    return render_template("article_detail.html", article=article, comments=comments)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now, just log/print — later adjust to send email or save to DB
        app.logger.info(f"Contact form submitted: {name} ({email}) - {message}")

        flash("Thank you! Your message has been sent.", "success")

        return redirect(url_for("contact"))

    return render_template("contact.html")

# --- Admin auth routes ---
@app.route("/admin/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.index"))
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
    flash("You have been logged out successfully.", "success")
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


# --- Entrypoint ---
if __name__ == "__main__":
    app.run(debug=True)
