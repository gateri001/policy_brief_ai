from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/brief")
def get_brief():
    df = pd.read_csv("data/synthetic_feedback.csv")
    summary = []
    for _, row in df.iterrows():
        summary.append(f"- Theme: {row['theme'].capitalize()} | Citizen voice: {row['feedback']}")
    return {"brief": summary}
