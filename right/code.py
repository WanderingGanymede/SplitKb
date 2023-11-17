print("Starting")
#Split36key Left
import board

from kmk.modules.split import Split, SplitType, SplitSide


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP16,board.GP18,board.GP20,board.GP22,board.GP26,)
keyboard.row_pins = (board.GP9,board.GP11,board.GP13,board.GP15,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(split_side=SplitSide.RIGHT,
              split_flip=False,
              data_pin=board.GP5,
              data_pin2= board.GP28,
              uart_flip=True,
              use_pio=True)

keyboard.modules.append(split)


keyboard.keymap = [
    [  KC.Y  ,  KC.U  ,  KC.I  ,  KC.O  ,  KC.P ,
  KC.H  ,  KC.J  ,  KC.K  ,  KC.L  ,  KC.NO , 
       KC.N  ,  KC.M  ,  KC.NO  ,  KC.NO  ,  KC.NO,
       KC.N1  ,  KC.N2  ,  KC.N3  ,  KC.NO  ,  KC.NO,
    ] 
    
]

if __name__ == '__main__':
    keyboard.go()