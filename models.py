from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase,relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Text
from datetime import datetime, timezone

class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    notes: Mapped["Notes"] = relationship("Notes", back_populates="author", cascade="all, delete-orphan")

class Notes(db.Model):
   id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
   created: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
   title: Mapped[str]
   content: Mapped[str]
   # Foreign key to User model
   user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
   # Define the relationship back to User
   author: Mapped["User"] = relationship("User", back_populates="notes")
   