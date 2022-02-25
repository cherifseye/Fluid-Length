from time import sleep
from pyfirmata import Arduino, util

port = '/dev/cu.usbmodem141101'
board = Arduino(port)
it = util.Iterator(board)
it.start()

ledpin = board.get_pin('d:13:o')

while True:
    ledpin.write(1)
    sleep(1)
    ledpin.write(0)
    sleep(1)