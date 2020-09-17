import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="VIRTUAL LAB ASSIGNMENT - AWP",font=("Arial Bold",40))
       label.place(x=270,y=200)
       label = tk.Label(self, text="Aditya Jain (17BEC003)", font=("Arial Bold", 20))
       label.place(x=500, y=300)
       label = tk.Label(self, text="Agrini Chaturvedi (17BEC005)", font=("Arial Bold", 20))
       label.place(x=450, y=330)
       label = tk.Label(self, text="Aim - To realize the concept of array antenna for isotropic sources and study the requirements of array\n antennae for improving directivity ", font=("Times New Roman", 20))
       label.place(x=100, y=500)


class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self,
                        text="INTRODUCTION",
                        font=("Times New Roman", 30))
       label.pack(side=tk.TOP)
       label = tk.Label(self,
                        text="Objective :\n",
                        font=("Times New Roman Bold", 20))
       label.place(x=10, y=100)
       label = tk.Label(self,
                        text="i) Realize the directivity improvementusing array of antenna like Broadside Antenna as compared to single dipole antenna\n "  ,
                        font=("Times New Roman ", 16))
       label.place(x=10,y=140)
       label = tk.Label(self,
                        text="ii) Synthesize the desired radiation pattern using array of isotropic sources using simulation",
                        font=("Times New Roman ", 16))
       label.place(x=10, y=170)
       label = tk.Label(self,
                        text="Theory :\n",
                        font=("Times New Roman Bold", 20))
       label.place(x=10, y=210)
       label = tk.Label(self,
                        text="An antenna array is a set of multiple connected antennas which work together as a single antenna, to transmit or receive radio \nwaves. Antenna arrays are widly used for improved directivity and Signal to Noise Ration (SNR) without changing the wavelength \nor frequency of the radiowave. One of the most common antenna array is the YagiUda antenna.\n"
                        "For the purpose of simplicity, the antennae are considered to be isotropic sources. The parameters that define an array antenna are \ngoverned by the Array Factor (AF). The Array Factor is a function of the positions of the antennas in the array and the weights used. \nBy tayloring these parameters the antenna array's performance may be optimized to achieve desirable properties.\n",
                        font=("Times New Roman ", 16), justify=tk.LEFT)
       label.place(x=10, y=240)
       label = tk.Label(self,
                        text="AF = (1/n)*sin(n*\u03C8/2)/sin(\u03C8/2)\n\n \u03C8 = \u03B2*d*cos \u03C6 +\u03B1",
                        font=("Times New Roman ", 16))
       label.place(x=450, y=400)
       label = tk.Label(self,
                        text="Where, n = number of array elements\n"
                        "\u03B2 = propogartion constant = 2*\u03C0/\u03BB \nd = distance between consecutive elements\n\u03C6 = angle made by the axis of array with a point in the far field region\n\u03B1 = Progressive phase shift.",
                        font=("Times New Roman ", 16), justify=tk.LEFT)
       label.place(x=10, y=500)


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self,
                        text="EXPERIMENT",
                        font=("Times New Roman", 30))
       label.pack(side=tk.TOP)
       label = tk.Label(self,
                        text="Requirements :\n",
                        font=("Times New Roman Bold", 20))
       label.place(x=10, y=100)
       label = tk.Label(self,
                        text="i) Transmitting array of antenna\nii) Recieving Antenna \niii) RF signal generator \niv) An interpreting system to plot the resultant radiation plot "  ,
                        font=("Times New Roman ", 16),justify=tk.LEFT)
       label.place(x=10,y=140)

       label = tk.Label(self,
                        text="Procedure :\n",
                        font=("Times New Roman Bold", 20))
       label.place(x=10, y=300)
       label = tk.Label(self,
                        text="i) We set up the antenna array as a transmitter, at a rotating shaft so as to plot its value for different. \u03C6's\nii) We use a linear dipole antenna as the static reciever.\niii) Connect the transmitting and the interpreting setup. \nOne thing to be noted is that the amplitude of RF signal supplied to each element must be equal in magnitude. \nWe need to find the radiation patterns for two basic type of antenna arrays :\n\ta) Broadside Array : Sources have zero phase change\n\tb) Endfire Array : Sources have opposite phase\nThe array axis is considered to be a horizontal axis in the simulation. ",
                        font=("Times New Roman ", 16), justify=tk.LEFT)
       label.place(x=10, y=350)



