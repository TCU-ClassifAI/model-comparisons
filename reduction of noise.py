import noisereduce as nr
from pydub import AudioSegment
import os

# only line you need to change :) - jhm
audio = AudioSegment.from_file('Linux-9-28-2023.m4a')



# Create a folder called "chunks" if it doesn't exist
if not os.path.isdir("chunks"):
    os.mkdir("chunks")
# If it already exists, delete all its contents
else:
    for file in os.listdir("./chunks"):
        os.remove(f"./chunks/{file}")

# Create a folder called "cleaned_chunks" if it doesn't exist
if not os.path.isdir("cleaned_chunks"):
    os.mkdir("cleaned_chunks")
# If it already exists, delete all its contents
else:
    for file in os.listdir("./cleaned_chunks"):
        os.remove(f"./cleaned_chunks/{file}")

# Split the audio into chunks of 1 minute each


chunk_length_ms = 60000
for i, chunk in enumerate(audio[::chunk_length_ms]):
    chunk_name = f"chunk_{i}.m4a"
    print(f"exporting {chunk_name}")
    chunk.export(f"./chunks/{chunk_name}", format="mp3")


    # Load the 1-minute segment
    audio_segment = AudioSegment.from_file(f"./chunks/{chunk_name}", format="mp3")

    # # Convert the segment to NumPy array
    data = audio_segment.get_array_of_samples()

    # # Apply noise reduction
    reduced_audio = nr.reduce_noise(y=data, sr=audio_segment.frame_rate, prop_decrease=0.5)

    # # Create a new AudioSegment from the cleaned audio
    cleaned_audio_segment = AudioSegment(
        reduced_audio.tobytes(),
        frame_rate=audio_segment.frame_rate,
        sample_width=reduced_audio.dtype.itemsize,
        channels=audio_segment.channels
    )

    # Export the cleaned segment
    cleaned_audio_segment.export(f"./cleaned_chunks/cleaned_{chunk_name}", format="mp3")

# Combine all cleaned chunks into a single file
combined = AudioSegment.empty()
for file in os.listdir("./cleaned_chunks"):
    if file.endswith(".m4a"):
        combined += AudioSegment.from_file(f"./cleaned_chunks/{file}", format="mp3")

# Export the combined audio file
combined.export("cleaned_audio.mp3", format="mp3")



