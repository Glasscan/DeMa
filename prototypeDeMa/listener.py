"""Module for handling voice input and passing the commands to ActionReader."""

import pyaudio
import queue
import re
import prototypeDeMa.actionReader as EX


class MicrophoneStream(object):
    """Opens an audio stream that yields audio chunks from a microphone.

    This works essentially the same as the class provided by Google in their
    Speech-to-Text Python example, but with some changes made to suit the
    application. The main difference is the handling of the output. Rather then
    outputting the audio as text, I introduce a new module which takes the
    audio input and parses it. The result: a command should be performed based
    on the input.

    Args:
        bitRate (int): For the bit rate of the audio stream.
        chunkSize (int): For the size of each audio chunk in bytes.

    Attributes:
        _bitRate (int): The bit rate of the audio stream.
        _chunkSize (int): The size of each audio chunk in bytes.
        _buff (Queue): A blocking queue which continuously accepts audio
            chunks.
        closed (boolean): Determines whether the stream is/should be closed.
        _thinker (ActionReader): For interpreting/handling the result.
        _interface (PyAudio): Audio interface provided by pyaudio.
        _stream (Stream): The audio stream.
    """

    def __init__(self, bitRate, chunkSize, botConfig):
        """Initialize an instance of a MicrophoneStream.

        The input paramaters are retrieved from a config file.
        """

        self._bitRate = bitRate
        self._chunkSize = chunkSize
        self._buff = queue.Queue()
        self.closed = True
        self._config = botConfig
        self._thinker = EX.ActionReader()

    def __enter__(self):
        """Initialize audio interface and stream when entering 'with' block.

        Uses the pyaudio library.

        Returns:
            self: This instance of MicrophoneStream
        """

        self._interface = pyaudio.PyAudio()
        self._stream = self._interface.open(
            rate=self._bitRate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self._chunkSize,
            stream_callback=self._fillBuffer)
        #   self._stream.start_stream()
        self.closed = False
        return self

    def __exit__(self, type, value, traceback):
        """Close the audio interface and stream.

        Upon exiting the 'with' block, close the stream and interface. The
        attribute, _buff, is sent a 'None,' signaling the queue to close.

        Args:
            type: not used
            value: not used
            traceback: not used
        """

        self._stream.stop_stream()
        self._stream.close()
        self._interface.terminate()
        self.closed = True
        self._buff.put(None)

    def _fillBuffer(self, in_data, frame_count, time_info, status_flags):
        """Fill our queue, _self, with audio chunks.

        This method is the callback for _stream and follows the parameters
        specified by the pyaudio library. The values in in_data should be
        the audio chunks obtained from our microphone.

        Returns:
            (None, pyaudio.paContinue): Outputs no data (None), and signals
                that there is still more audio to process (paContinues).
        """

        self._buff.put(in_data)
        return (None, pyaudio.paContinue)

    def outputGenerator(self):
        """'Yield' the resulting data in _buff; waiting when necessary.

        The outputGenerator continuously takes the audio chunks received
        as input and 'yields' the resulting byte string.

        Yields:
            A byte string made from our voice data.
        """

        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]
            # check to see if there is more audio to process
            while 1:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break
            yield b''.join(data)

    def listen(self, responses):
        """'Listen' for the processed audio and pass on result for command execution.

        The method takes the responses, which are audio chunks processed by
        Google's cloud Speech-to-Text API, and passes them on to _thinker to
        be processed. This function continues until it is told to 'break,'
        after which the we leave the 'with' block and execute __exit__().


        A regular expression is used to check for the 3 "exit" values: 'exit,'
        'quit,' and 'stop.'

        Args:
            responses (JSON): .JSON formatted object containing audio info.
        """

        for response in responses:
            result = response.results[0]
            alternative = result.alternatives[0]
            transcript = alternative.transcript.strip()

            if result.is_final:
                self._thinker.readAction(transcript)
                # Move below to actionReader
                if re.fullmatch(r'\b(exit|quit|stop)\b', transcript, re.I):
                    print("Exiting...")
                    break
