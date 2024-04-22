from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CinemasView, CinemasSearchView

router = DefaultRouter()

router.register("cinemas", CinemasView, "cinemas")
router.register("search_cinema", CinemasSearchView, "search_cinema")

urlpatterns = [
    path("", include(router.urls)),
]
