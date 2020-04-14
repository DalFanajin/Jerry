#!/bin/sh
python3 /home/pi/Jerry/scripts/listening.py &

pico2wave -l fr-FR -w /home/pi/Jerry/scripts/res/listening.wav "je vous écoute"
vlc --play-and-exit --alsa-audio-device output /home/pi/Jerry/scripts/res/listening.wav


