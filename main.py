def on_forever():
    basic.show_icon(IconNames.DUCK)
basic.forever(on_forever)

def on_button_pressed_b():
  basic.show_string("Quack")
input.on_button_pressed(Button.B, on_button_pressed_b)
