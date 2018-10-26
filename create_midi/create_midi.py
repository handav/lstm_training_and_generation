import os
import midiutil

def compose_midi(text):
    track = 0
    channel = 0
    time = 0   # in beats
    tempo = 120  # beats per minute
    volume = 100 # from 0-127
    midi_file = midiutil.MIDIFile(1, adjust_origin=True)
    midi_file.addTempo(track, time, tempo)
    
    for item in text.split():
        print list(item)
        note = ''.join(list(item)[:2])
        note = int(note)
        duration = ''.join(list(item)[2:])
        duration = float(duration)
        midi_file.addNote(track, channel, note, time, duration, volume)
        time = time + duration
    
    return midi_file

def save_midi(cleaned_tweet, midi_file):
    filename = 'sample_output.mid'
    with open(filename, 'wb') as output_file:
        midi_file.writeFile(output_file)
        print 'midi file saved'

with open('./output/notes.txt', 'r') as input_file:
    notes = input_file.read()
    midi_file = compose_midi(notes)
    save_midi(notes, midi_file)