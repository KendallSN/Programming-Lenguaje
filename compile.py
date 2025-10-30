
from compiler.functions import analyze_functions
from user_input import get_user_input

# Variable global para almacenar las funciones compiladas
compiled_functions = []

def fillTypeTable():
    return [
        ["funcion","si","sino","sinosi","cuando","para","mientras","imprimir","leer","retornar"],
        [],
        ["entero","flotante","booleano","caracter","texto"]
    ]

def smart_divide_function_content(function_content, internal_braces):
    """
    Divide el contenido de una función respetando paréntesis y llaves.
    Los punto y coma dentro de paréntesis no se consideran como delimitadores.
    """
    divided_content = []
    current_piece = ""
    paren_depth = 0
    brace_depth = 0
    in_quotes = False
    quote_char = None
    i = 0
    
    while i < len(function_content):
        char = function_content[i]
        
        # Manejo de comillas
        if char in ['"', "'"] and (i == 0 or function_content[i-1] != '\\'):
            if not in_quotes:
                in_quotes = True
                quote_char = char
            elif char == quote_char:
                in_quotes = False
                quote_char = None
        
        # Solo contar paréntesis y llaves fuera de comillas
        if not in_quotes:
            if char == '(':
                paren_depth += 1
            elif char == ')':
                paren_depth -= 1
            elif char == '{':
                brace_depth += 1
            elif char == '}':
                brace_depth -= 1
                current_piece += char
                # Si llegamos al nivel 0 de llaves, es el final de una estructura
                if brace_depth == 0:
                    divided_content.append(current_piece.strip())
                    current_piece = ""
                    i += 1
                    continue
            elif char == ';' and paren_depth == 0 and brace_depth == 0:
                # Solo dividir por ; si estamos fuera de paréntesis y llaves
                if current_piece.strip():
                    divided_content.append(current_piece.strip())
                    current_piece = ""
                i += 1
                continue
        
        current_piece += char
        i += 1
    
    # Agregar cualquier contenido restante
    if current_piece.strip():
        divided_content.append(current_piece.strip())
    
    return divided_content

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
                        _function_braces_2.append([content[_pos_word:auxtemp],'',[],auxtemp,_pos_close_brace,[],[]])
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
        #Revizar y guardar tipo de la funcion
        _doublepoints = element[0].find(':')
        if(_doublepoints!= -1 and validMethodType((element[0])[_doublepoints+1:len(element[0])], type_table)):
            element[5]=(element[0])[_doublepoints+1:len(element[0])]
        elif(_doublepoints == -1):
            element[5]=''
        else:
            output.insert(tk.END, f"Error: Funcion '{element[1]}' tipo de funcion incorrecto. \n")
            return
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
        # Dividir contenido por limitadores (respetando paréntesis y llaves)
        function_content = content[element[3]+1:element[4]]
        divided_function_content = []
        _internal_not_function_braces =[]
        findBraces(_internal_not_function_braces, function_content)
        
        # Nueva lógica de división que respeta paréntesis
        divided_function_content = smart_divide_function_content(function_content, _internal_not_function_braces)
        parse_function_content(divided_function_content,element, type_table)
        
        #element[6].append(divided_function_content)
        #Dividir el contenido de la función según estructuras [si, cuando, for, while, sino, etc...] usando ; y {}
        # Identificando las distintas partes dentro de una funcion
        #Revizar que exista la función principal
        #Iniciar a hacer las cosas según las estructuras en el orden dentro de principal
        #🖨️ Imprimir informacion para revisiones
        print(" funcion braces 2 ",element)
    
    # Verificar que existe la función principal
    has_principal = False
    principal_func = None
    for func in _function_braces_2:
        if func[1] == "principal":
            has_principal = True
            principal_func = func
            break
    
    if not has_principal:
        output.insert(tk.END, f"Error: No se encontró la función 'principal'. Todo programa debe tener una función principal.\n")
        return
    
    output.insert(tk.END, f"Compilación exitosa.\n")
    output.insert(tk.END, f"Funciones encontradas: {len(_function_braces_2)}\n")
    for func in _function_braces_2:
        output.insert(tk.END, f"  - {func[1]} ({len(func[2])} parámetros, {len(func[6])} instrucciones)\n")
    
    # Guardar las funciones compiladas para ejecución
    global compiled_functions
    compiled_functions = _function_braces_2
    
    return

