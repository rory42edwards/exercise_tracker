# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lifting_dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"../../assets/images/repdojo_clean_symbol_16x16.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* General */\n"
"QWidget {\n"
"    background-color: #121212;\n"
"    color: #E0E0E0;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"    background-color: #1F1F1F;\n"
"    border: 1px solid #F4A300;  /* orange */\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"    color: #E0E0E0;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2A2A2A;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C67C00;  /* deeper orange */\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #1F1F1F;\n"
"    border: 1px solid #4CAF50;  /* green */\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    color: #E0E0E0;\n"
"}\n"
"QComboBox:hover {\n"
"    background-color: #2A2A2A;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1F1F1F;\n"
"    border: 1px solid #4CAF50;\n"
"    selection-background-color: #4CAF50;\n"
"    color: #121212;\n"
"}\n"
"\n"
"/* SpinBox */\n"
"QSpinBox {\n"
"    ba"
                        "ckground-color: #1F1F1F;\n"
"    border: 1px solid #F4A300;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"    color: #E0E0E0;\n"
"}\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    background-color: #2A2A2A;\n"
"    border: none;\n"
"}\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #C67C00;\n"
"}\n"
"\n"
"/* LineEdit */\n"
"QLineEdit {\n"
"    background-color: #1F1F1F;\n"
"    border: 1px solid #F4A300;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    color: #E0E0E0;\n"
"}\n"
"\n"
"/* ToolTip */\n"
"QToolTip {\n"
"    background-color: #2A2A2A;\n"
"    color: #E0E0E0;\n"
"    border: 1px solid #F4A300;\n"
"    padding: 5px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* Shadows & Frames - emulated via borders where applicable */\n"
"QFrame {\n"
"    border: 1px solid #2A2A2A;\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.actionDark_Mode = QAction(MainWindow)
        self.actionDark_Mode.setObjectName(u"actionDark_Mode")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.graphHBoxLayout = QHBoxLayout()
        self.graphHBoxLayout.setObjectName(u"graphHBoxLayout")

        self.verticalLayout_2.addLayout(self.graphHBoxLayout)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_2.addWidget(self.spinBox)

        self.workoutHistorLabel = QLabel(self.centralwidget)
        self.workoutHistorLabel.setObjectName(u"workoutHistorLabel")

        self.verticalLayout_2.addWidget(self.workoutHistorLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.fromDateEdit = QDateEdit(self.centralwidget)
        self.fromDateEdit.setObjectName(u"fromDateEdit")

        self.horizontalLayout_2.addWidget(self.fromDateEdit)

        self.toDateEdit = QDateEdit(self.centralwidget)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setDate(QDate(2025, 1, 1))

        self.horizontalLayout_2.addWidget(self.toDateEdit)

        self.filterButton = QPushButton(self.centralwidget)
        self.filterButton.setObjectName(u"filterButton")

        self.horizontalLayout_2.addWidget(self.filterButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.workoutScrollArea = QScrollArea(self.centralwidget)
        self.workoutScrollArea.setObjectName(u"workoutScrollArea")
        self.workoutScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 765, 97))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.workoutTableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.workoutTableWidget.setObjectName(u"workoutTableWidget")

        self.verticalLayout.addWidget(self.workoutTableWidget)

        self.workoutScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.workoutScrollArea)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 32))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuView_2 = QMenu(self.menubar)
        self.menuView_2.setObjectName(u"menuView_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuView_2.menuAction())
        self.menuView_2.addAction(self.actionDark_Mode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RepDojo", None))
        self.actionDark_Mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Week", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2 Weeks", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Month", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3 Months", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"6 Months", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Year", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Time Range", None))
        self.workoutHistorLabel.setText(QCoreApplication.translate("MainWindow", u"Workout History", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView_2.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

