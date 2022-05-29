from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import FeedbackUserBusinessGamesForm
from .models import BusinessGames, FeedbackUserBusinessGames, UserBusinessGames


class BusinessGamesDetailView(DetailView):
    model = BusinessGames
    template_name = "pages/business-games-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        object = BusinessGames.objects.get(id=self.kwargs['pk'])
        context['object'] = object
        context['count_users'] = UserBusinessGames.objects.filter(business_games=object).count()

        try:
            if self.request.user.is_authenticated:
                is_user_in_program = UserBusinessGames.objects.get(
                business_games = object,
                user = self.request.user
                )
                if is_user_in_program:
                    context['is_user_in_program'] = True
        except UserBusinessGames.DoesNotExist:
            context['is_user_in_program'] = False

        context['feedbacks'] = FeedbackUserBusinessGames.objects.filter(user_business_games_id=self.kwargs['pk']).order_by('-date_created')

        return context

def registration_to_program(request, pk):
    """
    Запись на программу
    """
    user_business_games = UserBusinessGames.objects.create(
        user = request.user,
        business_games_id = pk,

    )
    user_business_games.save()
    return HttpResponseRedirect(reverse('user:success'))


def send_feedback(request, pk):
    """
    Отправка отзыва
    """
    if request.method == 'POST':
        form = FeedbackUserBusinessGamesForm(request.POST)
        if form.is_valid():

            try:
                user_business_games = UserBusinessGames.objects.get(id=pk)
            except UserBusinessGames.DoesNotExist:
                return redirect('user:error')

            feedback = FeedbackUserBusinessGames(
                user=request.user,
                user_business_games=user_business_games,
                text=form.cleaned_data['text'],
            )
            feedback.save()
        return redirect('business:detail', pk=pk)
