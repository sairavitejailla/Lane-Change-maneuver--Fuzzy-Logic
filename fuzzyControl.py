#importing libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
#configuring input and output variables
range_of_y = 1000
y=ctrl.Antecedent(np.arange(0,range_of_y+0.1,0.01),'lateral lane displacement')
range_of_acc= 300
y_acc=ctrl.Antecedent(np.arange(0,range_of_acc,0.001),'lateral accelaration')
error=100
e=ctrl.Antecedent(np.arange(-error,error,0.1),'error')
y['first']=fuzz.trapmf(y.universe,[0,range_of_y/16,3*range_of_y/16,4*range_of_y/16])
y['second']=fuzz.trapmf(y.universe,[5*range_of_y/16,6*range_of_y/16,7*range_of_y/16,8*range_of_y/16])
y['third']=fuzz.trapmf(y.universe,[9*range_of_y/16,10*range_of_y/16,11*range_of_y/16,12*range_of_y/16])
y['final']=fuzz.trapmf(y.universe,[13*range_of_y/16,14*range_of_y/16,15*range_of_y/16,16*range_of_y/16])
y_acc['GT0']=fuzz.trimf(y_acc.universe,[1,range_of_acc/2,range_of_acc])
y_acc['GE0']=fuzz.trimf(y_acc.universe,[0,range_of_acc/2,range_of_acc])
y_acc['LTM']=fuzz.trimf(y_acc.universe,[-range_of_acc,0,range_of_acc-1])
y_acc['GEM']=fuzz.trimf(y_acc.universe,[range_of_acc,range_of_acc,range_of_acc])
y_acc['GT-M']=fuzz.trimf(y_acc.universe,[-range_of_acc+1,0,range_of_acc])
y_acc['LE-M']=fuzz.trimf(y_acc.universe,[-range_of_acc,-range_of_acc,-range_of_acc])
y_acc['LT0']=fuzz.trimf(y_acc.universe,[-range_of_acc,-range_of_acc/2,-1])
y_acc['LE0']=fuzz.trimf(y_acc.universe,[-range_of_acc,-range_of_acc/2,0])
e['N']=fuzz.trimf(e.universe,[-error,-error,-1])
e['Z']=fuzz.trimf(e.universe,[-error/2,0,error/2])
e['P']=fuzz.trimf(e.universe,[1,error,error])

stear_angle=0.006
angle=ctrl.Consequent(np.arange(-stear_angle,stear_angle,0.0001),'stear_angle')
angle['s1']=fuzz.trimf(angle.universe,[0,0.0006/2,0.0006])
angle['b1']=fuzz.trimf(angle.universe,[0.00060001,0.0017,0.0034])
angle['b2']=fuzz.trimf(angle.universe,[0.0034001,0.0037,0.004])
angle['b3']=fuzz.trimf(angle.universe,[0.004001,0.0043,0.0046])
angle['s1']=fuzz.trimf(angle.universe,[0,0.0006/2,0.0006])
angle['b1']=fuzz.trimf(angle.universe,[0.00060001,0.0017,0.0034])
angle['b2']=fuzz.trimf(angle.universe,[0.0034001,0.0037,0.004])
angle['b3']=fuzz.trimf(angle.universe,[0.004001,0.0043,0.0046])
angle['-s1']=fuzz.trimf(angle.universe,[-0.0006,-0.0006/2,0])
angle['-b1']=fuzz.trimf(angle.universe,[-0.0034,-0.0017,-0.00060001])
angle['-b2']=fuzz.trimf(angle.universe,[-0.004,-0.0037,-0.0034001])
angle['-b3']=fuzz.trimf(angle.universe,[-0.0046,-0.0043,-0.004001])
angle['0']=fuzz.trimf(angle.universe,[0,0,0])
    
#rules
rule1=ctrl.Rule(y['first'] & y_acc['LTM'] & e['N'],angle['b3'])
rule2=ctrl.Rule(y['first'] & y_acc['LTM'] & e['Z'],angle['b2'])
rule3=ctrl.Rule(y['first'] & y_acc['LTM'] & e['P'],angle['b1'])
rule4=ctrl.Rule(y['first'] & y_acc['GEM'] & e['N'],angle['-s1'])
rule5=ctrl.Rule(y['first'] & y_acc['GEM'] & e['Z'],angle['0'])
rule6=ctrl.Rule(y['first'] & y_acc['GEM'] & e['P'],angle['-s1'])
rule7=ctrl.Rule(y['second'] & y_acc['GT0'] & e['N'],angle['-b1'])
rule8=ctrl.Rule(y['second'] & y_acc['GT0'] & e['Z'],angle['-b2'])
rule9=ctrl.Rule(y['second'] & y_acc['GT0'] & e['P'],angle['-b3'])
rule10=ctrl.Rule(y['second'] & y_acc['LE0'] & e['N'],angle['s1'])
rule11=ctrl.Rule(y['second'] & y_acc['LE0'] & e['Z'],angle['0'])
rule12=ctrl.Rule(y['second'] & y_acc['LE0'] & e['P'],angle['-s1'])
rule13=ctrl.Rule(y['third'] & y_acc['GT-M'] & e['N'],angle['-b1'])
rule14=ctrl.Rule(y['third'] & y_acc['GT-M'] & e['Z'],angle['-b2'])
rule15=ctrl.Rule(y['third'] & y_acc['GT-M'] & e['P'],angle['-b3'])
rule16=ctrl.Rule(y['third'] & y_acc['LE-M'] & e['N'],angle['s1'])
rule17=ctrl.Rule(y['third'] & y_acc['LE-M'] & e['Z'],angle['0'])
rule18=ctrl.Rule(y['third'] & y_acc['LE-M'] & e['P'],angle['-s1'])
rule19=ctrl.Rule(y['final'] & y_acc['LT0'] & e['N'],angle['-b1'])
rule20=ctrl.Rule(y['final'] & y_acc['LT0'] & e['Z'],angle['-b2'])
rule21=ctrl.Rule(y['final'] & y_acc['LT0'] & e['P'],angle['-b3'])
rule22=ctrl.Rule(y['final'] & y_acc['GE0'] & e['N'],angle['s1'])
rule23=ctrl.Rule(y['final'] & y_acc['GE0'] & e['Z'],angle['0'])
rule24=ctrl.Rule(y['final'] & y_acc['GE0'] & e['P'],angle['-s1'])

#feeding rules to ControlSystem
dla_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24])
dla=ctrl.ControlSystemSimulation(dla_ctrl)
