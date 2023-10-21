import noisereduce as nr


from pydub import AudioSegment
from scipy.io import wavfile
audio = AudioSegment.from_file('Linux-9-28-2023.m4a')
audio.export("your_audio.wav", format="wav")

# noise reduction

rate, data = wavfile.read("your_audio.wav")

# Perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)

# Save the noise-reduced audio as WAV
wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)