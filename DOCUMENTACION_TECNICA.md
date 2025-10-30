# Documentación Técnica - Compilador e Intérprete Lyra

## Arquitectura del Sistema

El sistema está compuesto por 5 módulos principales:

### 1. `main.py` - Interfaz Gráfica
- **Responsabilidad**: Interfaz de usuario con Tkinter
- **Componentes**:
  - Editor de código (`ScrolledText`)
  - Área de salida/consola (`Text`)
  - Botones de compilación y ejecución
  - Menú de opciones

### 2. `compile.py` - Compilador
- **Responsabilidad**: Análisis léxico, sintáctico y semántico
- **Fases de Compilación**:
  1. **Verificación de llaves**: Balance de `{` y `}`
  2. **Detección de funciones**: Identifica declaraciones de funciones
  3. **Validación de nombres**: Verifica palabras reservadas
  4. **Análisis de parámetros**: Valida tipos y nombres
  5. **Parseo de contenido**: Convierte a AST (Abstract Syntax Tree)
  6. **Verificación semántica**: Busca función `principal()`

#### Funciones Principales de `compile.py`

##### `fillTypeTable()`
Retorna la tabla de tipos con:
- `[0]`: Palabras reservadas
- `[1]`: Funciones declaradas
- `[2]`: Tipos de datos

##### `compileCode(output, code_area, tk)`
Función principal de compilación. Proceso:
1. Obtiene código del área de texto
2. Verifica balance de llaves
3. Identifica funciones y sus límites
4. Valida nombres y tipos
5. Parsea parámetros
6. Procesa contenido de funciones
7. Verifica función `principal()`
8. Almacena en `compiled_functions`

##### `parse_function_content(divided_function_content, element, type_table)`
Convierte el contenido textual de una función en estructuras de datos ejecutables.

##### `parse_instruction(section, type_table, function_name)`
Identifica y parsea cada tipo de instrucción:
- Declaración de variables
- Asignaciones
- Imprimir/Leer
- Condicionales (if/else)
- Bucles (while/for)
- Switch
- Llamadas a funciones

##### Funciones de Parseo Específicas
- `parse_variable_declaration()`: Parsea declaraciones de variables
- `parse_assignment()`: Parsea asignaciones
- `parse_print_statement()`: Parsea instrucciones de impresión
- `parse_read_statement()`: Parsea instrucciones de lectura
- `parse_if_statement()`: Parsea condicionales if
- `parse_while_statement()`: Parsea bucles while
- `parse_for_statement()`: Parsea bucles for
- `parse_switch_statement()`: Parsea estructuras switch
- `parse_function_call()`: Parsea llamadas a funciones
- `parse_expression()`: Parsea expresiones (literales, variables, operaciones)

#### Estructura de Datos: Función Compilada

```python
element = [
    "cabecera completa",           # [0] Header text
    "nombre_funcion",              # [1] Function name
    [["tipo", "nombre"], ...],     # [2] Parameters
    posicion_inicio,               # [3] Start position of body
    posicion_fin,                  # [4] End position of body
    "tipo_retorno",                # [5] Return type
    [instrucciones_parseadas]      # [6] Parsed instructions (AST)
]
```

### 3. `execute.py` - Intérprete
- **Responsabilidad**: Ejecución del código compilado
- **Variables Globales**:
  - `global_variables`: Diccionario de variables globales
  - `execution_output`: Referencia al widget de salida
  - `execution_tk`: Referencia a Tkinter

#### Funciones Principales de `execute.py`

##### `executeCode(output, code_area, tk)`
Función principal de ejecución:
1. Verifica que existe código compilado
2. Busca función `principal()`
3. Ejecuta función principal
4. Maneja errores de ejecución

##### `execute_function(func, arguments)`
Ejecuta una función con sus argumentos:
- Crea contexto local de variables
- Asigna parámetros
- Ejecuta instrucciones secuencialmente
- Retorna valor si hay instrucción `return`

