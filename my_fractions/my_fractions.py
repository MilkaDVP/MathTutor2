import random

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from fractions import Fraction
from fraction.frac_1 import Ui_Form  # Подключение сгенерированного файла с интерфейсом
from PyQt5.QtGui import QPalette, QColor


class MyFractionsApp(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация интерфейса
        self.setup_fraction()
        self.setWindowTitle("MathTutor")

        self.setFixedSize(self.size())

        # Привязка действий к кнопкам
        self.check.clicked.connect(self.check_fraction)
        self.continue_2.clicked.connect(self.continue_fraction)
        self.skip.clicked.connect(self.skip_fraction)

        self.incorrect_attempts = 0  # Счетчик неправильных попыток
        self.apply_dark_theme()  # Применение темной темы

    def apply_dark_theme(self):
        # Установка темной темы для окна с дробями
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

        self.setPalette(dark_palette)

        # Установка стилей для кнопок
        self.check.setStyleSheet(
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

        self.continue_2.setStyleSheet(
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

        self.skip.setStyleSheet(
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

    def generate_proper_fraction(self):
        # Генерация случайной правильной дроби
        numerator = random.randint(1, 9)
        denominator = random.randint(numerator + 1, 10)
        return Fraction(numerator, denominator)

    def setup_fraction(self):
        font = QtGui.QFont()
        font.setPointSize(18)
        # Генерация двух случайных правильных дробей
        first_fraction = self.generate_proper_fraction()
        second_fraction = self.generate_proper_fraction()

        # Генерация случайного знака
        signs = ['+', '-', '×', '÷']
        sign = random.choice(signs)

        # Отображение дробей и знака в пользовательском интерфейсе
        self.first_number.setText(str(first_fraction.numerator))
        self.second_number.setText(str(first_fraction.denominator))

        # Установка размера шрифта и выравнивания для знака операции
        self.sign.setFont(font)
        self.sign.setAlignment(QtCore.Qt.AlignCenter)  # Установка выравнивания в центр
        self.sign.setText(sign)

        self.fourth_number.setText(str(second_fraction.numerator))
        self.firth_number.setText(str(second_fraction.denominator))

        # Очистка полей ввода
        self.input_first_number.clear()
        self.input_second_number.clear()
        self.otvet.clear()

    def check_fraction(self):
        try:
            input_numerator = int(self.input_first_number.text())
            input_denominator = int(self.input_second_number.text())

            # Расчет ожидаемого результата
            first_fraction = Fraction(int(self.first_number.text()), int(self.second_number.text()))
            second_fraction = Fraction(int(self.fourth_number.text()), int(self.firth_number.text()))

            if self.sign.text() == '+':
                expected_result = first_fraction + second_fraction
            elif self.sign.text() == '-':
                expected_result = first_fraction - second_fraction
            elif self.sign.text() == '×':
                expected_result = first_fraction * second_fraction
            elif self.sign.text() == '÷':
                expected_result = first_fraction / second_fraction
            else:
                raise ValueError("Invalid sign")

            # Проверка ввода на соответствие ожидаемому результату (убеждаемся, что результат положительный)
            if expected_result >= 0 and Fraction(input_numerator, input_denominator) == expected_result:
                self.otvet.setText("Правильно!")
                self.incorrect_attempts = 0
            else:
                self.otvet.setText("Неправильно!")
                self.incorrect_attempts += 1
        except ValueError:
            self.otvet.setText("Неверный формат дроби")

    def continue_fraction(self):
        # Разрешить продолжение только в случае правильного последнего ответа
        if self.otvet.text() == "Правильно!":
            self.setup_fraction()
        else:
            self.otvet.setText("Сначала решите текущее задание правильно.")

    def skip_fraction(self):
        # Разрешить пропуск только после двух или более неправильных попыток
        if self.incorrect_attempts >= 2:
            self.setup_fraction()
            self.incorrect_attempts = 0
        else:
            self.otvet.setText("Нельзя пропустить задание после двух и менее неправильных ответов.")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    fractions_window = MyFractionsApp()
    fractions_window.exec_()  # Запуск приложения
