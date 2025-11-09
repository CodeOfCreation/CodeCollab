from django.urls import path
from . import views

urlpatterns = [
    path('', views.problems_list, name='problems_list'),
    path('<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('create/', views.create_problem, name='create_problem'),
]