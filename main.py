import io
import math
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import QPointF

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1000</width>
    <height>1000</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
    <horstretch>100</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>1000</width>
    <height>1000</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1000</width>
    <height>1000</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Знакомство с L-системами</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QSlider" name="slider">
    <property name="geometry">
     <rect>
      <x>25</x>
      <y>680</y>
      <width>160</width>
      <height>22</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class LSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.ll = 20
        self.color = QColor(0, 0, 0)
        self.slider.setMinimum(1)
        self.slider.setMaximum(5)
        self.slider.setFixedWidth(450)
        self.saved_positions = []

        data = [i.replace('\n', '') for i in
                open(QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0], mode="r").readlines()
                if i.replace('\n', '')][1:]
        self.n, self.axiom, self.theorem = int(data[0]), data[1], data[2:]
        self.theorem = {i.split()[0]: i.split()[1] for i in self.theorem}

        self.turning_degree = 360 / self.n
        self.coordinates = [250, 400, 0]
        self.new_axiom = self.axiom[:]
        self.act(1)

        self.slider.valueChanged.connect(lambda: self.act(self.slider.value()))

    def act(self, n):
        self.new_axiom = self.axiom[:]
        for _ in range(n):
            new = ''
            for i in self.new_axiom:
                new += self.theorem.get(i, i)
            self.new_axiom = new
        self.coordinates = [250, 400, 0]
        self.saved_positions = []
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for el in self.new_axiom:
            if el == 'F':
                self.coordinates[0] += round(self.ll * math.cos(math.radians(self.coordinates[2])), 20)
                self.coordinates[1] += round(self.ll * math.sin(math.radians(self.coordinates[2])), 20)
                qp.drawLine(QPointF(round(self.coordinates[0] - self.ll * math.cos(math.radians(self.coordinates[2])),
                                          20),
                                    round(self.coordinates[1] - self.ll * math.sin(math.radians(self.coordinates[2])),
                                          20)),
                            QPointF(self.coordinates[0], self.coordinates[1]))
            elif el == 'f':
                self.coordinates[0] += self.ll * math.cos(math.radians(self.coordinates[2]))
                self.coordinates[1] += self.ll * math.sin(math.radians(self.coordinates[2]))
            elif el == '+':
                self.coordinates[2] += self.turning_degree
            elif el == '-':
                self.coordinates[2] -= self.turning_degree
            elif el == '[':
                self.saved_positions.append(self.coordinates[:])
            elif el == ']':
                self.coordinates = self.saved_positions.pop(-1)
            elif el == '|':
                self.coordinates[2] -= 180
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LSystem()
    ex.show()
    sys.exit(app.exec())
