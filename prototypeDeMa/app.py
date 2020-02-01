from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from prototypeDeMa.listener import MicrophoneStream
from prototypeDeMa.settings.config import Config


def main():
    config = Config()
    bitRate = config.bitRate
    chunkSize = int(bitRate / 10)
    languageCode = config.languageCode

    client = speech.SpeechClient()
    clientConfig = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=bitRate,
        language_code=languageCode)
    streamingConfig = types.StreamingRecognitionConfig(config=clientConfig)
    print("Beginning live test...")
    with MicrophoneStream(bitRate, chunkSize) as audioStream:
        audioGenerator = audioStream.outputGenerator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audioGenerator)
        responses = client.streaming_recognize(streamingConfig, requests)
        audioStream.listen(responses)
