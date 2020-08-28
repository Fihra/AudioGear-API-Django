from django.shortcuts import render
# Imports needed
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import AudioGear
from .serializers import AudioGearSerializer
from django.views.decorators.csrf import csrf_exempt
# decorators api view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#Generic API View
from rest_framework import generics, mixins

#Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Generic Class API

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = AudioGearSerializer
    queryset = AudioGear.objects.all()

    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def patch(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

class AudioGearAPIView(APIView):
    
    def get(self, request):
        audiogears = AudioGear.objects.all()
        serializer = AudioGearSerializer(audiogears, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AudioGearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Class API

class AudioGearDetails(APIView):
    def get_object(self, id):
        try:
            return AudioGear.objects.get(id=id)
        except AudioGear.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        audiogear = self.get_object(id)
        serializer = AudioGearSerializer(audiogear)
        return Response(serializer.data)

    def patch(self, request, id):
        audiogear = self.get_object(id)
        serializer = AudioGearSerializer(audiogear, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        audiogear = self.get_object(id)
        audiogear.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Function-Based Views

# @csrf_exempt ///don't need in api_view 
@api_view(['GET', 'POST'])
# Create your views here.
def audiogear_list(request):
    if request.method == 'GET':
        audiogears = AudioGear.objects.all()
        serializer = AudioGearSerializer(audiogears, many=True)
        # return JsonResponse(serializer.data, safe = False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = AudioGearSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE'])
def audiogear_detail(request, pk):
    try:
        audiogear = AudioGear.objects.get(pk=pk)
    
    except AudioGear.DoesNotExist:
        # return HttpResponse(status=404)
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AudioGearSerializer(audiogear)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        # data = JSONParser().parse(request)
        print("VALID?")
        print(request.data)
        serializer = AudioGearSerializer(audiogear, data=request.data)
        if serializer.is_valid():
            
            
            serializer.save()
            # return JsonResponse(serializer.data)
            print(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        audiogear.delete()
        # return HttpResponse(status=204)
        return Response(status.HTTP_204_NO_CONTENT)