import requests
from bs4 import BeautifulSoup
import os


def save_first_google_image(album):
    album_name = album.name
    artist = album.artist
    album_id = album.id

    # Google-Bilder-URL für die Suche
    query = f"{artist} {album_name} album cover"
    url = f"https://www.google.com/search?hl=de&q={query}&tbm=isch"

    # Headers, um die Anfrage wie ein Browser erscheinen zu lassen
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Das erste Bild finden
    img_tags = soup.find_all("img")

    if img_tags:
        first_img_url = img_tags[1]['src']

        if 'https://' not in first_img_url:
            first_img_url = f"https://encrypted-tbn0.gstatic.com{first_img_url}"

        # Bilddaten abrufen
        img_data = requests.get(first_img_url).content

        # Pfad zu "static/album_covers" Verzeichnis
        save_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'album_covers')
        save_path = os.path.join(save_dir, f"{album_id}.jpg")

        # Verzeichnis erstellen, falls es nicht existiert
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Bild speichern
        with open(save_path, 'wb') as handler:
            handler.write(img_data)
        print(f"Cover für {artist} - {album_name} wurde als {album_id}.jpg gespeichert")
    else:
        print(f"Konnte kein Bild für {artist} - {album_name} (id = {album_id}) finden")
