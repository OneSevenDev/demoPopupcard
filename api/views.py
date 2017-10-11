from django.http import JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api.serializers import CommentSerializer

# Create your views here.
from apps.popup_card.models import Comment


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def comment_list(request, slug):
    if request.method == 'GET':
        snippets = Comment.objects.all()
        serializer = CommentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsAdminUser,)