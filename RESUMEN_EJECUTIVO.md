# Lyra - Lenguaje de Programación en Español

## Resumen Ejecutivo

**Lyra** es un lenguaje de programación diseñado específicamente para hispanohablantes, con sintaxis intuitiva y clara que facilita el aprendizaje de conceptos de programación sin la barrera del idioma inglés.

## Características Principales

### 🎯 Sintaxis en Español
- Palabras reservadas completamente en español
- Sintaxis clara y fácil de leer
- Diseñado para principiantes hispanohablantes

### 🔧 Características del Lenguaje

#### Tipos de Datos
- **Simples** (6): entero, flotante, booleano, caracter, texto, nulo
- **Compuestos** (en desarrollo): arreglos, listas

#### Operadores
- **Aritméticos**: +, -, *, /, %
- **Lógicos**: yy (and), oo (or), no (not)
- **Comparación**: ==, !=, <, >, <=, >=

#### Estructuras de Control
- **Condicionales**: si, sinosi, sino
- **Switch**: cuando-caso-defecto
- **Bucles**: mientras, para

#### Funciones
- Con y sin retorno
- Parámetros tipados
- Función principal obligatoria

### 💻 Entorno de Desarrollo

#### Interfaz Gráfica
- **Editor de código**: Área amplia para escribir programas
- **Consola de salida**: Muestra resultados y errores
- **Botones**: COMPILAR y EJECUTAR
- **Menú**: Opciones y ayuda

#### Compilador
- Análisis léxico, sintáctico y semántico
- Generación de AST (Abstract Syntax Tree)
- Detección de errores con mensajes claros
- Validación de tipos y nombres

#### Intérprete
- Ejecución directa del código compilado
- Gestión de variables (contextos local y global)
- Entrada/Salida interactiva
- Protección contra bucles infinitos
- Manejo robusto de errores

## Ejemplo de Código

```lyra
funcion factorial(entero n):entero{
    si (n <= 1){
        retornar 1;
    }
    entero resultado = 1;
    entero i = 2;
    mientras(i <= n){
        resultado = resultado * i;
        i = i + 1;
    }
    retornar resultado;
}

funcion principal(){
    entero numero = 5;
    entero fact = factorial(numero);
    imprimir("El factorial de", numero, "es:", fact);
}
```

**Salida**:
```
El factorial de 5 es: 120
```

## Arquitectura del Sistema

```
┌─────────────────────────────────────────┐
│           main.py (GUI)                 │
│  ┌────────────┐      ┌──────────────┐  │
│  │   Editor   │      │    Output    │  │
│  └────────────┘      └──────────────┘  │
│  [COMPILAR]  [EJECUTAR]                │
└─────────────────────────────────────────┘
            ↓                    ↓
    ┌──────────────┐    ┌──────────────┐
    │  compile.py  │    │  execute.py  │
    │  (Compiler)  │    │ (Interpreter)│
    └──────────────┘    └──────────────┘
            ↓                    ↓
    ┌──────────────┐    ┌──────────────┐
    │     AST      │ →  │  Execution   │
    │ (Structures) │    │   Engine     │
    └──────────────┘    └──────────────┘
```

## Flujo de Trabajo

1. **Escritura**: El usuario escribe código en Lyra
2. **Compilación**: Se verifica sintaxis y se genera AST
3. **Ejecución**: Se interpreta el AST y se ejecuta
4. **Salida**: Resultados mostrados en consola

## Ventajas de Lyra

### Para Estudiantes
- ✅ **Sin barrera idiomática**: Todo en español
- ✅ **Sintaxis clara**: Fácil de leer y entender
- ✅ **Mensajes de error comprensibles**: En español, con contexto
- ✅ **Curva de aprendizaje suave**: Ideal para principiantes

### Para Educadores
- ✅ **Enfoque en conceptos**: No en traducción de sintaxis
- ✅ **Ejemplos en contexto cultural**: Nombres y ejemplos familiares
- ✅ **Herramienta de enseñanza**: IDE integrado
- ✅ **Documentación completa**: Manuales y ejemplos

