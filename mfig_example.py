import mfig

mfig.init(origin="leftbottom")

mfig.vec(3, 1,'red')
mfig.vec(5, 6,'blue')

mfig.vec2(3+0.2,1+0.2,5+0.2,6-0.2,'#aaaaaa')

mfig.dot(3, 1)
mfig.dot(5, 6)

mfig.text(3.5, 1, "P(3,1)", 'xx-large')
mfig.text(5.5, 5.5, "P´(5,6)", 'xx-large')

mfig.show()

