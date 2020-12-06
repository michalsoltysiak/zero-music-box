import alsaaudio

def set_volume(mixer:alsaaudio.Mixer, volume: int):
    if volume > 100:
        volume = 100
    mixer.setvolume(volume)
    volume = mixer.getvolume()[0]
    print(f'Set volume to {volume}')

step = 10
mixers = alsaaudio.mixers()
print(mixers)
mixer = alsaaudio.Mixer(mixers[0])
volume = mixer.getvolume()[0]
print(f'volume is {volume}')

import sys
try:
    input = sys.argv[1]
    if input == '+':
        step = step
    elif input == '-':
        step = -step
    else:
        volume = int(input)
        step = 0
    set_volume(mixer, volume+step)
except IndexError:
    exit(0)
except ValueError:
    print('wrong param')
    exit(1)