def parse_function_content(divided_function_content, element, type_table):
    """
    Parsea el contenido de una función y lo convierte en estructuras ejecutables.
    element[6] contendrá una lista de instrucciones estructuradas.
    """
    for function_section in divided_function_content:
        function_section_stripped = function_section.strip()
        if not function_section_stripped:
            continue
            
        instruction = parse_instruction(function_section_stripped, type_table, element[1])
        if instruction:
            element[6].append(instruction)

def parse_instruction(section, type_table, function_name):
    """
    Convierte una sección de código en una estructura de datos ejecutable.
    Retorna un diccionario con el tipo de instrucción y sus componentes.
    """
    section = section.strip()
    if not section:
        return None
    
    # IMPRIMIR: imprimir(contenido); - Verificar PRIMERO antes de dividir en palabras
    # Esto es CRÍTICO para evitar que se confunda con una función
    if section.startswith("imprimir(") or section.startswith("imprimir ("):
        return parse_print_statement(section)
    
    section_divided = [word for word in section.split(' ') if word.strip()]
    if not section_divided:
        return None
    
    # Extraer la primera palabra antes de cualquier paréntesis
    first_word = section_divided[0].split('(')[0] if '(' in section_divided[0] else section_divided[0]
    
    # Verificar de nuevo imprimir por si había espacios
    if first_word == "imprimir":
        return parse_print_statement(section)
    
    # RETORNAR: retornar valor;
    elif first_word == "retornar":
        return parse_return_statement(section, section_divided)
    
    # CONDICIONAL SI: si (condicion){ ... }
    elif first_word == "si":
        return parse_if_statement(section, type_table, function_name)
    
    # CONDICIONAL SINOSI: sinosi (condicion){ ... }
    elif first_word == "sinosi":
        return parse_elseif_statement(section, type_table, function_name)
    
    # CONDICIONAL SINO: sino { ... }
    elif first_word == "sino":
        return parse_else_statement(section, type_table, function_name)
    
    # SWITCH CUANDO: cuando (variable){ caso valor: ... }
    elif first_word == "cuando":
        return parse_switch_statement(section, type_table, function_name)
    
    # BUCLE MIENTRAS: mientras (condicion){ ... }
    elif first_word == "mientras":
        return parse_while_statement(section, type_table, function_name)
    
    # BUCLE PARA: para (inicio; condicion; incremento){ ... }
    elif first_word == "para":
        return parse_for_statement(section, type_table, function_name)
    
    # LEER: variable = leer; - Verificar DESPUÉS de palabras clave de control
    # Esto evita que "mientras" sea detectado como "leer"
    elif "leer" in section and "=" in section and first_word not in type_table[0]:
        return parse_read_statement(section, section_divided, type_table)
    
    # DECLARACIÓN DE VARIABLE: tipo nombre = valor;
    elif first_word in type_table[2]:
        return parse_variable_declaration(section, section_divided, type_table)
    
    # ASIGNACIÓN: variable = valor;
    elif "=" in section and first_word not in type_table[2]:
        return parse_assignment(section, section_divided)
    
    # LLAMADA A FUNCIÓN: nombreFuncion(parametros); - Solo si NO es una palabra reservada
    elif "(" in section and first_word not in type_table[0] and first_word not in ["imprimir", "leer"]:
        return parse_function_call(section)
    
    return None

