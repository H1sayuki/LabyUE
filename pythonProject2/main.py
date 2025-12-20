import cv2
import numpy as np
import requests
from fastapi import FastAPI, UploadFile
from random import randint

app = FastAPI()

zadania = {}


def licz_ludzi(id_zadania, obraz):
    if obraz is None:
        zadania[id_zadania] = "Błąd: Nie udało się otworzyć zdjęcia"
        return

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    ludzie, _ = hog.detectMultiScale(obraz, winStride=(8, 8))

    zadania[id_zadania] = f"Zakończono. Liczba osób: {len(ludzie)}"


@app.get("/status")
def sprawdz_status(id_zadania: int):
    return {"wynik": zadania.get(id_zadania, "Brak zadania")}


@app.get("/plik_lokalny")
def z_dysku(sciezka: str):
    id_zadania = randint(1, 100)

    obraz = cv2.imread(sciezka)

    licz_ludzi(id_zadania, obraz)

    return {"id_zadania": id_zadania, "info": "Gotowe, sprawdź status"}


@app.get("/z_internetu")
def z_url(url: str):
    id_zadania = randint(1, 100)

    response = requests.get(url)
    arr = np.frombuffer(response.content, np.uint8)
    obraz = cv2.imdecode(arr, -1)

    licz_ludzi(id_zadania, obraz)

    return {"id_zadania": id_zadania, "info": "Gotowe, sprawdź status"}


@app.post("/upload")
async def przeslij_plik(plik: UploadFile):
    id_zadania = randint(1, 100)

    tresc = await plik.read()
    arr = np.frombuffer(tresc, np.uint8)
    obraz = cv2.imdecode(arr, -1)

    licz_ludzi(id_zadania, obraz)

    return {"id_zadania": id_zadania, "info": "Gotowe, sprawdź status"}
