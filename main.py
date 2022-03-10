"""
Copyright (c) 2022 Nanush7. MIT license, see LICENSE file.
"""
from typing import List

import numpy as np

from calculator import Calc
from output import Output
from utils import query_yes_no


class CalcApp:
    """
    Agregar descripción.
    """
    def __init__(self):
        # Instanciar clase output.
        use_colors = query_yes_no('¿Utilizar salida de colores?', 'no')
        self.out = Output(color=use_colors)

    def get_matrix(self) -> List[List[float]]:
        """
        Obtener la matriz ampliada del sistema a calcular.
        """
        # Obtener cantidad de filas y columnas.
        while True: 
            try:
                # m = filas (ecuaciones).
                # n = columnas (incógnitas).
                m = int(input('m (cantidad de filas) = '))
                n = int(input('n (cantidad de columnas) = '))
                if m < 1 or n < 1:
                    self.out.error('m y n deben ser mayores o iguales a 1.')
                    continue
                break
            except ValueError:
                self.out.error('m y n deben ser números de tipo int.')

        # Obtener valores.
        matrix = np.empty((m, n))
        for _ in range(m):
            row = []
            while True:
                try:
                    print()
                    row.append(float(input('--> ')))
                except ValueError:
                    self.out.error('Debe ser un valor de tipo float.')

        calc = Calc(matrix)

    def run(self):
        """
        Correr aplicación.
        """
        print('En los siguientes pasos deberá generar la matriz a calcular.')
        print(self.get_matrix())


if __name__ == '__main__':
    app = CalcApp()
    app.run()
