from django import forms

class ToDoListForm(forms.Form):
    text = forms.CharField(
        max_length=45,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo e.g Grocery Shopping',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn'
            }
        )
    )
