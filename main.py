import tkinter as tk
from tkinter import scrolledtext

from compile import compileCode
from execute import executeCode

def insert_code(code):
    position = code_area.index(tk.INSERT)
    code_area.insert(position, code)

def show_options():
    options = tk.Toplevel(window)
    options.title("Opciones")
    options.geometry("400x300")
    
    tk.Label(options, text="Insertar codigo:", font=("Arial", 12, "bold")).pack(pady=10)
    
    codes = {
        "Basic function": "def my_function():\n    pass\n",
    }
    
    for name, code in codes.items():
        tk.Button(options, text=name, 
                 command=lambda c=code: [insert_code(c), options.destroy()],
                 width=20).pack(pady=2)

# Main window
window = tk.Tk()
window.title("Code Editor")
window.geometry("700x450")

# Menu
menubar = tk.Menu(window)
window.config(menu=menubar)

menubar.add_command(label="Opciones", command=show_options)

# Main frame
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Code text area
code_area = scrolledtext.ScrolledText(main_frame, width=50, height=15, font=("Courier", 10))
code_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,5))

# Right frame
right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Output area
tk.Label(right_frame, text="OUTPUT").pack()
output = tk.Text(right_frame, width=30, height=15, bg="black", fg="green", 
                insertbackground="white", font=("Consolas", 9))
output.pack(pady=(5,10))

# Buttons
button_frame = tk.Frame(right_frame)
button_frame.pack(side=tk.BOTTOM)

tk.Button(button_frame, text="COMPILAR", command=lambda: compileCode(output,code_area,tk), width=10).pack(side=tk.LEFT, padx=2)
tk.Button(button_frame, text="EJECUTAR", command=lambda: executeCode(output,code_area,tk), width=10).pack(side=tk.LEFT, padx=2)

# Initial code
initial_code = '''funcion suma(entero a, entero b):entero{
    resultado = a + b;
    retornar resultado;
}

funcion mostrarMensaje(texto mensaje){
    imprimir(mensaje);
}

funcion principal(){
    imprimir("Ingrese el primer número:");
    num1 = leer;
    imprimir("Ingrese el segundo número:");
    num2 = leer;
    total = suma(num1; num2;);
    mostrarMensaje("El resultado de la suma es:");
    imprimir(total);
    
    si (total == 10){
        imprimir("El total es diez");
    }
    sino si (total > 10){
        imprimir("El total es mayor que diez");
    }
    sino {
        imprimir("El total es menor que diez");
    }
    
    cuando (total){
        caso 5:
            imprimir("El total es cinco");
            terminar;
        caso 10:
            imprimir("El total es diez (switch)");
            terminar;
        defecto:
            imprimir("Valor no esperado");
            terminar;
    }
}
'''

code_area.insert("1.0", initial_code)
window.mainloop()