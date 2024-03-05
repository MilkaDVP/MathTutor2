import random
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QDialog, QApplication
from fraction.frac_2 import Ui_Form


class MyFractionsApp2(QDialog, Ui_Form):
    def __init__(self):
        super(MyFractionsApp2, self).__init__()
        self.setupUi(self)
        self.generate_new_fraction()
        self.check.clicked.connect(self.check_fraction)
        self.continue_2.clicked.connect(self.generate_new_fraction)
        self.apply_dark_theme()

    def apply_dark_theme(self):
        # Применение темной темы для всего приложения
        QApplication.setStyle("Fusion")

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

        # Установка цветовой схемы для всего приложения
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

    def generate_new_fraction(self):
        # Генерация случайной неправильной дроби
        self.denominator = random.randint(2, 20)  # Знаменатель всегда больше 1
        self.numerator = random.randint(self.denominator + 1, 2 * self.denominator - 1)

        # Отображение дроби в интерфейсе
        self.first_number.setText(str(self.numerator))
        self.second_number.setText(str(self.denominator))

        # Очистка полей ввода и вывода
        self.input_number.clear()
        self.input_first_number.clear()
        self.input_second_number.clear()
        self.otvet.clear()

    def check_fraction(self):
        try:
            # Получение введенных пользователем значений
            user_numerator = int(self.input_first_number.text())
            user_denominator = int(self.input_second_number.text())
            user_number = int(self.input_number.text())

            # Проверка условий
            if (round(user_number) == self.numerator // self.denominator and
                    user_numerator == self.numerator - self.denominator and user_denominator == self.denominator):
                self.otvet.setText('Результат: Верно!')
            else:
                self.otvet.setText('Результат: Неверно.')

        except ValueError:
            # Обработка ошибки ввода
            self.otvet.setText('Введите целые числа в поля.')


if __name__ == '__main__':
    # Запуск приложения
    app = QApplication([])
    fractions_window = MyFractionsApp2()
    fractions_window.show()
    app.exec_()
