# Demo Script (2 minutes)

1. Simulate events:
   - python apps/cli/simulate_events.py --n 500

2. Compute hotspots:
   - python apps/cli/compute_hotspots.py --topk 10
   - Show printed top cells and artifacts/hotspots.csv

3. Plan route:
   - python apps/cli/plan_route.py --budget_min 60
   - Show artifacts/route.json

4. Start API:
   - python -m uvicorn apps.api.main:app --host 0.0.0.0 --port 8000

5. Test in PowerShell:
   - Invoke-WebRequest "http://localhost:8000/health"
   - Invoke-WebRequest "http://localhost:8000/hotspots?k=5"
   - Invoke-WebRequest -Uri "http://localhost:8000/routes" -Method POST -ContentType "application/json" -Body '{"budget_min":45}'
