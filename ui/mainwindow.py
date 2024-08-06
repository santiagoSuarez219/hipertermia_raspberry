# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowpFYFCR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1127, 552)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.RGB = QWidget()
        self.RGB.setObjectName(u"RGB")
        self.image_rgb = QLabel(self.RGB)
        self.image_rgb.setObjectName(u"image_rgb")
        self.image_rgb.setGeometry(QRect(10, 10, 861, 451))
        self.image_rgb.setStyleSheet(u"background-color: white")
        self.tabWidget.addTab(self.RGB, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget = QWidget(self.tab_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 861, 451))
        self.image_termica = QVBoxLayout(self.verticalLayoutWidget)
        self.image_termica.setObjectName(u"image_termica")
        self.image_termica.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 16, -1)
        self.parametros_termicos_label = QLabel(self.centralwidget)
        self.parametros_termicos_label.setObjectName(u"parametros_termicos_label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.parametros_termicos_label.setFont(font)

        self.verticalLayout.addWidget(self.parametros_termicos_label)

        self.temperatura_maxima = QLabel(self.centralwidget)
        self.temperatura_maxima.setObjectName(u"temperatura_maxima")
        font1 = QFont()
        font1.setPointSize(10)
        self.temperatura_maxima.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_maxima)

        self.temperatura_maxima_value = QLabel(self.centralwidget)
        self.temperatura_maxima_value.setObjectName(u"temperatura_maxima_value")
        self.temperatura_maxima_value.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_maxima_value)

        self.temperatura_minima = QLabel(self.centralwidget)
        self.temperatura_minima.setObjectName(u"temperatura_minima")
        self.temperatura_minima.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_minima)

        self.temperatura_minima_value = QLabel(self.centralwidget)
        self.temperatura_minima_value.setObjectName(u"temperatura_minima_value")
        self.temperatura_minima_value.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_minima_value)

        self.temperatura_promedio = QLabel(self.centralwidget)
        self.temperatura_promedio.setObjectName(u"temperatura_promedio")
        self.temperatura_promedio.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_promedio)

        self.temperatura_promedio_value = QLabel(self.centralwidget)
        self.temperatura_promedio_value.setObjectName(u"temperatura_promedio_value")
        self.temperatura_promedio_value.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_promedio_value)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.control_temperatura_label = QLabel(self.centralwidget)
        self.control_temperatura_label.setObjectName(u"control_temperatura_label")
        self.control_temperatura_label.setFont(font)

        self.verticalLayout.addWidget(self.control_temperatura_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toggleControl = QRadioButton(self.centralwidget)
        self.toggleControl.setObjectName(u"toggleControl")

        self.horizontalLayout_4.addWidget(self.toggleControl)

        self.toogleLazoAbierto = QRadioButton(self.centralwidget)
        self.toogleLazoAbierto.setObjectName(u"toogleLazoAbierto")

        self.horizontalLayout_4.addWidget(self.toogleLazoAbierto)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.actuador_label = QLabel(self.centralwidget)
        self.actuador_label.setObjectName(u"actuador_label")

        self.verticalLayout.addWidget(self.actuador_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.actuado_value = QSpinBox(self.centralwidget)
        self.actuado_value.setObjectName(u"actuado_value")

        self.horizontalLayout_7.addWidget(self.actuado_value)

        self.actuador_value_send = QPushButton(self.centralwidget)
        self.actuador_value_send.setObjectName(u"actuador_value_send")

        self.horizontalLayout_7.addWidget(self.actuador_value_send)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.temperatura_maxima_deseada_label = QLabel(self.centralwidget)
        self.temperatura_maxima_deseada_label.setObjectName(u"temperatura_maxima_deseada_label")
        self.temperatura_maxima_deseada_label.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_maxima_deseada_label)

        self.temperatura_maxima_deseada_value = QSpinBox(self.centralwidget)
        self.temperatura_maxima_deseada_value.setObjectName(u"temperatura_maxima_deseada_value")

        self.verticalLayout.addWidget(self.temperatura_maxima_deseada_value)

        self.temperatura_minima_deseada_label = QLabel(self.centralwidget)
        self.temperatura_minima_deseada_label.setObjectName(u"temperatura_minima_deseada_label")
        self.temperatura_minima_deseada_label.setFont(font1)

        self.verticalLayout.addWidget(self.temperatura_minima_deseada_label)

        self.tempertatura_minima_deseada_value = QSpinBox(self.centralwidget)
        self.tempertatura_minima_deseada_value.setObjectName(u"tempertatura_minima_deseada_value")

        self.verticalLayout.addWidget(self.tempertatura_minima_deseada_value)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.control_P_label = QLabel(self.centralwidget)
        self.control_P_label.setObjectName(u"control_P_label")
        self.control_P_label.setFont(font1)

        self.horizontalLayout_6.addWidget(self.control_P_label)

        self.control_P_value = QDoubleSpinBox(self.centralwidget)
        self.control_P_value.setObjectName(u"control_P_value")

        self.horizontalLayout_6.addWidget(self.control_P_value)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.control_I_label = QLabel(self.centralwidget)
        self.control_I_label.setObjectName(u"control_I_label")
        self.control_I_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.control_I_label)

        self.control_I_value = QDoubleSpinBox(self.centralwidget)
        self.control_I_value.setObjectName(u"control_I_value")

        self.horizontalLayout_5.addWidget(self.control_I_value)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.control_D_label = QLabel(self.centralwidget)
        self.control_D_label.setObjectName(u"control_D_label")
        self.control_D_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.control_D_label)

        self.control_D_value = QDoubleSpinBox(self.centralwidget)
        self.control_D_value.setObjectName(u"control_D_value")

        self.horizontalLayout_3.addWidget(self.control_D_value)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.send_button = QPushButton(self.centralwidget)
        self.send_button.setObjectName(u"send_button")

        self.verticalLayout.addWidget(self.send_button)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.toogleCSV = QRadioButton(self.centralwidget)
        self.toogleCSV.setObjectName(u"toogleCSV")

        self.verticalLayout.addWidget(self.toogleCSV)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1127, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aplicativo Hipertermia", None))
        self.image_rgb.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RGB), QCoreApplication.translate("MainWindow", u"RGB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Termica", None))
        self.parametros_termicos_label.setText(QCoreApplication.translate("MainWindow", u"Parametros termicos", None))
        self.temperatura_maxima.setText(QCoreApplication.translate("MainWindow", u"Temperatura maxima:", None))
        self.temperatura_maxima_value.setText(QCoreApplication.translate("MainWindow", u"43 \u00b0C", None))
        self.temperatura_minima.setText(QCoreApplication.translate("MainWindow", u"Temperatura minima:", None))
        self.temperatura_minima_value.setText(QCoreApplication.translate("MainWindow", u"30 \u00b0C", None))
        self.temperatura_promedio.setText(QCoreApplication.translate("MainWindow", u"Temperatura promedio", None))
        self.temperatura_promedio_value.setText(QCoreApplication.translate("MainWindow", u"35 \u00b0C", None))
        self.control_temperatura_label.setText(QCoreApplication.translate("MainWindow", u"Control de temperatura", None))
        self.toggleControl.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.toogleLazoAbierto.setText(QCoreApplication.translate("MainWindow", u"Lazo Abierto", None))
        self.actuador_label.setText(QCoreApplication.translate("MainWindow", u"Actuador", None))
        self.actuador_value_send.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.temperatura_maxima_deseada_label.setText(QCoreApplication.translate("MainWindow", u"Temperatura maxima deseada", None))
        self.temperatura_minima_deseada_label.setText(QCoreApplication.translate("MainWindow", u"Temperatura minima deseada", None))
        self.control_P_label.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.control_I_label.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.control_D_label.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.toogleCSV.setText(QCoreApplication.translate("MainWindow", u"Tomar datos CSV", None))
    # retranslateUi

