import json

#这玩意稳定性要求太强了
#看起来很糟糕的鸭子

voice = 'piano'
Global_Env = [0.0,0.8,0.8,0.8,0.6,0.6,0.3,0.0]
beat=6400
score = []

while True:
    TEXT = input('> ').split()
    if TEXT == 'show':
        print({'voice':voice,'envelop':Global_Env,'beat':beat,'score':score})
    elif len(TEXT) != 2:
        print('Error.')
    else:
        if TEXT[0] == 'save':
            with open(TEXT[1],'w',encoding='utf-8') as f:
                json.dump({'voice':voice,'envelop':Global_Env,'beat':beat,'score':score},f,indent=4, ensure_ascii=False)
            break
        if TEXT[0] == 'lrc':
            score.append({'lrc',TEXT[1]})
            pass
        if TEXT[0] == 'beat':
            beat = int(TEXT[1])
        try:
            p = float(TEXT[1])
        except ValueError:
            score.append({'beat':int(TEXT[0]),'pitchs':TEXT[1]})
        else:
            score.append({'beat':int(TEXT[0]),'pitchs':p})

            

    