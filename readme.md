
# Estructura de Datos del Compilador Lyra

## Estructura de Función (element)
- `element[0]` = Cabecera de la función (texto completo)
- `element[1]` = Nombre de la función
- `element[2]` = Parámetros [[tipo, nombre], ...]
- `element[3]` = Posición inicio del contenido { principal
- `element[4]` = Posición fin del contenido } principal
- `element[5]` = Tipo de retorno de la función ('' para sin tipo)
- `element[6]` = Lista de instrucciones parseadas (estructuras ejecutables)

## Estructura de Instrucciones

### Variable Declaration
```python
{
    "type": "variable_declaration",
    "var_type": "entero|flotante|booleano|caracter|texto",
    "var_name": "nombre",
    "value": <expresión>
}
```

### Assignment
```python
{
    "type": "assignment",
    "var_name": "nombre",
    "value": <expresión>
}
```

### Print
```python
{
    "type": "print",
    "content": [<expresión>, <expresión>, ...]
}
```

### Read
```python
{
    "type": "read",
    "var_type": "tipo" | None,
    "var_name": "nombre"
}
```

### Return
```python
{
    "type": "return",
    "value": <expresión>
}
```

### If
```python
{
    "type": "if",
    "condition": <expresión>,
    "body": [<instrucción>, ...]
}
```

### Else If
```python
{
    "type": "elseif",
    "condition": <expresión>,
    "body": [<instrucción>, ...]
}
```

### Else
```python
{
    "type": "else",
    "body": [<instrucción>, ...]
}
```

### Switch
```python
{
    "type": "switch",
    "variable": "nombre",
    "cases": [
        {
            "value": <expresión> | "default",
            "instructions": [<instrucción>, ...]
        }
    ]
}
```

### While
```python
{
    "type": "while",
    "condition": <expresión>,
    "body": [<instrucción>, ...]
}
```

### For
```python
{
    "type": "for",
    "init": <instrucción>,
    "condition": <expresión>,
    "increment": <expresión>,
    "body": [<instrucción>, ...]
}
```

### Function Call
```python
{
    "type": "function_call",
    "function_name": "nombre",
    "parameters": [<expresión>, ...]
}
```

## Estructura de Expresiones

### String Literal
```python
{
    "expr_type": "string_literal",
    "value": "texto"
}
```

### Character Literal
```python
{
    "expr_type": "char_literal",
    "value": "c"
}
```

### Integer Literal
```python
{
    "expr_type": "int_literal",
    "value": 123
}
```

### Float Literal
```python
{
    "expr_type": "float_literal",
    "value": 123.45
}
```

### Boolean Literal
```python
{
    "expr_type": "bool_literal",
    "value": True | False
}
```

### Null Literal
```python
{
    "expr_type": "null_literal",
    "value": None
}
```

### Variable
```python
{
    "expr_type": "variable",
    "name": "nombre"
}
```

### Operation (Binary)
```python
{
    "expr_type": "operation",
    "operator": "+|-|*|/|%|==|!=|<|>|<=|>=|yy|oo|+=|-=|*=|/=",
    "left": <expresión>,
    "right": <expresión>
}
```

### Operation (Unary - NOT)
```python
{
    "expr_type": "operation",
    "operator": "no",
    "operand": <expresión>
}
```

### Empty
```python
{
    "expr_type": "empty",
    "value": None
}
```

## Flujo de Compilación

1. **Análisis de llaves**: Verifica balanceo de llaves
2. **Detección de funciones**: Identifica todas las funciones
3. **Validación de nombres**: Verifica que no sean palabras reservadas
4. **Validación de tipos**: Verifica tipos de retorno y parámetros
5. **Parseo de parámetros**: Extrae y valida parámetros
6. **Parseo de contenido**: Convierte cada instrucción en estructura ejecutable
7. **Verificación de función principal**: Confirma existencia de `principal()`
8. **Almacenamiento**: Guarda en `compiled_functions` para ejecución

## Flujo de Ejecución

1. **Verificación de compilación**: Asegura que hay código compilado
2. **Búsqueda de principal**: Localiza función `principal()`
3. **Ejecución de función**: Procesa instrucciones secuencialmente
4. **Evaluación de expresiones**: Calcula valores de expresiones
5. **Gestión de variables**: Maneja contextos local y global
6. **Entrada/Salida**: Maneja `imprimir()` y `leer`
7. **Control de flujo**: Ejecuta if, while, for, switch
8. **Llamadas a funciones**: Ejecuta funciones definidas por el usuario 