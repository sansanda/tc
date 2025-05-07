# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

from viewmodel.instrument_viewmodel import InstrumentViewModel


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.viewmodel = InstrumentViewModel()
        self.viewmodel.voltageChanged.connect(self.update_voltage_display)
        self.viewmodel.measurementStarted.connect(self.on_measurement_started)

        self.pushButton.clicked.connect(self.send_current)

    def send_current(self):
        value = self.doubleSpinBox.value()
        self.viewmodel.set_current(value)

    def update_voltage_display(self, voltage):
        self.label.setText(f"Voltage: {voltage:.3f} V")
        self.progressBar.setVisible(False)

    def on_measurement_started(self):
        self.progressBar.setVisible(True)
        self.progressBar.setRange(0, 0)  # modo indeterminado

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(60, 40, 241, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 50, 161, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 190, 191, 51))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(150, 290, 311, 23))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        self.menuhola = QMenu(self.menubar)
        self.menuhola.setObjectName(u"menuhola")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuhola.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Voltage: 0.000 V", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"send_current", None))
        self.menuhola.setTitle(QCoreApplication.translate("MainWindow", u"hola", None))
    # retranslateUi

