def sumOfSeries(n: int, a: int, d: int) -> int:
    ans = n * (2 * a + (n - 1) * d) // 2
    return ans
