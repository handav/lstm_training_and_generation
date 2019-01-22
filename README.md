# LSTMs to generate lyrics and music

## About this repo

In this repo there are four folders:

1) (Optional) A process_midi folder with a script to show you how to get notes from a MIDI file (only if you're working with MIDI - see below)
2) The main folder, lstm, trains a model on lyrics or MIDI notes using Python and Tensorflow
3) A p5 sketch to generate from a trained model
4) (Optional) A Python script to create a MIDI file from generated MIDI notes 

Don't worry about digging into these just yet - we'll go through these in the workshop. For now, please read the following installation instructions and bring your computer with these ready to go.

## Bring your data! (optional, otherwise a cleaned lyrics dataset will be provided)

You can get lyrics or MIDI files anywhere online. The more you get, the better the model will be, but for the purposes of this workshop any amount will do (you can always add more and re-train it later). If you want to download a ton of data, you can get the lyrics of over 55,000 songs here (requires an account): https://www.kaggle.com/mousehead/songlyrics/version/1. You can open up the .csv file and copy lyrics from the "text" column. 

The lyrics should be in one input.txt files in your 'data' folder. If you have many text files, you can concatenate them all together by typing this command into terminal: ```ls *.txt | xargs -L 1 cat >> input.txt``` Everything in this file will be fed into the model, so you should delete any unnecessary information (like url links, for example).

MIDI data is much harder to process, but if you get a clean MIDI dataset, the model works the same way. The best place to get MIDI files is from here: https://colinraffel.com/projects/lmd/#get (I recommend the Clean MIDI subset). I'm also including a process_midi folder that you can use to help process your MIDIs, though you might have to adjust some lines if you MIDIs look different (for example, the main melody is in a different voice). MIDI experience and Python experience recommended. See the README in the process_midi for more information, and feel free to write ahandvanish@gmail.com with any questions before the workshop.

If you don't want to bring your own data, a cleaned dataset of David Bowie lyrics will be provided.


## Installation

The LSTM code needs two things to run: Tensorflow and Python. 

This tutorial has been tested and works with Python version 3.6.

### Install Miniconda:

Miniconda2 is for Python 2 and Miniconda3 is for Python 3. You can see which version of Python your computer is running by typing ```python -V``` into terminal. Download the shell script (the file that ends in .sh) for your version of Python and your operation system. For example, I downloaded Miniconda2-latest-MacOSX-x86_64.sh.

Main link here: https://conda.io/miniconda.html. If this link doesn't work there, here is an alternate link: https://repo.anaconda.com/miniconda/. 

Then, type this into terminal: 

```
bash /path/to/file/you/just/downloaded/for/example/Miniconda2-latest-MacOSX-x86_64.sh
```

Review the license and approve the license terms - type ```yes``` and press enter

Press Enter again to confirm the location of install

Type ```yes``` when it asks you if the install location should be prepended to PATH

Restart Terminal for changes to take effect

Type: ```conda info```

If it prints out some stuff then it has installed correctly

### Create a virtual environment:

```conda create -n ml5 python=3.5.2```

This should put (ml5) in parenthesis at the beginning of your terminal line.

### Install modules

```pip install numpy==1.10.4```

```pip install scipy==0.17.0```

```pip install tensorflow==1.0.0```

Then you're all set!

Email ahandvanish@gmail.com with any questions!

Installation instructions based on https://ml5js.org/docs/training-setup.html.

