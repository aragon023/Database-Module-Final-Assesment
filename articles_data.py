from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

  # Article Model

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), default='Mauricio Aragon')
    published_on = db.Column(db.Date, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False) 

    def __repr__(self):
        return f'<Article {self.title}>'

  # Comment Model

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    article = db.relationship('Article', backref=db.backref('comments', lazy=True))

    def __repr__(self):
        return f'<Comment by {self.name} on Article {self.article_id}>'
