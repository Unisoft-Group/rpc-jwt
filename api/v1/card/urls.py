from django.urls import path

from api.v1.card import view

urlpatterns = [
    path('', view.info)

]
