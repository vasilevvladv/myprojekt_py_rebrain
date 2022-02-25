from django.urls import path

from .views import (ServerAddView, ServerDetailView, ServerStatusSet,
                    ServerViewSet)

urlpatterns = [
    path('servers/', ServerViewSet.as_view()),
    path('servers/<int:pk>', ServerDetailView.as_view()),
    path('servers/add', ServerAddView.as_view()),
    path('servers/status', ServerStatusSet.as_view()),
]
