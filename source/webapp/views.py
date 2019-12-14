from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.mixins import StatsMixin
from webapp.models import Photo
# from webapp.mixins import StatsMixin


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


class PhotoCreateView(StatsMixin, CreateView):
    template_name = 'photo/create.html'
    model = Photo
    # form_class = PhotoForm
    fields = ['image', 'description', 'author_name', 'likes']

    def get_success_url(self):
        return reverse('webapp:index')


class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'photo/update.html'
    fields = ['image', 'description', 'author_name', 'likes']
    context_object_name = 'obj'
    def get_success_url(self):
        return reverse('webapp:index')


class PhotoDeleteView(DeleteView):
    template_name = 'photo/delete.html'
    model = Photo
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:index')