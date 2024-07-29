import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

ax = 0

#
#   init_graph(origin="center", aspect="square", max=10)
#     origin: center / leftbottom
#     aspect: square / landscape
#     max: graph size
#

def init_graph(max=10, origin="leftbottom", aspect="square"):
    global ax

    col = '#444444'

    pos_zero_x = -1
    pos_zero_y = -1
    pos_xlabel_x = -0.5
    pos_xlabel_y = -1.2
    pos_ylabel_x = -1.2
    pos_ylabel_y = -0.5

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal') # アスペクト比イコール
    
    if origin == "center":
        if aspect == "square":
            xmax = max
            ymax = max
            xmin = -max
            ymin = -max
        else: # landscape
            xmax = max * 1.3
            ymax = max
            xmin = -max * 1.3
            ymin = -max
    else:
        if aspect == "square":
            xmax = max
            ymax = max
            xmin = -max * 0.2
            ymin = -max * 0.2
        else: # landscape
            xmax = max * 1.3
            ymax = max
            xmin = -max * 0.2
            ymin = -max * 0.2

    xamax = xmax * 1.1
    yamax = ymax * 1.1
    xamin = xmin * 1.1
    yamin = ymin * 1.1

    point_x = {'start': [xamin, 0], 'end': [xamax, 0]}
    point_y = {'start': [0, yamin], 'end': [0, yamax]}

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
    if origin == "center":
        ax.set_xlim([-max, max])
        ax.set_ylim([-max, max])
    else:
        if aspect == "square":
            ax.set_xlim([-max, max])
            ax.set_ylim([-max, max])
        else:
            ax.set_xlim([-max * 0.2, max])
            ax.set_ylim([-max * 0.2, max * 0.6])

    ax.set_xlim([xamin, xamax])
    ax.set_ylim([yamin, yamax])

    ax.axis("off") # 外枠の軸を消す
    pos_scale = (-xamin + xamax) / 20
    ax.text(pos_zero_x * pos_scale, pos_zero_y * pos_scale, "0", fontstyle='oblique', fontname='serif', fontsize="large") # 原点０の表示
    ax.text(xamax + pos_xlabel_x * pos_scale, pos_xlabel_y * pos_scale, "x", fontstyle='oblique', fontname='serif', fontsize="x-large") # xの表示
    ax.text(pos_ylabel_x * pos_scale, yamax + pos_ylabel_y * pos_scale, "y", fontstyle='oblique', fontname='serif', fontsize="x-large") # yの表示
    


def draw_vec(x, y, col):
    global ax
    point = {'start': [0, 0], 'end': [x, y]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor=col, edgecolor=col))

# vecとvec2はひとつにしない
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

def draw_text(x, y, s, size="x-large"):
    global ax
    ax.text(x, y, s, fontstyle='oblique', fontname='serif', fontsize=size) 

def draw_dot(x, y):
    plt.plot(x,y,'black',marker='.', markersize=10)


def draw_arc(x0, y0, x1, y1, col):
    global ax
    a = patches.Arc((x0, y0), x1, y1, theta1=0, theta2=60, edgecolor=col, linewidth=1)
    ax.add_patch(a)

def show():
    plt.show()


