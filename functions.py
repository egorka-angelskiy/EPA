import re

def check_password(password):
    return re.fullmatch('[A-Za-z0-9]+', password)


def iter_string(form):
    string = ''
    counter = 0
    for i in form:
        counter += 1
        if counter == len(form):
            string += f"{i.lower()}='{form.get(i)}' "
        else:
            string += f"{i.lower()}='{form.get(i)}', " 
    return string