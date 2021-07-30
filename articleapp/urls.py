from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articaleapp/list.html'), name='list')

]