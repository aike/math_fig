import numpy as np
import mfig

x = np.array([1,2,3])

mfig.init_graph()

mfig.draw_vec(3, 1,'red')
mfig.draw_vec(5, 6,'blue')

mfig.draw_vec2(3+0.2,1+0.2,5+0.2,6-0.2,'#aaaaaa')

mfig.draw_dot(3, 1)
mfig.draw_dot(5, 6)

mfig.draw_text2(3.5, 1, "P(3,1)", 'xx-large')
mfig.draw_text2(5.5, 5.5, "P´(5,6)", 'xx-large')

mfig.show()

