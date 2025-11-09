from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Problem, Tag, Solution
from .forms import ProblemForm, SolutionForm


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
    
    solutions = problem.solutions.all()
    
    if request.method == 'POST' and request.user.is_authenticated:
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
    
    context = {
        'problem': problem,
        'solutions': solutions,
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