##### `execute_instruction(instruction, local_variables)`
Dispatcher que ejecuta cada tipo de instrucción según su `type`:
- `variable_declaration`
- `assignment`
- `print`
- `read`
- `return`
- `if` / `elseif` / `else`
- `switch`
- `while` / `for`
- `function_call`

##### Funciones de Ejecución Específicas
- `execute_variable_declaration()`: Crea y asigna variables
- `execute_assignment()`: Modifica valor de variables
- `execute_print()`: Muestra salida en consola
- `execute_read()`: Captura entrada del usuario
- `execute_if()`: Ejecuta bloques condicionales
- `execute_switch()`: Ejecuta switch-case
- `execute_while()`: Ejecuta bucles while con límite de iteraciones
- `execute_for()`: Ejecuta bucles for con límite de iteraciones
- `execute_function_call()`: Ejecuta funciones definidas por el usuario

##### `evaluate_expression(expr, local_variables)`
Evalúa expresiones recursivamente:
- Literales (string, int, float, bool, char, null)
- Variables (busca en contexto local y global)
- Operaciones (aritméticas, lógicas, comparación)
- Llamadas a funciones

##### `evaluate_operation(expr, local_variables)`
Evalúa operaciones binarias y unarias:
- Aritméticas: `+`, `-`, `*`, `/`, `%`
- Comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Lógicas: `yy` (and), `oo` (or), `no` (not)

### 4. `user_input.py` - Gestión de Entrada
- **Responsabilidad**: Captura de entrada del usuario en el área de salida
- **Funciones**:
  - `get_user_input(output, tk)`: Captura entrada del usuario
  - `block_output(output, tk)`: Bloquea entrada después de capturar

### 5. `compiler/functions.py` - Utilidades del Compilador
- **Responsabilidad**: Funciones auxiliares para análisis de código
- **Funciones**:
  - `extract_functions()`: Extrae funciones con regex
  - `parse_parameters()`: Parsea parámetros de funciones
  - `extract_function_body()`: Extrae contenido entre llaves
  - `analyze_functions()`: Analiza código y retorna resumen

## Flujo de Datos

```
[Usuario escribe código]
         ↓
[Presiona COMPILAR]
         ↓
[compileCode()] → Análisis léxico/sintáctico
         ↓
[parse_function_content()] → Construcción del AST
         ↓
[compiled_functions] ← Almacena funciones compiladas
         ↓
[Usuario presiona EJECUTAR]
         ↓
[executeCode()] → Busca función principal
         ↓
[execute_function()] → Ejecuta instrucciones
         ↓
[evaluate_expression()] → Evalúa expresiones
         ↓
[Salida en consola]
```

## Estructura del AST (Abstract Syntax Tree)

### Instrucciones

Cada instrucción es un diccionario con clave `type` que indica su naturaleza:

#### Variable Declaration
```python
{
    "type": "variable_declaration",
    "var_type": "entero|flotante|...",
    "var_name": "nombre",
    "value": <expresión>
}
```

#### Assignment
```python
{
    "type": "assignment",
    "var_name": "nombre",
    "value": <expresión>
}
```

#### Print
```python
{
    "type": "print",
    "content": [<expr1>, <expr2>, ...]
}
```

#### Condicionales
```python
{
    "type": "if|elseif",
    "condition": <expresión>,
    "body": [<instrucción>, ...]
}
```

#### Bucles
```python
{
    "type": "while",
    "condition": <expresión>,
    "body": [<instrucción>, ...]
}

{
    "type": "for",
    "init": <instrucción>,
    "condition": <expresión>,
    "increment": <expresión>,
    "body": [<instrucción>, ...]
}
```

### Expresiones

Cada expresión tiene clave `expr_type`:

