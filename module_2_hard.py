def password_com(n):
    if 3 > n and n < 20:
        return "Число должно быть от 3 до 20! "
    password = ''
    pairs = set()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                sum = i + j
                if n % sum == 0:
                    pair = f'{i}{j}'
                    pair2 = f'{j}{i}'
                    if pair not in pairs:
                        password += pair
                        pairs.add(pair)
                        pairs.add(pair2)
    return password
for i in range(3, 21):
    result = password_com(i)
    print(f'{i} - {result}')


