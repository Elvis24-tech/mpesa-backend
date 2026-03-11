from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import stk_push


@api_view(["POST"])
def stkpush(request):

    phone = request.data.get("phone")
    amount = request.data.get("amount")

    if not phone or not amount:
        return Response({"error": "Phone and amount required"}, status=400)

    response = stk_push(phone, amount)

    return Response(response)


@api_view(["POST"])
def mpesa_callback(request):

    data = request.data

    print("M-Pesa Callback Data:", data)

    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})