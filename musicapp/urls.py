from django.urls import path
from OudMusic import settings
# from django.contrib.auth.views import LogoutView

from musicapp.views import (
    trackDetails,
    addTrack,
    deleteTrack,
    updateTrack,
)


urlpatterns = [
    path("add", addTrack, name="addTrack"),
    path("details/<slug:slug>", trackDetails, name="trackDetail"),
    path("delete/<slug:slug>", deleteTrack, name="deleteTrack"),
    path("update/<slug:slug>", updateTrack, name="updateTrack"),
]
