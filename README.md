# Spa Website

A modern website for [Spa Name] built with Django and Svelte, deployed on Render.com.

## Features
- Email subscription system
- Contact form
- Admin panel for managing specials, bios, and content
- Calendar-based appointment booking
- Online product pickup with Stripe payments
- Customer authentication with rewards and referrals
- Employee portal for paystubs and availability

## Setup

### Backend
1. Create a virtual environment: `python -m venv venv`
2. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r backend/requirements.txt`
4. Copy `backend/.env.example` to `backend/.env` and fill in credentials
5. Run migrations: `python backend/manage.py migrate`
6. Start server: `python backend/manage.py runserver`

### Frontend
1. Navigate to `frontend/`: `cd frontend`
2. Install dependencies: `npm install`
3. Start dev server: `npm run dev`

### Admin
- Access at `http://localhost:8000/admin/`
- Create superuser: `python backend/manage.py createsuperuser`

## Deployment on Render

### Prerequisites
- Push project to a GitHub repository:
  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  git remote add origin https://github.com/yourusername/spa-website.git
  git push -u origin main
