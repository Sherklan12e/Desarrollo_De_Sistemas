import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Calculadora')
        self.ventana.geometry('300x400')
        self.ventana.configure(bg='#f0f0f0')
        
        # Variable para almacenar la expresión
        self.expresion = ''
        
        # Campo de entrada
        self.entrada = ttk.Entry(self.ventana, justify='right', font=('Arial', 20))
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        
        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Estilo para los botones
        style = ttk.Style()
        style.configure('Calc.TButton', font=('Arial', 12))
        
        # Crear y posicionar botones
        row = 1
        col = 0
        for boton in botones:
            cmd = lambda x=boton: self.click(x)
            ttk.Button(self.ventana, text=boton, style='Calc.TButton',
                      command=cmd).grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Botón Clear
        ttk.Button(self.ventana, text='C', style='Calc.TButton',
                  command=self.limpiar).grid(row=row, column=0, columnspan=4, padx=2, pady=2, sticky='nsew')
        
        # Configurar el grid
        for i in range(5):
            self.ventana.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.ventana.grid_columnconfigure(i, weight=1)
    
    def click(self, texto):
        if texto == '=':
            try:
                resultado = eval(self.expresion)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, str(resultado))
                self.expresion = str(resultado)
            except:
                messagebox.showerror('Error', 'Expresión inválida')
                self.limpiar()
        else:
            self.expresion += texto
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, self.expresion)
    
    def limpiar(self):
        self.expresion = ''
        self.entrada.delete(0, tk.END)
    
    def iniciar(self):
        self.ventana.mainloop()

if __name__ == '__main__':
    calc = Calculadora()
    calc.iniciar()