import random
import string
def check_length(password):
    return len(password) >= 8
def check_upper(password):
    for character in password:
        if character.isupper():
            return True
    return False
def check_lower(password):
    for character in password:
        if character.islower():
            return True
    return False
def check_number(password):
    for character in password:
        if character.isdigit():
            return True
    return False
def check_special(password):
    special_characters = "!@#$%^&*?"
    for character in password:
        if character in special_characters:
            return True
    return False
def calculate_score(password):
    score = 0
    if check_length(password):
        score += 1
    if check_upper(password):
        score += 1
    if check_lower(password):
        score += 1
    if check_number(password):
        score += 1
    if check_special(password):
        score += 1
    return score
def give_suggestions(password):
    suggestions = []
    if not check_length(password):
        suggestions.append("Use at least 8 characters")
    if not check_upper(password):
        suggestions.append("Add an uppercase letter")
    if not check_lower(password):
        suggestions.append("Add a lowercase letter")
    if not check_number(password):
        suggestions.append("Add a number")
    if not check_special(password):
        suggestions.append("Add a special character")
    return suggestions
def generate_password(length=12):
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    special = random.choice("!@#$%^&*?")
    characters = string.ascii_letters + string.digits + "!@#$%^&*?"
    password = uppercase + lowercase + number + special
    for i in range(length - 4):
        password += random.choice(characters)
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)