class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       lbl = tk.Label(self, text="RADIATION PATTERN - SIMULATION", font=("Arial", 30))
       lbl.pack(side=tk.TOP)

       Enter = tk.Label(self, text="Enter the specifications for the Antenna Array: ", font=("Times New Roman", 16))
       Enter.place(height=50, x=10, y=200)

       Num = tk.Label(self, text="Number of elements", font=("Times New Roman", 14))
       Num.place(height=50, x=10, y=280)

       NumB = tk.Entry(self, width=20)
       NumB.place(height=25, x=500, y=295)

       Dist =tk.Label(self, text="Distance between two consecutive elements in terms of \u03BB ",
                    font=("Times New Roman", 14))
       Dist.place(height=50, x=10, y=320)

       DistB = tk.Entry(self, width=20)
       DistB.place(height=25, x=500, y=335)

       Alpha = tk.Label(self, text="Progressive phase shift (\u03B1) as coefficient of \u03C0", font=("Times New Roman", 14))
       Alpha.place(height=50, x=10, y=360)

       AlphaB = tk.Entry(self, width=20)
       AlphaB.place(height=25, x=500, y=375)

       pi = np.pi

       def clicked():
           n = int(NumB.get())
           d = float(DistB.get())
           alpha = float(AlphaB.get())
           phi = np.arange(0, 2 * np.pi, .01)
           cos_phi = np.cos(np.array(phi))
           psi = (2 * pi * d * np.array(cos_phi)) + alpha * pi
           E = (1 / n) * (np.sin(n * np.array(psi) / 2)) / np.sin(np.array(psi) / 2)

           fig = Figure(figsize=(6, 6), dpi=100)
           a = fig.add_subplot(111, projection='polar')
           a.plot(phi,abs(E))
           a.set_rmax(1)
           a.set_rticks([0.25, 0.5, 0.75, 1])  # less radial ticks
           a.set_rlabel_position(-22.5)  # get radial labels away from plotted line
           a.grid(True)

           canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
           canvas.draw()
           canvas.get_tk_widget().place(x=650, y=60)
           toolbar = NavigationToolbar2Tk(canvas, self)
           toolbar.update()
           toolbar.place(x=750, y=663)

           def on_key_press(event):
               print("you pressed {}".format(event.key))
               key_press_handler(event, canvas, toolbar)

           canvas.mpl_connect("key_press_event", on_key_press)

       Plot = tk.Button(self, text="   Plot   ", command=clicked)
       Plot.place(height=30, x=10, y=450)

class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self,
                        text="RESULTS",
                        font=("Times New Roman", 30))
       label.pack(side=tk.TOP)
       label = tk.Label(self,
                        text="Observations :\n",
                        font=("Times New Roman Bold", 20))
       label.place(x=10, y=100)
       label = tk.Label(self,
                        text="i) As we increase the number of array elements, the directivity of the system improves..\nii) Radiation pattern observed for \n\ta) Broadside Array : Maxima perpendicular and minima parallel to array axis\n\tb) Endfire Array : Maxima parallel and minima perpendicular to array axis  ",
                        font=("Times New Roman ", 16),justify=tk.LEFT)
       label.place(x=10,y=140)

       label = tk.Label(self,
                        text="Conclusion :\n",
                        font=("Times New Roman Bold", 20))
       label.place(x=10, y=300)
       label = tk.Label(self,
                        text="The simulations show that the antenna array actually processes the signals better in some directions than others. In this manner, \na directional radiation pattern is obtained even though the antennas were assumed to be isotropic.\n"
                        "Even though this was shown for transmitting antenna, due to reciprocity, the recieving properties would be the same.\nWe had taken same amplitude for every array element, but if the amplitudes are chosen according to Binomial ratio, the Half Power \nBeam Width (HPBW) increases, though its directivity reduces. \n"
                        "By choosing the weights and geometry of an antenna array properly, the antenna array can be designed to cancel out energy from \nundesirable directions and receive energy most sensitively from other directions.", font=("Times New Roman ", 16), justify=tk.LEFT)
       label.place(x=10, y=350)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Home Page", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Introduction", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Experiment", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Simulation", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Results", command=p5.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root: Tk = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_title("AWP Special Assignment")
    root.wm_geometry('1300x700')
    root.mainloop()