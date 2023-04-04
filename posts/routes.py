from flask import Blueprint, request, jsonify
from posts.controller import PostsController

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/posts', methods=['POST'])
def create_post():
    title = request.json['title']
    content = request.json['content']
    post = PostsController.create_post(title, content)
    return jsonify(post)

