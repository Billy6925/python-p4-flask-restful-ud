from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData

metadata= MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(column_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Newsletter(db.Model, SerializerMixin):
    __tablename__ = 'newsletters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    published_at = db.Column(db.DateTime, server_default=db.func.now())
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Newsletter {self.title}, published at {self.published_at}.>'
