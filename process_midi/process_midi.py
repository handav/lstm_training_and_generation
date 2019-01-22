from mido import MidiFile
mid = MidiFile('twinkle_twinkle.mid')

# look at the track names
for i, track in enumerate(mid.tracks):
    print((i, track.name))

#pick the track that you want to get the melody of. Ignore all titles and metadata! Here the main melody is the Violoncello, track 1
track_number = 1

# create array of notes
notes = []
for message in mid.tracks[track_number]:
    #print(message)
    if message.type == 'note_on':
        message_components = str(message).split(' ')
        for item in message_components:
            if 'note=' in item:
                notes.append(item.split('note=')[1])
notes = ' '.join(notes)

# write notes to text file
note_file = open("notes.txt", "w")
note_file.write(notes)
note_file.close()