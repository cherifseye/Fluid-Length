#importer les librairies nécessaires
from pyfirmata import Arduino, util
import time
port = '/dev/cu.usbmodem141101' #Port Usb reliant l'arduino et l'ordinateur
board = Arduino(port)
it = util.Iterator(board)
it.start()

pindiode = board.get_pin('a:0:i') #Pin analog relie a la photodiode et resistance equivalent de Pinmode en Arduino

while True: #Tant que le programme n'est pas arrêté, revoir les données du capteur par intervalle de 500ms
    ival = pindiode.read()
    if ival is not None:
        print
        ival