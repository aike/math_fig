# math_fig: A simple python library for drawing mathematical figures
# https://github.com/aike/math_fig
# math_fig program is licensed under MIT License.
# Copyright 2024, aike (@aike1000)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

ax = 0

def init(max=10, origin="leftbottom", aspect="square", col = '#444444'):
    global ax

    pos_zero_x = -1
    pos_zero_y = -1
    pos_xlabel_x = -0.5
    pos_xlabel_y = -1.2
    pos_ylabel_x = -1.2
    pos_ylabel_y = -0.5

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    
    if origin == "center": # center origin
        if aspect == "square": # 1:1
            xmax = max
            ymax = max
            xmin = -max
            ymin = -max
        else: # landscape        1:1.3
            xmax = max * 1.3
            ymax = max
            xmin = -max * 1.3
            ymin = -max

    else:                  # leftbottom origin
        if aspect == "square": # 1:1
            xmax = max
            ymax = max
            xmin = -max * 0.2
            ymin = -max * 0.2
        else: # landscape        1:1.3
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
    

def vec(x, y, col):
    global ax
    point = {'start': [0, 0], 'end': [x, y]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor=col, edgecolor=col))

# vecとvec2はひとつにしない
def vec2(x0, y0, x1, y1, col):
    global ax
    point = {'start': [x0, y0], 'end': [x1, y1]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor=col, edgecolor=col))

def line(x0, y0, x1, y1, col):
    global ax
    point = {'start': [x0, y0], 'end': [x1, y1]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
            arrowprops=dict(arrowstyle='-', 
                            connectionstyle='arc3', 
                            facecolor=col, edgecolor=col))

def dline(x0, y0, x1, y1, col):
    global ax
    point = {'start': [x0, y0], 'end': [x1, y1]}
    ax.annotate('', xy=point['end'], xytext=point['start'],
            arrowprops=dict(arrowstyle='-', 
                            connectionstyle='arc3', 
                            linestyle='dotted',
                            alpha=0.7,
                            facecolor=col, edgecolor=col))

def text(x, y, s, size="x-large"):
    global ax
    ax.text(x, y, s.replace("'", "´"), fontstyle='oblique', fontname='serif', fontsize=size) 

def dot(x, y, size=10, col="black"):
    plt.plot(x,y,col,marker='.', markersize=size)

def arc(x0, y0, x1, y1, t0, t1, col):
    global ax
    a = patches.Arc((x0, y0), x1 * 2, y1 * 2, theta1=t0, theta2=t1, edgecolor=col, linewidth=1)
    ax.add_patch(a)

def show():
    plt.show()
