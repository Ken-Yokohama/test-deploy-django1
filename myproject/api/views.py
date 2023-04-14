from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Author
from api.serializers import AuthorSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    endpoints = {
        'Author List': '/author-list',
        'Author Detail': '/author-detail/<str:pk>',
        'CREATE': '/author-create',
        'UPDATE': '/author-list/<str:pk>',
        'DELETE': '/author-list/<str:pk>',
    }
    return Response(endpoints)

@api_view(['GET'])
def authorList(request):
    authors = Author.objects.all()
    serilizer = AuthorSerializer(authors, many=True)
    return Response(serilizer.data)

@api_view(['GET'])
def authorDetail(request, pk):
    author = Author.objects.get(id=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['POST'])
def authorCreate(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def authorUpdate(request, pk):
    author = Author.objects.get(id=pk)
    serializer = AuthorSerializer(author, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def authorDelete(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return Response("SUCCESFULLY DELETED")