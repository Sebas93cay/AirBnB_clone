class Lector:
    readed = 0

    def read(self, stdout):
        first_read = stdout.getvalue()
        last_part = first_read[self.readed:]
        self.readed = len(first_read)
        return last_part


reader = Lector()
