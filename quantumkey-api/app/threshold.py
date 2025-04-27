# quantumkey-api/app/threshold.py

import random
from fastapi import APIRouter

router = APIRouter()

def _is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    r = int(n**0.5)
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

def _next_prime(n: int) -> int:
    p = n + 1
    while not _is_prime(p):
        p += 1
    return p

def _eval_poly(coeffs: list[int], x: int, p: int) -> int:
    res = 0
    for power, c in enumerate(coeffs):
        res = (res + c * pow(x, power, p)) % p
    return res

@router.post("/split")
async def split_secret(secret: str, shares: int = 5, threshold: int = 3):
    # кодим строку в число
    secret_bytes = secret.encode()
    secret_int = int.from_bytes(secret_bytes, "big")
    # выбираем простое > secret_int
    prime = _next_prime(secret_int)
    # строим коэффициенты полинома степени threshold-1
    coeffs = [secret_int] + [random.randrange(0, prime) for _ in range(threshold - 1)]
    parts: list[str] = []
    for i in range(1, shares + 1):
        y = _eval_poly(coeffs, i, prime)
        parts.append(f"{i}:{y}")
    return {"prime": prime, "shares": parts}

@router.post("/recover")
async def recover_secret(parts: list[str], prime: int):
    # разбираем вход
    shares: list[tuple[int,int]] = []
    for part in parts:
        i_str, y_str = part.split(":")
        shares.append((int(i_str), int(y_str)))

    # Lagrange на x=0
    total = 0
    for j, (xj, yj) in enumerate(shares):
        num = 1
        den = 1
        for m, (xm, _) in enumerate(shares):
            if m == j:
                continue
            num = (num * (-xm)) % prime
            den = (den * (xj - xm)) % prime
        lag = num * pow(den, -1, prime)
        total = (total + yj * lag) % prime

    secret_int = total
    # обратно в строку
    b = secret_int.to_bytes((secret_int.bit_length()+7)//8, "big")
    return {"secret": b.decode()}
