from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from django.http import Http404
from rest_framework.views import APIView


class ArticleList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        res = {"status": "success", "result": serializer.data}
        return Response(res)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # article = self.get_object(pk)
        try:
            article = Article.objects.get(pk=pk)

            serializer = ArticleSerializer(article)
            res = {"status": "success", "result": serializer.data}
            return Response(res)

        except Article.DoesNotExist:
            notFound = {"status": "error", "result": []}
            return Response(notFound)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
