from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Release


class ReleaseListView(ListView):
    model = Release
    template_name = "pages/release-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Release.objects.all().order_by('-id')
        return context


class ReleaseDetailView(DetailView):
    model = Release
    template_name = "pages/release-detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object'] = Supplier.objects.get(id=self.kwargs['pk'])
    #     context['cloths'] = Cloth.objects.filter(supplier_id=self.kwargs['pk'])

    #     return context
