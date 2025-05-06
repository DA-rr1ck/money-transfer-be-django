from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from decimal import Decimal
from .models import Transfer, UserProfile
from .serializers import TransferSerializer

class LoginAPI(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)

class TransferAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        receiver_username = request.data.get('receiver')
        amount = Decimal(request.data.get('amount'))
        sender_profile = request.user.userprofile
        try:
            receiver = User.objects.get(username=receiver_username)
            receiver_profile = receiver.userprofile

            if sender_profile.balance >= amount:
                sender_profile.balance -= amount
                receiver_profile.balance += amount
                sender_profile.save()
                receiver_profile.save()
                Transfer.objects.create(sender=request.user, receiver=receiver, amount=amount)
                return Response({'status': 'success'})
            else:
                return Response({'error': 'Insufficient balance'}, status=400)
        except User.DoesNotExist:
            return Response({'error': 'Receiver not found'}, status=400)
