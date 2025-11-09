from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from .forms import SignUpForm
from problems.models import Problem, Solution, Comment, Upvote


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    problems_created = Problem.objects.filter(author=user).count()
    solutions_submitted = Solution.objects.filter(author=user).count()
    comments_posted = Comment.objects.filter(author=user).count()
    upvotes_received = 0  # This would need to be calculated from upvotes
    
    # Get recent activity
    recent_problems = Problem.objects.filter(author=user).order_by('-created_at')[:5]
    recent_solutions = Solution.objects.filter(author=user).order_by('-created_at')[:5]
    recent_comments = Comment.objects.filter(author=user).order_by('-created_at')[:5]
    
    context = {
        'user': user,
        'problems_created': problems_created,
        'solutions_submitted': solutions_submitted,
        'comments_posted': comments_posted,
        'upvotes_received': upvotes_received,
        'recent_problems': recent_problems,
        'recent_solutions': recent_solutions,
        'recent_comments': recent_comments,
    }
    return render(request, 'users/profile.html', context)