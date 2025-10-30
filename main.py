import tkinter as tk
from tkinter import scrolledtext

from compile import compileCode
from execute import executeCode

def insert_code(code):
    position = code_area.index(tk.INSERT)
    code_area.insert(position, code)

def show_options():
    options = tk.Toplevel(window)
    options.title("Opciones")
    options.geometry("400x300")
    
    tk.Label(options, text="Insertar codigo:", font=("Arial", 12, "bold")).pack(pady=10)
    
    codes = {
        "Basic function": "def my_function():\n    pass\n",
    }
    
    for name, code in codes.items():
        tk.Button(options, text=name, 
                 command=lambda c=code: [insert_code(c), options.destroy()],
                 width=20).pack(pady=2)

# Main window
window = tk.Tk()
window.title("Code Editor")
window.geometry("700x450")

# Menu
menubar = tk.Menu(window)
window.config(menu=menubar)

menubar.add_command(label="Opciones", command=show_options)

# Main frame
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Code text area
code_area = scrolledtext.ScrolledText(main_frame, width=50, height=15, font=("Courier", 10))
code_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,5))

# Right frame
right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Output area
tk.Label(right_frame, text="OUTPUT").pack()
output = tk.Text(right_frame, width=30, height=15, bg="black", fg="green", 
                insertbackground="white", font=("Consolas", 9))
output.pack(pady=(5,10))

# Buttons
button_frame = tk.Frame(right_frame)
button_frame.pack(side=tk.BOTTOM)

tk.Button(button_frame, text="COMPILAR", command=lambda: compileCode(output,code_area,tk), width=10).pack(side=tk.LEFT, padx=2)
tk.Button(button_frame, text="EJECUTAR", command=lambda: executeCode(output,code_area,tk), width=10).pack(side=tk.LEFT, padx=2)

