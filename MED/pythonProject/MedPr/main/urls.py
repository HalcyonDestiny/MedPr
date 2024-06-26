from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.QuestionsDetailView.as_view(), name='questions-detail'),
]
