print("Starting")
#Split36key Left
import board
from kmk.modules.layers import Layers
from kmk.modules.capsword import CapsWord
from kmk.modules.tapdance import TapDance

from kmk.modules.split import Split, SplitType, SplitSide
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.combos import Combos, Chord, Sequence

from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()


keyboard.col_pins = (board.GP26,board.GP22,board.GP20,board.GP18,board.GP16,)
keyboard.row_pins = (board.GP7,board.GP11,board.GP13,board.GP15,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(split_side=SplitSide.LEFT,
              split_flip=False,
              data_pin=board.GP5,
              data_pin2= board.GP28,
              uart_flip=True,
              use_pio=True)

holdtap = HoldTap() 
keyboard.modules.append(Layers()) 
combos = Combos()# default inactivity timeout is 8s
caps_word=CapsWord()
tapdance = TapDance()
keyboard.modules.append(caps_word)
keyboard.modules.append(combos)
keyboard.modules.append(tapdance)
keyboard.modules.append(holdtap)
# optional: set a custom tap timeout in ms
holdtap.tap_time = 300


LEFTSPACE =KC.SPACE
RIGHTSPACE = KC.SPACE
combos.combos= [
    Chord((LEFTSPACE,RIGHTSPACE),KC.ENTER),
    Chord((KC.G,KC.F),KC.ESCAPE),
    Chord((KC.H,KC.J),KC.ESCAPE),
    Chord((KC.X,KC.C),KC.TAB),
    Chord((KC.DOT,KC.SLASH),KC.ENTER),
    Chord((KC.M,KC.V),KC.CW)
]


keyboard.modules.append(split)
LGUI = KC.HT(KC.Z,KC.LGUI)
LALT = KC.HT(KC.X, KC.LALT)
LCTL = KC.HT(KC.C, KC.LCTRL)
LSFT = KC.HT(KC.V, KC.LSFT)

RGUI = KC.HT(KC.SLASH,KC.RGUI)
RALT = KC.HT(KC.DOT, KC.RALT)
RCTL = KC.HT(KC.COMMA, KC.RCTRL)
RSFT = KC.HT(KC.M, KC.RSFT)
NAVSPACE = KC.LT(1, LEFTSPACE) 

NUMTOG= KC.TG(2) 
NUMTAB = KC.L
NUMLAYER = KC.HT(KC.TAB,KC.TG(2))
NO = KC.NO
TP = KC.TRANSPARENT;
keyboard.keymap = [
    [  KC.Q  ,  KC.W  ,  KC.E  ,  KC.R  ,  KC.T ,KC.Y  ,  KC.U  ,  KC.I  ,  KC.O  ,  KC.P ,
      KC.A   , KC.S  , KC.D,  KC.F  ,  KC.G , KC.H  ,  KC.J ,  KC.K  ,  KC.L  ,  KC.SCOLON , 
      LGUI  ,  LALT  , LCTL,   LSFT,    KC.B, KC.N  , RSFT  ,  RCTL  , KC.DOT   , KC.SLASH    ,
       KC.NO  ,  KC.NO  ,  KC.ESCAPE  ,  KC.TAB  ,  LEFTSPACE, RIGHTSPACE,  KC.BSPACE  ,  KC.DELETE  ,  KC.NO  ,  KC.NO,
    ] ,             
    [  TP, TP, TP, TP, TP, TP, TP, TP, TP, TP,
       TP, TP, TP, TP, TP, KC.LEFT, KC.DOWN , KC.UP, KC.RIGHT, TP,
        TP, TP, TP, TP, TP, TP, TP, TP, TP, TP,
        NO, NO, TP, TP, TP, TP, TP, TP, NO, NO,
    ],
    [  NUMTOG, NUMTOG,NUMTOG, NUMTOG, NUMTOG, KC.KP_SLASH, KC.KP_7, KC.KP_8,KC.KP_9, KC.KP_EQUAL, 
       NUMTOG, NUMTOG,NUMTOG, NUMTOG, NUMTOG, KC.KP_ASTERISK , KC.KP_4, KC.KP_5,KC.KP_6,TP, 
       NUMTOG, NUMTOG,NUMTOG, NUMTOG, NUMTOG, KC.KP_0, KC.KP_1, KC.KP_2,KC.KP_3, KC.KP_0, 
        NO, NO, TP, NUMTOG, TP, TP,  TP, TP, NO ,  NO,
    
    ]
    ,
     [  KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,
       TP, TP, TP, TP, TP, TP , TP , TP,TP, TP,
        TP, TP, TP, TP, TP, TP, TP, TP, TP, TP,
        NO, NO, TP, TP, TP, TP, TP, TP, NO, NO,
    ]
    ,
     [ 
        TP  ,  KC.F7  ,  TP  ,  TP  , TP  ,            TP  ,  TP  ,  TP  ,  TP  , TP  ,
        TP  ,  TP  ,  TP  ,  TP  , TP  ,            TP  ,  TP  ,  TP  ,  TP  , TP  ,
        TP  ,  TP  ,  TP  ,  TP  , TP  ,            TP  ,  TP  ,  TP  ,  TP  , TP  ,
        TP  ,  TP  ,  TP  ,  TP  , TP  ,            TP  ,  TP  ,  TP  ,  TP  , TP  ,
    ]
]

if __name__ == '__main__':
    keyboard.go()
               