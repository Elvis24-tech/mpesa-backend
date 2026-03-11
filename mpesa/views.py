# mpesa_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests, datetime, base64
import os

# Get access token from Safaricom sandbox
def get_access_token():
    consumer_key = os.getenv("MPESA_CONSUMER_KEY")
    consumer_secret = os.getenv("MPESA_CONSUMER_SECRET")
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    try:
        response = requests.get(url, auth=(consumer_key, consumer_secret))
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        return data.get("access_token")
    except Exception as e:
        print("Access token error:", e)
        print("RAW RESPONSE:", response.text if 'response' in locals() else "No response")
        return None

@api_view(['POST'])
def stk_push(request):
    try:
        phone = request.data.get("phone")
        amount = request.data.get("amount")

        if not phone or not amount:
            return Response({"error": "Phone and amount are required"}, status=400)

        business_short_code = os.getenv("MPESA_SHORTCODE")
        lipa_na_mpesa_online_passkey = os.getenv("MPESA_PASSKEY")
        callback_url = os.getenv("MPESA_CALLBACK_URL")
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        password = base64.b64encode(f"{business_short_code}{lipa_na_mpesa_online_passkey}{timestamp}".encode()).decode()

        payload = {
            "BusinessShortCode": business_short_code,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://mydomain.com/mpesa-express-simulate/",
            "AccountReference": "GroceryMart",
            "TransactionDesc": "Payment test"
        }

        access_token = get_access_token()
        if not access_token:
            return Response({"error": "Failed to get access token"}, status=500)

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.post(
            "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
            json=payload,
            headers=headers
        )

        try:
            data = response.json()
        except Exception:
            data = {"error": "Invalid response from M-Pesa", "raw_response": response.text}

        return Response(data)

    except Exception as e:
        return Response({"error": str(e)})