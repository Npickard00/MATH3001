
"""
Created on Mon Mar 31 22:28:21 2025

@author: Natasha Pickard
"""
#This code is taken from Zheming Zhang and rivertestgen which can be found at:
#https://github.com/Flood-Excess-Volume/RiverDon/tree/master/Pythoncode
#and at
#https://github.com/Flood-Excess-Volume/RiverDon/tree/master/Integratedcode


#this code along with the Teme data was used to produce the graph relating to the River Teme FEV

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import bisect
from mpl_toolkits.mplot3d import Axes3D
fig, ax = plt.subplots()




#Import the data from a csv file. In this case I import my River Teme data
#data must have 3 columns with headings 'Time', 'Height', 'Flow'
#and note that this code will only work successfuly for data where there is
#one single peak

# Define your file mapping
file_paths = {
    "Armley_2015": r"C:\Users\Natasha Pickard\OneDrive - University of Leeds\Year 3\MATH3001\FINAL\Rotherham Don 2007.csv",
    "Armley_2020": r"C:\Users\Natasha Pickard\OneDrive - University of Leeds\Year 3\MATH3001\FINAL\Aire Armley 2020 Stage and Flow.csv",
    "Armley_2022": r"C:\Users\Natasha Pickard\OneDrive - University of Leeds\Year 3\MATH3001\FINAL\Aire Armley 2022 Stage and Flow.csv",
    "Don_Tesco_2007": r"C:\Users\Natasha Pickard\OneDrive - University of Leeds\Year 3\MATH3001\FINAL\Rotherham Don 2007.csv",
    "Don_Hadfields_2007": r"C:\Users\Natasha Pickard\OneDrive - University of Leeds\Year 3\MATH3001\FINAL\Don Hadfields 2007 Stage and Flow.csv"
}

# Set which file to load
selected_file = "Don_Tesco_2007"

# Load the CSV
Data = pd.read_csv(file_paths[selected_file])

# Automatically set threshold height 'h' based on the selected file
if selected_file == "Armley_2015":
    ht = 3.9
    error=0.055
    startdate=24
elif selected_file == "Armley_2020":
    ht = 3.9
    error=0.055
    startdate=8
elif selected_file == "Armley_2022":
    ht = 3.9
    error=0.055
    startdate=19
elif selected_file == "Don_Tesco_2007":
    ht = 1.9
    error=0.08
    startdate=24
elif selected_file == "Don_Hadfields_2007":
    ht = 2.9
    error=0.08
    startdate=24
else:
    raise ValueError("Threshold height for selected file is not defined.")

# Optional: print for confirmation
print(f"Loaded {selected_file} with threshold height h = {ht} m")

time=Data['Time']
height=Data['Height']
flow=Data['Flow']
height1=height[height>ht]
hm=np.mean(height1)
startdate=startdate
print(max(height))
print(hm)

