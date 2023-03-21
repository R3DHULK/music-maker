import tkinter as tk
# pip install simpleaudio
import simpleaudio as sa

class MusicMaker:
    def __init__(self, master):
        self.master = master
        master.title("Music Maker")

        self.note_labels = []
        self.notes = []

        # Create the note buttons
        self.note_button_names = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.note_buttons = [tk.Button(master, text=note_name, command=lambda note_name=note_name: self.play_sound(note_name)) for note_name in self.note_button_names]

        # Create the octave buttons
        self.octave_button_names = ['4', '5', '6', '7']
        self.octave_buttons = [tk.Button(master, text=octave_name, command=lambda octave_name=octave_name: self.set_octave(octave_name)) for octave_name in self.octave_button_names]

        # Create the clear button
        self.clear_button = tk.Button(master, text='Clear', command=self.clear_notes)

        # Create the play button
        self.play_button = tk.Button(master, text='Play', command=self.play_notes)

        # Create the stop button
        self.stop_button = tk.Button(master, text='Stop', command=self.stop_notes)

        # Create the note label grid
        for i in range(12):
            note_label = tk.Label(master, text=self.note_button_names[i%7])
            self.note_labels.append(note_label)
            note_label.grid(row=1, column=i+1)
        for i in range(4):
            octave_label = tk.Label(master, text=self.octave_button_names[i])
            octave_label.grid(row=i+2, column=0)

        # Grid the note buttons
        for i, note_button in enumerate(self.note_buttons):
            note_button.grid(row=2+(i%7), column=1+int(i/7))

        # Grid the octave buttons
        for i, octave_button in enumerate(self.octave_buttons):
            octave_button.grid(row=i+2, column=9)

        # Grid the clear button
        self.clear_button.grid(row=6, column=10)

        # Grid the play button
        self.play_button.grid(row=6, column=11)

        # Grid the stop button
        self.stop_button.grid(row=6, column=12)

        # Initialize variables
        self.current_octave = 4
        self.note_duration = 500

    def play_sound(self, note_name):
        # Create the sound object
        wave_obj = sa.WaveObject.from_wave_file(f'notes/{note_name}{self.current_octave}.wav')

        # Play the sound
        play_obj = wave_obj.play()

        # Add the note to the list of notes
        self.notes.append((note_name, self.current_octave))

    def set_octave(self, octave):
        self.current_octave = int(octave)

    def clear_notes(self):
        self.notes = []

    def play_notes(self):
        for note in self.notes:
            # Create the sound object
            wave_obj = sa.WaveObject.from_wave_file(f'notes/{note[0]}{note[1]}.wav')

            # Play the sound
            play_obj = wave_obj.play()

            # Wait for the note to finish playing
            play_obj.wait_done()

    def stop_notes(self):
        sa.stop_all()

root = tk.Tk()
my_music_maker = MusicMaker(root)
root.mainloop()
