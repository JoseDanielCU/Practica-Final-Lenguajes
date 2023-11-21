from PyQt5.QtWidgets import *
from Diccionario import Diccionario
from Emojis import emojis
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.emojis = emojis
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Analizador Lexicografico')
        self.setGeometry(0, 0, 700, 700)

        self.logo = QLabel()
        pixmap = QPixmap('logo_eafit_completo.png')
        self.logo.setPixmap(pixmap.scaled(150, 50, Qt.KeepAspectRatio))

        self.Titulo = QLabel("Universidad EAFIT Proyecto Final \n Lenguajes de Programación")
        self.Titulo.setFont(QFont('Arial', 20, QFont.Bold))

        self.textoEntrada = QLabel("Ingresa un Texto:")
        self.textoEntrada.setFont(QFont('Arial', 20, QFont.Bold))
        self.entrada_Texto = QLineEdit()
        self.entrada_Texto.setFixedSize(400, 50)
        self.entrada_Texto.setFont(QFont('Arial', 10))

        self.boton = QPushButton("Procesar Cadena de Texto")
        self.boton.clicked.connect(self.procesar_texto)
        self.boton.setFont(QFont('Arial', 8))
        self.boton.setStyleSheet("background-color: white; color: black; border: 1px solid black;")
        self.boton.setFixedSize(200, 40)

        self.textoSalida = QLabel("Salida:")
        self.textoSalida.setFont(QFont('Arial', 20, QFont.Bold))
        self.texto_salida = QLabel()
        self.texto_salida.setStyleSheet("color: blue")
        self.texto_salida.setFont(QFont('Arial', 20, QFont.Bold))

        self.encontrados = QLabel()
        self.encontrados.setStyleSheet("color: green")
        self.encontrados.setFont(QFont('Arial', 20, QFont.Bold))

        layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        header_layout.addWidget(self.logo)
        header_layout.addWidget(self.Titulo)
        layout.addLayout(header_layout)

        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(self.textoEntrada)
        entrada_layout.addWidget(self.entrada_Texto)
        layout.addLayout(entrada_layout)

        boton_layout = QHBoxLayout()
        boton_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding))
        boton_layout.addWidget(self.boton)
        boton_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding))
        layout.addLayout(boton_layout)

        salida_layout = QHBoxLayout()
        salida_layout.addWidget(self.textoSalida)
        salida_layout.addWidget(self.texto_salida)
        layout.addLayout(salida_layout)

        layout.addWidget(self.encontrados)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def procesar_texto(self):
        texto_original = self.entrada_Texto.text()
        texto = texto_original
        ContarPalabras = texto
        conteo_emojis = 0
        for emoji in self.emojis:
            conteo_emojis += texto.count(emoji)
            ContarPalabras = ContarPalabras.replace(emoji, ' ')
            texto_original = texto_original.replace(emoji,self.emojis[emoji])

        texto = texto.lower()
        ContarPalabras = ContarPalabras.lower()

        palabras = ContarPalabras.split()

        conteo_palabras_diccionario = 0
        for palabra in palabras:
            primera_letra = palabra[0]
            if primera_letra in Diccionario:
                for diccionario_palabra in Diccionario[primera_letra]:
                    diccionario_palabra = diccionario_palabra.lower()
                    if diccionario_palabra == palabra or palabra in diccionario_palabra:
                        conteo_palabras_diccionario += 1
                        break

        self.texto_salida.setText(texto_original)
        self.encontrados.setText(
            f"\n\n   Se encontraron {conteo_emojis} emojis y {conteo_palabras_diccionario} palabras\n                   del diccionario")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
