
from compiler.functions import analyze_functions
from user_input import get_user_input

def compileCode(output, code_area, tk):
    # 1 Revisar elementos grandes 
        # Funciones 
            # reconocer funciones (Palabra reservada y nombre)
            # verificar parametros (Tipo y nombre)
            # verificar contenido entre {}
    # 2 revisar que exista la funcion principal
    # 3 listar funciones (tipo, nombre, parametros[nombre,tipo], contenido)

    code = code_area.get("1.0", tk.END)
    
    # Habilitar edición temporalmente para limpiar y escribir
    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END) # Limpiar el output
    #output.insert(tk.END, f"Compiling...\n{code}\n")
    output.insert(tk.END, f"Compiling...\n")
    #output.insert(tk.END, "Compilation complete. Testing enable_input...")
    
    #analysis = analyze_functions(code)
    #print(analysis)
    content = code_area.get("1.0",tk.END)
    
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces != close_braces:
        output.insert(tk.END, f"Error: Llaves desbalanceadas. '{{':, '}}':\n")
        return 
    lines = content.split('\n')
    numberLine = 0

    auxContent = content
    _stack_open_braces = []
    _stack_close_braces = []
    _not_function_braces = []
    _function_braces = []
    _pos_last_open_brace = 0
    _pos_last_close_brace = 0
    _pos_end_last_function = 0
    _inside_function = False
    for line in lines:
        words = line.split(' ')
        for word in words:
            if(word != ' ') and (len(word)>0):
                #print(str(numberLine) + "[" + word + "]"+ str(len(word)))
                if(word == "funcion"):
                    _inside_function = True
                    _pos_word = content.find(word, _pos_end_last_function)
                    _pos_open_brace = content.find('{', _pos_word)
                    _pos_close_brace = content.find('}', _pos_word) 
                    _pos_end_last_function = _pos_close_brace
                    print(f"Posición de '{word}' en content: {_pos_word}")
                    print(f"Posición del primer '{{' en content: {_pos_open_brace}")
                    print(f"Posición del primer '}}' en content: {_pos_close_brace}")
                #elif not _inside_function:
                    #output.insert(tk.END, f"Error: Linea '{numberLine}' Todo debe estar contenido en funciones. \n")
                    #return
                
                #if(word.find('{') != -1):
                    #_pos_open_brace = content.find('{',_pos_last_open_brace)
                    #_stack_open_braces.append(_pos_open_brace)
                    #_pos_last_open_brace = _pos_open_brace
                #if(word.find('}') != -1):
                    #_pos_close_brace = content.find('}',_pos_last_close_brace)
                    #_pos_last_close_brace = _pos_close_brace
                    #_not_function_braces.append([_stack_open_braces.pop,_pos_close_brace])
                    #if not _inside_function:
                    #    output.insert(tk.END, f"Error: Linea '{numberLine}' Simbolo '}}' utilizado incorrectamente")
                    #    return
                    #if _inside_function:
                    #    _inside_function = False
                numberLine = numberLine + 1

    for idx, char in enumerate(content):
        if char == '{':
            _stack_open_braces.append(idx)
        if char == '}':
            if(len(_stack_open_braces)==0):
                output.insert(tk.END, f"Error: Simbolo '}}' sin '{{' correspondiente.")
                return
            print("count", len(_stack_open_braces))
            if(len(_stack_open_braces)==1):
                _function_braces.append([int(_stack_open_braces.pop()), idx])
            else:
                _not_function_braces.append([int(_stack_open_braces.pop()), idx])

    for element in _not_function_braces:
        print("not funcion braces",element)
    for element in _function_braces:
        print("funcion braces",element)

    get_user_input(output, tk)
    print("test")
    return