import simpleaudio
import threading

class Music(threading.Thread):
    def run(self):
        while True:
            wave_obj = simpleaudio.WaveObject.from_wave_file("sounds/hudba.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()

hudba = Music()
