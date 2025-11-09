from django import forms
from .models import Problem, Solution


class ProblemForm(forms.ModelForm):
    tags_str = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter tags separated by commas (e.g., array, string, recursion)'
        })
    )
    
    class Meta:
        model = Problem
        fields = ['title', 'description', 'difficulty', 'language', 'test_cases']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded h-40'}),
            'difficulty': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'language': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded'}),
            'test_cases': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded h-32', 'placeholder': 'Enter test cases (optional)'}),
        }


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['code', 'explanation']
        widgets = {
            'code': forms.Textarea(attrs={'class': 'w-full border rounded p-3', 'rows': 10, 'placeholder': 'Enter your solution code here...'}),
            'explanation': forms.Textarea(attrs={'class': 'w-full border rounded p-3', 'rows': 4, 'placeholder': 'Explain your solution...'}),
        }