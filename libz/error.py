class Error(Exception):
    def __init__(self, message):
        self.message = message

    def _print_error(self):
        print(f"\n{self.message}")

    def handle(self):
        self._print_error


class FatalError(Error):
    def __init__(self, message):
        new_message = f"{message} Check documentation for more information."
        super().__init__(new_message)

    def handle(self):
        self._print_error
        print("\nExiting the program with exit code 1.\n")
        exit(1)
