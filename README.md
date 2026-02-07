# WIKI-APP1

Minimal monorepo containing a FastAPI backend and a Vite React frontend.

## Repository layout

- `backend/` — FastAPI app, Python requirements in `backend/requirements.txt`
- `frontend/` — Vite + React app (npm)

## Prerequisites

- Python 3.10+
- Node 18+ and npm
- Git

## Backend: setup & run

1. Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1  # PowerShell
# or: .venv\\Scripts\\activate    # cmd
```

2. Install dependencies:

```powershell
pip install -r backend/requirements.txt
```

3. Run the backend (development):

```powershell
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000` (docs: `/docs`).

## Frontend: setup & run

1. Install dependencies:

```bash
cd frontend
npm install
```

2. Run the dev server:

```bash
npm run dev
```

The frontend dev server typically runs at `http://localhost:5173` and will proxy or call the backend as configured.

## Working locally

- Start the backend first, then the frontend. Adjust ports or proxy settings if needed.

## Git / GitHub

1. Create a GitHub repository and add it as `origin` if you haven't already.

```bash
git remote add origin https://github.com/<YOUR_USERNAME>/WIKI-APP1.git
git branch -M main
git push -u origin main
```

If prompted to authenticate when pushing, use a Personal Access Token or set up SSH keys.

## Questions or next steps

- Want me to set up a `.github/workflows` CI workflow, or add branch protection on `main`?
