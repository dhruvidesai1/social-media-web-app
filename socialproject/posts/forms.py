from .models import Post, Comment
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','caption')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','posted_by')