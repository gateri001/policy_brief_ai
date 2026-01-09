# Demo: generate events, compute hotspots, start API, query
Write-Host "Simulating events..."
python apps/cli/simulate_events.py --n 500 --output data/synthetic_events.csv

Write-Host "Computing hotspots..."
python apps/cli/compute_hotspots.py --events data/synthetic_events.csv --grid data/grid.geojson --output apps/rl/artifacts/hotspots.csv --topk 10

Write-Host "Planning route..."
python apps/cli/plan_route.py --hotspots apps/rl/artifacts/hotspots.csv --budget_min 60 --output apps/rl/artifacts/route.json

Write-Host "Starting API..."
python -m uvicorn apps.api.main:app --host 0.0.0.0 --port 8000
