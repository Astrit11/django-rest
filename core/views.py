from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Breed, Dog
from django.forms.models import model_to_dict
from .serializers import BreedSerializer, DogSerializer
from rest_framework.parsers import MultiPartParser


# Create your views here.

class BreedView(APIView):
    def post(self, request):
        serializer_class = BreedSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=200)
        return JsonResponse(serializer_class.errors, status=400)

    def get(self, request):
        queryset = Breed.objects.all().values()
        return JsonResponse({'message': list(queryset), 'status': 'success'}, status=200)


class DogsView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        serializer_class = DogSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=200)
        return JsonResponse(serializer_class.errors, status=400)

    def get(self, request, breed_id=None):
        if breed_id is None:
            queryset = Dog.objects.all().values()
            queryset = list(queryset)
        else:
            queryset = Dog.objects.filter(breed_id=breed_id).order_by('?').values()
            queryset = list(queryset)
            if queryset:
                queryset = queryset[0]['image']
        return JsonResponse({'message': queryset, 'status': 'success'})

