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

draw_vec(3, 1,'red')
draw_vec(5, 6,'blue')

draw_vec2(3+0.2,1+0.2,5+0.2,6-0.2,'#aaaaaa')

draw_dot(3, 1)
draw_dot(5, 6)

draw_text2(3.5, 1, "P(3,1)", 'xx-large')
draw_text2(5.5, 5.5, "P´(5,6)", 'xx-large')




pyplot.show()