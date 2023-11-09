import さいこ
import json

score = []
voice = []

def LoadJSONScore(file:str):
    global score
    with open(file,'r',encoding='utf-8') as f:
        score = json.loads(f.read())

def LoadJSONVoice(file:str):
    global voice
    with open(file,'r',encoding='utf-8') as f:
        voice = json.loads(f.read())

def Main():
    tmp = さいこ.np.array([],dtype=さいこ.np.float64)
    for track in score:
        spn = track.get('beat',64000)
        env = track.get('envelop',[1.])
        env = さいこ.np.array(env)
        eng = track.get('engine','SinWave')
        x,l,lt = さいこ.Score.SynthScore(voice,track.get('score',[]),track.get('voice',''),spn,eng,env)
        if tmp.size < x.size:
            tmp = さいこ.np.append(tmp,さいこ.np.zeros(x.size-tmp.size))
        tmp += x
    return tmp,l,lt

def Write(x,file):
    さいこ.sf.write(file,x,64000,'PCM_16')

def ProjectMain(project_name:str):
    print('Saiko Core Curse:START')
    LoadJSONScore(project_name+'.json')
    LoadJSONVoice('voice.json')
    track,l,lt = Main()
    Write(track,project_name+'.wav')
    with open(project_name+'.saikolrc','w',encoding='utf-8') as f:
        json.dump([l,lt],f,indent=1)
    print('Saiko Core Curse:END\n')

if __name__ == '__main__':
    import sys
    print('Saiko Core Curse:START')
    LoadJSONScore(sys.argv[1]+'.json')
    LoadJSONVoice('voice.json')
    track,l,lt = Main()
    Write(track,sys.argv[1]+'.wav')
    with open(sys.argv[1]+'.saikolrc','w') as f:
        json.dump([l,lt],f,indent=1)
    print('Saiko Core Curse:END\n')
    
