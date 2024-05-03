from rest_framework import serializers

from demo.models import StudentClasses

class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClasses
        fields = '__all__'

        
