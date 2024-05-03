from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from demo.serializers import StudentClassSerializer
from demo.models import StudentClasses

class StudentClassesView(APIView):
    def get(self,request):
        email = self.request.headers['email']
        try:
            className = StudentClasses.objects.filter(email = email)
        except:
            return Response("No classes yet!!",status=status.HTTP_400_BAD_REQUEST)
        serialized = StudentClassSerializer(className,many=True)
        return Response(serialized.data)
    
    def post(self,request):
        data = {}
        data['email'] = request.data.get('email')
        data['className'] =  request.data.get('className')
        serializer = StudentClassSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request):
        email = request.data.get('email')
        className = request.data.get('className')
        try:
            studentClasses = StudentClasses.objects.filter(email = email).filter(className = className)
        except StudentClasses.DoesNotExist:
            return Response("Student's wishlist doesn't have this class")
        else:
            studentClasses.delete()
            return Response("Class has been removed from your wishlist")
 