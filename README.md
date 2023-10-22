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
  RESULTS: (better than aws transcribe 1)

Whisper 2
- First used noise reduction on the audio
- Then used Large v2 model
    NO CUSTOMIZATION 
    NO special vocabulary
  results in whisper_2.json
  - Took around 10 minutes to run on 1 hour of audio, on ml.cs.tcu.edu
  RESULTS: (worse than whisper 1)


## Files

* [Original audio file](Linux-9-28-2023.m4a)
* [Reduced noise audio file](cleaned_audio.mp3)
* [AWS Transcribe 1](aws_transcribe_1.json)
* [Whisper 1](whisper_1.json)
* [Whisper 2](whisper_2.json)
* [AssemblyAPI Results](assemblyAI.csv)

- [Noise reduction script](noise_reduction.py)
- [Whisper Transcription script](whisper_transcription.py)

## Results

I used the [WER](https://en.wikipedia.org/wiki/Word_error_rate) metric to compare the results of the models. The lower the WER, the better the model.

Unfortunately I do not have a ground truth for this audio. 



