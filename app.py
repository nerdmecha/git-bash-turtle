import turtle as tt
from functions import *

tt.shape('turtle')
tt.onkeypress(left, 'Left')
tt.onkeypress(right, 'Right')
tt.onkeypress(up, 'Up')
tt.onkeypress(down, 'Down')

tt.onkeypress(pen_updown, 'Return')
tt.onkeypress(switch_color, 'c')
tt.onkeypress(clear, 'Escape')

tt.listen()
tt.mainloop()