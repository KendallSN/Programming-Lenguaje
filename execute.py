from user_input import get_user_input, block_output
import compile as compile_module

# Variables globales para la ejecución
global_variables = {}
execution_output = None
execution_tk = None

def executeCode(output, code_area, tk):
    """Ejecuta el código compilado"""
    global execution_output, execution_tk, global_variables
    execution_output = output
    execution_tk = tk
    global_variables = {}
    
    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END)
    
    # Verificar que hay código compilado
    compiled_functions = compile_module.compiled_functions
    if not compiled_functions or len(compiled_functions) == 0:
        output.insert(tk.END, "Error: Debe compilar el código antes de ejecutarlo.\n")
        return
    
    # Buscar la función principal
    principal_func = None
    for func in compiled_functions:
        if func[1] == "principal":
            principal_func = func
            break
    
    if not principal_func:
        output.insert(tk.END, "Error: No se encontró la función 'principal'.\n")
        return
    
    output.insert(tk.END, "=== EJECUTANDO PROGRAMA ===\n\n")
    
    try:
        # Ejecutar la función principal
        execute_function(principal_func, [])
        output.insert(tk.END, "\n\n=== EJECUCIÓN COMPLETADA ===\n")
    except Exception as e:
        output.insert(tk.END, f"\n\nError de ejecución: {str(e)}\n")
    
    block_output(output, tk)

def execute_function(func, arguments):
    """Ejecuta una función con los argumentos dados"""
    function_name = func[1]
    parameters = func[2]  # [[tipo, nombre], ...]
    instructions = func[6]  # Lista de instrucciones parseadas
    
    # Crear contexto local para la función
    local_variables = {}
    
    # Asignar parámetros
    for i, param in enumerate(parameters):
        if i < len(arguments):
            local_variables[param[1]] = arguments[i]
    
    # Ejecutar instrucciones
    for instruction in instructions:
        result = execute_instruction(instruction, local_variables)
        if result and result.get('type') == 'return':
            return result.get('value')
    
    return None

def execute_instruction(instruction, local_variables):
    """Ejecuta una instrucción individual"""
    if not instruction:
        return None
    
    inst_type = instruction.get('type')
    
    if inst_type == 'variable_declaration':
        return execute_variable_declaration(instruction, local_variables)
    
    elif inst_type == 'assignment':
        return execute_assignment(instruction, local_variables)
    
    elif inst_type == 'print':
        return execute_print(instruction, local_variables)
    
    elif inst_type == 'read':
        return execute_read(instruction, local_variables)
    
    elif inst_type == 'return':
        value = evaluate_expression(instruction['value'], local_variables) if instruction['value'] else None
        return {'type': 'return', 'value': value}
    
    elif inst_type == 'if':
        return execute_if(instruction, local_variables)
    
    elif inst_type == 'elseif':
        return execute_if(instruction, local_variables)
    
    elif inst_type == 'else':
        return execute_else(instruction, local_variables)
    
    elif inst_type == 'switch':
        return execute_switch(instruction, local_variables)
    
    elif inst_type == 'while':
        return execute_while(instruction, local_variables)
    
    elif inst_type == 'for':
        return execute_for(instruction, local_variables)
    
    elif inst_type == 'function_call':
        return execute_function_call(instruction, local_variables)
    
    return None

def execute_variable_declaration(instruction, local_variables):
    """Ejecuta una declaración de variable"""
    var_name = instruction['var_name']
    var_type = instruction['var_type']
    value = instruction['value']
    
    if value:
        evaluated_value = evaluate_expression(value, local_variables)
    else:
        # Valor por defecto según tipo
        if var_type == 'entero':
            evaluated_value = 0
        elif var_type == 'flotante':
            evaluated_value = 0.0
        elif var_type == 'booleano':
            evaluated_value = False
        elif var_type == 'caracter':
            evaluated_value = ''
        elif var_type == 'texto':
            evaluated_value = ''
        else:
            evaluated_value = None
    
    local_variables[var_name] = evaluated_value
    return None

