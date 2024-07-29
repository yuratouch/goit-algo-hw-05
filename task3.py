import timeit

def boyer_moore_search(pattern, text):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i = i + m - min(k, j + 1)
            k = m - 1
    return -1

def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0
    compute_lps_array(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp_search(pattern, text, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1

def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as file:
        return file.read()

def measure_time(search_func, pattern, text):
    timer = timeit.Timer(lambda: search_func(pattern, text))
    return timer.timeit(number=1000)

if __name__ == "__main__":
    text1 = read_file('стаття 1.txt')
    text2 = read_file('стаття 2.txt')

    patterns = {
        "existing1": "Більшість стандартних бібліотек",
        "non_existing1": "неіснуючий паттерн",
        "existing2": "Ключі вузла вказують інтервал",
        "non_existing2": "вигаданий паттерн"
    }

    for name, pattern in patterns.items():
        if '1' in name:
            text = text1
        else:
            text = text2

        bm_time = measure_time(boyer_moore_search, pattern, text)
        kmp_time = measure_time(kmp_search, pattern, text)
        rk_time = measure_time(rabin_karp_search, pattern, text)

        print(f"Pattern: {pattern}")
        print(f"Boyer-Moore time: {bm_time:.6f} seconds")
        print(f"KMP time: {kmp_time:.6f} seconds")
        print(f"Rabin-Karp time: {rk_time:.6f} seconds")
        print()
