import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor

from my_fractions.my_fractions import MyFractionsApp
from my_fractions.my_fractions_2 import MyFractionsApp2
from my_fractions.my_fractions_3 import MyFractionsApp3


# Класс для главного окна
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # Загрузка интерфейса из шаблона
        uic.loadUi('ui/frac_main.ui', self)

        # Фиксированный размер окна
        self.setFixedSize(self.size())

        # Заголовок окна
        self.setWindowTitle('MathTutor')

        # Привязка действий к кнопкам
        self.fractions.clicked.connect(self.show_fraction1_window)
        self.measurement.clicked.connect(self.show_fraction2_window)
        self.equations.clicked.connect(self.show_fraction3_window)

        # Применение темной темы
        self.apply_dark_theme()

        # Показываем окно
        self.show()

    # Метод для отображения окна с дробями
    def show_fraction1_window(self):
        fractions_window = MyFractionsApp()
        fractions_window.exec_()

    def show_fraction2_window(self):
        fractions_window = MyFractionsApp2()
        fractions_window.exec_()

    # Метод для отображения окна с общим знаменателем
    def show_fraction3_window(self):
        fractions_window = MyFractionsApp3()
        fractions_window.exec_()

    # Метод для применения темной темы
    def apply_dark_theme(self):
        # Установка стиля "Fusion" глобально для всего приложения
        QApplication.setStyle("Fusion")

        # Настройка цветовой схемы для темной темы
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

        # Установка цветовой схемы глобально для всего приложения
        QApplication.setPalette(dark_palette)

        # Установка стилей для кнопок
        self.setStyleSheet(
            """
            QPushButton {
                color: white;
                background-color: #2a82da;
                border: 1px solid #2a82da;
                padding: 5px 10px;
                border-radius: 5px;
            }

            QPushButton:disabled {
                background-color: #7f7f7f;
                border: 1px solid #7f7f7f;
            }
            """
        )


# Точка входа в приложение
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    sys.exit(app.exec_())
