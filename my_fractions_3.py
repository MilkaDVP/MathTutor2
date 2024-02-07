import random
from math import gcd
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPalette, QColor
from fraction.frac_3 import Ui_Form


class MyFractionsApp3(QDialog, Ui_Form):
    def __init__(self):
        super(MyFractionsApp3, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("MathTutor")
        self.resize(268, 207)

        self.setup_fraction_problem()
        self.continue_2.clicked.connect(self.setup_fraction_problem)
        self.check.clicked.connect(self.check_answer)

        # Применение темной темы
        self.apply_dark_theme()

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

    def setup_fraction_problem(self):
        # Генерация случайных чисел для задания дроби
        self.first_number.setText(str(random.randint(1, 10)))
        self.second_number.setText(str(random.randint(1, 10)))
        self.fourth_number.setText(str(random.randint(1, 10)))
        self.firth_number.setText(str(random.randint(1, 10)))
        self.input_number.clear()
        self.otvet.clear()

    def check_answer(self):
        # Получение числителя и знаменателя из интерфейса
        second_num = int(self.second_number.text())
        firth_num = int(self.firth_number.text())

        user_denominator_text = self.input_number.text()

        if user_denominator_text.strip():  # Проверка на пустую строку
            user_denominator = int(user_denominator_text)

            # Вычисление общего знаменателя
            common_denominator = abs(second_num * firth_num) // gcd(second_num, firth_num)

            # Проверка ответа пользователя
            if user_denominator == common_denominator:
                self.otvet.setText("Правильно! Знаменатель верен.")
            else:
                self.otvet.setText("Неправильно.")
        else:
            self.otvet.setText("Введите значение знаменателя.")


if __name__ == "__main__":
    app = QApplication([])
    fractions_app = MyFractionsApp3()
    fractions_app.show()
    app.exec_()
