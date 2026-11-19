import math

def digitsInFactorial(n: int) -> int:
    if n<=1:
      return 1

    log_sum = 0.0

    for i in range(2,n+1):
      log_sum += math.log10(i)
    return math.floor(log_sum)+1
