from django.urls import path

from . import views

app_name='app1'
urlpatterns=[
    path('', views.index, name='index'),
    #Path to DETAIL
    path('<int:question_id>/',views.detail, name='detail'),
    #Path to RESULTS
    path('<int:question_id>/results/',views.results, name='results'),
    #Path to VOTE
    path('<int:question_id>/vote/',views.vote, name='vote'),
]

