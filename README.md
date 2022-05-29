# Songify: Song Recommendation System

## Introduction
The aim of the project is to recommend songs on the basis of a given playlist. 

## Web App Screenshots
![Screenshot 2022-05-29 at 6 34 08 PM](https://user-images.githubusercontent.com/72307161/170870285-ed9fffc5-e660-4893-922d-ffb6a7ca1715.png)
![Screenshot 2022-05-29 at 6 34 40 PM](https://user-images.githubusercontent.com/72307161/170870292-a48ac71f-cd0d-458c-8c7e-ce2ce2a9a544.png)
![Screenshot 2022-05-29 at 6 35 09 PM](https://user-images.githubusercontent.com/72307161/170870296-fe1e62dd-7cd7-4503-b90d-20c6050aa5b6.png)

## Features
- Input playlist link and the number of song recommendations required
- Display list of recommended songs (click to get directed to the corresponding Spotify link)

## Recommendation Model
The recommendation model is summarized in the recommenderSystem.ipynb notebook. The following steps were followed:

* Data Preprocessing
* Feature Engineering
* Content-based Filtering Recommendation Model

## Installation

To create a virtual environment, run the following commands:
```sh
python3 -m venv .venv
source .venv/bin/activate (for Windows use .venv\scripts\activate)
```

Install the dependencies using:
```sh
pip install -r requirements.txt
```

To run the Flask application, use the following command in the terminal:
```sh
python run.py
```