def parse_variable_declaration(section, section_divided, type_table):
    """Parsea: tipo nombre = valor;"""
    if not section_divided or len(section_divided) == 0:
        return None
    
    var_type = section_divided[0]
    
    if "=" not in section:
        if len(section_divided) < 2:
            return None
        return {
            "type": "variable_declaration",
            "var_type": var_type,
            "var_name": section_divided[1].replace(';',''),
            "value": None
        }
    
    equal_pos = section.find('=')
    left_part = section[:equal_pos].strip()
    right_part = section[equal_pos+1:].strip().rstrip(';')
    
    parts = left_part.split()
    if len(parts) < 2:
        return None
    
    var_name = parts[1]
    value_expression = parse_expression(right_part)
    
    return {
        "type": "variable_declaration",
        "var_type": var_type,
        "var_name": var_name,
        "value": value_expression
    }

def parse_assignment(section, section_divided):
    """Parsea: variable = valor;"""
    equal_pos = section.find('=')
    var_name = section[:equal_pos].strip()
    value_part = section[equal_pos+1:].strip().rstrip(';')
    
    return {
        "type": "assignment",
        "var_name": var_name,
        "value": parse_expression(value_part)
    }

def parse_print_statement(section):
    """Parsea: imprimir(contenido);"""
    open_paren = section.find('(')
    close_paren = section.rfind(')')
    content = section[open_paren+1:close_paren].strip()
    
    # Parsear múltiples parámetros separados por coma
    params = []
    if content:
        # Dividir por comas, pero respetando paréntesis y comillas
        param_parts = split_by_comma(content)
        for param in param_parts:
            params.append(parse_expression(param.strip()))
    
    return {
        "type": "print",
        "content": params
    }

def parse_read_statement(section, section_divided, type_table):
    """Parsea: tipo variable = leer;"""
    equal_pos = section.find('=')
    left_part = section[:equal_pos].strip().split()
    
    if len(left_part) == 2 and left_part[0] in type_table[2]:
        return {
            "type": "read",
            "var_type": left_part[0],
            "var_name": left_part[1]
        }
    else:
        return {
            "type": "read",
            "var_type": None,
            "var_name": left_part[0]
        }

def parse_return_statement(section, section_divided):
    """Parsea: retornar valor;"""
    value_part = section[8:].strip().rstrip(';')
    
    return {
        "type": "return",
        "value": parse_expression(value_part) if value_part else None
    }

def parse_if_statement(section, type_table, function_name):
    """Parsea: si (condicion){ ... }"""
    open_paren = section.find('(')
    close_paren = find_matching_paren(section, open_paren)
    condition = section[open_paren+1:close_paren].strip()
    
    open_brace = section.find('{', close_paren)
    close_brace = find_matching_brace(section, open_brace)
    body = section[open_brace+1:close_brace].strip()
    
    return {
        "type": "if",
        "condition": parse_condition(condition),
        "body": parse_body(body, type_table, function_name)
    }

def parse_elseif_statement(section, type_table, function_name):
    """Parsea: sinosi (condicion){ ... }"""
    open_paren = section.find('(')
    close_paren = find_matching_paren(section, open_paren)
    condition = section[open_paren+1:close_paren].strip()
    
    open_brace = section.find('{', close_paren)
    close_brace = find_matching_brace(section, open_brace)
    body = section[open_brace+1:close_brace].strip()
    
    return {
        "type": "elseif",
        "condition": parse_condition(condition),
        "body": parse_body(body, type_table, function_name)
    }

def parse_else_statement(section, type_table, function_name):
    """Parsea: sino { ... }"""
    open_brace = section.find('{')
    close_brace = find_matching_brace(section, open_brace)
    body = section[open_brace+1:close_brace].strip()
    
    return {
        "type": "else",
        "body": parse_body(body, type_table, function_name)
    }

