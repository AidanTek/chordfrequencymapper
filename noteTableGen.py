# chordFrequencyMapper/noteTable.py

# this script will generate a new csv file on execution that generates the
# frequencies for 128 notes (the MIDI table) - if the file already exists then
# nothing happens.

import sys
import os
import csv
from math import pow

A0 = 27.5 # MIDI note 21
semi = pow(2.0, 1.0/12.0)
noteNames = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']

# The semitone formula is:
#   n+(n*(2^1/12))

# Output all notes between A0 and C8:
def noteGen():
    MIDINoteFreq = {} # Dictionary to store result table
    note = 0
    lastNote = 0

    for octave in range(1, 9):
        # print('Octave: {}'.format(octave))
        for n in range(21, 33):
            if (octave == 1) and (n == 21):
                note = A0
            elif (octave == 1) and (n == 1):
                lastNote = A0*semi
                note = lastNote
            else:
                lastNote = (note*semi)
                note = lastNote

            if (n-21) < 3:
                name = noteNames[n-21] + str(octave-1)
            else:
                name = noteNames[n-21] + str(octave)

            # Add entry to dictionary, with the note name as key:
            MIDINoteFreq[name] = n+(12*(octave-1)), round(note, 3)

            # print('Note: {} || Midi Note: {} || Frequency: {}hz'.format(name, n+(12*(octave-1)), note))

            # Stop at C8:
            if (n+(12*(octave-1))) == 108:
                break

    # Check if file exists, create it if not:
    if os.path.isfile('noteTable.csv'):
        #print('Table already exists')
        pass
    else:
        print('No table present, generating now...')

        with open(os.path.join(sys.path[0], 'noteTable.csv'), 'w') as f:
            writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for x, y in MIDINoteFreq.items():
                writer.writerow([str(x)]+[str(y[0])]+[str(y[1])])

            f.close()

    # # Print the dictionary:
    # for x,y in MIDINoteFreq.items():
    #     print(x,y[1])
    #
    # # Test at A4 (should result in 440.0hz):
    # print(MIDINoteFreq['A4'])
