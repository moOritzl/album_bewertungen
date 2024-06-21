from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from .cover_downloader import save_first_google_image
from .models import Album, Comment, Rating
from . import db

reviews = Blueprint('reviews', __name__)


@reviews.route('/')
def main_page():
    albums = Album.query.all()
    album_data = []

    for album in albums:
        # Initialize ratings and comments with None
        ratings = {1: None, 2: None}
        comments = {1: None, 2: None}

        for rating in Rating.query.filter_by(album_id=album.id).all():
            if rating:
                ratings[rating.user_id] = rating

        for comment in Comment.query.filter_by(album_id=album.id).all():
            if comment:
                comments[comment.user_id] = comment

        album_data.append({
            'album': album,
            'ratings': ratings,
            'comments': comments
        })

    return render_template('index.html', album_data=album_data)


@reviews.route('/hinzufuegen', methods=['GET', 'POST'])
def add_album():
    if request.method == 'POST':
        name = request.form.get('name')
        artist = request.form.get('artist')
        year = request.form.get('year')

        if name and artist and year:
            new_album = Album(name=name, artist=artist, year=int(year))
            db.session.add(new_album)
            db.session.commit()

            save_first_google_image(new_album)

            return redirect(url_for('reviews.main_page'))

    return render_template('hinzufuegen.html')


@reviews.route('/bearbeiten/<int:album_id>', methods=['GET', 'POST'])
def edit_album(album_id):
    album = Album.query.get_or_404(album_id)
    user_id = current_user.id

    rating = Rating.query.filter_by(album_id=album_id, user_id=user_id).first()
    comment = Comment.query.filter_by(album_id=album_id, user_id=user_id).first()

    if request.method == 'POST':
        new_rating = request.form.get('rating')
        new_comment = request.form.get('comment')

        if new_rating:
            if rating:
                rating.rating = int(new_rating)
            else:
                rating = Rating(rating=int(new_rating), album_id=album_id, user_id=user_id)
                db.session.add(rating)

        if new_comment:
            if comment:
                comment.content = new_comment
            else:
                comment = Comment(content=new_comment, album_id=album_id, user_id=user_id)
                db.session.add(comment)

        db.session.commit()
        return redirect(url_for('reviews.main_page'))

    return render_template('edit.html', album=album, rating=rating, comment=comment)