def execute_assignment(instruction, local_variables):
    """Ejecuta una asignación"""
    var_name = instruction['var_name']
    value = evaluate_expression(instruction['value'], local_variables)
    
    # Buscar la variable en local o global
    if var_name in local_variables:
        local_variables[var_name] = value
    else:
        global_variables[var_name] = value
    
    return None

def execute_print(instruction, local_variables):
    """Ejecuta imprimir"""
    global execution_output, execution_tk
    
    output_text = ""
    for expr in instruction['content']:
        value = evaluate_expression(expr, local_variables)
        if value is not None:
            output_text += str(value) + " "
    
    execution_output.insert(execution_tk.END, output_text.strip() + "\n")
    execution_output.see(execution_tk.END)
    execution_output.update()
    return None

def execute_read(instruction, local_variables):
    """Ejecuta leer (entrada del usuario)"""
    global execution_output, execution_tk
    
    var_name = instruction['var_name']
    var_type = instruction.get('var_type')
    
    execution_output.insert(execution_tk.END, ">> ")
    execution_output.see(execution_tk.END)
    execution_output.update()
    
    # Obtener entrada del usuario
    user_input = get_user_input(execution_output, execution_tk)
    
    # Convertir según el tipo de variable
    converted_value = user_input if user_input else ""
    
    if var_type == "entero":
        try:
            converted_value = int(user_input)
        except (ValueError, TypeError):
            converted_value = 0
    elif var_type == "flotante":
        try:
            converted_value = float(user_input)
        except (ValueError, TypeError):
            converted_value = 0.0
    elif var_type == "booleano":
        converted_value = user_input.lower() in ["verdadero", "true", "1", "si"]
    elif var_type == "caracter":
        converted_value = user_input[0] if user_input else ''
    # Para "texto" o None, dejar como string
    
    # Guardar en la variable
    local_variables[var_name] = converted_value
    
    return None

def execute_if(instruction, local_variables):
    """Ejecuta una estructura if"""
    condition = evaluate_expression(instruction['condition'], local_variables)
    
    if condition:
        for inst in instruction['body']:
            result = execute_instruction(inst, local_variables)
            if result and result.get('type') == 'return':
                return result
    
    return None

def execute_else(instruction, local_variables):
    """Ejecuta una estructura else"""
    for inst in instruction['body']:
        result = execute_instruction(inst, local_variables)
        if result and result.get('type') == 'return':
            return result
    
    return None

def execute_switch(instruction, local_variables):
    """Ejecuta una estructura switch"""
    switch_value = evaluate_expression({'expr_type': 'variable', 'name': instruction['variable']}, local_variables)
    
    for case in instruction['cases']:
        if case['value'] == 'default':
            # Ejecutar caso default
            for inst in case['instructions']:
                result = execute_instruction(inst, local_variables)
                if result and result.get('type') == 'return':
                    return result
            break
        else:
            case_value = evaluate_expression(case['value'], local_variables)
            if switch_value == case_value:
                # Ejecutar este caso
                for inst in case['instructions']:
                    result = execute_instruction(inst, local_variables)
                    if result and result.get('type') == 'return':
                        return result
                break
    
    return None

def execute_while(instruction, local_variables):
    """Ejecuta un bucle while"""
    max_iterations = 10000  # Prevenir bucles infinitos
    iterations = 0
    
    while iterations < max_iterations:
        condition = evaluate_expression(instruction['condition'], local_variables)
        if not condition:
            break
        
        for inst in instruction['body']:
            result = execute_instruction(inst, local_variables)
            if result and result.get('type') == 'return':
                return result
        
        iterations += 1
    
    if iterations >= max_iterations:
        raise Exception("Bucle while excedió el límite de iteraciones")
    
    return None

