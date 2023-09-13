from django.shortcuts import render
from rest_framework import viewsets
from QA_APP.models import Questions
from QA_APP.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class Custom08ObjectPagination(PageNumberPagination):

    def get_page_size(self, request):
        return 1

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'current_page':self.page.number,
            'results': data
        })

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    # pagination_class = Custom08ObjectPagination
    