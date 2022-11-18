from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base
from accounts.models import User

class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, index=True, unique=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    author = relationship("User", back_populates = "posts")
    