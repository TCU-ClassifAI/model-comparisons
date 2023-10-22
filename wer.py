import jiwer
import json

# Load AWS Transcribe output (convert json to string)
# {"jobName":"linux_1","accountId":"203578434481","status":"COMPLETED","results":{"transcripts":[{"transcript":"Gonna do some questions in partitions. We gonna do some questions in partition. You wann

with open('aws_transcribe_1.json') as f:
    data = json.load(f)

hypothesis = data['results']['transcripts'][0]['transcript']
# print(hypothesis)

# Load Whisper transcription output (convert json to string)
# {"text": " we're gonna do some questions in partitions. You definitely wanna know how to do partitions, okay? So we'll officially come to chapter five. We're gonna make partitions, all right? So befor

with open('whisper_1.json') as f:
    data = json.load(f)

reference = data['text']


import csv

# Specify the path to your CSV file
csv_file_path = 'Linux-9-28-2023 (Transcribed by AssemblyAI).csv'  
# Initialize an empty string to store concatenated values
concatenated_values = ""

# Open the CSV file and read its content
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        if len(row) > 2:  # Ensure that there is a third column
            # Extract the value from the third column (0-indexed)
            column3_value = row[2]
            # Remove the starting and ending quotes
            column3_value = column3_value.strip('"')
            # Concatenate the value to the result string
            concatenated_values += column3_value + " "



# Calculate WER and print result

transformation = jiwer.Compose([
    jiwer.ToLowerCase(),
    jiwer.RemovePunctuation(),
    jiwer.RemoveWhiteSpace(replace_by_space=True),
    jiwer.RemoveMultipleSpaces(),
]) 



# Transform reference and hypothesis into lists of words
w_ref = transformation(reference)
w_hyp = transformation(hypothesis)
w_concat = transformation(concatenated_values)

# print(w_ref)
# print(w_hyp)
print(w_concat)