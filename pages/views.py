from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page