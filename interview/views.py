from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404



from .models import Category, QuestionAnswer
from .serializer import CategorySerializer, QuestionAnswerSerializer, QuestionSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerListCreateAPIView(ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'question']


    def get_queryset(self):
        queryset = QuestionAnswer.objects.order_by('-importance')
        return queryset

    def perform_create(self, serializer):
        serializer.save()

class QuestionAnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionSerializer


    def get_queryset(self):
        queryset = self.queryset.order_by('importance')
        return queryset

