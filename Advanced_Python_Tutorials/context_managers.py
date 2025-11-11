# Safe way to open and write to a file using a context manager
# This ensures the file is properly closed after its suite finishes,
# even if an exception is raised at some point.

# Custom context manager


class CustomContextManager:
    def __init__(self, resource_name, mode):
        self.resource_name = resource_name
        self.resource = None
        self.mode = "w" if mode == "w" else "r"

    def __enter__(self):
        print("Entering the context.")
        self.resource = open(self.resource_name, self.mode)
        print(f"Resource {self.resource_name} opened in {self.mode} mode.")
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        self.resource.close()
        print("Exiting the context.")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True


# using CustomContextManager to write to a file
with CustomContextManager("custom_file.txt", "w") as custom_file:
    custom_file.write("This is written using a custom context manager.")

# using CustomContextManager to read from a file
with CustomContextManager("custom_file.txt", "r") as custom_file:
    content = custom_file.read()
    print("Content read from the file:")
    print(content)
