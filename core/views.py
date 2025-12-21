from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from problems.models import Problem, Solution, Comment, Upvote, Blog, AI_Tool
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
    blogs_created = Blog.objects.filter(author=user).count()
    ai_tools_created = AI_Tool.objects.filter(author=user).count()
    upvotes_received = 0  # This would need to be calculated from upvotes
    
    # Get recent problems (all problems, not just user's)
    recent_problems = Problem.objects.all().order_by('-created_at')[:5]
    recent_blogs = Blog.objects.filter(status='published').order_by('-created_at')[:5]
    recent_ai_tools = AI_Tool.objects.all().order_by('-created_at')[:5]
    
    context = {
        'user': user,
        'problems_created': problems_created,
        'solutions_submitted': solutions_submitted,
        'comments_posted': comments_posted,
        'blogs_created': blogs_created,
        'ai_tools_created': ai_tools_created,
        'upvotes_received': upvotes_received,
        'recent_problems': recent_problems,
        'recent_blogs': recent_blogs,
        'recent_ai_tools': recent_ai_tools,
    }
    return render(request, 'core/dashboard.html', context)