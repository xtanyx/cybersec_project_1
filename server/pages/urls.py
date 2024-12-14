from django.urls import path

from .views import homePageView, saveView, secretsView, getSecretView
urlpatterns = [
    path('', homePageView, name='home'),
    path('save/', saveView, name='save'),
    path('secrets/', secretsView, name='secrets'),
    path('secret/', getSecretView, name='getSecret')
]