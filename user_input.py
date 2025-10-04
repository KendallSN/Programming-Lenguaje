# Para probar, habilitar input después de 2 segundos
# Esperar a que el usuario ingrese un comando y obtener el resultado
def get_user_input(output, tk):
    # Usar una variable para almacenar el resultado
    user_input = {"value": None}

    def process_and_set(command, output, tk):
        output.config(state=tk.NORMAL)
        output.insert(tk.END, f"\nProcessing command: {command}")
        user_input["value"] = command  # Guardar el comando
        output.after(100, output.quit)  # Salir del mainloop

    # Redefinir enable_input para usar process_and_set
    def enable_input_and_capture(output, tk):
        output.config(state=tk.NORMAL)
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
        start_position = output.index(tk.END)
        output.insert(tk.END, "\nEnter command: ")
        input_start = output.index(tk.END)

        def handle_enter(event):
            all_content = output.get("1.0", tk.END)
            lines = all_content.split('\n')
            user_command = ""
            for line in reversed(lines):
                if "Enter command: " in line:
                    user_command = line.split("Enter command: ", 1)[1]
                    break
            process_and_set(user_command, output, tk)
            block_output(output, tk)
            return "break"

        def validate_position(event):
            if event.keysym in ['Left', 'Right', 'Up', 'Down', 'Home', 'End', 'Prior', 'Next']:
                current_pos = output.index(tk.INSERT)
                if output.compare(current_pos, '<', input_start):
                    output.mark_set(tk.INSERT, tk.END)
                    return "break"
            return None

        def validate_backspace(event):
            current_pos = output.index(tk.INSERT)
            if output.compare(current_pos, '<=', input_start):
                return "break"
            return None

        output.bind('<Return>', handle_enter)
        output.bind('<KeyPress>', validate_position)
        output.bind('<BackSpace>', validate_backspace)
        output.bind('<Delete>', validate_backspace)
        output.mark_set(tk.INSERT, tk.END)
        output.see(tk.END)

    enable_input_and_capture(output, tk)
    output.mainloop()  # Espera hasta que el usuario presione Enter
    #output.config(state=tk.NORMAL)
    return user_input["value"]

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
