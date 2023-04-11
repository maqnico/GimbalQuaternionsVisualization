import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import tkinter as tk
from tkinter import ttk


#make Window
gq_window = tk.Tk()
gq_window.title('Gimbal vs. Qaternions')
gq_window.geometry("1000x1000")

#defining variables
gq_phi= tk.DoubleVar()
gq_psi= tk.DoubleVar()
gq_theta= tk.DoubleVar()
gq_phi2= tk.DoubleVar()
gq_q1= tk.DoubleVar()
gq_q2= tk.DoubleVar()
gq_q3= tk.DoubleVar()

#defining functions

    #making 3D Plots
def gq_plot():

    global fig1
    fig1 = plt.figure()
    global ax1
    ax1 = plt.axes(projection='3d')

    global fig2
    fig2 = plt.figure()
    global ax2
    ax2 = plt.axes(projection='3d')

#TODO change Functions here
        # Functions Gimbal
    z1 = 1
    x1 = 1
    y1 = 1

        # Functions Quaternions
    z2 = 1
    x2 = 1
    y2 = 1

    ax1.plot3D(x1, y1, z1, 'green')
    ax1.set_title('Rotation with Gimbals')

    ax2.plot3D(x2, y2, z2, 'blue')
    ax2.set_title('Rotation with Quaternions')

    #printing 3D PLots to canvas
def gq_printGraph(printGraph_fig, printGraph_master):
        # creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(
        printGraph_fig,
        master=printGraph_master)
    canvas.draw()

        # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    #reset the plot values and rotation
#TODO fix this
def gq_reset():
    gq_phi.set(0.0)
    gq_psi.set(0.0)
    gq_theta.set(0.0)
    gq_phi2.set(0.0)
    gq_q1.set(0.0)
    gq_q2.set(0.0)
    gq_q3.set(0.0)

    #updating the labels and plots
def gq_sider_changed(slider, label):
    i = 1

#initialze the plots
gq_plot()

#Make rest of GUI
    #frame 1 containing 3 sliders with labels, graph and matix
        #define objects
gq_frame1 = ttk.Frame(borderwidth=5, relief='solid')
gq_frame1s = ttk.Frame(master=gq_frame1)
gq_slider_g1 = ttk.Scale(master=gq_frame1s, from_=-90, to= 90, orient='horizontal', variable=gq_phi)
gq_slider_g2 = ttk.Scale(master=gq_frame1s, from_=-90, to= 90, orient='horizontal', variable=gq_psi)
gq_slider_g3 = ttk.Scale(master=gq_frame1s, from_=-90, to= 90, orient='horizontal', variable=gq_theta)
gq_labelg1 = ttk.Label(master= gq_frame1s, text='Phi = ' + str(gq_phi.get()) + '°')
gq_labelg2 = ttk.Label(master= gq_frame1s, text='Psi =' + str(gq_psi.get()) + '°')
gq_labelg3 = ttk.Label(master= gq_frame1s, text='Theta = ' + str(gq_theta.get()) + '°')
gq_slider_g1.config(command=gq_sider_changed(gq_slider_g1, gq_labelg1))
#TODO display matrix
gq_box1 = tk.Frame(master=gq_frame1, height=100, width=100, background='white')
    #pack
gq_frame1.pack(fill=tk.X)
gq_frame1s.pack(side=tk.LEFT)
gq_slider_g1.grid(column=0, row=1)
gq_slider_g2.grid(column=0, row=2)
gq_slider_g3.grid(column=0, row=3)
gq_labelg1.grid(column=1, row=1)
gq_labelg2.grid(column=1, row=2)
gq_labelg3.grid(column=1, row=3)
gq_box1.pack(side=tk.RIGHT)
gq_printGraph(fig1, gq_frame1)

    #frame 2 containing 3 sliders with labels, graph and matix
        #define objects
gq_frame2 = ttk.Frame(borderwidth=5, relief='solid')
gq_frame2s = ttk.Frame(master=gq_frame2)
gq_slider_q1 = ttk.Scale(master=gq_frame2s, from_=-90, to=90, orient='horizontal')
gq_slider_q2 = ttk.Scale(master=gq_frame2s, from_=-1, to=1, orient='horizontal')
gq_slider_q3 = ttk.Scale(master=gq_frame2s, from_=-1, to=1, orient='horizontal')
gq_slider_q4 = ttk.Scale(master=gq_frame2s, from_=-1, to=1, orient='horizontal')
gq_labelq1 = ttk.Label(master=gq_frame2s, text='Angle = ' + str(gq_phi2.get()) + '°')
gq_labelq2 = ttk.Label(master=gq_frame2s, text='Q1 = ' + str(gq_q1.get()))
gq_labelq3 = ttk.Label(master=gq_frame2s, text='Q2 = ' + str(gq_q2.get()))
gq_labelq4 = ttk.Label(master=gq_frame2s, text='Q3 = ' + str(gq_q3.get()))
#TODO display quaternion
gq_box2 = tk.Frame(master=gq_frame2, height=100, width=100, background='white')
    #pack
gq_frame2.pack(fill=tk.X)
gq_frame2s.pack(side=tk.LEFT)
gq_slider_q1.grid(column=0, row=1)
gq_slider_q2.grid(column=0, row=2)
gq_slider_q3.grid(column=0, row=3)
gq_slider_q4.grid(column=0, row=4)
gq_labelq1.grid(column=1, row=1)
gq_labelq2.grid(column=1, row=2)
gq_labelq3.grid(column=1, row=3)
gq_labelq4.grid(column=1, row=4)

gq_box2.pack(side=tk.RIGHT)
gq_printGraph(fig2, gq_frame2)

    #reset button
gq_resetB = ttk.Button(master=gq_window, text='reset', command=gq_reset())
gq_resetB.pack()

#initiate mainloop
gq_window.mainloop()
