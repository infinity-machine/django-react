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
        print(f'request: {request}')
        print(f'request.data: {request.data}')
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
        print(request)
        userObj = UserModel.objects.get(pk=pk)
        try:
            userObj = UserModel.objects.get(pk = pk)
            userObj.delete()
        except:
            return Response('BOI NOT FOUND IN DATABASE')
        return Response(200)