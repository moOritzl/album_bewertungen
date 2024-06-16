from flask import Blueprint, render_template, request, redirect, url_for

from .cover_downloader import save_first_google_image
from .models import Album
from . import db

reviews = Blueprint('reviews', __name__)


@reviews.route('/')
def main_page():
    albums = Album.query.all()
    return render_template('index.html', albums=albums)


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
