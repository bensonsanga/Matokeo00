from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, Result
from flaskblog.posts.forms import PostForm, SearchForm
import requests
from bs4 import BeautifulSoup
import pandas as pd

posts = Blueprint('posts', __name__)


def numberToResult(iNumber, iYear, iExam):
    iSchoolnumber = iNumber[:5].lower()
    iLink = "https://necta.go.tz/results/{year}/{exam}/results/{number}.htm".format(year=iYear, exam=iExam, number=iSchoolnumber)
    request = requests.get(iLink)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    student = soup.find("font", string=iNumber.upper())
    studentReport = student.parent.parent
    studentResults = studentReport.find_all("font")
    studentNumber = studentResults[0].text
    studentSex = studentResults[1].text
    studentDivisionPoint = studentResults[2].text
    studentDivision = studentResults[3].text
    studentGrades = studentResults[4].text

    report = soup.find_all("p")
    schoolReport = report[1].text

    return{
        'studentNumber': studentNumber,
        'studentDivision': studentDivision,
        'studentDivisionPoint': studentDivisionPoint,
        'studentGrades': studentGrades,
        'schoolReport': schoolReport
    }


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/search", methods=['GET', 'POST'])
def new_search():
    form = SearchForm()
    if form.validate_on_submit():
        name = form.name.data.upper()
        result = numberToResult(form.student_number.data, form.year.data, form.exam.data.lower())
        flash(f"Dear { name },if your number is { form.student_number.data },then below are your results", 'success')
        return render_template('result.html', title='Preview results',
                               name=name, result=result, legend='Preview Results')

    return render_template('search_results.html', title='Search Results',
                           form=form, legend='Search Results')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
