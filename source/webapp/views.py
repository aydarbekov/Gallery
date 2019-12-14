from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Photo


class IndexView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photos'
    model = Photo
    ordering = '-creation_date'
    # paginate_by = 5
    # paginate_orphans = 1


class PhotoView(DetailView):
    template_name = 'photo/detail.html'
    pk_url_kwarg = 'pk'
    model = Photo
