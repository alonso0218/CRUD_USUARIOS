from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


# Create your views here.


class hello_api(APIView):
    serializer_class = serializers.hello_serializers 
    def get(self, request, format=None):

        an_apiview = [
        'usamos metodos http como funciones (get , post, delete,patch, put)',
        'es similar a una vista tradicional de django'
        'nos da mayor logica sobre nuestra aplicacion'
        'esta mapeado manualmente a los url'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
   

    def post(self,request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'hello {name}'
            return Response({'message': message})
        else: 
           return Response(
               serializers.errors,
               status.status.HTTP_400_BAD_REQUEST
           )
 #EL METODO PUT MANTIENE ACTUALIZADO UN OBJETO   
    def put(self, request, pk=None):
        return Response({'method':'PUT'})
# EL METODO PATCH MANTIENE PARCIALMENTE ACTUALIZADO UN OBJETO
    def patch(self,request, pk =None ):
        return Response({'method':'PATCH'})
#BORRA UN OBJETO
    def delete(self,request, pk =None ):
        return Response({'method':'DELETE'})