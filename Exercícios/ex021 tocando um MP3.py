from pygame import mixer

mixer.init()
mixer.music.load('assets/music/soundoflegend-maniac.mp3')
mixer.music.play()

stopMusic = input('Aperte ENTER para parar a música: ')
