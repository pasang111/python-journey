class MusicalInstrument:
    def __init__(self,name,instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f'The {self.name} is fun to play')

    def get_fact(self):
        return f'The {self.name} is part of {self.instrument_type} family of instruments.'
instrument_1 = MusicalInstrument("piano","vagan")
instrument_2 = MusicalInstrument("Violin","nyano")

(instrument_1.name)
(instrument_1.instrument_type)
(instrument_2.name)
(instrument_2.instrument_type)

instrument_1.play()
print(instrument_1.get_fact())

instrument_2.play()
print(instrument_2.get_fact())