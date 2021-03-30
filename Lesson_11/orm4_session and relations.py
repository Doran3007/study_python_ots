import sqlalchemy
import sqlite3
from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker, scoped_session, relationship
from datetime import datetime

engin = create_engine("sqlite:///example2.db")
Base = declarative_base(bind=engin)
session_factory = sessionmaker(bind=engin)
Session = scoped_session(session_factory)

posts_tags_table = Table(
    "posts_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


# ----------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())

    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    author_id = Column(Integer, ForeignKey(User.id))

    author = relationship(User, back_populates='posts')
    tags = relationship('Tag', secondary=posts_tags_table,  back_populates='posts')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author={self.author})"

    def __repr__(self):
        return str(self)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    posts = relationship('Post', secondary=posts_tags_table,  back_populates='tags')

    def __str__(self):
        return f"{self.__class__.__name__}(id = {self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    u = User(username='sam')
    print("before", u.id)
    session.add(u)
    session.commit()
    print("after", u.id)
    return u


def author_posts():
    # u = create_user("sam")
    user = session.query(User).filter_by(username="sam").one()
    print(user)

    # post = Post(title="First", author=user)
    # session.add(post)
    # session.commit()
    # print(post)
    # print(user.posts)

    post = Post(title="Second")
    # session.add(post)
    user.posts.append(post)
    session.commit()
    print(user.posts)


def create_tags():
    user = session.query(User).filter_by(username="jonh").one()
    user.is_staff = True

    tags = [Tag(name=name) for name in ("news", "python", "django", "flask")]
    post = Post(title="news flask versus django", author=user)
    post.tags.extend(tags)
    session.commit()

    print(post, post.tags)

    for tag in tags:
        print(tag, tag.posts)

if __name__ == "__main__":
    Base.metadata.create_all()
    session = Session()
    # u = create_user("sam")
    # author_posts()
    # create_tags()

    users = session.query(User).filter(
        User.id > 1,
        User.username != "jonh"
    ).all()
    print(users)

    posts = session.query(Post).all()

    for post in posts:
        print(post, post.tags)

    flas_posts = session.query(User).join(Post, User.id == Post.author_id).filter(Post.tags.any(Tag.name.ilike("new%")))
    print()
    print(flas_posts)
    print()
    print()
    print(flas_posts.all())

    session.close()
