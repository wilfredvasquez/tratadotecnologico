# -*- coding: utf-8 -*-
import re
from password_strength import PasswordStats

PASSWORD_STRENGTH = 0.3
PASSWORD_LENGTH = 8
PASSWORD_NUMBERS = 1
PASSWORD_UPPERCASE = 1
PASSWORD_SPECIAL = 1


class ValidationError(Exception):
    message = "Ha ocurrido un error en la validación"

    def __init__(self, message=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        self.error_response()

    def error_response(self):
        return {"message": self.message}

def validar_email(email):
    if not re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower()):
        raise ValidationError("email: El formato del email no es válido")

    return email

def validar_password(password1, password2):
    if not password1 == password2:
        raise ValidationError("password: Las contraseñas no coinciden")

    errors = []
    # password strength. Value range [0 : 1]
    if PasswordStats(password1).strength() < PASSWORD_STRENGTH:
        errors.append('Fortaleza: La contraseña es muy simple.')

    # Min length: 8
    if PasswordStats(password1).length < PASSWORD_LENGTH:
        errors.append(f'Tamaño: La contraseña debe tener al menos {PASSWORD_LENGTH} caracteres.')

    # Need min. 1 number
    if PasswordStats(password1).numbers < PASSWORD_NUMBERS:
        errors.append(f'Numeros: La contraseña debe tener al menos {PASSWORD_NUMBERS} número.')
    
    # Need min. 1 uppercase letters
    if PasswordStats(password1).letters_uppercase < PASSWORD_UPPERCASE:
        errors.append(f'Mayúscula: La contraseña debe tener al menos {PASSWORD_UPPERCASE} mayúscula.')

    # Need min. 1 special characters
    if PasswordStats(password1).special_characters < PASSWORD_SPECIAL:
        errors.append(f'Especial: La contraseña debe tener al menos {PASSWORD_SPECIAL} caracater especial.')

    if errors:
        raise ValidationError(errors)
    