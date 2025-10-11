
from compiler.functions import analyze_functions
from user_input import get_user_input

def fillTypeTable():
    return [
        [["funcion",[]],["si",[]],["cuando",[]]],
        []
    ]

def compileCode(output, code_area, tk):
    type_table = fillTypeTable()
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
    numberLine = 1
    
    _pos_last_open_brace = 0
    _pos_last_close_brace = 0
    _pos_end_last_function = 0
    _inside_function = False

    # Recorrer un string char por char con indice
    #for idx, char in enumerate(content):

    _stack_open_braces_2 = []
    _not_function_braces_2 = []
    _function_braces_2 = []

    for line in lines:
        words = line.split(' ')
        for word in words:
            if(word != ' ') and (len(word)>0):
                #print(str(numberLine) + "[" + word + "]"+ str(len(word)))
                if(word == "funcion") and not _inside_function:
                    _inside_function = True
                    _pos_word = content.find(word, _pos_end_last_function)
                    _pos_close_brace = content.find('}', _pos_word) 
                    _pos_end_last_function = _pos_close_brace
                    print(f"Posición de '{word}' en content: {_pos_word}")
                elif not _inside_function:
                    if(word == "funcion"):
                        output.insert(tk.END, f"Error: Linea '{numberLine}' No se permite declarar funciones dentro de otras funciones. \n")
                    else:
                        output.insert(tk.END, f"Error: Linea '{numberLine}' Todo debe estar contenido en funciones. \n")
                    return
                elif(word.find('{') != -1):
                    _pos_open_brace = content.find('{', _pos_last_open_brace)
                    _pos_last_open_brace = _pos_open_brace+1
                    _stack_open_braces_2.append(_pos_open_brace)
                elif(word.find('}') != -1):
                    _pos_close_brace = content.find('}', _pos_last_close_brace)
                    _pos_last_close_brace = _pos_close_brace+1
                    if(len(_stack_open_braces_2)==1):
                        auxtemp = int(_stack_open_braces_2.pop())
                        _function_braces_2.append([content[_pos_word:auxtemp],'',['',''],auxtemp,_pos_close_brace,[]])
                        _inside_function = False
                    else:
                        _not_function_braces_2.append([int(_stack_open_braces_2.pop()),_pos_close_brace])
        numberLine = numberLine + 1
    if _inside_function:
        output.insert(tk.END, f"Error:Todas las funciones deben tener llaves. \n")
        return

    output.insert(tk.END, f"Compiling...\n")

    for element in _not_function_braces_2:
        print("not funcion braces 2 ",element)
    for element in _function_braces_2:
        # 
        _first_space_header = element[0].find(' ')
        if(_first_space_header == -1):
            output.insert(tk.END, f"Error: Separe el nombre de la funcion con un espacio despues de la palabra funcion. \n")
            return
        _before_paramethers_ = (element[0])[0:element[0].find('(')]
        _words_before_paramethers = [w for w in _before_paramethers_.split(' ') if w.strip()]

        #Revizar que _words_before_paramethers_ solo sea funcion y nombre
        if(len(_words_before_paramethers)!=2):
            output.insert(tk.END, f'Error: La función unicamente debe tener tipo y nombre antes de los parentesis ( ). \n')
            return
        else:#Revizar que nombre sea valido
            if(_words_before_paramethers[0]!="funcion"):
                output.insert(tk.END, f'Error: La función debe ser definida con la palabra funcion. \n')
                return
            elif(not validMethodName(_words_before_paramethers[1],type_table, output, tk)):
                output.insert(tk.END, f'Error: Nombre de funcion invalida. \n')
                return
            else:
                element[1] = _words_before_paramethers[1]
                type_table[1].append([_words_before_paramethers[1],[]])
        #Obtener los parametros ()
        #Revizar que los parametros sean [Tipo, Nombre]
        #Dividir el contenido de la función según estructuras [si, cuando, for, while, sino, etc...] usando ; y {}
        #Revizar que exista la función principal
        #Iniciar a hacer las cosas según las estructuras en el orden dentro de principal
        #🖨️ Imprimir informacion para revisiones
        print(" funcion braces 2 ",element)
        print(_words_before_paramethers, len(_words_before_paramethers))
    get_user_input(output, tk)
    print("test")
    return

def validMethodName( _name, type_table, output, tk):
    #Revizar que el nombre que se quiera usar no sea una palabra restringida
    for element in type_table[0]:
        if(element[0]==_name):
            output.insert(tk.END, f'Un identificador no puede ser una palabra restringida. \n')
            return False
    #Revizar que el nombre que se quiera usar no sea un nombre ya utilizado
    for element in type_table[1]:
        if(element[0]==_name):
            output.insert(tk.END, f'Un mismo identificador esta siendo usado multiples veces. \n')
            return False
    return True