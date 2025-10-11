
from compiler.functions import analyze_functions
from user_input import get_user_input

def fillTypeTable():
    return [
        [["funcion",[]],["si",[]],["cuando",[]]],
        [],
        ["entero","flotante","booleano","caracter","texto"]
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
                        _function_braces_2.append([content[_pos_word:auxtemp],'',[],auxtemp,_pos_close_brace,[]])
                        _inside_function = False
                    else:
                        _not_function_braces_2.append([int(_stack_open_braces_2.pop()),_pos_close_brace])
        numberLine = numberLine + 1
    if _inside_function:
        output.insert(tk.END, f"Error:Todas las funciones deben tener llaves. \n")
        return

    output.insert(tk.END, f"Compiling...\n")
    for element in _function_braces_2:
        # 
        _first_space_header = element[0].find(' ')
        if(_first_space_header == -1):
            output.insert(tk.END, f"Error: Separe el nombre de la funcion con un espacio despues de la palabra funcion. \n")
            return
        _before_parameters_ = (element[0])[0:element[0].find('(')]
        _words_before_parameters = [w for w in _before_parameters_.split(' ') if w.strip()]

        #Revizar que _words_before_parameters_ solo sea funcion y nombre
        if(len(_words_before_parameters)!=2):
            output.insert(tk.END, f"Error: La función unicamente debe tener tipo y nombre antes de los parentesis ( ). \n")
            return
        else:#Revizar que nombre sea valido
            if(_words_before_parameters[0]!="funcion"):
                output.insert(tk.END, f"Error: La función debe ser definida con la palabra funcion. \n")
                return
            elif(not validMethodName(_words_before_parameters[1],type_table, output, tk)):
                output.insert(tk.END, f"Error: Nombre de funcion invalida. \n")
                return
            else:
                element[1] = _words_before_parameters[1]
                type_table[1].append([_words_before_parameters[1],[]])
        #Obtener los parametros ()
        if (not (element[0].count('(')==1) or not (element[0].count(')')==1)):
            output.insert(tk.END, f"Error: Funcion '{element[1]}' con parentesis mal usados. \n")
            return
        _open_parenthesis = element[0].find('(')
        _close_parenthesis = element[0].find(')')
        _parentheses_content = (element[0])[_open_parenthesis+1:_close_parenthesis]
        # Revizar si tiene parametros
        if _parentheses_content.strip():
            #Revizar si tiene multiples parametros
            if(not _parentheses_content.find(',')== -1):
                _divided_parameters= _parentheses_content.split(',')
            else:
                _divided_parameters = [_parentheses_content]
            #Revizar que los parametros sean [Tipo, Nombre]
            for parameter in _divided_parameters:
                divided_parameter = parameter.split(' ')
                divided_parameter = [p for p in parameter.split(' ') if p.strip()]
                #Revizar que para parametro solo sean dos piezas
                if(not len(divided_parameter) == 2):
                    output.insert(tk.END, f"Error: Funcion '{element[1]}'. Los parametros deben ser [<tipo> <identificador>]. \n")
                    return
                #Revizar que el tipo sea valido
                if divided_parameter[0] not in type_table[2]:
                    output.insert(tk.END, f"Error: Funcion '{element[1]}'. Tipo de los parametros mal definidos. \n")
                    return
                #Revizar que el nombre del parametro este disponible
                for existing_parameter in element[2]:
                    if(existing_parameter[1] == divided_parameter[1]):
                        output.insert(tk.END, f"Error: Funcion '{element[1]}'. Nombre de parametro '{existing_parameter[1]}' repetido. \n")
                        return
                #Si cumple todo se agrega a la lista de parametros
                element[2].append([divided_parameter[0],divided_parameter[1]])
        # Dividir contenido por limitadores
        function_content = content[element[3]+1:element[4]]
        divided_function_content = []
        end_line = function_content.find(';')
        start_code_section = function_content.find('{')
        last_cut = 0
        _internal_not_function_braces =[]
        findBraces(_internal_not_function_braces, function_content)
        while ( not (end_line == -1 and start_code_section == -1)):
            if((end_line<start_code_section or start_code_section == -1) and end_line != -1):
                functional_piece = function_content[last_cut:end_line]
                last_cut = end_line+1
            else:
                end_code_section = 0
                for braces in _internal_not_function_braces:
                    if(braces[0]==start_code_section):
                        end_code_section = braces[1]
                functional_piece = function_content[last_cut:end_code_section+1]
                last_cut = end_code_section+1
            divided_function_content.append(functional_piece)
            end_line = function_content.find(';',last_cut)
            start_code_section = function_content.find('{',last_cut)
        element[5].append(divided_function_content)
        #Dividir el contenido de la función según estructuras [si, cuando, for, while, sino, etc...] usando ; y {}
        # Identificando las distintas partes dentro de una funcion
        
        #Revizar que exista la función principal
        #Iniciar a hacer las cosas según las estructuras en el orden dentro de principal
        #🖨️ Imprimir informacion para revisiones
        print(" funcion braces 2 ",element)
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

def findBraces(_internal_not_function_braces, content):
    open_braces = []
    for idx, char in enumerate(content):
        if(char == '{'):
            open_braces.append(idx)
        elif(char == '}'):
            _internal_not_function_braces.append([open_braces.pop(),idx])
    return