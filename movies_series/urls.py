from django.urls import path
from movies_series.viewsets import (RandomMovieSeriesView, 
                                    MovieSeriesListView,
                                    RateMovieSeriesView)
from movies_series.viewsets.user_rating_viewset import MarkMovieSeriesAsWatchedView
from rest_framework.routers import SimpleRouter

router = SimpleRouter() 

router.register(r'watched', MarkMovieSeriesAsWatchedView)
router.register(r'rate', RateMovieSeriesView)

urlpatterns =  router.urls + [
    path('random/', RandomMovieSeriesView.as_view(), name='random_movie_series'),
    path('list/', MovieSeriesListView.as_view(), name='movie_series_list'),
]