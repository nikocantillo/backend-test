from django.urls import path
from movies_series.viewsets import (RandomMovieSeriesViewSet, 
                                    MovieViewSet,
                                    MovieMarkAsWatchedViewSet,
                                    MovieRateViewSet)
from rest_framework.routers import SimpleRouter

router = SimpleRouter() 


router.register(r'movies_watched', MovieMarkAsWatchedViewSet)
router.register(r'movies_rate', MovieRateViewSet)
router.register(r'random', RandomMovieSeriesViewSet)
router.register(r'list', MovieViewSet)



urlpatterns =  router.urls + []