def parse_switch_statement(section, type_table, function_name):
    """Parsea: cuando (variable){ ... defecto: ... }"""
    open_paren = section.find('(')
    close_paren = find_matching_paren(section, open_paren)
    variable = section[open_paren+1:close_paren].strip()
    
    open_brace = section.find('{', close_paren)
    close_brace = find_matching_brace(section, open_brace)
    body = section[open_brace+1:close_brace].strip()
    
    cases = parse_switch_cases(body, type_table, function_name)
    
    return {
        "type": "switch",
        "variable": variable,
        "cases": cases
    }

def parse_switch_cases(body, type_table, function_name):
    """Parsea los casos dentro de un switch"""
    cases = []
    lines = body.split('\n')
    current_case = None
    
    for line in lines:
        line = line.strip()
        if line.startswith('caso '):
            if current_case:
                cases.append(current_case)
            colon_pos = line.find(':')
            value = line[5:colon_pos].strip()
            current_case = {
                "value": parse_expression(value),
                "instructions": []
            }
            # Si hay código después de los dos puntos
            after_colon = line[colon_pos+1:].strip()
            if after_colon and after_colon != 'terminar':
                inst = parse_instruction(after_colon, type_table, function_name)
                if inst:
                    current_case["instructions"].append(inst)
        elif line.startswith('defecto:'):
            if current_case:
                cases.append(current_case)
            current_case = {
                "value": "default",
                "instructions": []
            }
            after_colon = line[8:].strip()
            if after_colon and after_colon != 'terminar':
                inst = parse_instruction(after_colon, type_table, function_name)
                if inst:
                    current_case["instructions"].append(inst)
        elif line == 'terminar' or line.endswith(';terminar'):
            if current_case:
                cases.append(current_case)
                current_case = None
        elif line and current_case:
            line_clean = line.rstrip(';')
            inst = parse_instruction(line_clean, type_table, function_name)
            if inst:
                current_case["instructions"].append(inst)
    
    if current_case:
        cases.append(current_case)
    
    return cases

def parse_while_statement(section, type_table, function_name):
    """Parsea: mientras (condicion){ ... }"""
    open_paren = section.find('(')
    close_paren = find_matching_paren(section, open_paren)
    condition = section[open_paren+1:close_paren].strip()
    
    open_brace = section.find('{', close_paren)
    close_brace = find_matching_brace(section, open_brace)
    body = section[open_brace+1:close_brace].strip()
    
    return {
        "type": "while",
        "condition": parse_condition(condition),
        "body": parse_body(body, type_table, function_name)
    }

def parse_for_statement(section, type_table, function_name):
    """Parsea: para(inicio; condicion; incremento){ ... }"""
    open_paren = section.find('(')
    
    # Encontrar el paréntesis de cierre correspondiente
    close_paren = find_matching_paren(section, open_paren)
    params = section[open_paren+1:close_paren].strip()
    
    parts = params.split(';')
    init = parts[0].strip() if len(parts) > 0 else ""
    condition = parts[1].strip() if len(parts) > 1 else ""
    increment = parts[2].strip() if len(parts) > 2 else ""
    
    open_brace = section.find('{', close_paren)
    close_brace = find_matching_brace(section, open_brace)
    body = section[open_brace+1:close_brace].strip()
    
    # El incremento puede ser una asignación (i = i + 1) o una expresión (i++)
    increment_inst = None
    if increment:
        if '=' in increment:
            increment_inst = parse_assignment(increment, increment.split())
        else:
            increment_inst = parse_expression(increment)
    
    return {
        "type": "for",
        "init": parse_instruction(init, type_table, function_name) if init else None,
        "condition": parse_condition(condition),
        "increment": increment_inst,
        "body": parse_body(body, type_table, function_name)
    }

