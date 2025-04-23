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


### Steps to Deploy on Render

Below is a clear, step-by-step guide for deploying the spa website on Render, tailored for your wife to follow.

#### 1. Prepare the Project
- **Push to GitHub**:
  1. Create a repository on [GitHub.com](https://github.com).
  2. In your project folder:
     ```bash
     cd spa-website
     git init
     git add .
     git commit -m "Initial commit"
     git remote add origin https://github.com/yourusername/spa-website.git
     git push -u origin main
     ```
- **Install Dependencies**:
  - Backend: `cd backend && pip install -r requirements.txt`
  - Frontend: `cd frontend && npm install`
- **Test Locally**:
  - Backend: `python backend/manage.py runserver`
  - Frontend: `cd frontend && npm run dev`
  - Ensure all features work (subscription, contact, booking, etc.).
- **Set Permissions**:
  - Run `chmod +x backend/build.sh` to make the build script executable.

#### 2. Create a PostgreSQL Database
1. Sign up or log in to [Render.com](https://render.com).
2. In the Render Dashboard, click **New** > **PostgreSQL**.
3. Configure:
   - **Name**: `spa-db`
   - **Region**: Oregon
   - **Plan**: Free (expires after 90 days)
4. Click **Create Database**.
5. Wait for the status to show **Available**.
6. Copy the **Internal Database URL** (e.g., `postgresql://user:password@host:port/dbname`) from the **Connections** section.

#### 3. Deploy Django Backend
1. In the Render Dashboard, click **New** > **Web Service**.
2. Connect your GitHub repository and select `spa-website`.
3. Configure:
   - **Name**: `spa-backend`
   - **Region**: Oregon
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Environment**: Python
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn spa.wsgi:application`
   - **Plan**: Free
4. Add environment variables:
   - `PYTHON_VERSION`: `3.9`
   - `DATABASE_URL`: Paste the Internal Database URL from Step 2
   - `SECRET_KEY`: Generate with `openssl rand -hex 32` or any random string
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `.onrender.com`
   - `CORS_ALLOWED_ORIGINS`: `https://spa-frontend.onrender.com` (update after frontend deployment)
   - `EMAIL_HOST`: `smtp.mailgun.org`
   - `EMAIL_PORT`: `587`
   - `EMAIL_HOST_USER`: Your Mailgun user (from mailgun.com)
   - `EMAIL_HOST_PASSWORD`: Your Mailgun password
   - `STRIPE_SECRET_KEY`: Your Stripe secret key (from stripe.com)
   - `FRONTEND_URL`: `https://spa-frontend.onrender.com` (update later)
5. Click **Create Web Service**.
6. Wait for deployment (status: **Live**). Note the URL (e.g., `https://spa-backend.onrender.com`).

#### 4. Deploy Svelte Frontend
1. In the Render Dashboard, click **New** > **Static Site**.
2. Connect your repository and select `spa-website`.
3. Configure:
   - **Name**: `spa-frontend`
   - **Region**: Oregon
   - **Branch**: `main`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Publish Directory**: `build`
   - **Plan**: Free
4. Add environment variable:
   - `VITE_API_URL`: `https://spa-backend.onrender.com`
5. Click **Create Static Site**.
6. Wait for deployment (status: **Live**). Note the URL (e.g., `https://spa-frontend.onrender.com`).

#### 5. Update CORS and Test
1. In the Render Dashboard, go to `spa-backend` > **Environment**.
2. Update:
   - `CORS_ALLOWED_ORIGINS`: `https://spa-frontend.onrender.com`
   - `FRONTEND_URL`: `https://spa-frontend.onrender.com`
3. Test the site:
   - Visit `https://spa-frontend.onrender.com`.
   - Test email subscription, contact form, booking, shop, login, and employee portal.
   - Access the admin at `https://spa-backend.onrender.com/admin/` (create a superuser locally first with `python backend/manage.py createsuperuser`).
4. Verify media uploads (e.g., product images) work by testing in the admin.

#### 6. Optional: Custom Domain
1. Purchase a domain (e.g., via Namecheap or GoDaddy).
2. In Render Dashboard, for each service (`spa-backend`, `spa-frontend`):
   - Go to **Settings** > **Custom Domains**.
   - Add your domain (e.g., `api.spasite.com` for backend, `www.spasite.com` for frontend).
3. At your registrar, update DNS:
   - Backend: Add a CNAME record pointing to `spa-backend.onrender.com`.
   - Frontend: Add a CNAME record pointing to `spa-frontend.onrender.com`.
4. Update backend environment variables:
   - `ALLOWED_HOSTS`: Add `api.spasite.com`
   - `CORS_ALLOWED_ORIGINS`: Add `https://www.spasite.com`
   - `FRONTEND_URL`: `https://www.spasite.com`

#### 7. Automate with `render.yaml` (Alternative)
Instead of manual setup:
1. Ensure `backend/render.yaml` has correct credentials (Mailgun, Stripe, frontend URL).
2. In Render Dashboard, click **Blueprints** > **New Blueprint Instance**.
3. Select your repository and click **Apply**.
4. Render deploys the database and backend automatically. Deploy the frontend manually as a static site (Step 4).

### Notes
- **Stre**: Replace `your-stripe-publishable-key` in `frontend/src/pages/Shop.svelte` with your Stripe publishable key from stripe.com.
- **Dynamic IDs**: In `Booking.svelte` and `Shop.svelte`, replace `service: 1`, `employee: 1`, `order_id: 1` with dropdowns for dynamic selection.
- **Free Tier**: Render’s free PostgreSQL expires after 90 days, and services sleep after inactivity. Upgrade to paid plans for production.
- **Security**: Render provides free TLS certificates. Store sensitive data in environment variables.
- **Media Files**: Render’s disk is ephemeral; for production, use a service like Cloudinary for media storage.
- **Time Estimate**: Deployment takes ~1–2 hours if the codebase is ready.

This provides a complete, Render-ready codebase with all files, comments, and deployment steps. 
