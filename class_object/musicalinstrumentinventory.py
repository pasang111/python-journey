# Create a MusicalInstrument class
class MusicalInstrument:

    # Initialize the instrument name and type
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    # Method to play the instrument
    def play(self):
        print(f'The {self.name} is fun to play')

    # Method to return a fact about the instrument
    def get_fact(self):
        return f'The {self.name} is part of {self.instrument_type} family of instruments.'


# Create two MusicalInstrument objects
instrument_1 = MusicalInstrument("piano", "vagan")
instrument_2 = MusicalInstrument("Violin", "nyano")


# Access the attributes of instrument 1
(instrument_1.name)
(instrument_1.instrument_type)

# Access the attributes of instrument 2
(instrument_2.name)
(instrument_2.instrument_type)


# Call the play() and get_fact() methods for instrument 1
instrument_1.play()
print(instrument_1.get_fact())

# Call the play() and get_fact() methods for instrument 2
instrument_2.play()
print(instrument_2.get_fact())