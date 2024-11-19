class vowels:
    def __init__(self, text):
        self.text = text
        self.vols = [el for el in self.text if el.lower() in 'aeuiyo']
        self.current_inx = -1

    def __iter__(self):
        # return iter(self.vols)
        return self

    def __next__(self):
        self.current_inx += 1
        if self.current_inx < len(self.vols):
            return self.vols[self.current_inx]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
