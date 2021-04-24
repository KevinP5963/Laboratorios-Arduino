import pyfirmata2

DELAY = 1 
PORT=pyfirmata2.Arduino.AUTODETECT

board = pyfirmata2.Arduino(PORT)

board.digital[3].write(1)
board.pass_time(DELAY)
boart.analog[4]
board.analogwrite(LED, 4)