# Manual de Usuario - Lenguaje Lyra

## Introducción
Lyra es un lenguaje de programación diseñado para hablantes de español, con sintaxis clara e intuitiva.

## Instalación y Uso
1. Ejecutar `main.py` para abrir el editor de Lyra
2. Escribir código en el área de texto izquierda
3. Hacer clic en **COMPILAR** para verificar el código
4. Hacer clic en **EJECUTAR** para ejecutar el programa

## Sintaxis Básica

### Función Principal
Todo programa en Lyra debe tener una función `principal()`:
```lyra
funcion principal(){
    imprimir("¡Hola Mundo!");
}
```

### Declaración de Variables
```lyra
entero edad = 25;
flotante precio = 19.99;
booleano activo = verdadero;
caracter letra = 'A';
texto nombre = "Juan";
```

### Tipos de Datos Simples
1. **entero**: Números enteros (ej: 1, -5, 100)
2. **flotante**: Números decimales (ej: 3.14, -0.5)
3. **booleano**: verdadero o falso
4. **caracter**: Un solo carácter entre comillas simples (ej: 'A')
5. **texto**: Cadena de texto entre comillas dobles (ej: "Hola")
6. **nulo**: Valor nulo

### Operadores Aritméticos
- `+` : Suma
- `-` : Resta
- `*` : Multiplicación
- `/` : División
- `%` : Módulo (residuo)

### Operadores de Comparación
- `==` : Igual a
- `!=` : Diferente de
- `<` : Menor que
- `>` : Mayor que
- `<=` : Menor o igual que
- `>=` : Mayor o igual que

### Operadores Lógicos
- `yy` : AND (y)
- `oo` : OR (o)
- `no` : NOT (negación)

### Entrada y Salida

#### Imprimir (Salida)
```lyra
imprimir("Texto", variable, "más texto");
```

#### Leer (Entrada)
```lyra
texto nombre = leer;
entero edad = leer;
```

### Condicionales

#### Si (If)
```lyra
si (condicion){
    // código si es verdadero
}
```

#### Si-Sino (If-Else)
```lyra
si (edad >= 18){
    imprimir("Mayor de edad");
}
sino {
    imprimir("Menor de edad");
}
```

#### Si-SinoSi-Sino (If-ElseIf-Else)
```lyra
si (nota >= 90){
    imprimir("Excelente");
}
sinosi (nota >= 70){
    imprimir("Bueno");
}
sino {
    imprimir("Regular");
}
```

### Switch (Cuando)
```lyra
cuando (variable){
    caso 1:
        imprimir("Opción 1");
        terminar;
    caso 2:
        imprimir("Opción 2");
        terminar;
    defecto:
        imprimir("Opción por defecto");
        terminar;
}
```

### Bucles

#### Mientras (While)
```lyra
entero contador = 0;
mientras(contador < 10){
    imprimir(contador);
    contador = contador + 1;
}
```

#### Para (For)
```lyra
para(entero i = 0; i < 10; i = i + 1){
    imprimir("Iteración:", i);
}
```

### Funciones

#### Función con Retorno
```lyra
funcion suma(entero a, entero b):entero{
    entero resultado = a + b;
    retornar resultado;
}
```

#### Función Sin Retorno
```lyra
funcion saludar(texto nombre){
    imprimir("¡Hola,", nombre, "!");
}
```

#### Llamada a Función
```lyra
entero resultado = suma(5, 3);
saludar("María");
```

## Reglas Importantes

1. **Punto y coma**: Todas las instrucciones terminan con `;`
2. **Llaves**: Las funciones y estructuras de control usan `{ }` para delimitar bloques
3. **Función principal**: Todo programa debe tener `funcion principal()`
4. **Palabras reservadas**: No se pueden usar como nombres de variables o funciones:
   - funcion, si, sino, sinosi, cuando, caso, terminar
   - mientras, para, verdadero, falso, yy, oo, no
   - retornar, imprimir, leer
5. **Tipos estrictos**: Las variables no pueden cambiar de tipo
6. **Nombres de variables**: Deben empezar con letra, sin caracteres especiales
7. **Mayúsculas y minúsculas**: Las palabras reservadas son en minúsculas

## Ejemplos Completos

### Calculadora Simple
```lyra
funcion sumar(entero a, entero b):entero{
    retornar a + b;
}

funcion restar(entero a, entero b):entero{
    retornar a - b;
}

funcion principal(){
    entero x = 10;
    entero y = 5;
    
    entero suma = sumar(x, y);
    entero resta = restar(x, y);
    
    imprimir("Suma:", suma);
    imprimir("Resta:", resta);
}
```

### Factorial
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
    imprimir("Factorial de", numero, "es:", fact);
}
```

### Números Pares
```lyra
funcion esPar(entero numero):booleano{
    entero residuo = numero % 2;
    si (residuo == 0){
        retornar verdadero;
    }
    retornar falso;
}

funcion principal(){
    imprimir("Números pares del 1 al 10:");
    para(entero i = 1; i <= 10; i = i + 1){
        si (esPar(i)){
            imprimir(i);
        }
    }
}
```

## Mensajes de Error Comunes

1. **"Llaves desbalanceadas"**: Verificar que cada `{` tenga su correspondiente `}`
2. **"No se encontró la función 'principal'"**: Falta definir `funcion principal()`
3. **"Un identificador no puede ser una palabra restringida"**: No usar palabras reservadas como nombres
4. **"Variable no definida"**: Declarar la variable antes de usarla
5. **"División por cero"**: Verificar que el divisor no sea 0
6. **"Función no encontrada"**: Verificar el nombre de la función llamada

## Mejores Prácticas

1. **Nombres descriptivos**: Usar nombres claros para variables y funciones
2. **Comentarios**: Aunque no estén implementados, documentar el código
3. **Indentación**: Mantener código ordenado con sangría consistente
4. **Funciones pequeñas**: Dividir código complejo en funciones más simples
5. **Validación**: Verificar condiciones antes de operaciones críticas (ej: división)

## Limitaciones Actuales

- No soporta arreglos ni listas (en desarrollo)
- No soporta comentarios (en desarrollo)
- Límite de 10,000 iteraciones en bucles (prevención de bucles infinitos)
- Sin soporte para recursión profunda

## Contacto y Soporte

Para reportar errores o sugerencias, contactar al equipo de desarrollo.

---
**Lyra** - Programación en Español 🎵
Versión 1.0 - 2025
