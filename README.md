# Model Comparisons

Compares the performance of STT (transcription) models on classrom audio data.

## Data

https://tcu.app.box.com/file/1339927312124?s=gdr527kvqai17wtnhqc03kr8yq2iwc2h

Completely unprocessed. 

## Models

AWS Transcribe 1
- https://aws.amazon.com/transcribe/
- Used English general model
    NO CUSTOMIZATION 
    NO special vocabulary
  results in aws_transcribe_1.json
    
Whisper 1
- https://github.com/openai/whisper/
- Used Large v2 model
    NO CUSTOMIZATION 
    NO special vocabulary
  results in whisper_1.json
  - Took around 10 minutes to run on 1 hour of audio, on ml.cs.tcu.edu