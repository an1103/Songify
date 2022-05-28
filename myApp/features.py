import pandas as pd

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def fetch_tracks(id, df):
    """ 
    Pull songs from a specific playlist.

    Parameters: 
        id: id of the playlist you'd like to pull from the spotify API
        df (pandas dataframe): spotify dataframe
        
    Returns: 
        playlist: all songs in the playlist THAT ARE AVAILABLE IN THE KAGGLE DATASET
    """
    #set up the client id and secret key variables
    cid = "70e1036d72f94384a09bb3f99878398b"
    secret = "542d003637fe428dae96ae94c329ffef"

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    #generate playlist dataframe
    playlist = pd.DataFrame()

    for ix, i in enumerate(sp.playlist(id)['tracks']['items']):
        #print(i['track']['artists'][0]['name'])
        playlist.loc[ix, 'artist'] = i['track']['artists'][0]['name']
        playlist.loc[ix, 'name'] = i['track']['name']
        playlist.loc[ix, 'id'] = i['track']['id'] # ['uri'].split(':')[2]
        playlist.loc[ix, 'url'] = i['track']['album']['images'][1]['url']
        playlist.loc[ix, 'date_added'] = i['added_at']

    playlist['date_added'] = pd.to_datetime(playlist['date_added'])  
    
    playlist = playlist[playlist['id'].isin(df['id'].values)].sort_values('date_added',ascending = False)
    
    return playlist

    