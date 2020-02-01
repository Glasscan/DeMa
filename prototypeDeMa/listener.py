import pyaudio
import queue
import re
import prototypeDeMa.actionReader as EX


class MicrophoneStream(object):
    def __init__(self, bitRate, chunkSize):
        self._bitRate = bitRate
        self._chunkSize = chunkSize
        self._buff = queue.Queue()
        self.closed = True
        self._thinker = EX.ActionReader()

    def __enter__(self):
        self._interface = pyaudio.PyAudio()
        self._stream = self._interface.open(
            rate=self._bitRate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self._chunkSize,
            stream_callback=self._fillBuffer)
#           self._stream.start_stream()
        self.closed = False
        return self

    def __exit__(self, type, value, traceback):
        self._stream.stop_stream()
        self._stream.close()
        self._interface.terminate()
        self.closed = True
        self._buff.put(None)

#   Following the PyAudio documentation:
#   in_data: recorded/input data
#   frame_count: number of frames
#   time_info: a dictionary
#   status_flags: PaCallbackFlags
    def _fillBuffer(self, in_data, frame_count, time_info, status_flags):
        self._buff.put(in_data)
        return (None, pyaudio.paContinue)

    def outputGenerator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]
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
        for response in responses:
            result = response.results[0]
            alternative = result.alternatives[0]
            transcript = alternative.transcript.strip()

            if result.is_final:
                self._thinker.readAction(transcript)
                if re.fullmatch(r'\b(exit|quit|stop)\b', transcript, re.I):
                    print("Exiting...")
                    break
