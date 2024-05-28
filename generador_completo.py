
from dokusan import generators
import numpy as np

def generar_tablero():
    sudoku_str = str(generators.random_sudoku(avg_rank=150))
    sudoku_numbers = [int(char) for char in sudoku_str if char.isdigit()]
    return np.array(sudoku_numbers).reshape(9, 9)

def resolver_sudoku(tablero):
    # Función auxiliar para verificar si un número es válido en una posición dada
    def es_valido(num, fila, columna):
        # Verificar fila
        if num in tablero[fila, :]:
            return False

        # Verificar columna
        if num in tablero[:, columna]:
            return False

        # Verificar submatriz 3x3
        fila_inicio, col_inicio = 3 * (fila // 3), 3 * (columna // 3)
        submatriz = tablero[fila_inicio:fila_inicio + 3, col_inicio:col_inicio + 3]
        if num in submatriz:
            return False

        return True

    # Función principal de resolución usando backtracking
    def resolver():
        for i in range(9):
            for j in range(9):
                if tablero[i, j] == 0:
                    for num in range(1, 10):
                        if es_valido(num, i, j):
                            tablero[i, j] = num
                            if resolver():
                                return True
                            tablero[i, j] = 0
                    return False
        return True

    resolver()
    return tablero
