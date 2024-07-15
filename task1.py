def catching_fibonacci():
    # Creating dict for function cache
    cache = {}
    def fibonacci(number):
        if number <= 0:
            return 0
        if number == 1:
            return 1
        # If the number is already in the cache, immediately return the result of the function
        if number in cache:
            return cache[number]
        # Recursive calculation of a number
        cache[number] = fibonacci(number-1) + fibonacci(number-2)
        return cache[number]
    return fibonacci
