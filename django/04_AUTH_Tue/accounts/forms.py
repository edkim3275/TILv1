from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    # little customize
    class Meta:
        model = User
        fields = ('username', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'address',)