import torch
import json

#cuda
if not torch.cuda.is_available():
    raise Exception("CUDA not available- this makes the medium/large model too slow to run.")

import whisper

model = whisper.load_model("large") # Runs largev2 
result = model.transcribe("Linux-9-28-2023.m4a")


# Save the result as a JSON file
with open("result.json", "w") as f:  # Use "result.json" instead of "result.txt"
    # Serialize the result as JSON and write it to the file
    json.dump(result, f, indent=4)

# Save result to file
with open("result.txt", "w") as f:
    f.write(result["text"])