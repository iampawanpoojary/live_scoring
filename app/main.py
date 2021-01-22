from typing import Optional
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firestore_helper as helper

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "random-client",
})

db = firestore.client()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/score")
def read_item():
    score = helper.getGoal(db)
    return score


@app.post("/goal/{team}")
def update_item(team: str):
    if(validTeam(team)):
        score = helper.updateScoreBoard(db,team)
        return score
    else:
        return {"error": "Valid teams are 'home' or 'away'"}


def validTeam(team):
    if(team.casefold() == "home" or team.casefold() =="away" ):
        return True
    else: 
        return False