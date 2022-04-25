from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import EducationalProgram, UserEducationalProgram


class EducationalProgramDetailView(DetailView):
    model = EducationalProgram
    template_name = "pages/educational-program-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        object = EducationalProgram.objects.get(id=self.kwargs['pk'])
        context['object'] = object
        context['count_users'] = UserEducationalProgram.objects.filter(educational_program=object).count()

        try:
            if self.request.user.is_authenticated:
                is_user_in_program = UserEducationalProgram.objects.get(
                educational_program = object,
                user = self.request.user
                )
                if is_user_in_program:
                    context['is_user_in_program'] = True
        except UserEducationalProgram.DoesNotExist:
            context['is_user_in_program'] = False

        return context

def registration_to_program(request, pk):
    """
    Запись на программу
    """
    user_educational_program = UserEducationalProgram.objects.create(
        user = request.user,
        educational_program_id = pk,

    )
    user_educational_program.save()
    return HttpResponseRedirect(reverse('user:success'))
