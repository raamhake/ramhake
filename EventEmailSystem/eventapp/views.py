# eventapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from eventapp.models import Event, EmailLog
from eventapp.serializers import EventSerializer, EmailLogSerializer

class SendEventEmailsView(APIView):
    def get(self, request):
        # Call the email sending logic here
        return Response({'message': 'Email sending process initiated'})

class EmailLogListView(APIView):
    def get(self, request):
        email_logs = EmailLog.objects.all()
        serializer = EmailLogSerializer(email_logs, many=True)
        return Response(serializer.data)
