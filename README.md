# Songify: Song Recommendation System

## Introduction
The aim of the project is to recommend songs on the basis of a given playlist. 

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
