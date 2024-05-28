import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
import generador_completo
import random
os.system('cls')
matplotlib.use('Agg')

def cantidad(espaniol, inicial, n1, n2, n3, n4, n5):
    n1 = [1] * n1
    n2 = [2] * n2
    n3 = [3] * n3
    n4 = [4] * n4
    n5 = [5] * n5
    cantidad_sudokus = n1 + n2 + n3 + n4 + n5 
    paginaxnivel = 0
    paginaactual = 1
    for pagina, niveles in enumerate(cantidad_sudokus):
        if niveles == paginaactual:
            paginaxnivel += 1
        else:
            paginaxnivel = 1
            paginaactual = niveles
        sudoku = generar_sudoku()
        dibujar_sudoku(espaniol, sudoku, pagina+1, inicial, niveles, paginaxnivel)


def dibujar_sudoku(espaniol, tablero, pagina, inicial, niveles, paginaxnivel):

    if espaniol == 1:
        pag = 'Página'
    else:
        pag = 'Page'
 
    fig, ax = plt.subplots(figsize=(5, 8))  

    for i in range(10):
        if i == 3 or i == 6:
            lw = 2
        elif i == 0 or i == 9:
            lw = 4
        else:
            lw = 0.5
        ax.axhline(i, lw=lw, color='black')
        ax.axvline(i, lw=lw, color='black')


    for i in range(9):
        for j in range(9):
            if tablero[i][j] != 0:
                ax.text(j + 0.5, 8.5 - i, str(tablero[i][j]), ha='center', va='center')

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')


    # Añade el título aquí
    ax.set_title(f'\n \n{pag} {pagina+inicial-1}', fontsize=16, fontweight='bold', pad='70')

    # Agrega el texto "Página 1"
    plt.text(4.5, -3, '\n \n \n \n \n  \n ', ha='center', fontsize=12)

    # Agrega texto a la izquierda
    plt.text(-1, 4.5, '  ', va='center', ha='center', fontsize=12, rotation='vertical')

    # Agrega texto a la derecha
    plt.text(10, 4.5, '  ', va='center', ha='center', fontsize=12, rotation='vertical')


    # Guardar el gráfico en un archivo PDF
    plt.savefig(f'resolucion_{pagina}.png', format='png', bbox_inches='tight')

    if espaniol == 1:
        if niveles == 1:
            numero_random = random.randint(32, 45)
            nivel_nombre = 'Facil'
        elif niveles == 2:
            numero_random = random.randint(46, 51)
            nivel_nombre = 'Medio'
        elif niveles == 3:
            numero_random = random.randint(52, 57)
            nivel_nombre = 'Dificil'
        elif niveles == 4:
            numero_random = random.randint(58, 63)
            nivel_nombre = 'Experto'
        elif niveles == 5:
            numero_random = random.randint(63, 64)
            nivel_nombre = 'Diabólico'
    else:
        if niveles == 1:
            numero_random = random.randint(32, 45)
            nivel_nombre = 'Easy'
        elif niveles == 2:
            numero_random = random.randint(46, 51)
            nivel_nombre = 'Medium'
        elif niveles == 3:
            numero_random = random.randint(52, 57)
            nivel_nombre = 'Difficult'
        elif niveles == 4:
            numero_random = random.randint(58, 63)
            nivel_nombre = 'Expert'
        elif niveles == 5:
            numero_random = random.randint(63, 64)
            nivel_nombre = 'Diabolical'
    tablero = quitar_numeros(tablero, numero_random)
    
    fig, ax = plt.subplots(figsize=(5, 8))  

    for i in range(10):
        if i == 3 or i == 6:
            lw = 2
        elif i == 0 or i == 9:
            lw = 4
        else:
            lw = 0.5
        ax.axhline(i, lw=lw, color='black')
        ax.axvline(i, lw=lw, color='black')

    # Rellena los números
    for i in range(9):
        for j in range(9):
            if tablero[i][j] != 0:
                ax.text(j + 0.5, 8.5 - i, str(tablero[i][j]), ha='center', va='center')

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Añade el título aquí
    ax.set_title(f'\nSudoku\n{nivel_nombre} {paginaxnivel}', fontsize=16, fontweight='bold', pad='70')

    # Agrega el texto "Página 1"
    plt.text(4.5, -3, f'\n \n \n \n \n{pag} {pagina+inicial-1}\n ', ha='center', fontsize=12)

    # Agrega texto a la izquierda
    plt.text(-1, 4.5, '  ', va='center', ha='center', fontsize=12, rotation='vertical')

    # Agrega texto a la derecha
    plt.text(10, 4.5, '  ', va='center', ha='center', fontsize=12, rotation='vertical')

    # Guardar el gráfico en un archivo PDF
    plt.savefig(f'GenSudoku_{pagina}.png', format='png', bbox_inches='tight')

def generar_sudoku():
    tablero = generador_completo.generar_tablero()
    solucion = generador_completo.resolver_sudoku(tablero.copy())
    return solucion



def quitar_numeros(tablero, cantidad):
    tablero_con_numeros_faltantes = [fila[:] for fila in tablero]  # Copiar el tablero completo

    for _ in range(cantidad):
        while cantidad > 0:
            fila, columna = random.randint(0, 8), random.randint(0, 8)
            if tablero_con_numeros_faltantes[fila][columna] > 0:
                tablero_con_numeros_faltantes[fila][columna] = 0
                cantidad -= 1

    return tablero_con_numeros_faltantes

#if __name__ == '__main__':
#    cantidad(1,3,2,2,2,3,2)
    

