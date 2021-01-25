from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firestoreHelper as helper
from enum import Enum



# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "random-client",
})

# Initialize database connection client
db = firestore.client()



class Team(str, Enum):
    home = "home"
    away = "away"

class Goal(BaseModel):
    player: Optional[str]
    team: Team

class Score(BaseModel):
    home: int = 0
    away: int = 0

# Run FastApi
app = FastAPI()

@app.post("/goal/", response_model=Score)
async def post_goal(goal: Goal):
    score = helper.updateScoreBoard(db,goal.team)
    return score

@app.get("/score", response_model=Score)
def get_score():
    score = helper.getGoal(db)
    return score


