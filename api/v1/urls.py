from django.urls import path, include

urlpatterns = [
    path('card/', include('api.v1.card.urls'))
]