# Initial code
initial_code = '''funcion sumarNumeros(entero x, entero y):entero{
    entero resultado = x + y;
    retornar resultado;
}

funcion restarNumeros(entero x, entero y):entero{
    retornar x - y;
}

funcion multiplicarNumeros(entero x, entero y):entero{
    retornar x * y;
}

funcion dividirNumeros(flotante x, flotante y):flotante{
    si (y == 0){
        imprimir("Error: Division por cero!");
        retornar 0.0;
    }
    retornar x / y;
}

funcion esParOImpar(entero numero):texto{
    entero residuo = numero % 2;
    si (residuo == 0){
        retornar "Par";
    }
    sino {
        retornar "Impar";
    }
}

funcion calcularPromedio(entero nota1, entero nota2, entero nota3):flotante{
    entero suma = nota1 + nota2 + nota3;
    flotante promedio = suma / 3.0;
    retornar promedio;
}

funcion calificarEstudiante(flotante promedio):texto{
    si (promedio >= 90.0){
        retornar "Excelente";
    }
    sinosi (promedio >= 80.0){
        retornar "Muy Bueno";
    }
    sinosi (promedio >= 70.0){
        retornar "Bueno";
    }
    sinosi (promedio >= 60.0){
        retornar "Regular";
    }
    sino {
        retornar "Insuficiente";
    }
}

funcion obtenerDiaSemana(entero dia):texto{
    texto nombreDia = "";
    cuando (dia){
        caso 1:
            nombreDia = "Lunes";
            terminar;
        caso 2:
            nombreDia = "Martes";
            terminar;
        caso 3:
            nombreDia = "Miercoles";
            terminar;
        caso 4:
            nombreDia = "Jueves";
            terminar;
        caso 5:
            nombreDia = "Viernes";
            terminar;
        caso 6:
            nombreDia = "Sabado";
            terminar;
        caso 7:
            nombreDia = "Domingo";
            terminar;
        defecto:
            nombreDia = "Dia invalido";
            terminar;
    }
    retornar nombreDia;
}

funcion mostrarTablaMultiplicar(entero numero){
    imprimir("Tabla de multiplicar del", numero);
    imprimir("================================");
    para(entero i = 1; i <= 10; i = i + 1){
        entero resultado = numero * i;
        imprimir(numero, "x", i, "=", resultado);
    }
}

funcion contarHasta(entero limite){
    imprimir("Contando hasta", limite);
    entero contador = 1;
    mientras(contador <= limite){
        imprimir("Numero:", contador);
        contador = contador + 1;
    }
}

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

funcion esPrimo(entero numero):booleano{
    si (numero <= 1){
        retornar falso;
    }
    si (numero == 2){
        retornar verdadero;
    }
    entero divisor = 2;
    mientras(divisor < numero){
        entero residuo = numero % divisor;
        si (residuo == 0){
            retornar falso;
        }
        divisor = divisor + 1;
    }
    retornar verdadero;
}

funcion mostrarMenu(){
    imprimir("a ");
    imprimir("===================================");
    imprimir("  SISTEMA DE GESTION ESTUDIANTIL");
    imprimir("===================================");
    imprimir("1. Calculadora Basica");
    imprimir("2. Analizar Numero");
    imprimir("3. Calcular Promedio de Notas");
    imprimir("4. Mostrar Dia de la Semana");
    imprimir("5. Tabla de Multiplicar");
    imprimir("6. Contar Numeros");
    imprimir("7. Calcular Factorial");
    imprimir("8. Verificar Numero Primo");
    imprimir("9. Operaciones Logicas");
    imprimir("0. Salir");
    imprimir("===================================");
}

funcion menuCalculadora(){
    imprimir("");
    imprimir("=== CALCULADORA BASICA ===");
    imprimir("Ingrese primer numero:");
    entero num1 = leer;
    imprimir("Ingrese segundo numero:");
    entero num2 = leer;
    
    entero suma = sumarNumeros(num1, num2);
    entero resta = restarNumeros(num1, num2);
    entero multiplicacion = multiplicarNumeros(num1, num2);
    flotante division = dividirNumeros(num1, num2);
    
    imprimir("");
    imprimir("Resultados:");
    imprimir("Suma:", suma);
    imprimir("Resta:", resta);
    imprimir("Multiplicacion:", multiplicacion);
    imprimir("Division:", division);
}

funcion menuAnalizar(){
    imprimir("");
    imprimir("=== ANALIZAR NUMERO ===");
    imprimir("Ingrese un numero:");
    entero numero = leer;
    
    texto tipo = esParOImpar(numero);
    imprimir("El numero", numero, "es:", tipo);
    
    booleano primo = esPrimo(numero);
    si (primo){
        imprimir("El numero", numero, "es primo");
    }
    sino {
        imprimir("El numero", numero, "NO es primo");
    }
}

funcion menuPromedio(){
    imprimir("");
    imprimir("=== CALCULAR PROMEDIO ===");
    imprimir("Ingrese nota 1 (0-100):");
    entero nota1 = leer;
    imprimir("Ingrese nota 2 (0-100):");
    entero nota2 = leer;
    imprimir("Ingrese nota 3 (0-100):");
    entero nota3 = leer;
    
    flotante promedio = calcularPromedio(nota1, nota2, nota3);
    texto calificacion = calificarEstudiante(promedio);
    
    imprimir("");
    imprimir("Notas ingresadas:", nota1, nota2, nota3);
    imprimir("Promedio:", promedio);
    imprimir("Calificacion:", calificacion);
}

funcion menuDiaSemana(){
    imprimir("");
    imprimir("=== DIA DE LA SEMANA ===");
    imprimir("Ingrese numero del dia (1-7):");
    entero dia = leer;
    
    texto nombreDia = obtenerDiaSemana(dia);
    imprimir("El dia", dia, "corresponde a:", nombreDia);
}

funcion menuTablaMultiplicar(){
    imprimir("");
    imprimir("=== TABLA DE MULTIPLICAR ===");
    imprimir("Ingrese un numero:");
    entero numero = leer;
    
    mostrarTablaMultiplicar(numero);
}

funcion menuContar(){
    imprimir("");
    imprimir("=== CONTAR NUMEROS ===");
    imprimir("Contar hasta:");
    entero limite = leer;
    
    contarHasta(limite);
}

funcion menuFactorial(){
    imprimir("");
    imprimir("=== CALCULAR FACTORIAL ===");
    imprimir("Ingrese un numero:");
    entero numero = leer;
    
    entero fact = factorial(numero);
    imprimir("El factorial de", numero, "es:", fact);
}

funcion menuPrimo(){
    imprimir("");
    imprimir("=== VERIFICAR NUMERO PRIMO ===");
    imprimir("Ingrese un numero:");
    entero numero = leer;
    
    booleano primo = esPrimo(numero);
    si (primo){
        imprimir("El numero", numero, "ES primo");
    }
    sino {
        imprimir("El numero", numero, "NO es primo");
    }
}

funcion menuOperacionesLogicas(){
    imprimir("");
    imprimir("=== OPERACIONES LOGICAS ===");
    booleano a = verdadero;
    booleano b = falso;
    
    imprimir("a = verdadero");
    imprimir("b = falso");
    imprimir("");
    imprimir("a yy b =", a yy b);
    imprimir("a oo b =", a oo b);
    imprimir("no a =", no a);
    imprimir("no b =", no b);
    
    imprimir("");
    imprimir("Comparaciones:");
    entero x = 10;
    entero y = 20;
    imprimir("x = 10, y = 20");
    imprimir("x == y:", x == y);
    imprimir("x != y:", x != y);
    imprimir("x < y:", x < y);
    imprimir("x > y:", x > y);
    imprimir("x <= y:", x <= y);
    imprimir("x >= y:", x >= y);
}

funcion principal(){
    imprimir("Bienvenido al Sistema de Gestion Estudiantil");
    imprimir("Desarrollado en Lenguaje Lyra");
    
    booleano continuar = verdadero;
    entero intentos = 0;
    
    mientras(continuar yy intentos < 20){
        imprimir("Seleccione una opcion:");
        mostrarMenu();
        entero opcion = leer;
        
        cuando (opcion){
            caso 1:
                menuCalculadora();
                terminar;
            caso 2:
                menuAnalizar();
                terminar;
            caso 3:
                menuPromedio();
                terminar;
            caso 4:
                menuDiaSemana();
                terminar;
            caso 5:
                menuTablaMultiplicar();
                terminar;
            caso 6:
                menuContar();
                terminar;
            caso 7:
                menuFactorial();
                terminar;
            caso 8:
                menuPrimo();
                terminar;
            caso 9:
                menuOperacionesLogicas();
                terminar;
            caso 0:
                imprimir("");
                imprimir("Gracias por usar el sistema!");
                imprimir("Hasta pronto!");
                continuar = falso;
                terminar;
            defecto:
                imprimir("Opcion invalida. Intente nuevamente.");
                terminar;
        }
        
        intentos = intentos + 1;
    }
    
    si (intentos >= 20){
        imprimir("");
        imprimir("Limite de operaciones alcanzado.");
    }
    
    imprimir("");
    imprimir("Fin del programa.");
}
'''

code_area.insert("1.0", initial_code)
window.mainloop()