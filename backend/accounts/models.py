from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from blog.models import Post
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
    
    posts = relationship("Post", back_populates='author')