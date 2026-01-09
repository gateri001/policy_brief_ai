from fastapi import FastAPI
from . import router_brief, router_recommendations

app = FastAPI(title="Policy Brief Generator API")

@app.get("/health")
def health():
    return {"status":"ok"}

app.include_router(router_brief.router)
app.include_router(router_recommendations.router)
