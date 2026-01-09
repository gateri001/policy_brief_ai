# Smoke test for judges
Write-Host "Compute hotspots"
python apps/cli/compute_hotspots.py
Write-Host "Plan route"
python apps/cli/plan_route.py --budget_min 30

Write-Host "API health"
Invoke-WebRequest -Uri "http://localhost:8000/health" -Method GET | Select-Object -ExpandProperty Content

Write-Host "API hotspots"
Invoke-WebRequest -Uri "http://localhost:8000/hotspots?k=5" -Method GET | Select-Object -ExpandProperty Content

Write-Host "API route"
Invoke-WebRequest -Uri "http://localhost:8000/routes" -Method POST -ContentType "application/json" -Body '{"budget_min":45}' | Select-Object -ExpandProperty Content
