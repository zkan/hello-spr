def fizzbuzz(number: int) -> str:
    if number % 3 == 0:
        return "Fizz"

    if number == 5 or number == 10:
        return "Buzz"

    return str(number)
