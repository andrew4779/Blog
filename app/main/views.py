from flask import render_template, redirect,url_for,request,flash
from . import main
from flask_login import login_required,current_user
from ..models import Blog,Comment
from .forms import NewblogForm,CommentForm
from .. import db
from app.request import getQuotes

# Views
@main.route('/')
def index():
    quote = getQuotes()
    title = 'Home - Fine Blog'
    print(quote)
    blogs = Blog.query.all()
    blogs = blogs[::-1]
    return render_template('index.html',title = title,quote = quote,blogs=blogs)

@main.route('/newblog',methods = ["GET","POST"])
@login_required
def newblog():
    form = NewblogForm()
    if form.validate_on_submit():
        blog = Blog (title = form.title.data, blog = form.blog.data,author_id = current_user._get_current_object().id)
        blog.save()
        flash('Post created succesfully')
        return redirect(url_for('main.index'))
    return render_template('newblog.html',form = form)


@main.route('/edit_blog/<blog_id>/edit',methods = ["GET","POST"])
@login_required
def edit_blog(blog_id):
    form = NewblogForm()
    blog = Blog.query.get(blog_id)
    if current_user != blog.user:
        return redirect(url_for('main.index'))
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.blog = form.blog.data
        db.session.commit()
        return redirect(url_for('main.index'))
    if request.method == 'GET':
        form.title.data = blog.title
        form.blog.data = blog.blog
    return render_template ('newblog.html',form = form)

@main.route('/blog/<blog_id>/delete',methods = ["GET","POST"])
@login_required
def deleteblog(blog_id):
    blog = Blog.query.get(blog_id)
    if current_user != blog.user:
        return redirect(url_for('main.index'))
    db.session.delete(blog)
    db.session.commit()
    flash('Deleted Succesfully')
    return redirect(url_for('main.index'))

@main.route('/newcomment/<blog_id>',methods = ["GET","POST"])
@login_required
def newcomment(blog_id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(comment = form.comment.data, blog_id = blog_id, user_id = current_user._get_current_object().id )
        new_comment.save()
        return redirect (url_for('main.index'))
    return render_template('comment.html', form = form )
