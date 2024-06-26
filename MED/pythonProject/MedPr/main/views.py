from django.shortcuts import render
from django.views.generic import DetailView
from .models import Questions


def index(request):
    return render(request, 'main/table.html')


class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'main/detail.html'
    context_object_name = 'question'
