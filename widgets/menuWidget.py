# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates_ui/menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MenuWidget(QWidget):
    def __init__(self, parent=None):
        super(MenuWidget, self).__init__(parent)

        self.setupUi(self);

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 524)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMouseTracking(False)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.label = QLabel(Form)
        self.label.setMinimumSize(QSize(250, 50))
        self.label.setMaximumSize(QSize(200, 64))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quizBtn = QPushButton(Form)
        self.quizBtn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quizBtn.sizePolicy().hasHeightForWidth())
        self.quizBtn.setSizePolicy(sizePolicy)
        self.quizBtn.setMinimumSize(QSize(250, 50))
        self.quizBtn.setMaximumSize(QSize(250, 50))
        font = QFont()
        font.setPointSize(16)
        self.quizBtn.setFont(font)
        self.quizBtn.setObjectName("quizBtn")
        self.verticalLayout.addWidget(self.quizBtn)
        self.freeBtn = QPushButton(Form)
        self.freeBtn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freeBtn.sizePolicy().hasHeightForWidth())
        self.freeBtn.setSizePolicy(sizePolicy)
        self.freeBtn.setMinimumSize(QSize(250, 50))
        self.freeBtn.setMaximumSize(QSize(250, 50))
        font = QFont()
        font.setPointSize(16)
        self.freeBtn.setFont(font)
        self.freeBtn.setObjectName("freeBtn")
        self.verticalLayout.addWidget(self.freeBtn)
        self.abotBtn = QPushButton(Form)
        self.abotBtn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abotBtn.sizePolicy().hasHeightForWidth())
        self.abotBtn.setSizePolicy(sizePolicy)
        self.abotBtn.setMinimumSize(QSize(250, 50))
        self.abotBtn.setMaximumSize(QSize(250, 50))
        font = QFont()
        font.setPointSize(16)
        self.abotBtn.setFont(font)
        self.abotBtn.setObjectName("abotBtn")
        self.verticalLayout.addWidget(self.abotBtn)
        self.exitBtn = QPushButton(Form)
        self.exitBtn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setMinimumSize(QSize(250, 50))
        self.exitBtn.setMaximumSize(QSize(250, 50))
        font = QFont()
        font.setPointSize(16)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout.addWidget(self.exitBtn)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">EmoTrainer</span></p></body></html>"))
        self.quizBtn.setText(_translate("Form", "Определить эмоцию"))
        self.freeBtn.setText(_translate("Form", "Выразить Эмоцию"))
        self.abotBtn.setText(_translate("Form", "О программе"))
        self.exitBtn.setText(_translate("Form", "Выйти"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = MenuWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
