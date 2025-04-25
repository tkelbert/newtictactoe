def factorial(n):
    if n == 0:
        print(f"factorial {n} -> base case reached, returning 1")
        return 1
    else:
        print(f"factorial {n} --> calling factorial({n-1})")
        recursive_result = factorial(n - 1)
        result = n * recursive_result
        print(
            f"factorial{n} --> returning {n} * {recursive_result} = {result}")
        return result


print("\nCalculating factorial(3)")
final_answer = factorial(4)
print(f"the final answer to factorial(3) is {final_answer}")
