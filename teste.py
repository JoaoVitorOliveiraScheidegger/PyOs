from driverVideo import DriverVideo
from time import sleep
video = DriverVideo()

video.turn_on()

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


video.draw([[7, 6, 'Deligando']])
sleep(2)
video.turn_off()