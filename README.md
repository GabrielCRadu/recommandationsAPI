
# 👥 recommandationsAPI

Un API REST simplu, scris în **FastAPI**, care generează recomandări de utilizatori pentru aplicația **KREATE** pe baza relațiilor sociale din Firebase Firestore („prieteni ai prietenilor”).

---

## 🎯 Scop

Oferirea de sugestii de persoane pe care un utilizator ar putea să le urmărească, în funcție de activitatea rețelei sale sociale.

---

## 🛠️ Funcționalități

- Endpoint `GET /recommend/{user_id}`  
- Conectare la **Firebase Firestore** pentru citirea rețelei de utilizatori  
- Algoritm de recomandare tip „friends of friends”, cu excluderea duplicatelor  
- Suport CORS pentru integrare în aplicații Flutter/FlutterFlow (domenii whitelisted)

---

## 🔄 Exemplu de funcționare

Pentru utilizatorul `user_id`, se vor recomanda utilizatori pe care:
- îi urmăresc **cei pe care deja îi urmărește** `user_id`
- dar pe care **încă nu îi urmărește**

---

## 🚀 Instalare & Rulare

```bash
git clone https://github.com/GabrielCRadu/recommandationsAPI.git
cd recommandationsAPI

pip install -r requirements.txt
```

### Setări Firebase
Asigură-te că ai fișierul `serviceAccountKey.json` în directorul proiectului, exportat din Firebase Console.

---

### Rulare locală
```bash
uvicorn main:app --reload
```

---

## 📬 Endpoint-uri

### `GET /recommend/{user_id}`

Returnează o listă de ID-uri ale utilizatorilor recomandați.

**Răspuns:**
```json
{
  "success": true,
  "recommendations": ["uid_abc", "uid_xyz", ...]
}
```

---

## 🔐 Securitate

- Conectarea la Firebase se face cu credentiale de tip `serviceAccountKey.json`
- CORS activ doar pentru domeniile:
  - `https://kreateapp.com`
  - `https://www.kreateapp.com`
  - `https://kreate.flutterflow.app`

---

## 👨‍💻 Autor

**Gabriel Radu** – radugabriel796@gmail.com  
Parte din proiectul [KREATE](https://kreateapp.com)

---

## 📄 Licență

MIT – vezi `LICENSE`




# Deploy FastAPI on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.

See https://render.com/docs/deploy-fastapi or follow the steps below:

## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/render-examples/fastapi)

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!
