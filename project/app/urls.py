from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'uploadScore/',upload_score),
    url(r'uploadScoreForm/',upload_score_form),
    url(r'rankInfo/',rank_info),
    url(r'searchRankInfo/',search_rank_info),
]