from django import forms
from posts.models import Author

class PostForm(forms.Form):
   
    choices = {}

    for author in Author.objects.all():
        choices[author.id] = author.email
    
    title = forms.CharField(required=True)
    content = forms.CharField(widget=forms.Textarea(), required=True)
    author = forms.ChoiceField(choices=choices, required=True)

    field_order = ['title', 'content', 'author']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = cleaned_data.get('author')

        if not (title and content and author):
            raise forms.ValidationError("Nie podano żadnej wartości!")
        
class AuthorForm(forms.Form):
    
    email = forms.EmailField(required=True)
    bio = forms.CharField(widget=forms.Textarea(),required=False)
    nick = forms.CharField(required=True)

    field_order = ['email', 'nick', 'bio']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        bio = cleaned_data.get('bio')
        nick = cleaned_data.get('nick')

        if not (email and nick):
            raise forms.ValidationError("Nie podano wymaganych pól")
        

