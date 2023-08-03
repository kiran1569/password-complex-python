def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_special_char(password):
    for char in password:
        if not char.isalnum():
            return True
    return False

password = input("Enter a password: ")

length = len(password)
has_upper = has_uppercase(password)
has_lower = has_lowercase(password)
has_digit_char = has_digit(password)
has_special = has_special_char(password)

complexity_score = 0

if length >= 8:
    complexity_score += 1

if has_upper:
    complexity_score += 1

if has_lower:
    complexity_score += 1

if has_digit_char:
    complexity_score += 1

if has_special:
    complexity_score += 1

print("Complexity Score:", complexity_score)

if complexity_score <= 2:
    print("Password is weak.")
elif complexity_score <= 3:
    print("Password is moderate.")
else:
    print("Password is strong.")
