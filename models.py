from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), default="Mauricio Aragon")
    published_on = db.Column(db.Date, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    article = db.relationship("Article", backref=db.backref("comments", lazy=True))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=True)

    # auth helpers
    def set_password(self, pw): self.password_hash = generate_password_hash(pw)
    def check_password(self, pw): return check_password_hash(self.password_hash, pw)

    # flask-login interface
    @property
    def is_authenticated(self): return True
    @property
    def is_active(self): return True
    @property
    def is_anonymous(self): return False
    def get_id(self): return str(self.id)
