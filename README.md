# Setup Vite.js with Python Flask

This repository provides a basic setup for integrating Vite.js with a Python Flask backend. This combination allows you to build modern web applications using Vite.js on the frontend and Flask on the backend.


## installation required
- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)


## Additional Frontend CSS Framework
- [Tailwind CSS](https://tailwindcss.com/)
- [Material Tailwind CSS](https://material-tailwind.com/)

For detailed versions, check the `frontend/package.json` file.

## Frontend Usage
    ```bash
    cd frontend
    npm install
    npm run dev
    ```


## Backend Requirements
- [flask](https://pypi.org/project/Flask/)
- [flask-cors](https://pypi.org/project/Flask-Cors/)

For a comprehensive list of backend requirements, refer to the `backend/requirements.txt` file.

## Backend Usage ( use virtual environment )
    ```bash
    cd backend
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python server.py
    ```
