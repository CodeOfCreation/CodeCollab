from django.urls import path
from . import views

urlpatterns = [
    # Specific patterns first
    path('create/', views.create_problem, name='create_problem'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blog/create/', views.create_blog, name='create_blog'),
    path('upvote/solution/<int:solution_id>/', views.upvote_solution, name='upvote_solution'),
    path('comment/<int:problem_id>/', views.add_comment, name='add_comment'),
    
    # General patterns last
    path('<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    
    # Default pattern last
    path('', views.problems_list, name='problems_list'),
]