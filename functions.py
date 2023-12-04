import re

def check_password(password):
    return re.fullmatch('[A-Za-z0-9]+', password)
