import random
import string

def parse_bool(text: str) -> bool:
    return text.lower() == "true"

raw = input(
    "Enter length and booleans (e.g. 12 true true true false):\n"
    "length uppercase lowercase numbers special → "
)
length_str, upp, low, num, spec = raw.split()
length           = int(length_str)
use_uppercase    = parse_bool(upp)
use_lowercase    = parse_bool(low)
use_numbers      = parse_bool(num)
use_specials     = parse_bool(spec)

def generate_password(
        length: int,
        uppercase: bool = True,
        lowercase: bool = True,
        numbers:   bool = True,
        specials:  bool = True
) -> str:
    if length <= 0:
        raise ValueError("Password length must be positive.")

    pools = []
    if uppercase: pools.append(string.ascii_uppercase)
    if lowercase: pools.append(string.ascii_lowercase)
    if numbers:   pools.append(string.digits)
    if specials:  pools.append("!@#$%^&*()_+-=[]{}|;':\",.<>?/")

    if not pools:
        raise ValueError("Select at least one character category.")

    password_chars = [random.choice(pool) for pool in pools]

    all_allowed = ''.join(pools)
    password_chars += random.choices(all_allowed, k=length - len(password_chars))

    random.shuffle(password_chars)
    return ''.join(password_chars)

print("Your password:", generate_password(
    length, use_uppercase, use_lowercase, use_numbers, use_specials
))