plt.rcParams["figure.figsize"] = [11,8]
plt.rcParams['axes.edgecolor']='white'
ax.spines['left'].set_position(('zero'))
ax.spines['bottom'].set_position(('zero'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')

time_increment=(time[1]-time[0])*24*3600

number_of_days=int((len(time)*(time[1]-time[0])))

def scale(x):
    return ((x-min(x))/(max(x)-min(x)))


error_height_up = [i * (1+error) for i in height]
error_height_down = [i * (1-error) for i in height]
scaledtime=scale(time)
scaledheight=scale(height)
scaledFlow=scale(flow)
hup=ht*(1+error)
print(hup)

#here we calculate qt, qtmin and, qtmax 
#This code was taken from rivertestgen

qt = 0
nwin = 0
for i in range(1,len(height)):
        if height[i] > ht and height[i-1] < ht and nwin==0:
            qt =  flow[i-1]+(flow[i]-flow[i-1])*(ht-height[i-1])/(height[i]-height[i-1])
            nwin = 1
        if height[i] < ht and height[i-1] > ht and nwin==0:
            qt =  flow[i-1]+(flow[i]-flow[i-1])*(ht-height[i-1])/(height[i]-height[i-1])
            nwin = 1
qtmin = (1.0-error)*qt
qtmax = (1.0+error)*qt

scaledFlow_up = [i*(1+error) for i in scaledFlow]
scaledFlow_down = [i*(1-error) for i in scaledFlow]
negheight=-scaledheight
negday=-(scaledtime)

#Now the 4 quadrant graph is plotted

ax.plot(negheight,scaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'blue',linestyle='--',marker='',linewidth=2)
ax.plot(scaledtime, scaledFlow,'black',linewidth=2)
ax.plot(negheight, negday,'black',linewidth=2)

scaledht = (ht-min(height))/(max(height)-min(height))
scaledqt = (qt-min(flow))/(max(flow)-min(flow))

QT=[]
for i in scaledFlow:
    i = scaledqt
    QT.append(i)

SF=np.array(scaledFlow)
e=np.array(QT)
    
ax.fill_between(scaledtime,SF,e,where=SF>=e,facecolor='blue')

idx = np.argwhere(np.diff(np.sign(SF - e))).flatten()

f=scaledtime[idx[0]]
print(f)
g=scaledtime[idx[-1]]
print(g)

def unscaletime(x):
    return (((max(time)-min(time))*x)+min(time))

C=unscaletime(f)
d=unscaletime(g)

Tf=(d-C)*24

time_increment=(time[1]-time[0])*24*3600

#from rivertestgen

Flowmin = (1.0-error)*flow
Flowmax = (1.0+error)*flow

Flow = []
for i in flow:
    if i>=qt:
        Flow.append((i-qt)*(time_increment))
flowmin = []
for i in Flowmin:
    if i >= qtmin:
        flowmin.append((i - qtmin) * (time_increment))
flowmax = []
for i in Flowmax:
    if i >= qtmax:
        flowmax.append((i - qtmax) * (time_increment))

FEV=sum(Flow)
FEV_max=sum(flowmax)
FEV_min=sum(flowmin)
Tfs=Tf*(60**2)

qm=(FEV/Tfs)+qt
print(qm)
scaledqm = (qm-min(flow))/(max(flow)-min(flow))


scaledhm = (hm-min(height))/(max(height)-min(height))

ax.plot([-scaledht,-scaledht],[-1,scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm],'black',linestyle='--',linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm],'black',linestyle='--',linewidth=1)

ax.plot([f,f,f],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([g,g,g],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([f,f],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([f,g],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([f,g],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([g,g],[scaledqm,scaledqt], 'black',linewidth=1.5)
plt.annotate('', xy=(f-1/100,-1/5), xytext=(g+1/100,-1/5), arrowprops=dict(arrowstyle='<->'))

h=[]
for i in np.arange(1,number_of_days+1):
    h.append(i/number_of_days)


l=np.arange(0,max(flow)+50,50)
m=bisect.bisect(l,min(flow))

n=[]
for i in np.arange(l[m],max(flow)+50,50):
    n.append(int(i))


o=np.arange(0,max(height)+1,1)
p=bisect.bisect(o,min(height))

q=[]
for i in np.arange(o[p],max(height)+1,1):
    q.append(i)

k=[]
for i in q:
    k.append(-(i-min(height))/(max(height)-min(height))) 

j=[]
for i in n:
    j.append((i-min(flow))/(max(flow)-min(flow)))

ticks_x=k+h

r=[]
for i in h:
    r.append(-i)

ticks_y=r+j


s=[]
for i in np.arange(1,number_of_days+1):
    s.append(i)

s=[x+startdate for x in s]
Ticks_x=q+s
print(Ticks_x)
Ticks_y=s+n
    

ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels([])
ax.set_yticklabels(Ticks_y)
lists1 = sorted(zip(*[negheight, scaledFlow_down]))
negheight1, scaledFlow_down1 = list(zip(*lists1))
lists2 = sorted(zip(*[negheight, scaledFlow_up]))
negheight1, scaledFlow_up1 = list(zip(*lists2))
ax.fill_between(negheight1,scaledFlow_down1,scaledFlow_up1,color="grey", alpha = 0.3)
ax.fill_between(scaledtime,scaledFlow_up,scaledFlow_down,color="grey", alpha = 0.3)
QtU = scaledqt*(1+error)
QtD = scaledqt*(1-error)
ax.fill_between([scaledtime[idx[0]], scaledtime[idx[-1]]], QtU, QtD, color = "grey", alpha = 0.3)
ax.tick_params(axis='x',colors='black',direction='out',length=9,width=1)
ax.tick_params(axis='y',colors='black',direction='out',length=10,width=1)

plt.text(-scaledht+1/100, -1,'$h_T$', size=13)
plt.text(-scaledhm+1/100, -1,'$h_m$', size=13)
plt.text(1, scaledqm,'$Q_m$', size=13)
plt.text(1, scaledqt,'$Q_T$', size=13)
plt.text((f+g/2)-0.2,-0.27,'$T_f$',size=13)

plt.text(0.01, 1.05,'$Q$ [m$^3$/s]', size=13)
plt.text(0.95, -0.17,'$t$ [day]', size=13)
plt.text(0.01, -1.09,'$t$ [day]', size=13)
plt.text(-1.1, 0.02,'$\overline {h}$ [m]', size=13)

ax.scatter(0,0,color='white')

A=round(FEV/(10**6),2)
B=round(Tf,2)
C=round(ht,2)
D=round(hm,2)
E=round(qt,2)
F=round(qm,2)
Amax=round((FEV*1.16)/(10**6),2)
Amin=round((FEV*0.84)/(10**6),2)
Emax=round(max(flow),2)
H=round(max(height),2)
start_y = -0.4
spacing = 0.08

plt.text(0.4, start_y - spacing * 0, fr'$FEV \approx {A}\,\mathrm{{Mm}}^3$', size=15)
plt.text(0.4, start_y - spacing * 1, fr'$FEV_{{max}} \approx {Amax}\,\mathrm{{Mm}}^3$', size=15)
plt.text(0.4, start_y - spacing * 2, fr'$FEV_{{min}} \approx {Amin}\,\mathrm{{Mm}}^3$', size=15)
plt.text(0.4, start_y - spacing * 3, fr'$T_f = {B}\,\mathrm{{hrs}}$', size=15)
plt.text(0.4, start_y - spacing * 4, fr'$h_T = {C}\,\mathrm{{m}}$', size=15)
plt.text(0.4, start_y - spacing * 5, fr'$h_m = {D}\,\mathrm{{m}}$', size=15)
plt.text(0.4, start_y - spacing * 6, fr'$h_{{max}} = {H}\,\mathrm{{m}}$', size=15)
plt.text(0.4, start_y - spacing * 7, fr'$Q_T = {E}\,\mathrm{{m^3/s}}$', size=15)
plt.text(0.4, start_y - spacing * 8, fr'$Q_m = {F}\,\mathrm{{m^3/s}}$', size=15)
plt.text(0.4, start_y - spacing * 9, fr'$Q_{{max}} = {Emax}\,\mathrm{{m^3/s}}$', size=15)


#Here a 3D square lake of depth 2m is plotted

fig = plt.figure(figsize=plt.figaspect(1)*0.6)
ax = Axes3D(fig)
plt.rcParams['axes.edgecolor']='white'
plt.rcParams["figure.figsize"] = [10,8]

ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

sl = (FEV/2)**0.5
a = [sl, sl]
b = [sl, sl]
c = [2, 0]

d = [sl, 0]
e = [sl, sl]
f = [0, 0]

g = [sl, sl]
h = [sl, 0]
i = [0, 0]

ax.plot(a, b, c, '--', color = 'k', linewidth=2)
ax.plot(d, e, f, '--', color = 'k', linewidth=2)
ax.plot(g, h, i, '--', color = 'k', linewidth=2)


x = [sl, sl, sl, 0, 0, 0, sl, sl, 0, 0, 0, 0]
y = [sl, 0, 0, 0, 0, sl, sl, 0, 0, 0, sl, sl]
z = [2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2]

ax.plot(x, y, z, color = 'k', linewidth=3)

ax.text(5*(sl/9), -5*(sl/9), 0, 'Side-length [m]', size=9)
ax.text(-sl/4, sl/4, 0, 'Side-length [m]', size=9)
ax.text(-0.02*sl, 1.01*sl, 0.8, 'Depth [m]',size=9)


ax.text(7*(sl/10), 5*(sl/4), 1, ''+str(int(round(sl)))+'m', size=9)
ax.text(14*(sl/10), 6*(sl/10), 1, ''+str(int(round(sl)))+'m', size=9)
ax.text(17*(sl/10), 6*(sl/10), 1, 'm', size=9)
ax.set_zticks([0, 2])

ax.set_xlim(sl,0)
ax.set_ylim(0,sl)
ax.set_zlim(0,10)
