#!/usr/bin/env python

import random
import string

def get_random_password(password_length):
    """Generates a random password with given length."""

    if password_length < 6:
        password_length = 6

    numbers = ''.join(random.SystemRandom().choice(string.digits) for _ in range(round(password_length / 5)))
    special_signs = ''.join(random.SystemRandom().choice('&+%|$!?_-') for _ in range(round(password_length / 3)))
    char_set = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(password_length - len(numbers) - len(special_signs)))
    return(''.join(random.sample(char_set + numbers + special_signs, password_length)))

print(get_random_password(6))
