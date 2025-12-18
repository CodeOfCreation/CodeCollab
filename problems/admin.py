from django.contrib import admin
from .models import Problem, Solution, Comment, Tag, Upvote, Blog


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at', 'upvotes', 'views')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('created_at', 'updated_at', 'slug')
    filter_horizontal = ('tags',)


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'difficulty', 'language', 'created_at', 'upvotes', 'views')
    list_filter = ('difficulty', 'language', 'created_at')
    search_fields = ('title', 'description', 'author__username')
    readonly_fields = ('created_at',)
    filter_horizontal = ('tags',)


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('problem', 'author', 'created_at', 'upvotes')
    list_filter = ('created_at', 'upvotes')
    search_fields = ('problem__title', 'author__username', 'code')
    readonly_fields = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'problem', 'solution', 'blog', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'content', 'problem__title', 'solution__problem__title', 'blog__title')
    readonly_fields = ('created_at',)


@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem', 'solution', 'blog', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'problem__title', 'solution__problem__title', 'blog__title')
    readonly_fields = ('created_at',)