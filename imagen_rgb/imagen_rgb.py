from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtCore import QThread
from picamera2 import PiCamera2
import time 
import cv2

class ImagenRGB(QThread):
    def __init__(self, grafica):
        super(ImagenRGB, self).__init__() 
        self.piCam = PiCamera2()
        self.piCam.preview_configuration.main.size = (1280, 720)
        self.piCam.preview_configuration.main.format = "RGB888"
        self.piCam.preview_configuration.align()
        self.piCam.configure("preview")
        self.piCam.start()
        self.grafica = grafica

    def run(self):
        while True:
            self.actualizar_datos()
            time.sleep(.050)

    def actualizar_datos(self):
        try: 
            frame = self.piCam.capture_array()
            self.actualizar_graficas()
        except Exception as e:
            print(e)
        
    
    def actualizar_graficas(self):
        self.grafica.g1.clear()
        self.grafica.g1.imshow(self.frame)
        self.grafica.draw()


class GraficaRGB(FigureCanvasQTAgg):
    # temperatura_control_signal = Signal(float)
    def __init__(self):
        # Crear la figura y asignarle el mismo tamaño que el widget y color de fondo oscuro
        figura = Figure(layout='tight') 
        super(GraficaRGB, self).__init__(figura)
        self.g1 = figura.add_subplot(111)
        self.frame = None
