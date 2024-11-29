from os import name
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from uploader.models import Image


class UserManager(BaseUserManager):
    """Manager for users."""
    
    use_in_migrations = True

class UserManager(BaseUserManager):
    """Manager for users."""
    
    use_in_migrations = True

    def create_user(self, email, password=None, name=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("Users must have an email address.")

        # Corrigir para usar 'name' no lugar de 'username'
        user = self.model(email=self.normalize_email(email), name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, name=None, **extra_fields):
        """Create, save and return a new superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Passar 'name' para 'create_user'
        return self.create_user(email, password, name=name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""

    passage_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("passage_id"),
        help_text=_("Passage ID"),
        default=uuid.uuid4
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=_("email"),
        help_text=_("Email")
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("name"),
        help_text=_("Username")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Usuário está ativo"),
        help_text=_("Indica que este usuário está ativo.")
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Usuário é da equipe"),
        help_text=_("Indica que este usuário pode acessar o Admin.")
    )
    matricula = models.PositiveIntegerField(
        unique=True,
        default=None,
        verbose_name=_("matricula"),
        help_text=_("Matrícula do aluno"),
        null=True
    )
    foto = models.ForeignKey(Image, related_name="+", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    reset_code = models.CharField(max_length=6, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    EMAIL_FIELD = "email"
    class Meta:
        """Meta options for the model."""
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
