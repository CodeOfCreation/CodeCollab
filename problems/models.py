from django.db import models
from users.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('c', 'C'),
        ('cpp', 'C++'),
        ('javascript', 'JavaScript'),
        ('go', 'Go'),
        ('rust', 'Rust'),
        ('r', 'R'),
        ('ruby', 'Ruby'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='problems')
    upvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    test_cases = models.TextField(blank=True)
    
    def __str__(self):
        return self.title


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='solutions')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='solutions')
    code = models.TextField()
    explanation = models.TextField(blank=True)
    upvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Solution by {self.author.username} for {self.problem.title}"


class Comment(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author.username}"


class Upvote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True, blank=True, related_name='upvotes_by_users')
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True, blank=True, related_name='upvotes_by_users')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'problem', 'solution')
    
    def __str__(self):
        if self.problem:
            return f"{self.user.username} upvoted problem {self.problem.title}"
        elif self.solution:
            return f"{self.user.username} upvoted solution for {self.solution.problem.title}"