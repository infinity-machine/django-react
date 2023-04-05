from api.models import UserModel
from api.serialize import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# class ReactView():
#     def get(self, request):
#         return render(request, )

class UsersTable(APIView):
    def get(self, request):
        userObj = UserModel.objects.all()
        serialized = UserSerializer(userObj, many = True)
        return Response(serialized.data)
    
    def post(self, request):
        serializeObj = UserSerializer(data = request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class UsersDelete(APIView):
    def delete(self, request, pk):
        userObj = UserModel.objects.get(pk=pk)
        try:
            userObj = UserModel.objects.get(pk = pk)
            print(userObj)
            userObj.delete()
        except:
            return Response('BOI NOT FOUND IN DATABASE')
        return Response(200)