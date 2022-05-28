from myApp import app
from flask import render_template, request, url_for

from myApp.features import *
from myApp.model import *

songDF = pd.read_csv("./data/songs.csv")
complete_feature_set = pd.read_csv("./data/complete_feature.csv")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
   #requesting the URL form the HTML form
   URL = request.form['URL']
   #fetch id from URL
   id = URL.split("/")[-1].split("?")[0]
   #using the extract function to get a features dataframe
   df = fetch_tracks(id, songDF)
   #retrieve the results and get as many recommendations as the user requested
   edm_top40 = recommend_from_playlist(songDF, complete_feature_set, df)
   number_of_records = int(request.form['number_of_records'])
   my_songs = []
   for i in range(number_of_records):
      my_songs.append([str(edm_top40.iloc[i,2]) + " " + str(edm_top40.iloc[i,6]), "https://open.spotify.com/track/"+ str(edm_top40.iloc[i,1])])
   return render_template('results.html',songs= my_songs)
