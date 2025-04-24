from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import * 
from django.utils import timezone
from  rest_framework.response  import Response
from rest_framework  import status
class TaskCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Create a new task."""
        data = request.data
        data['assigned_to'] = request.user.id  # Set the assigned user to the current user
        serializer = TaskCreateSerializer(data=data)
        
        if serializer.is_valid():
            task = serializer.save()
            task.updated_at = timezone.now()
            task.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)