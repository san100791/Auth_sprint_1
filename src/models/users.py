import uuid
from sqlalchemy.dialects.postgresql import UUID
from src.db.db_postgres import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    login = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.string, nullable=False, unique=True)
    first_name = db.Column(db.string, nullable=False)
    last_name = db.Column(db.string, nullable=False)

    def __repr__(self):
        return f'<User {self.login}>'