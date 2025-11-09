from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from problems.models import Problem, Solution, Comment
from users.models import CustomUser


def index(request):
    """Home page view"""
    return render(request, 'core/index.html')


@login_required
def dashboard(request):
    """Dashboard view showing user's activity"""
    user = request.user
    
    # Get user stats
    problems_created = Problem.objects.filter(author=user).count()
    solutions_submitted = Solution.objects.filter(author=user).count()
    comments_posted = Comment.objects.filter(author=user).count()
    total_upvotes = 0  # This would need to be calculated from upvotes
    
    # Get recent problems (all problems, not just user's)
    recent_problems = Problem.objects.all().order_by('-created_at')[:5]
    
    context = {
        'user': user,
        'problems_created': problems_created,
        'solutions_submitted': solutions_submitted,
        'comments_posted': comments_posted,
        'total_upvotes': total_upvotes,
        'recent_problems': recent_problems,
    }
    return render(request, 'core/dashboard.html', context)