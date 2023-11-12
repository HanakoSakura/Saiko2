# -*- coding: UTF-8 -*-

# 仅用于测试
# 单音轨乐谱

if __name__ == '__main__':
    import Core
    import PITCH
else:
    from . import Core,PITCH
import numpy as np

def Analyzer(voice_table:dict,score:list,**other):
    '''
    other参数:
    default_voice,sr,SamplePerBeat,Volume,Envelop,Engine
    '''
    # 歌词部分
    lyc = [] # 歌词
    lyctime = [] # 歌词对应时间
    # 音符合成缓冲区
    notes_list = []

    # 音符位置
    mov = 1
    # 当前采样
    sample = 0
    for note in score:
        print('Core Curse Analyzing : ',mov,'/',len(score),end='\r')
        mov += 1

        # 注释
        if note.get('note') != None:
            continue
        # 歌词
        if note.get('lyc') != None:
            lyc.append(note.get('lyc'))
            lyctime.append(sample)
            continue
        if note.get('lrc') != None:
            lyc.append(note.get('lrc'))
            lyctime.append(sample)
            continue
        
        # 获取音色
        _voice = voice_table.get(
            note.get(
                'voice',other.get('default_voice')
            )
            ,
            [[1,0,1]]
        )
        # 采样率
        SampleRate = other.get('sr',64000)
        # 音调
        freqs = note.get('pitchs')
        if freqs == None:
            freqs = note.get('pitch')
            if freqs == None:
                freqs = 0.
        if type(freqs) != list:
            freqs = [freqs]
        for i in range(len(freqs)):
            if type(freqs[i])  == str:
                freqs[i] = PITCH.GetPitch(freqs[i])
        
        # 节拍数
        length = note.get('beat',1)
        spb = other.get('SamplePerBeat',64000)

        sample += length*spb

        # 音量
        vol = note.get('vol',other.get('Volume',1.0))
        # 包络线
        env = note.get('envelop',other.get('Envelop',[1.,1.]))

        tmp = np.zeros(length*spb)
        engine = other.get('Engine','SinWave')
        for pernote in freqs:
            if engine == 'SinWave':
                tmp += Core.Envelop(Core.Synth(_voice,length*spb,pernote,vol),env)
            elif engine == 'SquartWave':
                tmp += Core.Envelop(Core.SquartSynth(1/3,length*spb,pernote,vol),env)
        notes_list.append(tmp)
    print()
    return np.concatenate(notes_list),lyc,lyctime


        
        
