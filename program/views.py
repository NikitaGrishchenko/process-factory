from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import FeedbackToEducationalProgramForm
from .models import (EducationalProgram, FeedbackToEducationalProgram,
                     UserEducationalProgram)


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

        context['feedbacks'] = FeedbackToEducationalProgram.objects.filter(educational_program_id=self.kwargs['pk']).order_by('-date_created')

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



def send_feedback(request, pk):
    """
    Отправка отзыва
    """
    if request.method == 'POST':
        form = FeedbackToEducationalProgramForm(request.POST)
        if form.is_valid():

            try:
                educational_program = EducationalProgram.objects.get(id=pk)
            except EducationalProgram.DoesNotExist:
                return redirect('user:error')

            feedback = FeedbackToEducationalProgram(
                user=request.user,
                educational_program=educational_program,
                text=form.cleaned_data['text'],
            )
            feedback.save()
        return redirect('program:detail', pk=pk)
