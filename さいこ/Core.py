# -*- coding: UTF-8 -*-

import numpy as np

# [[freq,AmpReal,AmpImag],...]
def Synth(__voice:list,__length:int,__freq:float,__vol:float,SampleRate = 64000):
    # 音轨缓冲区
    track = np.zeros(__length)
    # 时间序列
    timeRange = np.arange(__length,dtype=np.float64)*2*np.pi/SampleRate

    for voiceunit in __voice:
        # 实部
        track +=( __vol * voiceunit[1] )*np.cos((__freq*voiceunit[0])*timeRange)
        # 虚部
        track +=( __vol * voiceunit[2] )*np.sin((__freq*voiceunit[0])*timeRange)
    return track

# 包络线
def Envelop(__track:np.ndarray,envelop:np.ndarray):
    env = np.interp(
        np.arange(0,envelop.size,envelop.size / __track.size),
        np.arange(envelop.size),
        envelop
    )
    return env*__track

def SquartSynth(__High:float,__length:int,__freq:float,__vol:float,SampleRate = 64000):
    # 一小节长度
    if __freq > 0.:
        length = int(SampleRate/__freq)
    else:
        return np.array([1.]*__length)
    # HIGH长度
    HIGH = int(length*__High)

    ver = np.array([1.]*HIGH+[-1.]*(length-HIGH),dtype=np.float64)
    rep = int(np.ceil(__length/length))

    track = np.array([],dtype=np.float64)

    for i in range(rep):
        track = np.append(track,ver)


    return track[:__length]*__vol


