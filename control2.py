import pyfirmata
from pyfirmata import util
import time

comport = 'COM5'    # Replace with COM port
board = pyfirmata.Arduino(comport)

sR = board.get_pin('d:10:o')
one = board.get_pin('d:9:o')
two = board.get_pin('d:6:o')
three = board.get_pin('d:5:o')
four = board.get_pin('d:3:o')
sL = board.get_pin('d:11:o')
# IR sensor pins
ir_front = board.get_pin('d:12:i')
ir_back = board.get_pin('d:13:i')
thread = util.Iterator(board)
thread.start()
time.sleep(1) 
# print("IR 2 :",board.digital[13].read())
# print("IR 1 :",board.digital[12].read())
def operation(total):
    if total == 4 and not board.digital[13].read():
        total = 0
    elif not board.digital[12].read() and total != 4:
        total = 0
    else:
        pass
    print(total)
    if total == 0:
        print("stop")
        sR.write(0)
        sL.write(0)
        one.write(0)
        two.write(0)
        three.write(0)
        four.write(0)
    elif total == 1:
        print("forward")
        sR.write(1)
        sL.write(1)
        one.write(1)
        two.write(0)
        three.write(1)
        four.write(0)
    elif total == 2:
        print("right")
        sR.write(1)
        sL.write(1)
        one.write(0)
        two.write(0)
        three.write(1)
        four.write(0)
    elif total == 3:
        print("left")
        sR.write(1)
        sL.write(1)
        one.write(1)
        two.write(0)
        three.write(0)
        four.write(0)
    elif total == 4:
        print("backward")
        sR.write(1)
        sL.write(1)
        one.write(0)
        two.write(1)
        three.write(0)
        four.write(1)
    elif total == 5:
        print("break")
        sR.write(0)
        sL.write(0)
        one.write(0)
        two.write(0)
        three.write(0)
        four.write(0)
    return