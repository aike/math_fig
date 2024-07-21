import numpy as np
from matplotlib import pyplot
from matplotlib import patches

ax = 0

def init_graph():
    global ax

    size = 10
    col = '#444444'
    
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal') # アスペクト比イコール
    
    point_x = {'start': [-3, 0], 'end': [7, 0]}
    point_y = {'start': [0, -2], 'end': [0, size * 0.7]}

    ax.annotate('', xy=point_x['end'], xytext=point_x['start'],  # X軸
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor=col, edgecolor=col)
               )
    ax.annotate('', xy=point_y['end'], xytext=point_y['start'],  # Y軸
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor=col, edgecolor=col)
               )


    # グラフの範囲
    ax.set_xlim([-3, 7])
    ax.set_ylim([-2, size * 0.7])

    ax.axis("off") # 外枠の軸を消す
    ax.text(-0.5, -0.5, "0", fontstyle='oblique', fontname='serif', fontsize="large") # 原点０の表示
    ax.text(7 * 0.95, -0.8, "x", fontstyle='oblique', fontname='serif', fontsize="x-large") # xの表示
    ax.text(-0.8, size * 0.65, "y", fontstyle='oblique', fontname='serif', fontsize="x-large") # yの表示
    


def draw_vec(x, y, col):
    global ax
    point = {'start': [0, 0], 'end': [x, y]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor=col, edgecolor=col))

def draw_vec2(x0, y0, x1, y1, col):
    global ax
    point = {'start': [x0, y0], 'end': [x1, y1]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor=col, edgecolor=col))

def draw_line(x0, y0, x1, y1, col):
    global ax
    point = {'start': [x0, y0], 'end': [x1, y1]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
            arrowprops=dict(arrowstyle='-', 
                            connectionstyle='arc3', 
                            facecolor=col, edgecolor=col))

def draw_dline(x0, y0, x1, y1, col):
    global ax
    point = {'start': [x0, y0], 'end': [x1, y1]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
            arrowprops=dict(arrowstyle='-', 
                            connectionstyle='arc3', 
                            linestyle='dotted',
                            alpha=0.7,
                            facecolor=col, edgecolor=col))

def draw_text(x, y, s):
    global ax
    ax.text(x, y, s, fontstyle='oblique', fontname='serif', fontsize="x-large") 

def draw_text2(x, y, s, size):
    global ax
    ax.text(x, y, s, fontstyle='oblique', fontname='serif', fontsize=size) 


def draw_dot(x, y):
    pyplot.plot(x,y,'black',marker='.', markersize=10)


def draw_arc(x0, y0, x1, y1, col):
    global ax
    a = patches.Arc((x0, y0), x1, y1, theta1=0, theta2=60, edgecolor=col, linewidth=1)
    ax.add_patch(a)


init_graph()

# draw_vec2(0, 0.2, 5.0, 2.7, 'red')
# draw_vec2(0, 0, 5.1, 2.55, 'blue')

# draw_text(3.8, 3.2, 'P(x, y)')
# draw_text(6.5, 4.5, "P'(kx, ky)")

draw_dot(3,0)
draw_dot(5,0)
draw_dot(3,2)
draw_dot(5,2)

draw_line(3,0,5,0,'red')
draw_line(5,0,5,2,'red')
draw_line(5,2,3,2,'red')
draw_line(3,2,3,0,'red')

# 45 deg
p0 = [2.09807621, 2.3660254 ]
p1 = [3.83012702, 3.3660254 ]
p2 = [2.83012702, 5.09807621]
p3 = [1.09807621, 4.09807621]

# 60 deg
p0 = [0.6339746,  3.09807621]
p1 = [1.6339746,  4.83012702]
p2 = [-0.09807621,  5.83012702]
p3 = [-1.09807621, 4.09807621]

p0 = [1.5,        2.59807621]
p1 = [2.5,        4.33012702]
p2 = [0.76794919, 5.33012702]
p3 = [-0.23205081,  3.59807621]

draw_dot(p0[0], p0[1])
draw_dot(p1[0], p1[1])
draw_dot(p2[0], p2[1])
draw_dot(p3[0], p3[1])

draw_line(p0[0],p0[1],p1[0],p1[1],'blue')
draw_line(p1[0],p1[1],p2[0],p2[1],'blue')
draw_line(p2[0],p2[1],p3[0],p3[1],'blue')
draw_line(p3[0],p3[1],p0[0],p0[1],'blue')

draw_dline(0,0,p0[0],p0[1],'gray')

draw_arc(0, 0, 2, 2, 'black')

draw_text2(3.2, 2.3, 'P1', 'medium')
draw_text2(5.2, 2.3, 'P2', 'medium')
draw_text2(3.2, 0.3, 'P3', 'medium')
draw_text2(5.2, 0.3, 'P4', 'medium')

draw_text2(-1, 3.3, "P1'", 'medium')
draw_text2(0.9, 5.5, "P2'", 'medium')
draw_text2(1.8, 2.5, "P3'", 'medium')
draw_text2(2.8, 4.3, "P4'", 'medium')

draw_text(1, 0.5, "θ",)



pyplot.show()