def parse_function_call(section):
    """Parsea: nombreFuncion(parametros);"""
    open_paren = section.find('(')
    function_name = section[:open_paren].strip()
    
    close_paren = section.rfind(')')
    params = section[open_paren+1:close_paren].strip()
    
    param_list = []
    if params:
        param_parts = split_by_comma(params)
        for param in param_parts:
            param_list.append(parse_expression(param.strip()))
    
    return {
        "type": "function_call",
        "function_name": function_name,
        "parameters": param_list
    }

def find_operator_position(expr, operator):
    """Encuentra la posición del operador fuera de comillas y paréntesis"""
    in_quotes = False
    quote_char = None
    paren_count = 0
    
    i = 0
    while i < len(expr):
        char = expr[i]
        
        # Manejo de comillas
        if char in ['"', "'"] and not in_quotes:
            in_quotes = True
            quote_char = char
        elif char == quote_char and in_quotes:
            in_quotes = False
            quote_char = None
        
        # Solo buscar operadores fuera de comillas y paréntesis
        if not in_quotes:
            if char == '(':
                paren_count += 1
            elif char == ')':
                paren_count -= 1
            elif paren_count == 0:
                # Verificar si encontramos el operador
                if expr[i:i+len(operator)] == operator:
                    return i
        
        i += 1
    
    return -1

def parse_expression(expr):
    """Parsea una expresión y determina su tipo"""
    expr = expr.strip()
    
    if not expr:
        return {"expr_type": "empty", "value": None}
    
    # Literal de texto (entre comillas)
    if (expr.startswith('"') and expr.endswith('"')):
        return {"expr_type": "string_literal", "value": expr[1:-1]}
    
    # Literal de carácter (entre comillas simples)
    if (expr.startswith("'") and expr.endswith("'")):
        return {"expr_type": "char_literal", "value": expr[1:-1]}
    
    # Booleano
    if expr in ['verdadero', 'falso']:
        return {"expr_type": "bool_literal", "value": expr == 'verdadero'}
    
    # Número flotante
    if '.' in expr and expr.replace('.', '').replace('-', '').isdigit():
        return {"expr_type": "float_literal", "value": float(expr)}
    
    # Número entero
    if expr.replace('-', '').isdigit():
        return {"expr_type": "int_literal", "value": int(expr)}
    
    # Nulo
    if expr == 'nulo':
        return {"expr_type": "null_literal", "value": None}
    
    # Llamada a función (pero NO si es imprimir o leer, que son instrucciones)
    if '(' in expr and ')' in expr:
        func_name = expr[:expr.find('(')].strip()
        # Solo tratar como llamada a función si NO es una palabra reservada de instrucción
        if func_name not in ['imprimir', 'leer', 'si', 'sino', 'sinosi', 'cuando', 'mientras', 'para']:
            return parse_function_call(expr)
    
    # Operadores lógicos con palabras
    for op in ['yy', 'oo']:
        if ' ' + op + ' ' in expr:
            parts = expr.split(' ' + op + ' ', 1)
            return {
                "expr_type": "operation",
                "operator": op,
                "left": parse_expression(parts[0].strip()),
                "right": parse_expression(parts[1].strip())
            }
    
    # Operadores de comparación y aritméticos (ordenados por longitud para evitar conflictos)
    operators = ['==', '!=', '<=', '>=', '+=', '-=', '*=', '/=', '<', '>', '+', '-', '*', '/', '%']
    for op in operators:
        if op in expr:
            # Buscar el operador fuera de comillas y paréntesis
            op_pos = find_operator_position(expr, op)
            if op_pos != -1:
                left_part = expr[:op_pos].strip()
                right_part = expr[op_pos + len(op):].strip()
                
                # Evitar casos donde el operador es parte de otro (ej: <= en lugar de <)
                if left_part and right_part:
                    return {
                        "expr_type": "operation",
                        "operator": op,
                        "left": parse_expression(left_part),
                        "right": parse_expression(right_part)
                    }
    
    # Operador NOT
    if expr.startswith('no '):
        return {
            "expr_type": "operation",
            "operator": "no",
            "operand": parse_expression(expr[3:].strip())
        }
    
    # Variable
    return {"expr_type": "variable", "name": expr}

