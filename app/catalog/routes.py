from app.catalog import main
from app import db
from app.catalog.models import Publication, Book
from flask import render_template,flash,request,redirect,url_for
from flask_login import login_required
from app.catalog.forms import EditBookForm,CreateBookForm

@main.route('/')
def display_book():
        #return "hello world"
        books = Book.query.all()
        return render_template('home.html',books=books)

@main.route('/display/publisher/<publisher_id>',methods=['GET','POST'])
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_book = Book.query.filter_by(pub_id = publisher_id).all()
    return render_template('publisher.html',publisher = publisher,publisher_book=publisher_book)

@main.route('/book/delete/<book_id>',methods=['GET','POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash("book delete successfully")
        return redirect(url_for('main.display_book'))
    return render_template('delete_book.html',book=book,book_id=book.id)

@main.route('/edit/book/<book_id>',methods=['GET','POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.title.data
        book.num_page = form.num_page.data
        db.session.add(book)
        db.session.commit()
        flash("book edit successfully")
        return redirect(url_for('main.display_book'))
    return render_template('edit_book.html',form=form)

@main.route('/create/book/<pub_id>',methods=['GET','POST'])
@login_required
def create_book(pub_id):
    form = CreateBookForm()
    form.pub_id.data = pub_id
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author =form.author.data,
            avg_rating = form.avg_rating.data,
            format= form.format.data,
            image=form.img_url.data,
            num_page=form.num_page.data,
            pub_id=form.pub_id.data
        )

        db.session.add(book)
        db.session.commit()
        flash("book added sucessfully")
        return redirect(url_for('main.display_publisher',publisher_id= pub_id))
    return render_template('create_book.html',form=form, pub_id=pub_id)

