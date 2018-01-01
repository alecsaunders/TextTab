class Note():
    def __init__(self, measure, string, position, duration):
        self.measure = measure
        self.string = string
        self.position = position
        self.duration = duration
        self.char_len = None
        num, den = duration.split('/')
        num = num.strip()
        den = den.strip()
        self.numerator = num
        self.denominator = den
        self.duration_frac = float(self.numerator) / float(self.denominator)

        self.set_char_len()

    def set_char_len(self):
        self.position = self.position.strip()
        self.char_len =  len(self.position)
