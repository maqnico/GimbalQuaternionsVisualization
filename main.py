import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk

#making 3D Plots
def gq_plot():

    fig1 = plt.figure()
    ax1 = plt.axes(projection ='3d')

    fig2 = plt.figure()
    ax2 = plt.axes(projection='3d')

# TODO change Functions here
# Functions Gimbal
    z1 = np.linspace(0, 1, 100)
    x1 = z1 * np.sin(25 * z1)
    y1 = z1 * np.cos(25 * z1)

# Functions Quaternions
    z2 = np.linspace(0, 1, 100)
    x2 = z2 
    y2 = z2 * np.cos(25 * z2)

    ax1.plot3D(x1, y1, z1, 'green')
    ax1.set_title('Gimbal')

    ax2.plot3D(x2, y2, z2, 'blue')
    ax2.set_title('Quaternion')

    # creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(
        fig1,
        master=gq_window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(
        fig2,
        master=gq_window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

#GUI
#make Window
gq_window = tk.Tk()
gq_window.title('Gimbal vs. Qaternions')
gq_window.geometry("1000x1000")
#make content
gq_label1 = tk.Label(text="Rotation with Gimbals")
gq_label1.pack()
gq_label2 = tk.Label(text="Rotation with Quaternions")
gq_label2.pack()
gq_plot()
#initiate mainloop
gq_window.mainloop()
