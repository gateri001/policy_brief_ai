# Judge Summary

## Problem
Police patrols often follow static routes, missing dynamic hotspots. This reduces deterrence and community safety.

## Solution
Smart Patrol Planner AI predicts near-term hotspots from recent incidents and suggests efficient patrol routes to maximize risk coverage.

## Tech
- Spatiotemporal risk signals from synthetic events (recency-weighted density)
- Greedy orienteering route planner (fast baseline)
- FastAPI endpoints for hotspots and routes

## Impact
- Better coverage of high-risk areas
- Efficient patrol allocation
- Ready for real data integrations and RL optimization post-hackathon

## Demo Steps
1. Simulate events → compute hotspots
2. Plan route → start API
3. Query /hotspots and /routes via PowerShell
