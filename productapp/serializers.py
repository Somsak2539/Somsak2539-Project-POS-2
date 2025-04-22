

from rest_framework import serializers

from productapp.models import Product1

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product1
        
       # fields=["title","description","active"]  
         
        fields="__all__"
        
class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model=Product1
        
       
         
        fields="__all__"