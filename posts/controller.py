from posts.models import Post
from app import db


class PostsController:
    @staticmethod
    def create_post(title, content):
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def get_all_posts():
        return Post.query.all()
