from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import Mobiles
from api.serializer import MobileSerializer


class MobileListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        #deserialization query to py native
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        return Response(data={"message":"mobile list post"})
class MobileUpdateDetailDestroyView(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data={"message":"mobile detail"})
    
    def put(self,request,*args,**kwargs):
        return Response(data={"message":"mobile-update"})
    
    def delete(self,request,*args,**kwargs):
        return Response(data={"message":"mobile deleteview"})
    
    # loclahost:8000/api/mobile/{id}/