def execute_for(instruction, local_variables):
    """Ejecuta un bucle for"""
    # Inicialización
    if instruction['init']:
        execute_instruction(instruction['init'], local_variables)
    
    max_iterations = 10000
    iterations = 0
    
    while iterations < max_iterations:
        # Verificar condición
        condition = evaluate_expression(instruction['condition'], local_variables)
        if not condition:
            break
        
        # Ejecutar cuerpo
        for inst in instruction['body']:
            result = execute_instruction(inst, local_variables)
            if result and result.get('type') == 'return':
                return result
        
        # Incremento - puede ser una instrucción (asignación) o expresión
        increment = instruction.get('increment')
        if increment:
            if isinstance(increment, dict) and increment.get('type') == 'assignment':
                execute_instruction(increment, local_variables)
            else:
                evaluate_expression(increment, local_variables)
        
        iterations += 1
    
    if iterations >= max_iterations:
        raise Exception("Bucle for excedió el límite de iteraciones")
    
    return None

def execute_function_call(instruction, local_variables):
    """Ejecuta una llamada a función"""
    func_name = instruction['function_name']
    params = instruction['parameters']
    
    # Evaluar parámetros
    evaluated_params = []
    for param in params:
        evaluated_params.append(evaluate_expression(param, local_variables))
    
    # Verificar si es una función built-in (como imprimir)
    if func_name == "imprimir":
        # Ejecutar imprimir directamente
        global execution_output, execution_tk
        output_text = ""
        for value in evaluated_params:
            if value is not None:
                output_text += str(value) + " "
        execution_output.insert(execution_tk.END, output_text.strip() + "\n")
        execution_output.see(execution_tk.END)
        execution_output.update()
        return None
    
    # Buscar la función definida por el usuario
    compiled_functions = compile_module.compiled_functions
    for func in compiled_functions:
        if func[1] == func_name:
            return execute_function(func, evaluated_params)
    
    raise Exception(f"Función '{func_name}' no encontrada")

def evaluate_expression(expr, local_variables):
    """Evalúa una expresión y retorna su valor"""
    if not expr:
        return None
    
    expr_type = expr.get('expr_type')
    
    if expr_type == 'string_literal':
        return expr['value']
    
    elif expr_type == 'char_literal':
        return expr['value']
    
    elif expr_type == 'int_literal':
        return expr['value']
    
    elif expr_type == 'float_literal':
        return expr['value']
    
    elif expr_type == 'bool_literal':
        return expr['value']
    
    elif expr_type == 'null_literal':
        return None
    
    elif expr_type == 'variable':
        var_name = expr['name']
        if var_name in local_variables:
            return local_variables[var_name]
        elif var_name in global_variables:
            return global_variables[var_name]
        else:
            raise Exception(f"Variable '{var_name}' no definida")
    
    elif expr_type == 'operation':
        return evaluate_operation(expr, local_variables)
    
    elif expr_type == 'empty':
        return None
    
    # Si es una llamada a función
    elif expr.get('type') == 'function_call':
        return execute_function_call(expr, local_variables)
    
    return None

def evaluate_operation(expr, local_variables):
    """Evalúa una operación (aritmética o lógica)"""
    operator = expr['operator']
    
    # Operador unario NOT
    if operator == 'no':
        operand = evaluate_expression(expr['operand'], local_variables)
        return not operand
    
    # Operadores binarios
    left = evaluate_expression(expr['left'], local_variables)
    right = evaluate_expression(expr['right'], local_variables)
    
    # Operadores aritméticos
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        if right == 0:
            raise Exception("División por cero")
        return left / right
    elif operator == '%':
        return left % right
    
    # Operadores de comparación
    elif operator == '==':
        return left == right
    elif operator == '!=':
        return left != right
    elif operator == '<':
        return left < right
    elif operator == '>':
        return left > right
    elif operator == '<=':
        return left <= right
    elif operator == '>=':
        return left >= right
    
    # Operadores lógicos
    elif operator == 'yy':
        return left and right
    elif operator == 'oo':
        return left or right
    
    # Operadores de asignación compuesta
    elif operator == '+=':
        return left + right
    elif operator == '-=':
        return left - right
    elif operator == '*=':
        return left * right
    elif operator == '/=':
        if right == 0:
            raise Exception("División por cero")
        return left / right
    
    return None