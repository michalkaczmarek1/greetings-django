from django import forms
from posts.models import Post, Author

class PostForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = cleaned_data.get('author')

        if not (title and content and author):
            raise forms.ValidationError("Nie podano żadnej wartości!")
        
    class Meta:
        model = Post
        fields = "__all__"

        
class AuthorForm(forms.ModelForm):
    field_order = ['email', 'nick', 'bio']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        bio = cleaned_data.get('bio')
        nick = cleaned_data.get('nick')

        if not (email and nick):
            raise forms.ValidationError("Nie podano wymaganych pól")
        
    class Meta:
        model = Author
        fields = "__all__"

