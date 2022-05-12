from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import BusinessGames, UserBusinessGames


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
