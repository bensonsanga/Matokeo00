from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/")
@main.route("/about")
def about():
    return render_template('landing.html', title='About')


@main.route("/stats")
def stats():
    return render_template('charts.html', title='About')
