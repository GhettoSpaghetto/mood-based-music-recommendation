from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware


from app.model import MoodModel
from app.music import get_music

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["mood-based-music-recommendation.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = MoodModel("model/model_weights.pth")



@app.post("/predict")
async def predict_mood(file: UploadFile = File(...)):

    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    mood = model.predict(image)


    songs = get_music(mood)

    return{
        "mood": mood,
        "recommend_music": songs
    }