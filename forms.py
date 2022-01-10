from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class NewsContentForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["date", "author"]