from django import forms

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Auto
        fields = ['marka', 'gos_number', 'post', 'photo', 'is_published', 'cat']
        widgets = {
            'marka': forms.TextInput(attrs={'class': 'form-input'}),
            'post': forms.Textarea(attrs={'cols': 70, 'rows': 10})
        }

        # marka = forms.CharField(max_length=255, label='Марка', widget=forms.TextInput(attrs={'class': 'form-input'}))
        # gos_number = forms.CharField(max_length=10, label='Гос.№')
        # slug = forms.SlugField(max_length=255, label='URL')
        # post = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), label='Описание последних работ')
        # is_published = forms.BooleanField(label='Исправность', required=False, initial=True)
        # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Не выбрана')

        # marka = forms.CharField(max_length=255)
        # gos_number = forms.CharField(max_length=10)
        # slug = forms.SlugField(max_length=255)
        # post = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}))
        # is_published = forms.BooleanField()
        # cat = forms.ModelChoiceField(queryset=Category.objects.all())
