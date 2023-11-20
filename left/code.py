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
    Chord((KC.D,KC.F),KC.ESCAPE),
    Chord((KC.K,KC.J),KC.ESCAPE),
    Chord((KC.F,KC.J),KC.ESCAPE),
    Chord((KC.X,KC.C),KC.TAB),
    Chord((KC.DOT,KC.SCOLON),KC.ENTER),   
    Chord((KC.DOT,KC.SLASH),KC.RSFT),   
    Chord((KC.L,KC.SCOLON),KC.RCTRL),
    Chord((KC.DOT,KC.COMMA),KC.RALT),
    
    Chord((KC.SCOLON,KC.SLASH),KC.RSFT(KC.RCTL)),   
    Chord((KC.SCOLON,KC.COMMA),KC.RCTRL(KC.RALT)),
    Chord((KC.DOT,KC.COMMA,KC.SLASH),KC.RALT(KC.RSFT)),
]

keyboard.modules.append(split)

UNDO = KC.LCTRL(KC.Y)
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
 
NAVTAB = KC.LT(1,KC.TAB)
NUMLAYER = KC.HT(KC.TAB,KC.TG(2))
NO = KC.NO
TP = KC.TRANSPARENT;

FNLAYER = KC.LT(4,KC.DELETE) 
NUMLAYER = KC.LT(2,KC.BSPACE)
SFT_TD= KC.TD(
    KC.LSFT,
    KC.CW
    )

keyboard.keymap = [
    [  KC.Q  ,  KC.W  ,  KC.E  ,  KC.R  ,  KC.T ,KC.Y  ,  KC.U  ,  KC.I  ,  KC.O  ,  KC.P ,
      KC.A   , KC.S  , KC.D,  KC.F  ,  KC.G , KC.H  ,  KC.J ,  KC.K  ,  KC.L  ,  KC.SCOLON , 
      LGUI  ,  LALT  , LCTL,   KC.V,    KC.B, KC.N  , KC.M  ,  KC.COMMA  , KC.DOT   , KC.SLASH    ,
       KC.NO  ,  KC.NO  ,  SFT_TD ,  NAVTAB  ,  LEFTSPACE, RIGHTSPACE,  NUMLAYER  ,  FNLAYER  ,  KC.NO  ,  KC.NO,
    ] ,             
    [  TP, TP, TP, TP, TP, TP, TP, TP, TP, TP,
       TP, TP, TP, TP, TP, KC.LEFT, KC.DOWN , KC.UP, KC.RIGHT, TP,
        TP, TP, TP, TP, TP, TP, TP, TP, TP, TP,
        NO, NO, TP, TP, TP, TP, TP, TP, NO, NO, ],
    [ 
     KC.LBRC, KC.N7, KC.N8,KC.N9, KC.RBRC, TP , TP , TP , TP , TP ,   
      KC.COLON , KC.N4, KC.N5,KC.N6,KC.KP_PLUS, TP , KC.RSFT, KC.RALT , KC.RTCL , KC.RGUI,
     TP, KC.N1, KC.N2,KC.N3, KC.BSLASH,   TP , TP , TP , TP , TP ,
        NO, NO, TP, KC.N0,KC.KP_MINUS,  TP, TP , TP, NO ,  NO,
    
    ]
    ,
    #Symbols
     [  
        TP , TP , TP , TP , TP , TP , TP , TP , TP , TP ,
        TP , TP , TP , TP , TP , TP , TP , TP , TP , TP ,
        TP , TP , TP , TP , TP , TP , TP , TP , TP , TP ,
        NO , NO , TP , TP , TP , TP , TP , TP , NO , NO ,
    ]
    ,
    #FN keys
    
     [ 
        KC.F12  ,  KC.F7  ,  KC.F8  ,  KC.F9  , TP  ,            TP  ,  TP  ,  TP  ,  TP  , TP  ,
        KC.F11  ,  KC.F4  ,  KC.F5  ,  KC.F6  , TP  ,            TP  ,  TP  ,  TP  ,  TP  , TP  ,
        KC.F10  ,  KC.F1  ,  KC.F2  ,  KC.F3  , TP  ,            TP  ,  TP  ,  TP  ,  TP  , TP  ,
        TP      ,  TP     ,  TP     ,  TP     , TP  ,            TP  ,  TP  ,  TP  ,  TP  , TP  ,
    ]
]

if __name__ == '__main__':
    keyboard.go()
               