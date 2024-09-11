import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

results = sp.search(q='genre:j-pop', type='track', limit=10)  

# Extract track details
for track in results['tracks']['items']:
    print(f"Song: {track['name']}, Artist: {track['artists'][0]['name']}, Album: {track['album']['name']}")
    
    # Fetch and print audio features
    features = sp.audio_features(track['id'])[0]
    print(features)
