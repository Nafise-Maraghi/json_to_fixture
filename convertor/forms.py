from django import forms


class ConvertorForm(forms.Form):
    file = forms.FileField()
    model_name = forms.CharField(max_length=200, help_text="(app_name.model)")
