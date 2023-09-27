from django.shortcuts import render
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"
# Load the pickled files
similarity = pickle.load(open('E:/MSR/music_recommendation/similarity.pkl', 'rb'))
df = pickle.load(open('E:/MSR/music_recommendation/df.pkl', 'rb'))
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"


def recommendations(request):
    # Get the list of all songs
    songs = df['song'].tolist()

    recommended_songs = []
    recommended_music_posters = []
    if request.method == 'POST':
        song_name = request.POST.get('song_name')
        try:
            idx = df[df['song'] == song_name].index[0]
            distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
            
            # Iterate through the top similar songs and add them to the list
            for m_id in distances[1:21]:
                recommended_songs.append(df.iloc[m_id[0]].song)
                 # Assuming you have a function get_song_album_cover_url(song, artist) 
                # that returns the URL of the album cover
                poster_url = get_song_album_cover_url(df.iloc[m_id[0]].song, df.iloc[m_id[0]].artist)
                recommended_music_posters.append(poster_url)
                 # Zip the songs and posters
            song_poster_zip = zip(recommended_songs, recommended_music_posters)

            return render(request, 'recommendations/recommended_songs.html', {'song_poster_zip': song_poster_zip})
        except IndexError:
            pass

    return render(request, 'recommendations/home.html', {'songs': songs})






















