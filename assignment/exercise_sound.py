#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

""" 
freq: float = 30
duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

for i in range(64):
    print(freq)
    playtone(freq, duration)
    freq = int(freq * 1.1)
"""
# Happy Birthday Notes
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
C5 = 523.25

# Happy Birthday melody
happy_birthday = [
    (C4, 1), (C4, 1), (D4, 1), (C4, 1), (F4, 1), (E4, 2),
    (C4, 1), (C4, 1), (D4, 1), (C4, 1), (G4, 1), (F4, 2),
    (C4, 1), (C4, 1), (C5, 1), (A4, 1), (F4, 1), (E4, 1), (D4, 2),
    (B4, 1), (B4, 1), (A4, 1), (F4, 1), (G4, 1), (F4, 2)
]

for note, duration in happy_birthday:
    print(f"Playing frequency (Hz): {note:.2f} ")
    playtone(note, duration)
    quiet()
    utime.sleep(0.1)






# Turn off the PWM
quiet()
