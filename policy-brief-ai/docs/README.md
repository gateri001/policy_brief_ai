# Smart Patrol Planner AI (MVP)

Predicts crime hotspots and suggests efficient patrol routes using spatiotemporal risk signals and a greedy orienteering baseline. Built for rapid demo: synthetic events → hotspots → route → API.

## Quick start
1. python -m venv .venv && .\.venv\Scripts\activate.bat
2. pip install -r requirements.txt
3. python apps/cli/simulate_events.py --n 500
4. python apps/cli/compute_hotspots.py
5. python apps/cli/plan_route.py
6. python -m uvicorn apps.api.main:app --host 0.0.0.0 --port 8000

## Test endpoints
- GET /health
- GET /hotspots?k=10
- POST /routes {"budget_min":60}

## Notes
- Risk computation = recency-weighted counts per grid cell.
- Route = greedy coverage on a small synthetic graph (fast, deterministic).
- RL hooks present as stubs for future work.
