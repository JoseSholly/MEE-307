import tkinter as tk
from tkinter import StringVar, ttk
import math
from tkinter import messagebox
from time import time

def check(): 
    '''Funtion check() determines the flow type in every second, 
       as long as the Fluid Density, Pipe diameter, Flow velocity and Dynamic viscosity provided in textbox 
    '''
    ACCELERATION_DUE_GRAVITY = 9.8;
    
    if  len(density_entry.get())>=1 and len(PD_entry.get())>=1 and len(flow_velocity.get())>=1 and len(dynamic_vis.get())>=1
        try:
            density = float(density_var.get()) 
            D = float(pd_var.get()) 
            V = float(fv_var.get()) 
            dynamic_viscosity = float(dv_var.get())
            reynold_number = (density * D * V ) / dynamic_viscosity
            Rey_ans= ttk.Label(root, text= '{:.2f}'.format(reynold_number),style= 'label.TLabel').grid(column=1, row=10, sticky=tk.W, ipadx=50)
            if reynold_number<2000: # Actives Pipe Roughness textbox if flow is Laminar flow
                pipe_roughness['state']= 'readonly'
            elif 2000<=reynold_number<=4000:
                pipe_roughness['state']='active' # Actives Pipe Roughness textbox if flow is transistional flow

            else:
                pipe_roughness['state']='active' ## Actives Pipe Roughness textbox if flow is Turbulent flow
        except:
            pass
    root.after(1000, check)

def solve():
    ACCELERATION_DUE_GRAVITY = 9.8;
    
    density = float(density_entry.get()) 
    D = float(PD_entry.get()) 
    V = float(flow_velocity.get()) 
    dynamic_viscosity = float(dynamic_vis.get()) 
    reynold_number = (density * D * V ) / dynamic_viscosity
    friction_factor=0
    if (reynold_number < 2000):

        friction_factor=64 / reynold_number

        L = float(pipe_length.get())
        headloss = friction_factor * L/ D * V**2 /(2 * ACCELERATION_DUE_GRAVITY)

        CONDUCTIVITY = float(conductivity.get())
        SHC= float(shcf.get())

        Pressure = -density * ACCELERATION_DUE_GRAVITY * headloss;
        Pr =( dynamic_viscosity * SHC) / CONDUCTIVITY;
        CoH = 0.023 * (reynold_number**0.8) * Pr**0.4 * CONDUCTIVITY / D
    
        Rey_ans= ttk.Label(root, text= '{:.2f}'.format(reynold_number),style= 'label.TLabel').grid(column=1, row=10, sticky=tk.W, ipadx=50)
        head_loss= ttk.Label(root, text= '{:.4f} '.format(headloss),style= 'label.TLabel').grid(column=1, row=11, sticky=tk.W, ipadx=50)
        pressure_diff= ttk.Label(root,text='{:.2f} Pa'.format(Pressure), style= 'label.TLabel').grid(column=1, row=12, sticky=tk.W,  ipadx=50)
        co_heat_transfer= ttk.Label(root, text= '{:.2f}'.format(CoH) , style= 'label.TLabel').grid(column=1, row=13, sticky=tk.W, ipadx=50)
        leb= ttk.Label(root, text='Laminar Flow' , style= 'label.TLabel').grid(column=1, row=14, sticky=tk.W, ipadx=50)

    elif (reynold_number > 4000):
        friction_factor= 2 * ((8 / reynold_number) ** 12 + ((2.457 * math.log((0.27 * float(pipe_roughness.get()) / D) + (7 / reynold_number ) ** 0.9 )) ** 16 + ( 37530 / reynold_number ) ** 16 ) ** ( -3 / 2 )) ** ( 1/12 )

        L = float(pipe_length.get())
        headloss = friction_factor * L/ D * V**2 /(2 * ACCELERATION_DUE_GRAVITY)

        CONDUCTIVITY = float(conductivity.get())
        SHC= float(shcf.get())

        Pressure = -density * ACCELERATION_DUE_GRAVITY * headloss;
        Pr =( dynamic_viscosity * SHC) / CONDUCTIVITY;
        CoH = 0.023 * (reynold_number**0.8) * Pr**0.4 * CONDUCTIVITY / D
        #print(reynold_number, headloss, Pressure, CoH)
        Rey_ans= ttk.Label(root, text= '{:.2f}'.format(reynold_number),style= 'label.TLabel').grid(column=1, row=10, sticky=tk.W, ipadx=50)
        head_loss= ttk.Label(root, text= '{:.4f}'.format(headloss),style= 'label.TLabel').grid(column=1, row=11, sticky=tk.W, ipadx=50)
        pressure_diff= ttk.Label(root,text='{:.2f} Pa'.format(Pressure), style= 'label.TLabel').grid(column=1, row=12, sticky=tk.W,  ipadx=50)
        co_heat_transfer= ttk.Label(root, text= '{:.2f}'.format(CoH) , style= 'label.TLabel').grid(column=1, row=13, sticky=tk.W, ipadx=50)
        leb= ttk.Label(root, text='Turbulent Flow' , style= 'label.TLabel').grid(column=1, row=14, sticky=tk.W, ipadx=50)
    elif (2000 <= reynold_number <= 4000):
        friction_factor= 2 * ((8 / reynold_number) ** 12 + ((2.457 * math.log((0.27 * float(pipe_roughness.get()) / D) + (7 / reynold_number ) ** 0.9 )) ** 16 + ( 37530 / reynold_number ) ** 16 ) ** ( -3 / 2 )) ** ( 1/12 )

        L = float(pipe_length.get())
        headloss = friction_factor * L/ D * V**2 /(2 * ACCELERATION_DUE_GRAVITY)

        CONDUCTIVITY = float(conductivity.get())
        SHC= float(shcf.get())

        Pressure = -density * ACCELERATION_DUE_GRAVITY * headloss;
        Pr =( dynamic_viscosity * SHC) / CONDUCTIVITY;
        CoH = 0.023 * (reynold_number**0.8) * Pr**0.4 * CONDUCTIVITY / D
        #print(reynold_number, headloss, Pressure, CoH)
        Rey_ans= ttk.Label(root, text= '{:.2f}'.format(reynold_number),style= 'label.TLabel').grid(column=1, row=10, sticky=tk.W, ipadx=50)
        head_loss= ttk.Label(root, text= '{:.4f}'.format(headloss),style= 'label.TLabel').grid(column=1, row=11, sticky=tk.W, ipadx=50)
        pressure_diff= ttk.Label(root,text='{:.2f} Pa'.format(Pressure), style= 'label.TLabel').grid(column=1, row=12, sticky=tk.W,  ipadx=50)
        co_heat_transfer= ttk.Label(root, text= '{:.2f}'.format(CoH) , style= 'label.TLabel').grid(column=1, row=13, sticky=tk.W, ipadx=50)
        leb= ttk.Label(root, text='Transistional Flow' , style= 'label.TLabel').grid(column=1, row=14, sticky=tk.W, ipadx=50)

