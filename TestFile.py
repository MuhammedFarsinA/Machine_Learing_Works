import assemblyai as aai

transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/meeting.mp4")

context = "A GitLab meeting to discuss logistics"
answer_format = "A list of bullet points"

result = tran