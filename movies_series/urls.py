from django.urls import path
from movies_series.viewsets import (RandomMovieSeriesView, 
                                    MovieSeriesListView, 
                                    MarkMovieSeriesAsWatchedView, 
                                    RateMovieSeriesView)


urlpatterns = [
    path('random/', RandomMovieSeriesView.as_view(), name='random_movie_series'),
    path('list/', MovieSeriesListView.as_view(), name='movie_series_list'),
    path('watched/<int:user_rating_id>/', MarkMovieSeriesAsWatchedView.as_view(), name='mark_movie_series_watched'),
    path('rate/<int:user_rating_id>/', RateMovieSeriesView.as_view(), name='rate_movie_series'),
]