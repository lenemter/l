import random
import string

def random_string(length: int) -> string:
    return "".join(random.choices(string.ascii_letters, k=length))
