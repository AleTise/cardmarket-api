.PHONY: backend frontend

# Attiva virtualenv e avvia backend
backend:
	cd backend && source ../venv/bin/activate && python -m cardmarket_api.api

# Avvia frontend (assumendo npm start esistente)
frontend:
	cd frontend && npm start

# Avvia backend e frontend in parallelo (serve installare 'concurrently' o usa due terminali)
start:
	@echo "Avvia backend e frontend in due terminali separati"