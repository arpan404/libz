class Error:
    def __init__(self, message):
        self.message = message

    def handle(self):
        print(f"\n{self.message}\n")