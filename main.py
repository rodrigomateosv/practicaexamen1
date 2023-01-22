def Xbonacci(signature, n):
    x = len(signature)
    if n <= x:
        return signature[:n]
    for i in range(n-x):
        signature.append(sum(signature[-x:]))
    return signature
