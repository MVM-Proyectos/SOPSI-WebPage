from django.urls import path
from . import views

app_name='app1'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    #path to DETAIL
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    #Path to RESULTS
    path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),
    #Path to VOTE
    path('<int:question_id>/vote/',views.vote, name='vote'),
]

