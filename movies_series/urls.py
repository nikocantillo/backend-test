from django.urls import path
from movies_series.viewsets import (RandomMovieSeriesViewSet, 
                                    MovieViewSet,
                                    RateMovieSeriesView,
                                    MovieMarkAsWatchedViewSet,
                                    MovieRateViewSet)
from movies_series.viewsets.user_rating_viewset import MarkMovieSeriesAsWatchedView
from rest_framework.routers import SimpleRouter

router = SimpleRouter() 

router.register(r'watched', MarkMovieSeriesAsWatchedView)
router.register(r'rate', RateMovieSeriesView)
router.register(r'movies_watched', MovieMarkAsWatchedViewSet)
router.register(r'movies_rate', MovieRateViewSet)
router.register(r'random', RandomMovieSeriesViewSet)
router.register(r'list', MovieViewSet)



urlpatterns =  router.urls + []