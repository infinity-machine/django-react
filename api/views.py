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
        print(serialized.data)
        return Response(serialized.data)
    
    def post(self, request):
        print(f'post request: {request}')
        print(f'post request data: {request.data}')
        serializeObj = UserSerializer(data = request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class UsersDelete(APIView):
    def delete(self, request, pk):
        print(f'delete request: {request}')
        print(f'delete request data: {request.data}')
        userObj = UserModel.objects.get(pk=pk)
        try:
            userObj = UserModel.objects.get(pk = pk)
            userObj.delete()
        except:
            return Response('BOI NOT FOUND IN DATABASE')
        return Response(200)