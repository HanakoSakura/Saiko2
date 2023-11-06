# -*- coding: UTF-8 -*-

from . import Core
from . import PITCH
import soundfile as sf
import numpy as np

def SynthScore(voice:dict,score:list,default_voice:str,SamplePerBeat:int,Engine:str,DefaultEnvelop:np.ndarray):
    lyc = []
    lyctime = []
    tracks = []


    mov = 1
    tim = 0
    for note in score:
        print('Core Curse Running : ',mov,'/',len(score),end='\r')
        mov+=1
        if note.get('lyc') != None:
            lyc.append(note.get('lyc'))
            lyctime.append(tim)
        elif note.get('lrc') != None:
            lyc.append(note.get('lrc'))
            lyctime.append(tim)
        else:
            _voi = voice.get(
                note.get(
                'voice',default_voice
                ),
                [[1,0,1]]
            )

            length = note.get('beat',1)
            tim+=length*SamplePerBeat

            freqs = note.get('pitchs',None)
            if freqs == None:
                freqs = note.get('pitch',None)
                if freqs == None:
                    print('\n*ERROR*:Cannot find Pitch value')
                    raise TypeError
            if type(freqs) != list:
                freqs = [freqs]
            for i in range(len(freqs)):
                if type(freqs[i]) == str:
                    freqs[i] = PITCH.GetPitch(freqs[i])
                

            vol = note.get('vol',1.0)

            env = note.get('envelop',DefaultEnvelop)

            for pernote in freqs:
                if Engine == 'SinWave':
                    tracks.append(
                        Core.Envelop(Core.Synth(_voi,length*SamplePerBeat,pernote,vol),env)
                    )
                elif Engine == 'SquartWave':
                    tracks.append(
                        Core.Envelop(Core.SquartSynth(1/3,length*SamplePerBeat,pernote,vol),env)
                    )
    
    print()
    return Core.np.concatenate(tracks),lyc,lyctime

def SupportEngine():
    return ('SinWave','SquartWave')

if __name__ == '__main__':
    v = {'test':[[1,0,0.5],[2,0,0.25]]}
    s = [
        {'lyc':'Testing'},
        {'lyc':'do'},
        {'beat':1,'pitchs':['A4']},
        {'lyc':'re'},
        {'beat':1,'pitchs':['B4']},
        {'lyc':'mi'},
        {'beat':1,'pitchs':['#C4']},
        {'lyc':'fa'},
        {'beat':1,'pitchs':['D4']},
        {'lyc':'so'},
        {'beat':1,'pitchs':['E4']},
        {'lyc':'la'},
        {'beat':1,'pitchs':['#F4']},
        {'lyc':'si'},
        {'beat':1,'pitchs':['#G4']},
        {'lyc':'do'},
        {'beat':1,'pitchs':['A5']},
    ]


    import time
    t1 = time.time_ns()
    t,l,lt = SynthScore(v,s,'test',64000)
    t2 = time.time_ns()
    print('Time:',(t2-t1)/1000000,'ms')
    print(l)
    print(lt)
    sf.write('test.wav',t,64000,'PCM_16')
