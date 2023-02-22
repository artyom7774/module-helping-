def fib(count) -> list:
    out = []

    for _ in range(2, count):
        v1, v2 = v2, v1 + v2
        out.append(v2)