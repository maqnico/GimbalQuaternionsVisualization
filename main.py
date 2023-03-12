import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk

#defining variables
phi = 0
psi = 0
theta = 0
phi2 = 0
q1 = 0
q2 = 0
q3 = 0

#defining functions
#making 3D Plots
def gq_plot():

    global fig1
    fig1 = plt.figure()
    global ax1
    ax1 = plt.axes(projection ='3d')

    global fig2
    fig2 = plt.figure()
    global ax2
    ax2 = plt.axes(projection='3d')

# TODO change Functions here
# Functions Gimbal
    z1 = phi
    x1 = psi
    y1 = theta

# Functions Quaternions
    z2 = q1
    x2 = q2
    y2 = q3

    ax1.plot3D(x1, y1, z1, 'green')
    ax1.set_title('Rotation with Gimbals')

    ax2.plot3D(x2, y2, z2, 'blue')
    ax2.set_title('Rotation with Quaternions')

def gq_printGraph(printGraph_fig, printGraph_master):
    # creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(
        printGraph_fig,
        master=printGraph_master)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

#TODO fix this
def gq_reset():
    i = 1
# phi, psi, theta, phi2, q1, q2, q3 = 0
 # gq_printGraph(fig1, gq_frame1)
 #   gq_printGraph(fig2, gq_frame2)


#GUI
#make Window
gq_window = tk.Tk()
gq_window.title('Gimbal vs. Qaternions')
gq_window.geometry("1000x1000")

gq_plot()

#make content
#frame 1 with 3 sliders, graph and matix
#define objects
gq_frame1 = ttk.Frame(borderwidth=5, relief='solid')
gq_frame1s = ttk.Frame(master=gq_frame1)
gq_slider_g1 = ttk.Scale(master=gq_frame1s, from_=-90, to= 90,  orient='horizontal', variable=phi)
gq_slider_g2 = ttk.Scale(master=gq_frame1s, from_=-90, to= 90,  orient='horizontal', variable=psi)
gq_slider_g3 = ttk.Scale(master=gq_frame1s, from_=-90, to= 90,  orient='horizontal', variable=theta)
gq_labelg1 = ttk.Label(master= gq_frame1s, text= 'Phi =')
gq_labelg2 = ttk.Label(master= gq_frame1s, text= 'Psi =')
gq_labelg3 = ttk.Label(master= gq_frame1s, text= 'Theta =')
#TODO display matrix
gq_box1 = tk.Frame(master=gq_frame1, height=100, width=100, background='white')
#pack
gq_frame1.pack(fill=tk.X)
gq_frame1s.pack(side=tk.LEFT)
gq_slider_g1.grid(column= 0, row= 1)
gq_labelg1.grid(column= 1, row= 1)
gq_slider_g2.grid(column= 0, row= 2)
gq_labelg2.grid(column= 1, row= 2)
gq_slider_g3.grid(column= 0, row= 3)
gq_labelg3.grid(column= 1, row= 3)
gq_box1.pack(side=tk.RIGHT)
gq_printGraph(fig1, gq_frame1)

#frame 2 with four sliders, graph and quaternion
#define objects
gq_frame2 = ttk.Frame(borderwidth=5, relief='solid')
gq_frame2s = ttk.Frame(master=gq_frame2)
gq_slider_q1 = ttk.Scale(master=gq_frame2s, from_=-1, to=1,  orient='horizontal', variable=phi2)
gq_slider_q2 = ttk.Scale(master=gq_frame2s, from_=-1, to=1,  orient='horizontal', variable=q1)
gq_slider_q3 = ttk.Scale(master=gq_frame2s, from_=-1, to=1,  orient='horizontal', variable=q2)
gq_slider_q4 = ttk.Scale(master=gq_frame2s, from_=-1, to=1,  orient='horizontal', variable=q3)
gq_labelq1 = ttk.Label(master= gq_frame2s, text= 'Angle =')
gq_labelq2 = ttk.Label(master= gq_frame2s, text= 'Q1 =')
gq_labelq3 = ttk.Label(master= gq_frame2s, text= 'Q2 =')
gq_labelq4 = ttk.Label(master= gq_frame2s, text= 'Q3 =')
#TODO display quaternion
gq_box2 = tk.Frame(master=gq_frame2, height=100, width=100, background='white')
#pack
gq_frame2.pack(fill=tk.X)
gq_frame2s.pack(side=tk.LEFT)
gq_slider_q1.grid(column= 0, row= 1)
gq_labelq1.grid(column= 1, row= 1)
gq_slider_q2.grid(column= 0, row= 2)
gq_labelq2.grid(column= 1, row= 2)
gq_slider_q3.grid(column= 0, row= 3)
gq_labelq3.grid(column= 1, row= 3)
gq_slider_q4.grid(column= 0, row= 4)
gq_labelq4.grid(column= 1, row= 4)

gq_box2.pack(side=tk.RIGHT)
gq_printGraph(fig2, gq_frame2)

#reset button
gq_resetB = ttk.Button(master=gq_window, text='reset', command=gq_reset())
gq_resetB.pack()

#initiate mainloop
gq_window.mainloop()
