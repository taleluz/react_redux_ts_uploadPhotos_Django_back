from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from .models import Imgs
# Create your views here.


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imgs
        fields = '__all__'


class imgView(APIView):
    def get(self, request):
        my_model = Imgs.objects.all()
        serializer = ImgSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = ImgSerializer(data=request.data, context={
                                   'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        my_model = Imgs.objects.get(pk=pk)
        serializer = ImgSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        my_model = Imgs.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def test(req):
    return Response("Test")


@api_view(["GET"])
def testdata(req):
    return Response([{'test': 20}, {'baga': 10}])
