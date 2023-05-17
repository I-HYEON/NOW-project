from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializer import ArticlesListSerializer, CommentSerializer, ArticleSerializer
from .models import Article, Comment

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticlesListSerializer(articles, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'DELETE', 'PUT'])
# def article_detail(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)