# Test Simple - Lyra

## Test 1: Hola Mundo
```lyra
funcion principal(){
    imprimir("Hola Mundo");
}
```

## Test 2: Variables y Operaciones
```lyra
funcion principal(){
    entero a = 5;
    entero b = 3;
    entero suma = a + b;
    imprimir("La suma es:", suma);
}
```

## Test 3: Función con Retorno
```lyra
funcion suma(entero a, entero b):entero{
    entero resultado = a + b;
    retornar resultado;
}

funcion principal(){
    entero total = suma(10, 20);
    imprimir("Total:", total);
}
```

## Test 4: Condicional Simple
```lyra
funcion principal(){
    entero edad = 25;
    si (edad >= 18){
        imprimir("Mayor de edad");
    }
    sino {
        imprimir("Menor de edad");
    }
}
```

## Test 5: Bucle For Simple
```lyra
funcion principal(){
    para(entero i = 0; i < 5; i = i + 1){
        imprimir("Iteracion:", i);
    }
}
```

## Test 6: Bucle While
```lyra
funcion principal(){
    entero contador = 0;
    mientras(contador < 5){
        imprimir("Contador:", contador);
        contador = contador + 1;
    }
}
```

## Test 7: Switch
```lyra
funcion principal(){
    entero dia = 2;
    cuando (dia){
        caso 1:
            imprimir("Lunes");
            terminar;
        caso 2:
            imprimir("Martes");
            terminar;
        defecto:
            imprimir("Otro dia");
            terminar;
    }
}
```
