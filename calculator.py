"""
Copyright (c) 2022 Nanush7. MIT license, see LICENSE file.
"""
import numpy as np


class Calc:
    def __init__(self, matrix, m, n):
        self.matrix = matrix
        self.m: int = m
        self.n: int = n

    def calculate(self):
        """
        Calcular variables con el método de escalerización
        reducido.
        i in [1..m]
        j in [1..n]
        """
        # Paso 1: se revisa la primera columna.
        # Si es nula, se ignora.
        # De lo contrario, Los coeficientes no nulos pasan para arriba.
        # self.n - 1 porque la columna de los términos independientes no va.

        i0 = 0  # Fila en la que comienza la ventana.

        for j in range(self.n):
            if all(i == 0 for i in self.matrix[:, j]):
                continue

            for i in range(self.m):
                if self.matrix[i, j] != 0:
                    for ii in range(i):
                        if self.matrix[ii, j] == 0:
                            # Las filas se intercambian de lugar.
                            self.matrix[[i, ii]] = self.matrix[[ii, i]]
                            break

            # Ahora hay que hacer las combinaciones
            # lineales correspondientes.
            for i in range(i0 + 1, self.m):
                self.matrix[i, :] -= (self.matrix[i, j] / self.matrix[i0, j]) * self.matrix[i0, :]

            # TODO: Ajustar i0.
            i0 += 1  # ¿Está bien esto?
