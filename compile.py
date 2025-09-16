def compileCode(output, code_area, tk):
    # 1 Revisar elementos grandes 
        # funciones
    # 2 revisar que exista la funcion principal
    # 3 listar funciones (tipo, nombre, parametros[nombre,tipo], contenido)
    # 4 
    code = code_area.get("1.0", tk.END)
    
    # Habilitar edición temporalmente para limpiar y escribir
    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Compiling...\n{code}\n")
    output.insert(tk.END, "Compilation complete. Testing enable_input...")
    
    # Para probar, habilitar input después de 2 segundos
    output.after(2000, lambda: enable_input(output, tk))

def block_output(output, tk):
    """Bloquea la entrada del usuario pero permite escribir desde código"""
    # Limpiar todos los eventos
    try:
        output.unbind('<KeyPress>')
        output.unbind('<Return>')
        output.unbind('<Button-1>')
        output.unbind('<Button-2>')
        output.unbind('<Button-3>')
        output.unbind('<BackSpace>')
        output.unbind('<Delete>')
    except:
        pass  # Si no había eventos vinculados
    
    # Bloquear entrada del usuario pero mantener el widget en modo NORMAL para código
    output.bind('<KeyPress>', lambda e: "break")
    output.bind('<Button-1>', lambda e: "break")
    output.bind('<Button-2>', lambda e: "break")  
    output.bind('<Button-3>', lambda e: "break")
    output.bind('<BackSpace>', lambda e: "break")
    output.bind('<Delete>', lambda e: "break")
    
    # Mantener en NORMAL para que el código pueda escribir
    output.config(state=tk.NORMAL)

def enable_input(output, tk):
    """Permite escribir/borrar solo desde la posición actual hacia adelante"""
    # Habilitar el widget
    output.config(state=tk.NORMAL)
    
    # Limpiar eventos previos
    try:
        output.unbind('<KeyPress>')
        output.unbind('<Return>')
        output.unbind('<Button-1>')
        output.unbind('<Button-2>')
        output.unbind('<Button-3>')
        output.unbind('<BackSpace>')
        output.unbind('<Delete>')
    except:
        pass
    
    # Marcar la posición inicial donde puede empezar a escribir
    start_position = output.index(tk.END)
    output.insert(tk.END, "\nEnter command: ")
    input_start = output.index(tk.END)  # Posición donde inicia la entrada del usuario
    
    def handle_enter(event):
        # Debug: mostrar información sobre las posiciones
        current_pos = output.index(tk.INSERT)
        end_pos = output.index(tk.END)
        
        # Obtener todo el contenido y dividirlo en líneas
        all_content = output.get("1.0", tk.END)
        lines = all_content.split('\n')
        
        # Buscar la última línea que contiene "Enter command: "
        user_input = ""
        for line in reversed(lines):
            #if "Enter command: " in line:
                # Extraer solo la parte después de "Enter command: "
                #user_input = line.split("Enter command: ", 1)[1]
            user_input = line
            break
        # Procesar el comando
        process_command(user_input, output, tk)
        
        # Bloquear nuevamente la entrada
        block_output(output, tk)
        
        return "break"
    
    def validate_position(event):
        # Solo interceptar teclas especiales que podrían mover el cursor a posiciones no válidas
        # Permitir todas las teclas normales de escritura
        if event.keysym in ['Left', 'Right', 'Up', 'Down', 'Home', 'End', 'Prior', 'Next']:
            current_pos = output.index(tk.INSERT)
            # Solo bloquear movimientos que vayan antes del punto permitido
            if output.compare(current_pos, '<', input_start):
                output.mark_set(tk.INSERT, tk.END)
                return "break"
        
        # Permitir todas las demás teclas (letras, números, etc.)
        return None
    
    def validate_backspace(event):
        # Obtener posición actual del cursor
        current_pos = output.index(tk.INSERT)
        
        # No permitir borrar antes de input_start
        if output.compare(current_pos, '<=', input_start):
            return "break"
        
        # Permitir borrar si está después de input_start
        return None
    
    # Vincular eventos
    output.bind('<Return>', handle_enter)
    output.bind('<KeyPress>', validate_position)
    output.bind('<BackSpace>', validate_backspace)
    output.bind('<Delete>', validate_backspace)
    
    # Posicionar cursor al final
    output.mark_set(tk.INSERT, tk.END)
    output.see(tk.END)

def process_command(command, output, tk):
    """Procesa el comando extraído del usuario"""
    # Aquí puedes procesar el comando como necesites
    output.config(state=tk.NORMAL)
    output.insert(tk.END, f"\nProcessing command: {command}")
    
    # Ejemplo de procesamiento básico
    if command.lower() == "help":
        output.insert(tk.END, "\nAvailable commands: help, clear, exit")
    elif command.lower() == "clear":
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Console cleared.")
    else:
        output.insert(tk.END, f"\nUnknown command: {command}")