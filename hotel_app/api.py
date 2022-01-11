from rest_framework import generics 
from .serializers import AppartmentSerializer , LoginSerializer, UserSerializer
from .models import Appartments
from rest_framework.response import  Response
from knox.models import AuthToken


# class LoginApiPost(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self,request,*args,**kwargs):
#         print(request.data)
#         serializer = self.get_serializer(data= request.data)
#         serializer.is_valid(raise_exception= True)
#         user = serializer.validated_data
#         return Response({"user":UserSerializer(user,context=self.get_serializer_context()).data , "token": AuthToken.objects.create(user)[1]})


class ApartmentAPI(generics.GenericAPIView):
    serializer_class = AppartmentSerializer

    def get(self,request,*args,**kwargs):
        appartment = Appartments.objects.all()
        serializer = AppartmentSerializer(appartment, many=True)
        return Response(serializer.data)

    def post(self, request, *args,**kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"thank":"yes"})

    
        