def parse_condition(condition):
    """Parsea una condición (para if, while, etc.)"""
    return parse_expression(condition)

def parse_body(body, type_table, function_name):
    """Parsea el cuerpo de una estructura (if, while, for, etc.)"""
    instructions = []
    
    if not body or not body.strip():
        return instructions
    
    # Dividir por punto y coma, pero respetando llaves
    statements = split_statements(body)
    
    for statement in statements:
        statement = statement.strip()
        if not statement:
            continue
        
        # Parsear la instrucción
        inst = parse_instruction(statement, type_table, function_name)
        if inst:
            instructions.append(inst)
    
    return instructions

def split_statements(body):
    """Divide el cuerpo en declaraciones respetando llaves"""
    if not body or not body.strip():
        return []
    
    statements = []
    current = ""
    brace_count = 0
    paren_count = 0
    in_quotes = False
    quote_char = None
    
    for char in body:
        current += char
        
        # Manejo de comillas
        if char in ['"', "'"] and not in_quotes:
            in_quotes = True
            quote_char = char
        elif char == quote_char and in_quotes:
            in_quotes = False
            quote_char = None
        
        # Solo contar llaves y paréntesis fuera de comillas
        if not in_quotes:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
            elif char == '(':
                paren_count += 1
            elif char == ')':
                paren_count -= 1
            elif char == ';' and brace_count == 0 and paren_count == 0:
                statements.append(current[:-1].strip())
                current = ""
    
    if current.strip():
        statements.append(current.strip())
    
    return statements

def split_by_comma(text):
    """Divide por comas respetando paréntesis y comillas"""
    parts = []
    current = ""
    paren_count = 0
    in_quotes = False
    quote_char = None
    
    for char in text:
        if char in ['"', "'"] and not in_quotes:
            in_quotes = True
            quote_char = char
            current += char
        elif char == quote_char and in_quotes:
            in_quotes = False
            quote_char = None
            current += char
        elif char == '(' and not in_quotes:
            paren_count += 1
            current += char
        elif char == ')' and not in_quotes:
            paren_count -= 1
            current += char
        elif char == ',' and paren_count == 0 and not in_quotes:
            parts.append(current.strip())
            current = ""
        else:
            current += char
    
    if current.strip():
        parts.append(current.strip())
    
    return parts

def find_matching_brace(text, open_pos):
    """Encuentra la llave de cierre correspondiente"""
    count = 0
    for i in range(open_pos, len(text)):
        if text[i] == '{':
            count += 1
        elif text[i] == '}':
            count -= 1
            if count == 0:
                return i
    return len(text) - 1

def find_matching_paren(text, open_pos):
    """Encuentra el paréntesis de cierre correspondiente"""
    count = 0
    for i in range(open_pos, len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
            if count == 0:
                return i
    return len(text) - 1
    
def validMethodName( _name, type_table, output, tk):
    #Revizar que el nombre que se quiera usar no sea una palabra restringida
    for element in type_table[0]:
        if(element==_name):
            output.insert(tk.END, f'Un identificador no puede ser una palabra restringida. \n')
            return False
    #Revizar que el nombre que se quiera usar no sea un nombre ya utilizado
    for element in type_table[1]:
        if(element[0]==_name):
            output.insert(tk.END, f'Un mismo identificador esta siendo usado multiples veces. \n')
            return False
    return True

def validMethodType(type, type_table):
    print("type",type)
    if not type.strip():
        return True
    for element in type_table[2]:
        if element == type:
            return True
    return False

def findBraces(_internal_not_function_braces, content):
    open_braces = []
    for idx, char in enumerate(content):
        if(char == '{'):
            open_braces.append(idx)
        elif(char == '}'):
            _internal_not_function_braces.append([open_braces.pop(),idx])
    return