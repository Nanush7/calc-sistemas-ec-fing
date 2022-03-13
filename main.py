"""
Copyright (c) 2022 Nanush7. MIT license, see LICENSE file.
"""
import fractions
import os
from time import sleep
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
        use_colors = query_yes_no('¿Utilizar salida de colores?', 'si')
        self.out = Output(color=use_colors)
        self.os = os.name

    def get_matrix(self):
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
                self.m = m
                self.n = n
                if m < 1 or n < 1:
                    self.out.error('m y n deben ser mayores o iguales a 1.')
                    continue
                break
            except ValueError:
                self.out.error('m y n deben ser números de tipo int.')

        self.clear()

        # Obtener valores.
        self.out.info(
            'Para ingresar una fila a la matriz, debes escribir todos los coeficientes y el término independiente, separados por espacios.')
        self.out.info('Las fracciones deben ingresarse con la forma a/b.')
        self.out.info(f'Debe ingresar {n} números por fila.')

        # ¿float64?
        matrix = np.zeros((m, n), dtype=np.float32)

        # Se agrega fila por fila a la matriz.
        for row_index in range(m):
            print('----------------------')
            while True:
                self.out.info(f'Fila: {row_index + 1}')

                try:
                    user_input = input('--> ')
                    row_list = self._get_float_list(user_input)
                    if len(row_list) != n:
                        raise IndexError

                    # Preguntar al usuario si la fila es correcta.
                    if query_yes_no('¿Continuar?', 'si'):
                        # Agregar la fila a la matriz.
                        matrix[row_index] = row_list
                        break

                except ValueError:
                    self.out.error('Debe ingresar valores de tipo float. Inténtelo nuevamente.')
                except IndexError:
                    self.out.error(f'La fila debe tener {m} columnas.')
                except ZeroDivisionError:
                    sleep(1)
                    self.out.error('Acaba de morir un gatito :(')
                    sleep(4)
                    self.out.warning('El programa procede a hacer un minuto de silencio.')
                    try:
                        sleep(60)
                    except KeyboardInterrupt:
                        self.out.warning('Interrumpiste el minuto de silencio >:(')

        return Calc(matrix, m, n)

    def _get_float_list(self, string_input: str) -> List[float]:
        # Separar el input donde hay espacios.
        raw_list = string_input.split(' ')

        # Verificar y crear objetos de fracciones.
        for index, val in enumerate(raw_list):
            if '/' in val:
                # Obtener los números de la fracción.
                nums = val.split('/')
                # Reemplazar por el objeto de Fraction. Si hay más de un "/", se ignora.
                raw_list[index] = fractions.Fraction(int(nums[0]), int(nums[1]))

        # Tomar las entradas de la lista y transformarlas en float.
        float_list = []
        for num in raw_list:
            # Puede haber espacios agregados por error,
            # no es deseable que de errores al intentar convertilos a float,
            # simplemente se ignoran.
            if num != '':
                # Si el valor es una fracción, evitar convertirlo a float.
                if isinstance(num, fractions.Fraction):
                    float_list.append(num)
                else:
                    float_list.append(float(num))

        return float_list

    def clear(self) -> None:
        if self.os == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def run(self):
        """
        Correr aplicación.
        """
        self.clear()

        self.out.info(
            'En los siguientes pasos deberá generar la matriz a calcular.')

        # matrix = self.get_matrix()
        matrix = Calc(np.array([[-2, 0, 1, 0, 0, 4], [0, -8, 0, 4, -2, 4], [-1, 0, 1, 0, 0, 3], [0, -2, 0, 1, -1, 3], [1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 1, 1]], dtype=np.float32), 6, 6)
        self.clear()

        self.out.success(str(matrix.matrix))  # DEBUG.
        result = matrix.calculate()
        self.out.success(str(matrix.matrix))  # DEBUG.

if __name__ == '__main__':
    app = CalcApp()
    app.run()
