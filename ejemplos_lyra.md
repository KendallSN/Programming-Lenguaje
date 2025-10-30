# Ejemplos de Código en Lyra

## Ejemplo 1: Hola Mundo
```lyra
funcion principal(){
    imprimir("¡Hola Mundo desde Lyra!");
}
```

## Ejemplo 2: Suma de dos números
```lyra
funcion suma(entero a, entero b):entero{
    entero resultado = a + b;
    retornar resultado;
}

funcion principal(){
    entero num1 = 10;
    entero num2 = 20;
    entero total = suma(num1, num2);
    imprimir("La suma es:", total);
}
```

## Ejemplo 3: Condicionales
```lyra
funcion esMayor(entero numero):texto{
    si (numero > 18){
        retornar "Es mayor de edad";
    }
    sino {
        retornar "Es menor de edad";
    }
}

funcion principal(){
    entero edad = 25;
    texto mensaje = esMayor(edad);
    imprimir(mensaje);
}
```

## Ejemplo 4: Bucle While
```lyra
funcion principal(){
    entero contador = 1;
    mientras(contador <= 5){
        imprimir("Contador:", contador);
        contador = contador + 1;
    }
}
```

## Ejemplo 5: Bucle For
```lyra
funcion principal(){
    para(entero i = 0; i < 10; i = i + 1){
        imprimir("Iteración:", i);
    }
}
```

## Ejemplo 6: Switch (Cuando)
```lyra
funcion obtenerDia(entero numero):texto{
    texto dia = "";
    cuando (numero){
        caso 1:
            dia = "Lunes";
            terminar;
        caso 2:
            dia = "Martes";
            terminar;
        caso 3:
            dia = "Miércoles";
            terminar;
        defecto:
            dia = "Día no válido";
            terminar;
    }
    retornar dia;
}

funcion principal(){
    entero numeroDia = 2;
    texto dia = obtenerDia(numeroDia);
    imprimir("El día es:", dia);
}
```

## Ejemplo 7: Calculadora Simple
```lyra
funcion sumar(entero a, entero b):entero{
    retornar a + b;
}

funcion restar(entero a, entero b):entero{
    retornar a - b;
}

funcion multiplicar(entero a, entero b):entero{
    retornar a * b;
}

funcion dividir(flotante a, flotante b):flotante{
    si (b == 0){
        imprimir("Error: División por cero");
        retornar 0.0;
    }
    retornar a / b;
}

funcion principal(){
    imprimir("=== CALCULADORA ===");
    entero num1 = 10;
    entero num2 = 5;
    
    imprimir("Suma:", sumar(num1, num2));
    imprimir("Resta:", restar(num1, num2));
    imprimir("Multiplicación:", multiplicar(num1, num2));
    imprimir("División:", dividir(num1, num2));
}
```

## Ejemplo 8: Número Par o Impar
```lyra
funcion esPar(entero numero):booleano{
    entero residuo = numero % 2;
    si (residuo == 0){
        retornar verdadero;
    }
    sino {
        retornar falso;
    }
}

funcion principal(){
    entero numero = 7;
    booleano resultado = esPar(numero);
    
    si (resultado){
        imprimir("El número", numero, "es par");
    }
    sino {
        imprimir("El número", numero, "es impar");
    }
}
```

## Ejemplo 9: Factorial
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

## Ejemplo 10: Fibonacci
```lyra
funcion fibonacci(entero n):entero{
    si (n <= 1){
        retornar n;
    }
    entero a = 0;
    entero b = 1;
    entero i = 2;
    mientras(i <= n){
        entero temp = a + b;
        a = b;
        b = temp;
        i = i + 1;
    }
    retornar b;
}

funcion principal(){
    imprimir("Serie Fibonacci (primeros 10):");
    para(entero i = 0; i < 10; i = i + 1){
        entero valor = fibonacci(i);
        imprimir("F(", i, ") =", valor);
    }
}
```

## Ejemplo 11: Operaciones Lógicas
```lyra
funcion principal(){
    booleano a = verdadero;
    booleano b = falso;
    
    imprimir("a yy b:", a yy b);
    imprimir("a oo b:", a oo b);
    imprimir("no a:", no a);
    imprimir("no b:", no b);
}
```

## Ejemplo 12: Comparaciones
```lyra
funcion principal(){
    entero x = 10;
    entero y = 20;
    
    imprimir("x == y:", x == y);
    imprimir("x != y:", x != y);
    imprimir("x < y:", x < y);
    imprimir("x > y:", x > y);
    imprimir("x <= y:", x <= y);
    imprimir("x >= y:", x >= y);
}
```

## Ejemplo 13: Tipos de Datos
```lyra
funcion principal(){
    entero edad = 25;
    flotante pi = 3.14159;
    booleano activo = verdadero;
    caracter inicial = 'J';
    texto nombre = "Juan";
    
    imprimir("Edad:", edad);
    imprimir("Pi:", pi);
    imprimir("Activo:", activo);
    imprimir("Inicial:", inicial);
    imprimir("Nombre:", nombre);
}
```

## Ejemplo 14: Función Sin Retorno
```lyra
funcion saludar(texto nombre){
    imprimir("¡Hola,", nombre, "!");
    imprimir("Bienvenido a Lyra");
}

funcion principal(){
    saludar("María");
    saludar("Pedro");
}
```

## Ejemplo 15: Condicional Múltiple (sinosi)
```lyra
funcion calificar(entero nota):texto{
    si (nota >= 90){
        retornar "Excelente";
    }
    sinosi (nota >= 80){
        retornar "Muy Bueno";
    }
    sinosi (nota >= 70){
        retornar "Bueno";
    }
    sinosi (nota >= 60){
        retornar "Regular";
    }
    sino {
        retornar "Insuficiente";
    }
}

funcion principal(){
    entero nota1 = 95;
    entero nota2 = 75;
    entero nota3 = 55;
    
    imprimir("Nota", nota1, ":", calificar(nota1));
    imprimir("Nota", nota2, ":", calificar(nota2));
    imprimir("Nota", nota3, ":", calificar(nota3));
}
```
