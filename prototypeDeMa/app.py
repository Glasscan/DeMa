"""Module for initializing the application."""

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from prototypeDeMa.listener import MicrophoneStream
from prototypeDeMa.settings.config import Config


def main():
    """Application's main method. Loads configs and creates audio stream.

    After loading the configurations, we use these settings to initialize
    the client used for the cloud Speech-to-Text API. The client is used
    to continuously process audio retrieved from a microphone before passing
    the data back to be further processed by the application via ActionReader.
    """

    botConfig = Config()
    bitRate = botConfig.bitRate
    chunkSize = int(bitRate / 10)
    languageCode = botConfig.languageCode

    client = speech.SpeechClient()
    clientConfig = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=bitRate,
        language_code=languageCode)
    streamingConfig = types.StreamingRecognitionConfig(config=clientConfig)

    print("Beginning live test...")
    with MicrophoneStream(bitRate, chunkSize, botConfig) as audioStream:
        audioGenerator = audioStream.outputGenerator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audioGenerator)
        responses = client.streaming_recognize(streamingConfig, requests)
        audioStream.listen(responses)
