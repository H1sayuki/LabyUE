import csv
from Zadania import SessionLocal, Movie, Link, Rating, Tag

db = SessionLocal()


def importuj_plik(nazwa_pliku, Model, mapa_kolumn):
    try:
        with open(nazwa_pliku, encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)

            obiekty = []
            for row in reader:
                dane = {}
                for pole_bazy, index_csv in mapa_kolumn.items():
                    dane[pole_bazy] = row[index_csv]

                obiekty.append(Model(**dane))

            db.add_all(obiekty)
            db.commit()
            print(f"Sukces: {nazwa_pliku} załadowany.")
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {nazwa_pliku}")



importuj_plik('movies.csv', Movie, {'id': 0, 'title': 1, 'genres': 2})
importuj_plik('links.csv', Link, {'movie_id': 0, 'imdb_id': 1, 'tmdb_id': 2})
importuj_plik('ratings.csv', Rating, {'user_id': 0, 'movie_id': 1, 'rating': 2, 'timestamp': 3})
importuj_plik('tags.csv', Tag, {'user_id': 0, 'movie_id': 1, 'tag': 2, 'timestamp': 3})

db.close()