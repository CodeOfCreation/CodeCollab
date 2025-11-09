from django.urls import path
from . import views

urlpatterns = [
    path('', views.problems_list, name='problems_list'),
    path('<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('create/', views.create_problem, name='create_problem'),
    path('upvote/solution/<int:solution_id>/', views.upvote_solution, name='upvote_solution'),
    path('comment/<int:problem_id>/', views.add_comment, name='add_comment'),
]