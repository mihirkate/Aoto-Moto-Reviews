# Auto Moto Reviews Setup Guide

This project has two main parts:

- `backend/`: Django backend API
- `frontend/`: React + Vite frontend

Follow these steps from a fresh clone of the repository.

## Prerequisites

Install these before starting:

- Python `3.12+`
- `pip`
- Node.js `20.19+` or `22.12+`
- npm
- MongoDB running locally on port `27017`
- Git

The project was created with Python `3.12.3`, Django `6.0.5`, React `19`, and Vite `8`.

## Backend Setup

From the project root:

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

On Windows PowerShell, activate the virtual environment with:

```powershell
venv\Scripts\Activate.ps1
```

Then run Django setup commands from the `backend/` directory:

```bash
cd backend
python manage.py migrate
python manage.py runserver 8000
```

The backend should be available at:

```text
http://localhost:8000/
```

Expected response:

```json
{
  "message": "Auto Moto Reviews API"
}
```

Important: use `backend/manage.py` for Django commands. The Django `core` package is inside `backend/`, so running the root-level `manage.py` can fail with import path issues.

## Backend Dependencies

Python dependencies are listed in `requirements.txt`.

Install all backend dependencies with:

```bash
pip install -r requirements.txt
```

Complete backend package list:

| Package | Version |
| --- | --- |
| `annotated-doc` | `0.0.4` |
| `annotated-types` | `0.7.0` |
| `anyio` | `4.13.0` |
| `asgiref` | `3.11.1` |
| `bcrypt` | `5.0.0` |
| `click` | `8.4.1` |
| `Django` | `6.0.5` |
| `django-cors-headers` | `4.9.0` |
| `djangorestframework` | `3.17.1` |
| `djongo` | `1.3.7` |
| `dnspython` | `2.8.0` |
| `ecdsa` | `0.19.2` |
| `fastapi` | `0.136.3` |
| `h11` | `0.16.0` |
| `idna` | `3.17` |
| `motor` | `3.7.1` |
| `passlib` | `1.7.4` |
| `pillow` | `12.2.0` |
| `pyasn1` | `0.6.3` |
| `pydantic` | `2.13.4` |
| `pydantic_core` | `2.46.4` |
| `pymongo` | `4.17.0` |
| `python-dotenv` | `1.2.2` |
| `python-jose` | `3.5.0` |
| `pytz` | `2026.2` |
| `rsa` | `4.9.1` |
| `six` | `1.17.0` |
| `sqlparse` | `0.5.5` |
| `starlette` | `1.2.1` |
| `typing-inspection` | `0.4.2` |
| `typing_extensions` | `4.15.0` |
| `uvicorn` | `0.48.0` |

The file includes packages for Django, MongoDB access, Django REST Framework, and FastAPI/JWT support. They are installed together even though the current backend entry point is Django.

## MongoDB Setup

The Django settings currently point to a local MongoDB instance:

```python
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB_NAME = "automoto"
```

These values are defined in `backend/core/settings.py`.

Start MongoDB locally before using backend features that read or write MongoDB collections. The project expects these collections inside the `automoto` database:

- `users`
- `vehicles`
- `reviews`

Start MongoDB using your operating system's service manager before running the backend.

## Frontend Setup

Open a new terminal from the project root:

```bash
cd frontend
npm install
npm run dev
```

The frontend should be available at:

```text
http://localhost:5173/
```

The frontend API client is configured in `frontend/src/api/axios.js` and points to:

```text
http://localhost:8000
```

Keep the Django backend running on port `8000` while working on frontend features that call the API.

## Frontend Dependencies

Frontend dependencies are listed in `frontend/package.json` and locked in `frontend/package-lock.json`.

Install all frontend dependencies with:

```bash
npm install
```

Runtime dependencies:

| Package | Version range |
| --- | --- |
| `axios` | `^1.16.1` |
| `react` | `^19.2.6` |
| `react-dom` | `^19.2.6` |

Development dependencies:

| Package | Version range |
| --- | --- |
| `@eslint/js` | `^10.0.1` |
| `@types/react` | `^19.2.14` |
| `@types/react-dom` | `^19.2.3` |
| `@vitejs/plugin-react` | `^6.0.1` |
| `eslint` | `^10.3.0` |
| `eslint-plugin-react-hooks` | `^7.1.1` |
| `eslint-plugin-react-refresh` | `^0.5.2` |
| `globals` | `^17.6.0` |
| `vite` | `^8.0.12` |

## Useful Commands

Backend:

```bash
source venv/bin/activate
cd backend
python manage.py runserver 8000
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```

Frontend:

```bash
cd frontend
npm run dev
npm run build
npm run preview
npm run lint
```

## Full Local Run Checklist

1. Start MongoDB on `localhost:27017`.
2. Start the Django backend:

   ```bash
   source venv/bin/activate
   cd backend
   python manage.py runserver 8000
   ```

3. Start the React frontend in a second terminal:

   ```bash
   cd frontend
   npm run dev
   ```

4. Open:

   ```text
   http://localhost:5173/
   ```

## Troubleshooting

If `python manage.py runserver` cannot import `core.settings`, make sure you are inside the `backend/` directory.

If frontend install fails because of Node version, upgrade Node to `20.19+` or `22.12+`.

If API calls fail from the frontend, confirm:

- Django is running at `http://localhost:8000`
- MongoDB is running at `mongodb://localhost:27017/`
- The frontend API base URL in `frontend/src/api/axios.js` still matches the backend URL

If `npm run lint` reports existing template issues, fix those in the frontend source before treating lint as a required passing check.
