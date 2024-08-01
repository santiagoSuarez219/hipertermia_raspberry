import time
from PySide6.QtCore import QThread, Signal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt

import time
import board
import busio
import adafruit_mlx90640

class ImagenTermica(QThread):
    actualizar_labels_signal = Signal(float, float, float)
    def __init__(self, grafica):
        super(ImagenTermica, self).__init__() 
        self.i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
        self.mlx = adafruit_mlx90640.MLX90640(self.i2c)
        print("MLX addr detected on I2C", [hex(i) for i in self.mlx.serial_number])
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
        self.frame = [0] * 768 # 32 * 24
        self.grafica = grafica
        self.mlx.getFrame(self.frame)
        self.data_imagen_termica = np.array(self.frame).reshape((24, 32))
        self.isAreaSelected = False
        self.maxima_temperatura_actual = 0

    def run(self):
        while True:
            self.actualizar_datos()
            time.sleep(.050)

    def actualizar_datos(self):
        self.mlx.getFrame(self.frame)
        self.data_imagen_termica = np.array(self.frame).reshape((24, 32))
        self.actualizar_graficas()
        if self.data_imagen_termica is not None:
            if self.grafica.x1 is not None and self.grafica.x2 is not None and self.grafica.y1 is not None and self.grafica.y2 is not None:
                data_area_seleccionada = self.data_imagen_termica[self.grafica.y1:self.grafica.y2, self.grafica.x1:self.grafica.x2]
                maxima = np.max(data_area_seleccionada)
                minima = np.min(data_area_seleccionada)
                promedio = np.mean(data_area_seleccionada)
            else:
                maxima = np.max(self.data_imagen_termica)
                minima = np.min(self.data_imagen_termica)
                promedio = np.mean(self.data_imagen_termica)
                self.maxima_temperatura_actual = maxima
            self.actualizar_labels_signal.emit(maxima, minima, promedio)
    
    def actualizar_graficas(self):
        self.grafica.g1.clear()
        if self.data_imagen_termica is not None:
            self.grafica.g1.imshow(self.data_imagen_termica, cmap='jet')
            # self.grafica.data_imagen_termica = self.data_imagen_termica
        self.grafica.draw()


class Grafica(FigureCanvasQTAgg):
    # temperatura_control_signal = Signal(float)
    def __init__(self):
        # Crear la figura y asignarle el mismo tamaño que el widget y color de fondo oscuro
        figura = Figure(layout='tight') 
        super(Grafica, self).__init__(figura)
        self.g1 = figura.add_subplot(111)
        self.data_imagen_termica = np.zeros((24, 32))
        self.area_seleccionada = None
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.RS = RectangleSelector(self.g1, self.line_select_callback, useblit=True,
                                    button=[1], minspanx=5, minspany=5, spancoords='pixels',
                                    interactive=True)

    
    def line_select_callback(self, eclick, erelease):
        """
        Callback for line selection.

        *eclick* and *erelease* are the press and release events.
        """
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        # self.area_seleccionada = self.data_imagen_termica[int(y1):int(y2), int(x1):int(x2)]
        #if self.area_seleccionada is not None:
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)
            #self.temperatura_control_signal.emit(np.max(self.area_seleccionada))
            #print(f"Temperatura promedio en el área seleccionada: {np.mean(self.area_seleccionada)}")

