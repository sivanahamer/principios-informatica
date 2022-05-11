def numero_triangular_n(n):
    if n == 1:
        return 1
    else:
        return n + numero_triangular_n(n - 1)