import numpy as np
from matplotlib import pyplot

ax = 0

def init_graph():
    global ax

    size = 10
    col = '#444444'
    
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal') # アスペクト比イコール
    
    point_x = {'start': [-2, 0], 'end': [size, 0]}
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
    ax.set_xlim([-2, size])
    ax.set_ylim([-2, size * 0.7])

    ax.axis("off") # 外枠の軸を消す
    ax.text(-0.8, -0.8, "0", fontstyle='oblique', fontname='serif', fontsize="large") # 原点０の表示
    ax.text(size * 0.95, -0.8, "x", fontstyle='oblique', fontname='serif', fontsize="x-large") # xの表示
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

def draw_dot(x, y):
    pyplot.plot(x,y,'black',marker='.', markersize=10)


init_graph()

draw_vec2(0, 0.2, 4, 2.2, 'red')
draw_vec2(0, 0, 8, 4, 'blue')

draw_text(4.5, 6.5, '(x, y)')
draw_text(8.5, 7, "(x', y')")

pyplot.show()