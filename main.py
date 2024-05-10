from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials, firestore

origins = [
    #Domeniile aplicatiti trebuie adaugate aici ori cererea este refuzata
    "https://kreateapp.com",  
    "https://www.kreateapp.com", 
    "https://kreate.flutterflow.app", 
]

# Firebase config
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# FastAPI config
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def getDocument(collection, document):
    doc_ref = db.collection(collection).document(document)
    doc = await doc_ref.get()
    if doc.exists:
        return doc
    else:
        raise Exception("Document not found!")

@app.get("/")
async def index():
    return {"Server has woken up"}

@app.get("/recommend/{user_id}")
async def get_user_recommandations(user_id: str):
    user_ref = db.collection("users").document(user_id)
    user = user_ref.get()

    if user.exists:
        user_data = user.to_dict()
        following = user_data.get('following', [])  

        following_ids = set()
        recommendations_set = set()  

        # Adăugăm id-urile followerilor inițiali într-un set
        for follower_ref in following:
            person = follower_ref.get()
            following_ids.add(person.id)

        # Parcurgem lista de following a fiecărui follower și adăugăm recomandările în setul de recomandări
        for follower_id in following_ids:
            follower_ref = db.collection("users").document(follower_id)
            follower = follower_ref.get()
            follower_data = follower.to_dict()
            follower_following = follower_data.get('following', [])

            # Excludem id-ul utilizatorului curent din lista de following a fiecărui follower
            if user_id in follower_following:
                follower_following.remove(user_id)

            # Adăugăm în setul de recomandări doar persoanele care nu sunt în lista de following a utilizatorului inițial
            for following_ref in follower_following:
                following_person = following_ref.get()
                following_person_id = following_person.id
                if following_person_id != user_id and following_person_id not in following_ids:
                    recommendations_set.add(following_person_id)

        recommendations = list(recommendations_set)
        
        # Returnăm un mesaj JSON cu rezultatul
        return {"success": True, "recommendations": recommendations}
    
    # Dacă utilizatorul nu există, ridicăm o excepție HTTP cu codul 404
    raise HTTPException(status_code=404, detail="User was not found")
