import math
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import os


class AreaCalculator(QMainWindow):
    """Clase principal para la calculadora de áreas.

    Calcula áreas de: círculos, triángulos, rectángulos y cuadrados.
    """

    def __init__(self):
        """Inicializa la aplicación cargando la interfaz y conectando señales."""
        super().__init__()

        # Cargar la interfaz de usuario
        ruta = os.path.join(os.path.dirname(__file__), '..', 'vista', 'Form.ui')
        uic.loadUi(ruta, self)

        # Conectar eventos
        self.btnCalcular.clicked.connect(self.calcular_area)
        self.btnBorrar.clicked.connect(self.borrar_campos)

        # Configurar campos iniciales
        self.actualizar_campos()

    def actualizar_campos(self):
        """Actualiza el estado de los campos según la figura seleccionada."""
        is_circulo = self.rbCirculo.isChecked()
        is_triangulo = self.rbTriangulo.isChecked()
        is_cuadrado = self.rbCuadrado.isChecked()

        self.txtAltura.setEnabled(not is_circulo)
        self.txtBase.setEnabled(is_triangulo or not is_cuadrado)
        self.txtRadio.setEnabled(is_circulo)

        if is_cuadrado:
            self.label_2.setText("Lado")
        else:
            self.label_2.setText("Altura")

    def obtener_valor(self, widget):
        """Obtiene y valida un valor numérico de un widget.

        Args:
            widget: QTextEdit del cual obtener el valor

        Returns:
            float: Valor numérico convertido

        Raises:
            ValueError: Si el valor no es válido
        """
        texto = widget.toPlainText().strip()
        if not texto:
            raise ValueError("Campo vacío")

        try:
            valor = float(texto.replace(",", "."))
            if valor <= 0:
                raise ValueError("El valor debe ser positivo")
            return valor
        except ValueError:
            raise ValueError("Valor no numérico")

    def calcular_area(self):
        """Calcula el área según la figura seleccionada."""
        try:
            if self.rbCirculo.isChecked():
                radio = self.obtener_valor(self.txtRadio)
                area = math.pi * (radio ** 2)
            elif self.rbTriangulo.isChecked():
                base = self.obtener_valor(self.txtBase)
                altura = self.obtener_valor(self.txtAltura)
                area = (base * altura) / 2
            elif self.rbRectangulo.isChecked():
                base = self.obtener_valor(self.txtBase)
                altura = self.obtener_valor(self.txtAltura)
                area = base * altura
            elif self.rbCuadrado.isChecked():
                lado = self.obtener_valor(self.txtAltura)
                area = lado ** 2
            else:
                raise ValueError("Seleccione una figura geométrica")

            self.lblResultado.setText(f"{area:.2f}")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def borrar_campos(self):
        """Reinicia todos los campos a su estado inicial."""
        self.txtAltura.clear()
        self.txtBase.clear()
        self.txtRadio.clear()
        self.lblResultado.clear()
        for rb in [self.rbCirculo, self.rbTriangulo,
                   self.rbRectangulo, self.rbCuadrado]:
            rb.setChecked(False)
        self.actualizar_campos()