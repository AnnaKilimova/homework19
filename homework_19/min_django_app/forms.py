from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class RegistrationForm(forms.ModelForm):
    '''Форма для регистрации нового пользователя.'''

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        '''Для определения дополнительных настроек формы.'''

        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        '''Метод переопределяется для выполнения кастомной валидации формы.'''

        # (4) Для захисту від XSS додамо валідацію в форму для перевірки вхідних даних
        username = forms.CharField(
            max_length=150,
            validators=[validate_slug],  # Додаємо валідацію
            help_text="Ім'я користувача може містити лише букви, цифри, підкреслення та дефіси."
        )

        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class LoginForm(AuthenticationForm):
    '''Форма для входа пользователя.'''

    username = forms.EmailField(label="Email")
