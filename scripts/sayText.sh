#!/bin/sh
pico2wave -l fr-FR -w /home/pi/Jerry/scripts/res/message.wav "$1"
cvlc --pitch-shift -5 --audio-filter=scaletempo_pitch --play-and-exit --alsa-audio-device output /home/pi/Jerry/scripts/res/message.wav
