
from compiler.functions import analyze_functions
from user_input import get_user_input

def compileCode(output, code_area, tk):
    # 1 Revisar elementos grandes 
        # funciones
    # 2 revisar que exista la funcion principal
    # 3 listar funciones (tipo, nombre, parametros[nombre,tipo], contenido)
    # 4 
    code = code_area.get("1.0", tk.END)
    
    # Habilitar edición temporalmente para limpiar y escribir
    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END) # Limpiar el output
    output.insert(tk.END, f"Compiling...\n{code}\n")
    output.insert(tk.END, "Compilation complete. Testing enable_input...")
    
    #analysis = analyze_functions(code)
    #print(analysis)
    content = code_area.get("1.0",tk.END)
    lines = content.split('\n')
    numberLine = 0
    for line in lines:
        words = line.split(' ')
        for word in words:
            if(word != ' ') and (len(word)>0):
                print(str(numberLine) + "[" + word + "]"+ str(len(word)))
        numberLine=numberLine+1

    get_user_input(output, tk)
    print("test")
    return