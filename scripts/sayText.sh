#!/bin/sh
pico2wave -l fr-FR -w /home/pi/Jerry/scripts/res/message.wav "$1"
vlc --play-and-exit --alsa-audio-device output /home/pi/Jerry/scripts/res/message.wav
