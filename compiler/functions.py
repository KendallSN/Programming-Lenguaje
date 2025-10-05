import re

def extract_functions(code):
    """
    Extrae funciones con la estructura: funcion nombre(parametros):tipo{ contenido }
    Retorna una lista de diccionarios con la información de cada función
    """
    functions = []
    
    # Patrón regex para capturar: funcion nombre(parametros):tipo{
    # El tipo es opcional (puede estar vacío después de los :)
    pattern = r'funcion\s+(\w+)\s*\(([^)]*)\)\s*:\s*(\w*)\s*\{'
    
    matches = re.finditer(pattern, code)
    
    for match in matches:
        function_name = match.group(1)  # Nombre de la función
        parameters_str = match.group(2) if match.group(2) else ""  # Parámetros
        return_type = match.group(3) if match.group(3) else None  # Tipo de retorno
        start_pos = match.start()
        
        # Parsear parámetros (formato: tipo nombre, tipo nombre)
        parameters = parse_parameters(parameters_str)
        
        # Extraer contenido entre llaves
        content = extract_function_body(code, start_pos)
        
        function_info = {
            'name': function_name,
            'parameters': parameters,
            'return_type': return_type,
            'content': content,
            'declaration': match.group(0)
        }
        
        functions.append(function_info)
    
    return functions

def parse_parameters(parameters_str):
    """
    Parsea los parámetros en formato: tipo nombre, tipo nombre
    Retorna lista de diccionarios con 'type' y 'name'
    """
    parameters = []
    
    if not parameters_str.strip():
        return parameters
    
    # Dividir por comas si hay múltiples parámetros
    param_parts = [p.strip() for p in parameters_str.split(',')]
    
    for param_part in param_parts:
        if param_part:
            # Dividir cada parámetro en palabras
            words = param_part.split()
            if len(words) >= 2:
                param_type = words[0]
                param_name = words[1]
                parameters.append({
                    'type': param_type,
                    'name': param_name
                })
            elif len(words) == 1:
                # Solo hay un nombre sin tipo
                parameters.append({
                    'type': None,
                    'name': words[0]
                })
    
    return parameters

def extract_function_body(code, start_pos):
    """
    Extrae el contenido entre llaves de una función
    """
    # Buscar la primera llave de apertura desde start_pos
    brace_start = code.find('{', start_pos)
    if brace_start == -1:
        return ""
    
    # Contar llaves para encontrar la llave de cierre correspondiente
    brace_count = 0
    content_start = brace_start + 1
    
    for i in range(brace_start, len(code)):
        if code[i] == '{':
            brace_count += 1
        elif code[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                # Encontramos la llave de cierre
                return code[content_start:i].strip()
    
    # Si no se encontró la llave de cierre, tomar hasta el final
    return code[content_start:].strip()

def analyze_functions(code):

    """
    Analiza las funciones y retorna un resumen
    """
    functions = extract_functions(code)
    
    analysis = {
        'total_functions': len(functions),
        'functions': functions,
        'has_main': False,
        'main_function': None
    }
    
    # Buscar función main
    for func in functions:
        if func['name'] == 'main':
            analysis['has_main'] = True
            analysis['main_function'] = func
            break
    
    return analysis

#

def findFunctions(code):
    return null