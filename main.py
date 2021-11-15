随机数字 = 0

def on_gesture_shake():
    global 随机数字
    随机数字 = randint(1, 3)
    soundExpression.sad.play()
    if 随机数字 == 1:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        """)
    elif 随机数字 == 2:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    else:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
