from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __iter__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disable = True