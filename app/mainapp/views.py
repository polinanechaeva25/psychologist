from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView


class TitleContextMixin:

    def get_title(self):
        return getattr(self, 'title', '')

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        return context


class MainListView(TitleContextMixin, ListView):
    title = 'Psychologist from Miami'
    model = User
    template_name = 'mainapp/index.html'
