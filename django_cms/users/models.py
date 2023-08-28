from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField
from django.urls import reverse


class User(AbstractUser):
    """
    Default custom user model for contentflow.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField("Nombre completo", blank=True, max_length=255)
    sex = CharField("Sexo", blank=True, max_length=1, choices=(("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")))
    birth_date = DateField("Fecha de nacimiento", blank=True, null=True)

    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
