def count_up_to(max_value):
    """A generator that counts from 1 to max_value."""
    count = 1
    while count <= max_value:
        yield count  # Yield the current count and pause execution - Hold the state of the value for the next call
        count += 1  # Increment count for the next iteration


# Using the generator
if __name__ == "__main__":
    for number in count_up_to(5):
        print(number)