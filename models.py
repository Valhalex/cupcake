"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
default_image = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """cupcakes profile"""
    
    __tablename__ = "cupcake"
    
    
    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    flavor = db.Column(db.Text,
                       nullable=False)
    size = db.Column(db.Text,
                       nullable=False)
    rating = db.Column(db.Float,
                       nullable=False)
    image = db.Column(db.Text,
                      nullable=False, default=default_image)
    
    def to_dict(self):
        """Serialize cupcake to a dict of cupcake info."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }