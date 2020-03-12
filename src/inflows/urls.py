from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inflows import views

urlpatterns = [
    path('inflows/', views.InflowList.as_view()),
    path('inflows/<str:pk>/', views.InflowDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
