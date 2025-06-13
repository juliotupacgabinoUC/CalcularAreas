import sys
from PyQt6.QtWidgets import QApplication
from src.logica.CalcularAreas import AreaCalculator

def main():
    """Función principal que inicia la aplicación."""
    app = QApplication(sys.argv)

    calculadora = AreaCalculator()
    calculadora.setWindowTitle("Calculadora de Áreas")
    calculadora.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()