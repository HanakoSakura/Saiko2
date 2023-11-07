# さいこ2 (Saiko2)

一个小小的正弦波合成器

## Usage

+ Synth
    
    > ./SaikoMain.py Scores/kokoronashi
    
    然后Saiko将会读取`kokoronashi.json`,<br>
    生成`WAV`文件和`saikolrc`文件(歌词，遵循JSON规范)

+ Play
    > ./Player.py Scores/kokoronashi

    Saiko将会尝试读取`kokoronashi.wav`和`kokoronashi.saikolrc`
    然后使用`pygame`来播放音乐和实时显示歌词
    界面部分还没有完成