def clear():
    density_entry.delete(0, 'end'),PD_entry.delete(0, 'end'),flow_velocity.delete(0, 'end');
    pipe_length.delete(0, 'end'),dynamic_vis.delete(0, 'end'),conductivity.delete(0, 'end');
    shcf.delete(0, 'end'),pipe_roughness.delete(0, 'end');
  
    
def main_body():
    global root
    

    root= tk.Tk()
    root.title("Fluid Mechanics (Vertical)")
    root.geometry("450x550")
    root.resizable(0,0)
    root.configure(background='white')
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('label.TLabel', font=('Franklin Gothic Book', 10, ), foreground = 'black', background='white' , padding=8)
    s.configure('entry.TEntry', font=('', 10), foreground = 'black', background="white")
    frame1= ttk.Frame(root, style= 'frame1.TFrame', borderwidth= 5, padding=5)
    options = {'side':'left', 'expand':'False', 'fill':'y'}
    frame1.grid(column=0, row=0, sticky=tk.W)

    global density_entry, PD_entry, flow_velocity, pipe_length, dynamic_vis,conductivity,shcf,pipe_roughness, density_var, pd_var, fv_var, dv_var, roughness


    density_var= StringVar()
    density_label= ttk.Label(root, text='Fluid Density', style= 'label.TLabel').grid(column=0, row=0, sticky=tk.W)
    density_entry= ttk.Entry(root, width=20, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10), textvariable= density_var)
    density_entry.focus()
    density_entry.grid(column=1, row=0, sticky='ew', padx=15,  pady=5)

    pd_var= StringVar()
    PD_label= ttk.Label(root, text='Pipe Diameter', style= 'label.TLabel').grid(column=0, row=1, sticky=tk.W)
    PD_entry= ttk.Entry(root, width=20, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10), textvariable= pd_var)
    PD_entry.focus()
    PD_entry.grid(column=1, row=1, sticky='ew', padx=15,  pady=5 )

    fv_var= StringVar()
    FV_label= ttk.Label(root, text='Flow Velocity', style= 'label.TLabel').grid(column=0, row=2, sticky=tk.W)
    flow_velocity= ttk.Entry(root, width=20, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10), textvariable=fv_var)
    flow_velocity.focus()
    flow_velocity.grid(column=1, row=2, sticky='ew', padx=15, pady=5 )

    dv_var= StringVar()
    DV_label= ttk.Label(root, text='Dynamic Viscosity', style= 'label.TLabel').grid(column=0, row=3, sticky=tk.W)
    dynamic_vis= ttk.Entry(root, width=20, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10), textvariable=dv_var)
    dynamic_vis.focus()
    dynamic_vis.grid(column=1, row=3, sticky='ew', padx=15, pady=5 )

    roughness= StringVar()
    PR_label= ttk.Label(root, text='Pipe Roughness', style= 'label.TLabel').grid(column=0, row=4, sticky=tk.W)
    pipe_roughness= ttk.Entry(root, width=20, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10), state='readonly', textvariable=roughness)
    pipe_roughness.focus()
    pipe_roughness.grid(column=1, row=4, sticky='ew', padx=15, pady=5 )

    PL_label= ttk.Label(root, text='Pipe Length', style= 'label.TLabel').grid(column=0, row=5, sticky=tk.W)
    pipe_length= ttk.Entry(root, width=20, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10))
    pipe_length.focus()
    pipe_length.grid(column=1, row=5, sticky='ew', padx=15, pady=5 )

    C_label= ttk.Label(root, text='Conductivity', style= 'label.TLabel').grid(column=0, row=6, sticky=tk.W)
    conductivity= ttk.Entry(root, width=20, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10))
    conductivity.focus()
    conductivity.grid(column=1, row=6, sticky='ew', padx=15, pady=5 )

    SHCF_label= ttk.Label(root, text='Specific heat Capacity of Fluid', style= 'label.TLabel').grid(column=0, row=7, sticky=tk.W)
    shcf= ttk.Entry(root, width=20, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10))
    shcf.focus()
    shcf.grid(column=1, row=7, sticky='ew', padx=15, pady=5 )

    s.configure('C.TButton', font=('Franklin Gothic Book', 12), foreground = '#DADADA', background="#0A1172",focusthickness=3,relief= 'flat') #focusthickness=3,relief= 'flat'
    s.map("C.TButton", 
    foreground=[('pressed', 'white'), ('active', 'white')], 
    background=[('pressed', '#003166'), ('active', '#003166')])


    res= {'width':10, 'style':"C.TButton", 'padding':(10,10,10,10), 'cursor': 'hand2' }

    solve_button = ttk.Button(root, text= 'Solve',**res , command= solve)
    solve_button.grid(column=0, row=8, padx=10, pady=10, ipadx= 30 ) 

    clear_button = ttk.Button(root, text= 'Clear',**res , command= clear)
    clear_button.grid(column=1, row=8, padx=10, pady=10, ipadx= 25 ) 
    global Rey_ans, head_loss, pressure_diff, co_heat_transfer

    l1= ttk.Label(root, text='Reynold\'s Number: ', style= 'label.TLabel').grid(column=0, row=10, sticky=tk.W)

    l2= ttk.Label(root, text='Head Loss: ', style= 'label.TLabel').grid(column=0, row=11, sticky=tk.W)

    l3= ttk.Label(root, text='Pressure Head(difference): ', style= 'label.TLabel').grid(column=0, row=12, sticky=tk.W)

    l4= ttk.Label(root, text='Co-efficient of Heat transfer: ', style= 'label.TLabel').grid(column=0, row=13, sticky=tk.W)

    l4= ttk.Label(root, text='Flow Type: ', style= 'label.TLabel').grid(column=0, row=14, sticky=tk.W)
    
    check()
    root.mainloop()
    
if __name__=="__main__":
    main_body()
