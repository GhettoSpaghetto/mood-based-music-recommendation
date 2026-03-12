import requests
from app.config import settings


API_KEY = settings.LASTFM_API_KEY
BASE_URL = settings.BASE_URL

MOOD_MAP = {
    "happy": "happy",
    "sad": "sad",
    "angry": "aggressive",
    "neutral": "chillout",
    "surprise": "experimental"
}

def get_music(mood):
    tag = MOOD_MAP.get(mood.lower(), "chillout")

    params = {
        "method": "tag.gettoptracks",
        "tag": tag,
        "api_key": API_KEY,
        "format": "json",
        "limit": 5
    }

    try:
        response = requests.get(BASE_URL, params=params)
        print(f"Status code: {response.status_code}")
        print(f"Raw response: {response.text}") 
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            print(f"Last.fm API error {data['error']}: {data['message']}")
            return [{"name": "Error fetching music", "artist": "Last.fm", "url": "#"}]

        tracks = data.get("tracks", {}).get("track", [])
        songs = []
        for track in tracks:
            songs.append({
                "name": track["name"],
                "artist": track["artist"]["name"],
                "url": track["url"]
            })
        return songs

    except Exception as e:
        print(f"last.fm Error: {e}")
        import traceback
        traceback.print_exc()
    return [{"name": "Error fetching music", "artist": "Last.fm", "url": "#"}]