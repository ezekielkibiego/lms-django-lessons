from django import forms
from .models import Blog, Author

class BlogForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label='Select an author')
    
    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'is_published']