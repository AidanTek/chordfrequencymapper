# chordFrequencyMapper/main.py

# The objective of this project is to provide a CLI app to work out the
# frequency of notes in a chord, based on user input. A simple algorithm is
# used to work out the frequency of each note. This is just a learning exercise
# for myself and for fun - feel free to use to your own devices or to criticise
# my hacky programming!

# By Aidan Taylor. 2018.

# List of things to do...
# - Make formula to work out notes in chord from table based on root
# - Make formula to work out notes in chord from algebra based on root
# - User input commands
# - make pretty

# User input option table:
#   - Display input note Frequency
#       - select note (output)
#   - Display chord frequency table
#       - select chord type (major/minor)
#           - select root note (output)

import noteTableGen
import userInput

noteTableGen.noteGen()

userInput.inputLoop()
