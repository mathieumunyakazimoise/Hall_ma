# Import necessary modules from Django
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

# Custom user manager class extending BaseUserManager
class UserManager(BaseUserManager):
    # Method to validate email format
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Please enter a valid email address.'))

    # Method to create a regular user
    def create_user(
        self, email, username,
        first_name, last_name, password=None, **extra_fields):

        # Normalize email
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Please provide an email address.'))
        
        # Check if username is provided
        if not username:
            raise ValueError(_('Username must be provided.'))

        
        # Check if first name is provided
        if not first_name:
            raise ValueError(_('First name must be provided.'))

        # Check if last name is provided
        if not last_name:
            raise ValueError(_('Last name must be provided.'))

        # Create user instance
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name, last_name=last_name, **extra_fields
        )

        # Set password and save user
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Method to create a superuser
    def create_superuser(
        self, email, username,
        first_name, last_name, password=None, **extra_fields):
        
        # Set default values for superuser fields
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        # Check if password is provided for superuser
        if password is None:
            raise ValueError(_('Superuser must have a password.'))

        # Check if username is provided for superuser
        if username is None:
            raise ValueError(_('Superuser must have a username.'))
        
        # Check if first name is provided for superuser
        if first_name is None:
            raise ValueError(_('Superuser must have a first name.'))

        # Check if last name is provided for superuser
        if last_name is None:
            raise ValueError(_('Superuser must have a last name.'))

        # Ensure is_superuser is set to True for superuser
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be set to True.'))
        
        # Ensure is_staff is set to True for superuser
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Staff must be set to True.'))

        # Create superuser using create_user method and save
        user = self.create_user(
            email, username,
            first_name, last_name, password, **extra_fields
        )
        user.save(using=self._db)
        return user