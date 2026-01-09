from fastapi import APIRouter

router = APIRouter()

@router.get("/recommendations")
def get_recommendations():
    recs = [
        "Increase healthcare funding in underserved regions",
        "Launch youth employment programs",
        "Enhance rural security patrols",
        "Support ongoing education reforms"
    ]
    return {"recommendations": recs}
