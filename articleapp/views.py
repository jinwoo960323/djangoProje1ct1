from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleapp.models import Article
from articleapp.templates.forms import ArticleCreationForm


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)