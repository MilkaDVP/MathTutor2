import io
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPalette, QColor

from my_fractions_3 import MyFractionsApp3
from my_fractions import MyFractionsApp
from my_fractions_2 import MyFractionsApp2

# Шаблон XML для интерфейса
template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <!-- Главное окно -->
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>644</width>
    <height>129</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <!-- Центральный виджет сеткой -->
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout_2">
    <!-- Вложенная сетка для размещения метки -->
    <item row="0" column="1">
     <layout class="QGridLayout" name="gridLayout">
      <item row="0" column="1">
       <widget class="QLabel" name="textmath">
        <!-- Настройки шрифта метки -->
        <property name="font">
         <font>
          <family>Times New Roman</family>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <!-- Текст метки -->
        <property name="text">
         <string>                     ДРОБИ</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <!-- Кнопка "ОБЩИЙ ЗНАМЕНАТЕЛЬ" -->
    <item row="1" column="2">
     <widget class="QPushButton" name="equations">
      <!-- Базовый размер кнопки -->
      <property name="baseSize">
       <size>
        <width>450</width>
        <height>50</height>
       </size>
      </property>
      <!-- Настройки шрифта кнопки -->
      <property name="font">
       <font>
        <family>Times New Roman</family>
       </font>
      </property>
      <!-- Текст кнопки -->
      <property name="text">
       <string>ОБЩИЙ ЗНАМЕНАТЕЛЬ</string>
      </property>
     </widget>
    </item>
    <!-- Кнопка "НЕПРАВИЛЬНЫЕ ДРОБИ" -->
    <item row="1" column="1">
     <widget class="QPushButton" name="measurement">
      <!-- Настройки шрифта кнопки -->
      <property name="font">
       <font>
        <family>Times New Roman</family>
       </font>
      </property>
      <!-- Текст кнопки -->
      <property name="text">
       <string>НЕПРАВИЛЬНЫЕ ДРОБИ</string>
      </property>
     </widget>
    </item>
    <!-- Кнопка "ДРОБИ" -->
    <item row="1" column="0">
     <widget class="QPushButton" name="fractions">
      <!-- Настройки шрифта кнопки -->
      <property name="font">
       <font>
        <family>Times New Roman</family>
       </font>
      </property>
      <!-- Текст кнопки -->
      <property name="text">
       <string>ДРОБИ</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <!-- Меню -->
  <widget class="QMenuBar" name="menubar">
   <!-- Геометрия меню -->
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>644</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <!-- Строка состояния -->
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <!-- Ресурсы -->
 <resources/>
 <!-- Соединения -->
 <connections/>
</ui>'''


# Класс для главного окна
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # Загрузка интерфейса из шаблона
        f = io.StringIO(template)
        loadUi(f, self)

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
