from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView

from .models import News, OurProjects, QualityLibrary, Site


class SiteListView(ListView):
    model = Site
    template_name = "pages/site-list.html"

class UsefulMaterialsView(TemplateView):
    template_name = "pages/useful-materials.html"

class QualityLibraryListView(ListView):
    model = QualityLibrary
    template_name = "pages/quality-library-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = QualityLibrary.objects.filter(type='book').order_by('-id')
        context['elec'] = QualityLibrary.objects.filter(type='elec').order_by('-id')
        return context


class OurProjectsListView(ListView):
    model = OurProjects
    template_name = "pages/our-projects-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = OurProjects.objects.all().order_by('-id')
        return context


class OurProjectsDetailView(DetailView):
    model = OurProjects
    template_name = "pages/our-projects-detail.html"


class NewsDetailView(DetailView):
    model = News
    template_name = "pages/news-detail.html"


class NewsListView(ListView):
    model = News
    paginate_by = 20
    template_name = "pages/news-list.html"
