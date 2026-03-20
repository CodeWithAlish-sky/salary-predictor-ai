from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="Random Forest Salary Predictor")

# Mount the static directory to serve HTML, CSS, and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

class PredictionRequest(BaseModel):
    level: float

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Serve index.html on root
    with open("static/index.html", "r") as f:
         return f.read()

@app.post("/predict")
async def predict(req: PredictionRequest):
    if not os.path.exists(model_path):
        raise HTTPException(
            status_code=500, 
            detail="model.pkl not found! Please run train.py first to generate the model artifact."
        )
    
    try:
        model = joblib.load(model_path)
        prediction = model.predict([[req.level]])
        return {"salary": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
