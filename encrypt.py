import numpy as np
import sounddevice as sd
from scipy.fft import rfft, rfftfreq

def play_note(note):
    """
    Generate and play a tone corresponding to the given cipher.
    """
    note_frequencies = {
        "[A]": 440.0,   # A4
        "[AA]": 466.16, # A#4/Bb4
        "[AAA]": 493.88, # B4
        "[B]": 523.25,  # C5
        "[BB]": 554.37, # C#5/Db5
        "[BBB]": 587.33, # D5
        "[C]": 622.25,  # D#5/Eb5
        "[CC]": 659.25, # E5
        "[CCC]": 698.46, # F5
        "[D]": 739.99,  # F#5/Gb5
        "[DD]": 783.99, # G5
        "[DDD]": 830.61, # G#5/Ab5
        "[E]": 880.0,   # A5
        "[EE]": 932.33, # A#5/Bb5
        "[EEE]": 987.77, # B5
        "[F]": 1046.50, # C6
        "[FF]": 1108.73, # C#6/Db6
        "[FFF]": 1174.66, # D6
        "[G]": 1244.51, # D#6/Eb6
        "[GG]": 1318.51, # E6
        "[GGG]": 1396.91, # F6
        "[H]": 1479.98, # F#6/Gb6
        "[HH]": 1567.98, # G6
        "[HHH]": 1661.22, # G#6/Ab6
        "[I]": 1760.0,  # A6
        "[II]": 1864.66, # A#6/Bb6
    }

    if note in note_frequencies:
        frequency = note_frequencies[note]
        duration = 0.5
        sample_rate = 44100

        t = np.linspace(0, duration, int(sample_rate * duration), False)
        tone = 0.5 * np.sin(2 * np.pi * frequency * t)

        sd.play(tone, samplerate=sample_rate)
        sd.wait()


def encrypt():
    message = input("Enter the message to encrypt: ")

    letters = {
        "A": "[A]", "B": "[AA]", "C": "[AAA]", "D": "[B]", "E": "[BB]", "F": "[BBB]",
        "G": "[C]", "H": "[CC]", "I": "[CCC]", "J": "[D]", "K": "[DD]", "L": "[DDD]",
        "M": "[E]", "N": "[EE]", "O": "[EEE]", "P": "[F]", "Q": "[FF]", "R": "[FFF]",
        "S": "[G]", "T": "[GG]", "U": "[GGG]", "V": "[H]", "W": "[HH]", "X": "[HHH]",
        "Y": "[I]", "Z": "[II]"
    }

    message = message.upper()

    first_enc = ""
    for char in message:
        if char in letters:
            first_enc += letters[char]
        else:
            first_enc += char

    second_letters = {
        "[A]": "[A1]", "[AA]": "[A2]", "[AAA]": "[A3]", "[B]": "[B1]", "[BB]": "[B2]", "[BBB]": "[B3]",
        "[C]": "[C1]", "[CC]": "[C2]", "[CCC]": "[C3]", "[D]": "[D1]", "[DD]": "[D2]", "[DDD]": "[D3]",
        "[E]": "[E1]", "[EE]": "[E2]", "[EEE]": "[E3]", "[F]": "[F1]", "[FF]": "[F2]", "[FFF]": "[F3]",
        "[G]": "[G1]", "[GG]": "[G2]", "[GGG]": "[G3]", "[H]": "[H1]", "[HH]": "[H2]", "[HHH]": "[H3]",
        "[I]": "[I1]", "[II]": "[I2]"
    }

    second_enc = ""
    i = 0
    while i < len(first_enc):
        match_found = False
        for key in second_letters:
            if first_enc[i:i+len(key)] == key:
                second_enc += second_letters[key]
                play_note(key)  # Play the piano note for the matched cipher
                i += len(key)
                match_found = True
                break
        if not match_found:
            second_enc += first_enc[i]
            i += 1

    print(f"Encrypted message: {second_enc}")


if __name__ == "__main__":
    encrypt()
