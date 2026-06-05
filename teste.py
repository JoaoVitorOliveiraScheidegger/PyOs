from driverVideo import DriverVideo
from time import sleep
video = DriverVideo()

video.ligar()

video.draw([[2, 3, 'Oi']])

for i in range(10):
    video.draw([[2, 3, 'Carregando.'], [4, 5, 'Oi']])
    sleep(0.1)
    video.draw([[2, 3, 'Carregando..'], [4, 5, 'Oi']])
    sleep(0.1)
    video.draw([[2, 3, 'Carregando...'], [4, 5, 'Oi']])
    sleep(0.1)
    video.draw([[2, 3, 'Carregando....'], [4, 5, 'Oi']])
    sleep(0.1)

sleep(2)

video.desligar()