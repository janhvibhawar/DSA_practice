def roundToNearest(s: str) -> str:
    num = int(s)

    if num % 10 == 5:
        ans = num-5
    else:
        ans = round(num, -1)
    return ans

