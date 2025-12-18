from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Problem, Tag, Solution, Comment, Upvote, Blog
from .forms import ProblemForm, BlogForm


def problems_list(request):
    """List all problems with filters"""
    problems = Problem.objects.all().order_by('-created_at')
    tags = Tag.objects.all()
    
    # Apply filters
    difficulty = request.GET.get('difficulty', 'all')
    language = request.GET.get('language', 'all')
    tag_filter = request.GET.get('tag', 'all')
    
    if difficulty != 'all':
        problems = problems.filter(difficulty=difficulty)
    
    if language != 'all':
        problems = problems.filter(language=language)
    
    if tag_filter != 'all':
        problems = problems.filter(tags__name=tag_filter)
    
    context = {
        'problems': problems,
        'tags': tags,
        'selected_difficulty': difficulty,
        'selected_language': language,
        'selected_tag': tag_filter,
    }
    return render(request, 'problems/problems.html', context)


def problem_detail(request, problem_id):
    """View problem details and solutions"""
    problem = get_object_or_404(Problem, id=problem_id)
    problem.views += 1
    problem.save()
    
    solutions = problem.solutions.all().order_by('-upvotes', '-created_at')
    comments = problem.comments.all()
    
    # Check if current user has upvoted this problem
    user_upvoted = False
    if request.user.is_authenticated:
        user_upvoted = Upvote.objects.filter(user=request.user, problem=problem).exists()
    
    if request.method == 'POST' and request.user.is_authenticated:
        if 'code' in request.POST:  # Submit solution
            code = request.POST.get('code')
            explanation = request.POST.get('explanation', '')
            
            if code:
                solution = Solution.objects.create(
                    problem=problem,
                    author=request.user,
                    code=code,
                    explanation=explanation
                )
                messages.success(request, 'Solution submitted successfully!')
                return redirect('problem_detail', problem_id=problem.id)
            else:
                messages.error(request, 'Please enter your solution code.')
        
        elif 'comment' in request.POST:  # Add comment
            content = request.POST.get('comment')
            if content:
                Comment.objects.create(
                    problem=problem,
                    author=request.user,
                    content=content
                )
                messages.success(request, 'Comment added successfully!')
                return redirect('problem_detail', problem_id=problem.id)
            else:
                messages.error(request, 'Comment cannot be empty.')
        
        elif 'upvote' in request.POST:  # Upvote problem
            upvote, created = Upvote.objects.get_or_create(
                user=request.user,
                problem=problem
            )
            if created:
                problem.upvotes += 1
                problem.save()
                messages.success(request, 'Problem upvoted!')
            else:
                # Remove upvote if already exists
                upvote.delete()
                problem.upvotes -= 1
                problem.save()
                messages.info(request, 'Upvote removed.')
            
            return redirect('problem_detail', problem_id=problem.id)
    
    context = {
        'problem': problem,
        'solutions': solutions,
        'comments': comments,
        'user_upvoted': user_upvoted,
    }
    return render(request, 'problems/problem_detail.html', context)


@login_required
def create_problem(request):
    """Create a new problem"""
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.author = request.user
            problem.save()
            
            # Handle tags
            tags_str = form.cleaned_data.get('tags_str', '')
            if tags_str:
                tags_list = [tag.strip() for tag in tags_str.split(',')]
                for tag_name in tags_list:
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(name=tag_name.lower())
                        problem.tags.add(tag)
            
            return redirect('problem_detail', problem_id=problem.id)
    else:
        form = ProblemForm()
    
    return render(request, 'problems/create_problem.html', {'form': form})


@login_required
def upvote_solution(request, solution_id):
    """Upvote a solution"""
    solution = get_object_or_404(Solution, id=solution_id)
    upvote, created = Upvote.objects.get_or_create(
        user=request.user,
        solution=solution
    )
    
    if created:
        solution.upvotes += 1
        solution.save()
        messages.success(request, 'Solution upvoted!')
    else:
        # Remove upvote if already exists
        upvote.delete()
        solution.upvotes -= 1
        solution.save()
        messages.info(request, 'Upvote removed.')
    
    return redirect('problem_detail', problem_id=solution.problem.id)


@login_required
def add_comment(request, problem_id):
    """Add a comment to a problem"""
    problem = get_object_or_404(Problem, id=problem_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                problem=problem,
                author=request.user,
                content=content
            )
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'Comment cannot be empty.')
    
    return redirect('problem_detail', problem_id=problem.id)


# Blog Views
def blog_list(request):
    """List all published blogs"""
    blogs = Blog.objects.filter(status='published').order_by('-created_at')
    draft_blogs = []
    
    if request.user.is_authenticated:
        draft_blogs = Blog.objects.filter(author=request.user, status='draft').order_by('-created_at')
    
    context = {
        'blogs': blogs,
        'draft_blogs': draft_blogs,
    }
    return render(request, 'problems/blogs.html', context)


def blog_detail(request, slug):
    """View blog details"""
    blog = get_object_or_404(Blog, slug=slug)
    if blog.status == 'draft' and blog.author != request.user:
        # Only allow author to view their own draft
        if not request.user.is_authenticated or blog.author != request.user:
            return redirect('blog_list')
    
    blog.views += 1
    blog.save()
    
    comments = blog.comments.all()
    
    # Check if current user has upvoted this blog
    user_upvoted = False
    if request.user.is_authenticated:
        user_upvoted = Upvote.objects.filter(user=request.user, blog=blog).exists()
    
    if request.method == 'POST' and request.user.is_authenticated:
        if 'comment' in request.POST:  # Add comment
            content = request.POST.get('comment')
            if content:
                Comment.objects.create(
                    blog=blog,
                    author=request.user,
                    content=content
                )
                messages.success(request, 'Comment added successfully!')
                return redirect('blog_detail', slug=blog.slug)
            else:
                messages.error(request, 'Comment cannot be empty.')
        
        elif 'upvote' in request.POST:  # Upvote blog
            upvote, created = Upvote.objects.get_or_create(
                user=request.user,
                blog=blog
            )
            if created:
                blog.upvotes += 1
                blog.save()
                messages.success(request, 'Blog upvoted!')
            else:
                # Remove upvote if already exists
                upvote.delete()
                blog.upvotes -= 1
                blog.save()
                messages.info(request, 'Upvote removed.')
            
            return redirect('blog_detail', slug=blog.slug)
    
    context = {
        'blog': blog,
        'comments': comments,
        'user_upvoted': user_upvoted,
    }
    return render(request, 'problems/blog_detail.html', context)


@login_required
def create_blog(request):
    """Create a new blog"""
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            
            # Handle tags
            tags_str = form.cleaned_data.get('tags_str', '')
            if tags_str:
                tags_list = [tag.strip() for tag in tags_str.split(',')]
                for tag_name in tags_list:
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(name=tag_name.lower())
                        blog.tags.add(tag)
            
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm()
    
    return render(request, 'problems/create_blog.html', {'form': form})