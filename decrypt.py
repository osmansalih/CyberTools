import numpy as np
import sounddevice as sd
from scipy.fft import rfft, rfftfreq
import threading

def play_note(note):
    """
    Generate and play a tone corresponding to the given cipher.
    """
    # Map ciphers to frequencies (in Hz) for all letters A to Z
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
        "[H]": 1479.98, # F#6/Gb5
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


def record_audio(duration=10, sample_rate=44100):
    """
    Record audio for a given duration and return the recorded waveform.
    """
    print("Recording... Play the notes now.")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64')
    sd.wait()  # Wait until recording is finished
    print("Recording complete.")
    return audio.flatten(), sample_rate

def analyze_frequency(audio, sample_rate):
    """
    Analyze the dominant frequency in the recorded audio.
    """
    # Perform Fourier Transform to get frequency components
    N = len(audio)
    yf = rfft(audio)
    xf = rfftfreq(N, 1 / sample_rate)

    # Find the frequency with the highest magnitude
    idx = np.argmax(np.abs(yf))
    dominant_frequency = xf[idx]
    return dominant_frequency

def segment_audio(audio, sample_rate, note_duration=0.3):
    """
    Segment the audio into chunks based on the duration of each note.
    """
    segment_length = int(note_duration * sample_rate)
    return [audio[i:i + segment_length] for i in range(0, len(audio), segment_length)]

def break_cipher():
    
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

    # Record audio manually
    audio, sample_rate = record_audio_manually()

    # Segment the audio into chunks
    note_duration = 0.5  # Match the note duration in encrypt.py
    segments = segment_audio(audio, sample_rate, note_duration)

    # Analyze each segment and reconstruct the message
    reconstructed_message = ""
    for segment in segments:
        if len(segment) == 0:  # Skip empty segments
            continue
        dominant_frequency = analyze_frequency(segment, sample_rate)
        print(f"Detected frequency: {dominant_frequency} Hz")

        # Find the closest matching cipher
        closest_note = None
        min_difference = float('inf')
        for note, freq in note_frequencies.items():
            difference = abs(dominant_frequency - freq)
            if difference < min_difference:
                min_difference = difference
                closest_note = note

        if closest_note and min_difference < 10:  # Add a tolerance range
            print(f"Detected cipher: {closest_note}")
            reconstructed_message += closest_note
        else:
            print("No matching cipher found.")

    print(f"Reconstructed message: {reconstructed_message}")

    # Decrypt the reconstructed message
    decryption = {
        "[A]": "A", "[AA]": "B", "[AAA]": "C", "[B]": "D", "[BB]": "E", "[BBB]": "F",
        "[C]": "G", "[CC]": "H", "[CCC]": "I", "[D]": "J", "[DD]": "K", "[DDD]": "L",
        "[E]": "M", "[EE]": "N", "[EEE]": "O", "[F]": "P", "[FF]": "Q", "[FFF]": "R",
        "[G]": "S", "[GG]": "T", "[GGG]": "U", "[H]": "V", "[HH]": "W", "[HHH]": "X",
        "[I]": "Y", "[II]": "Z"
    }

    msg = ""
    temp = ""  # Temporary variable to store the current cipher
    for char in reconstructed_message:
        temp += char  # Build the cipher string one character at a time
        if temp in decryption:  # Check if the full cipher exists in the dictionary
            msg += decryption[temp]  # Add the corresponding plaintext letter to the message
            temp = ""  # Reset the temporary variable for the next cipher

    print(f"Decrypted message: {msg}")

def record_audio_manually(sample_rate=44100):
    """
    Record audio manually, allowing the user to start and stop the recording.
    """
    print("Recording... Press 'Ctrl+C' to stop recording.")
    audio_data = []
    recording = True

    def callback(indata, frames, time, status):
        """
        Callback function to collect audio data in chunks.
        """
        if status:
            print(status)
        audio_data.append(indata.copy())

    # Start the recording stream
    with sd.InputStream(samplerate=sample_rate, channels=1, callback=callback):
        try:
            while recording:
                sd.sleep(100)  # Keep the stream alive
        except KeyboardInterrupt:
            print("\nRecording stopped.")

    # Combine all recorded chunks into a single array
    audio = np.concatenate(audio_data, axis=0).flatten()
    return audio, sample_rate

if __name__ == "__main__":
    break_cipher()
