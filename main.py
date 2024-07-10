"""
Converts an input file to a .wav file by encoding each byte as a pre-defined note.
"""

# Starting frequency of the notes  # https://www.quora.com/What-formula-maps-musical-notes-to-frequency
BASE_FREQUENCY = 55 # A1

# Number of notes in an octave
NOTES_IN_OCTAVE = 12

# Generate 256 notes
NOTES = [BASE_FREQUENCY * (2 ** (i / NOTES_IN_OCTAVE)) for i in range(256)]

# Path to the input file
INPUT_FILE = "input.txt"