### Técnicas
- ✅ **Arquitectura modular**: Fácil de extender
- ✅ **Código limpio**: Bien documentado
- ✅ **Manejo de errores robusto**: No crashes inesperados
- ✅ **Protecciones de seguridad**: Límites de iteración

## Casos de Uso

### 1. Educación
- Introducción a la programación
- Cursos de lógica de programación
- Talleres para principiantes

### 2. Práctica
- Ejercicios de algoritmos
- Resolución de problemas
- Preparación para otros lenguajes

### 3. Prototipado
- Prueba rápida de algoritmos
- Validación de lógica
- Diseño de flujos de control

## Comparación con Otros Lenguajes

| Característica | Lyra | Python | JavaScript |
|---------------|------|--------|------------|
| Idioma | Español | Inglés | Inglés |
| Tipado | Estático | Dinámico | Dinámico |
| Sintaxis | Clara | Clara | Compleja |
| Curva Aprendizaje | Baja | Media | Media-Alta |
| Target | Educación | General | Web |

## Impacto Esperado

### Comunidad Hispanohablante
- Reducir abandono en aprendizaje de programación
- Aumentar inclusión en tecnología
- Facilitar comprensión de conceptos fundamentales

### Sector Educativo
- Herramienta pedagógica efectiva
- Material didáctico en español
- Resultados de aprendizaje mejorados

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **GUI**: Tkinter
- **Paradigma**: Orientado a objetos e imperativo
- **Arquitectura**: Compilador + Intérprete

## Métricas del Proyecto

- **Líneas de código**: ~2,500+
- **Módulos**: 5 principales
- **Palabras reservadas**: 17
- **Tipos de datos**: 6 simples
- **Estructuras de control**: 6
- **Operadores**: 15+
- **Ejemplos de código**: 15+
- **Documentos**: 5 (Manual, Técnico, Ejemplos, Estado, Este)

## Equipo de Desarrollo

**Desarrolladores**:
- Morales Román Joselyn
- Salazar Navarro Kendall

**Institución**:
Universidad Nacional de Costa Rica
Sede Regional Brunca - Campus Pérez Zeledón

**Curso**:
Paradigmas de Programación - NRC 50262 - Grupo 84

**Profesor**:
Msc. Josías Ariel Chaves Murillo

**Fecha**:
II Ciclo 2025 - Noviembre 2025

## Conclusión

Lyra representa un paso importante en la democratización del aprendizaje de programación para la comunidad hispanohablante. Al eliminar la barrera del idioma inglés, permite que los estudiantes se enfoquen en comprender los conceptos fundamentales de la programación, facilitando así su entrada al mundo del desarrollo de software.

El proyecto cumple con los objetivos establecidos de crear un lenguaje funcional con sintaxis en español, un compilador robusto, un intérprete efectivo, y una interfaz gráfica amigable para el usuario.

## Recursos Adicionales

### Documentación
- `MANUAL_USUARIO.md` - Guía completa para usuarios
- `DOCUMENTACION_TECNICA.md` - Documentación para desarrolladores
- `ejemplos_lyra.md` - 15 ejemplos de código
- `ESTADO_PROYECTO.md` - Estado actual del proyecto
- `readme.md` - Estructura de datos del compilador

### Archivos del Sistema
- `main.py` - Interfaz gráfica
- `compile.py` - Compilador
- `execute.py` - Intérprete
- `user_input.py` - Gestión de entrada
- `compiler/functions.py` - Utilidades del compilador

### Ejemplos Incluidos
15 ejemplos completos desde "Hola Mundo" hasta algoritmos como Fibonacci y Factorial.

---

**Lyra** 🎵 - Programación en Español
*"Haciendo la programación accesible para todos los hispanohablantes"*

© 2025 - Universidad Nacional de Costa Rica
