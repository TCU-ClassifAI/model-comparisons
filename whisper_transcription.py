import torch

#cuda
if not torch.cuda.is_available():
    raise Exception("CUDA not available- this makes the medium/large model too slow to run.")

import whisper

model = whisper.load_model("large") # Runs largev2 
result = model.transcribe("Linux-9-28-2023.m4a")

# Save result to file
with open("result.txt", "w") as f:
    f.write(result)