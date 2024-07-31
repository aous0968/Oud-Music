from django.urls import path
from OudMusic import settings
# from django.contrib.auth.views import LogoutView

from controlPanle.views import (
    index,
    TracksControlPanle,
)


urlpatterns = [
    path("", index, name="control_panle"),
    path("tracks", TracksControlPanle, name="tracks_control_panle"),
]