#### Literales
```python
{"expr_type": "string_literal", "value": "texto"}
{"expr_type": "int_literal", "value": 123}
{"expr_type": "float_literal", "value": 3.14}
{"expr_type": "bool_literal", "value": True}
{"expr_type": "char_literal", "value": "A"}
{"expr_type": "null_literal", "value": None}
```

#### Variables
```python
{"expr_type": "variable", "name": "nombre_var"}
```

#### Operaciones
```python
{
    "expr_type": "operation",
    "operator": "+|-|*|/|==|!=|...",
    "left": <expresión>,
    "right": <expresión>
}
```

## Gestión de Variables

### Contextos
1. **Local**: Variables dentro de una función (diccionario `local_variables`)
2. **Global**: Variables compartidas entre funciones (diccionario `global_variables`)

### Búsqueda de Variables
Al evaluar una variable:
1. Busca en contexto local
2. Si no existe, busca en contexto global
3. Si no existe, lanza error

## Limitaciones y Protecciones

### Bucles Infinitos
- Límite de 10,000 iteraciones por bucle
- Lanza excepción si se excede

### División por Cero
- Verifica divisor antes de dividir
- Lanza excepción si es cero

### Variables No Definidas
- Verifica existencia antes de usar
- Lanza excepción con nombre de variable

## Validaciones Semánticas

Durante compilación:
1. **Balance de llaves**: Verifica que cada `{` tenga su `}`
2. **Palabras reservadas**: No permite usar palabras reservadas como identificadores
3. **Tipos válidos**: Verifica que los tipos de retorno y parámetros sean válidos
4. **Parámetros duplicados**: No permite parámetros con mismo nombre
5. **Función principal**: Verifica existencia de `funcion principal()`

## Extensibilidad

### Agregar Nuevo Tipo de Instrucción

1. **Compilador** (`compile.py`):
   - Agregar caso en `parse_instruction()`
   - Crear función `parse_nueva_instruccion()`
   - Definir estructura de datos

2. **Intérprete** (`execute.py`):
   - Agregar caso en `execute_instruction()`
   - Crear función `execute_nueva_instruccion()`

### Agregar Nuevo Operador

1. **Compilador** (`compile.py`):
   - Agregar operador en lista de `parse_expression()`

2. **Intérprete** (`execute.py`):
   - Agregar caso en `evaluate_operation()`

### Agregar Nuevo Tipo de Dato

1. Agregar tipo a `fillTypeTable()[2]`
2. Definir valor por defecto en `execute_variable_declaration()`
3. Implementar conversiones si es necesario

## Manejo de Errores

### Errores de Compilación
- Mostrados en área de salida con prefijo "Error:"
- Detienen la compilación
- No se genera código ejecutable

### Errores de Ejecución
- Capturados por try-except en `executeCode()`
- Mostrados en área de salida
- Detienen la ejecución

## Testing

### Casos de Prueba Recomendados

1. **Sintaxis básica**:
   - Declaración de variables
   - Asignaciones
   - Operaciones aritméticas

2. **Estructuras de control**:
   - If/else simples y anidados
   - Switch con múltiples casos
   - Bucles while y for

3. **Funciones**:
   - Con y sin retorno
   - Con y sin parámetros
   - Recursivas (con cuidado del límite)

4. **Errores**:
   - Llaves desbalanceadas
   - Variables no definidas
   - División por cero
   - Tipos incorrectos

## Optimizaciones Futuras

1. **Tabla de símbolos**: Implementar tabla de símbolos completa
2. **Type checking**: Verificación de tipos en compilación
3. **Optimización de AST**: Reducción de nodos redundantes
4. **Compilación a bytecode**: Generar código intermedio
5. **JIT compilation**: Compilación just-in-time para mejor rendimiento

## Contribuciones

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear rama con feature
3. Implementar cambios con pruebas
4. Actualizar documentación
5. Pull request con descripción detallada

---
**Lyra Compiler & Interpreter**
Desarrollado para el curso de Paradigmas de Programación
Universidad Nacional de Costa Rica - 2025
