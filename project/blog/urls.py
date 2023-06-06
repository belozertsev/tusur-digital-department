from django.urls import path, re_path
from django.shortcuts import render
from .controllers import accountController, apiController

urlpatterns = [
    path('account/register', accountController.register),
    path('account/login', accountController.login),

    path('api/posts/<str:_parameter>', apiController.posts),
    path('api/settings', apiController.settings),
    path('api/settings/check', apiController.settingsCheck),
    path('api/settings/add', apiController.settingsAdd),

    path('api/friends', apiController.friends),
    
    re_path(r'.*', apiController.returnReactApp)
]
