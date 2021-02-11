import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
import tkinter.font as TkFont
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
from fuzzyControl import *
class Home:
    def __init__(self):
        window = tk.Tk()
        window.geometry("400x470")
        window.configure(background = 'gray35')
        fontStyle = TkFont.Font(family="Lucida Grande", size=12)
        fontStyle1 = TkFont.Font(family="Lucida Grande", size=15)
        fontStyle2 = TkFont.Font(family = "Lucida Grande", size = 11)
        
         #Dialgram Fields

        diag_frame = tk.Frame(window, bg = 'gray', width = 400, height = 100)
        
        tk.Label(diag_frame, text = "GRAPHS", font = fontStyle1, bg = "gray", fg = "purple").grid(row = 0, column = 0, sticky = tk.W, pady = (10, 10))
        
        tk.Button(diag_frame, text = "Displacement", bg = "green", font = fontStyle2, command = self.plot_dis).grid(row = 1, column = 0, sticky = tk.W, padx = (0, 18), pady = (0, 5))

        tk.Button(diag_frame, text = "Acceleration", bg = "green", font = fontStyle2, command = self.plot_acc).grid(row = 1, column = 1, sticky = tk.W, padx = (0, 18), pady = (0, 5))

        tk.Button(diag_frame, text = "Error", bg = "green", font = fontStyle2, command = self.plot_error).grid(row = 1, column = 2, sticky = tk.W, padx = (0, 18), pady = (0, 5))

        tk.Button(diag_frame, text = "Stear Angle", bg = "green", font = fontStyle2, command = self.plot_angle).grid(row = 1, column = 3, sticky = tk.W, padx = (0, 0), pady = (0, 5))
    
        diag_frame.grid(row = 1, column = 0, sticky = tk.W, pady = (3, 3))

        #input fields

        input_frame = tk.Frame(window, bg = 'gray', width = 500, height = 100)
        
        tk.Label(input_frame, text = "INPUTS", font = fontStyle1, bg = "gray", fg = "purple").grid(row = 0, column = 0, sticky = tk.W, pady = (10, 10))

        tk.Label(input_frame, text = "Lateral Displacement: ", bg = "gray", font = fontStyle).grid(row = 1, column = 0, sticky = tk.W, pady = (8, 8))
        self.lateral_dis = tk.StringVar()
        tk.Entry(input_frame, textvariable = self.lateral_dis).grid(row = 1, column = 1, sticky = tk.W, pady = (8, 8), padx = (3, 3))
        tk.Label(input_frame, text = "m", bg = "gray", font = fontStyle).grid(row = 1, column = 2, sticky = tk.W, pady = (8, 8))
        
        tk.Label(input_frame, text = "Lateral Acceleration: ", bg = "gray", font = fontStyle).grid(row = 2, column = 0, sticky = tk.W, pady = (8, 8))
        self.lateral_acc = tk.StringVar()
        tk.Entry(input_frame, textvariable = self.lateral_acc).grid(row = 2, column = 1, sticky = tk.W, pady = (8, 8), padx = (3, 3))
        tk.Label(input_frame, text = "m/s2", bg = "gray", font = fontStyle).grid(row = 2, column = 2, sticky = tk.W, pady = (8, 8))

        tk.Label(input_frame, text = "Error: ", bg = "gray", font = fontStyle).grid(row = 3, column = 0, sticky = tk.W, pady = (8, 8))
        self.lateral_error = tk.StringVar()
        tk.Entry(input_frame, textvariable = self.lateral_error).grid(row = 3, column = 1, sticky = tk.W, pady = (8, 8), padx = (3, 3))
        tk.Label(input_frame, text = "", bg = "gray", font = fontStyle).grid(row = 3, column = 2, sticky = tk.W, pady = (8, 8))
        tk.Button(input_frame, text = "Predict", bg = "green", font = fontStyle2, command = self.predict).grid(row = 4, column = 0, sticky = tk.W, pady = (8, 8), padx = (5, 0))
        input_frame.grid(row = 2, column = 0, sticky = tk.W, pady = (3, 3))
        
        #Outputs
        
        output_frame = tk.Frame(window, bg = 'gray', width = 500, height = 100)
        
        tk.Label(output_frame, text = "OUTPUT", font = fontStyle1, bg = "gray", fg = "purple").grid(row = 0, column = 0, sticky = tk.W, pady = (10, 10))
        
        tk.Label(output_frame, text = "Stear Angle: ", font = fontStyle2, bg = "gray").grid(row = 1, column = 0, sticky = tk.W, pady = (0, 8), padx = (0, 8))
        self.angle_bh = tk.Label(output_frame, text = "0.0", font = fontStyle1, bg = "gray")
        self.angle_bh.grid(row = 1, column = 1, sticky = tk.W, pady = (0, 8))
        tk.Button(output_frame, text = "Stear Angle Graph", bg = "green", font = fontStyle2, command = self.plot_output).grid(row = 2, column = 0, sticky = tk.W, pady = (0, 3))
        
        output_frame.grid(row = 3, column = 0, sticky = tk.W, pady = (3, 0))
        
        window.mainloop()
    def plot_dis(self):
        y.view()
        plt.show()
        
    def plot_acc(self):
        y_acc.view()
        plt.show()
        
    def plot_error(self):
        e.view()
        plt.show()
        
    def plot_angle(self):
        angle.view()
        plt.show()
        
    def predict(self):
        dis = float(self.lateral_dis.get())
        acc = float(self.lateral_acc.get())
        error = float(self.lateral_error.get())
        dla.input['lateral lane displacement']=dis
        dla.input['lateral accelaration']=acc
        dla.input['error']=error
        dla.compute()
        self.angle_bh['text'] = str(round(dla.output['stear_angle'], 3))
    
    def plot_output(self):
        angle.view(sim = dla)
        plt.show()
Home()
