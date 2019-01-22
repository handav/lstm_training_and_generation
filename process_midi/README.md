This script requires mido. In your terminal, please type:

```
pip install mido
```

The point of this script is to try to extract the melody from the MIDI file. MIDI is hard to work with and is pretty inconsistent between files, so you have to do a little searching to find out which track the melody is on. For the purpose of this workshop, processing one MIDI file is fine (you can always process more data over time and use the same tutorial to train the model again).

If you're feeling ambitious, you can also save more parts of the MIDI than single melody notes. This is called creating an 'encoding'. For example, the encoding for Twinkle Twinkle Little Star is:

50 50 57 57 59 59 57 55 55 54 54 52 52 50 57 57 55 55 54 54 52 57 57 55 55 54 54 52 50 50 57 57 59 59 57 55 55 54 54 52 52 50

But you could also save the note durations, for example by appending them with an underscore: 50_1 50_1 57_1 57_1 59_1 59_1 57_2 (where 1 is quarter note and 2 is half note). 

You can make up any encoding as you want, as long as they are consistent! This LSTM is a **character model**, which means that as long as your input are characters, we can train it the same way as any other text.