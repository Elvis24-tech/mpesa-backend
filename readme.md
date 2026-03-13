# 🏦 GroceryMart Backend
A **Django REST backend** for GroceryMart that manages products, shopping carts, and **M-Pesa STK Push payments** using Safaricom Daraja API.

This backend is deployed on **Render** and communicates with a **React frontend** deployed on Vercel.

---

##  Live API

**Backend API:**  
https://mpesa-backend-1rkj.onrender.com

**Frontend (for reference):**  
https://grocerymart-delta.vercel.app

---

## Features

### 🛒 Shopping & Cart
- Provides endpoints for products and cart management
- Returns JSON responses for easy integration with frontend

### 📱 M-Pesa Integration
- STK Push payment requests
- Callback endpoint to handle M-Pesa responses
- Secure handling of consumer key, secret, and passkey via environment variables

### ⚡ API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/mpesa/stkpush/` | POST | Initiate M-Pesa STK Push payment |
| `/api/mpesa/callback/` | POST | Receive payment callback from Safaricom |
| `/admin/` | GET | Django admin panel |

---

##  Tech Stack

- **Backend:** Django 6.0, Django REST Framework 3.16  
- **Database:** SQLite (default, can be swapped for PostgreSQL)  
- **Payment Integration:** Safaricom Daraja API (M-Pesa STK Push)  
- **Deployment:** Render  

---

##  Project Structure
mpesa_project/
├── mpesa/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── mpesa_project/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/
├── .env
├── .gitignore
├── build.sh
├── db.sqlite3
├── manage.py
├── readme.md
├── render.yaml
├── requirements.txt
└── start.sh


---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Elvis24-tech/mpesa-backend
cd grocerymart-backend

## Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

## Install dependencies:
pip install -r requirements.txt

## Set up environment variables in a .env file:
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,mpesa-backend-1rkj.onrender.com

MPESA_CONSUMER_KEY=your_consumer_key
MPESA_CONSUMER_SECRET=your_consumer_secret
MPESA_SHORTCODE=174379
MPESA_PASSKEY=your_passkey
MPESA_CALLBACK_URL=https://mpesa-backend-1rkj.onrender.com/api/mpesa/callback/

## Run migrations and start the server:
python manage.py migrate
python manage.py runserver

## API Usage
 STK Push Request
- POST /api/mpesa/stkpush/
Request body:

{
  "phone": "254712345678",
  "amount": 500
}

## Response:

{
  "MerchantRequestID": "12345",
  "CheckoutRequestID": "ws_CO_12345",
  "ResponseCode": "0",
  "ResponseDescription": "Success. Request accepted for processing",
  "CustomerMessage": "Success. Request accepted for processing"
}

## Callback
- POST /api/mpesa/callback/
- Safaricom sends the payment result here
- Logs callback for debugging
- Returns status {"status": "success"}

 ## Security
- Sensitive keys and passkeys are stored in environment variables
- M-Pesa integration uses base64-encoded passwords and timestamping
- Debug should be set to False in production

## Mobile Support
- The backend is fully compatible with mobile frontend, allowing users to initiate payments from phones via STK Push.

## Future Improvements
- Connect orders to authenticated users
- Store transaction history in the database
- Email/SMS notifications on successful payment
- Add product management API for admin

## Author
- Elvis Muasya
- Fullstack Developer

Skills: HTML, CSS, JavaScript, React, Tailwind CSS, Python, Django, Flask

##License
This project is for educational and portfolio purposes.