# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Auth(object):
    def setupUi(self, Auth):
        if not Auth.objectName():
            Auth.setObjectName(u"Auth")
        Auth.resize(400, 300)
        self.auth = QWidget(Auth)
        self.auth.setObjectName(u"auth")
        self.auth.setGeometry(QRect(30, 40, 331, 211))
        self.verticalLayout = QVBoxLayout(self.auth)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.username_label = QLabel(self.auth)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setMinimumSize(QSize(120, 25))
        self.username_label.setMaximumSize(QSize(120, 25))
        self.username_label.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.verticalLayout.addWidget(self.username_label)

        self.username_input = QLineEdit(self.auth)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(240, 25))
        self.username_input.setMaximumSize(QSize(240, 25))
        self.username_input.setSizeIncrement(QSize(0, 0))
        self.username_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.username_input.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid rgb(24, 24, 24);")

        self.verticalLayout.addWidget(self.username_input)

        self.password_label = QLabel(self.auth)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMinimumSize(QSize(60, 25))
        self.password_label.setMaximumSize(QSize(60, 25))
        self.password_label.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(self.auth)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(240, 25))
        self.password_input.setMaximumSize(QSize(240, 25))
        self.password_input.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid rgb(24, 24, 24);")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.password_input)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.auth_button = QPushButton(self.auth)
        self.auth_button.setObjectName(u"auth_button")
        self.auth_button.setMinimumSize(QSize(120, 25))
        self.auth_button.setMaximumSize(QSize(100, 30))
        self.auth_button.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.auth_button)

        self.to_reg_button = QPushButton(self.auth)
        self.to_reg_button.setObjectName(u"to_reg_button")
        self.to_reg_button.setMinimumSize(QSize(120, 25))
        self.to_reg_button.setMaximumSize(QSize(100, 16777215))
        self.to_reg_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.to_reg_button.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255)")

        self.horizontalLayout.addWidget(self.to_reg_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.reg = QWidget(Auth)
        self.reg.setObjectName(u"reg")
        self.reg.setGeometry(QRect(30, 20, 351, 231))
        self.verticalLayoutWidget = QWidget(self.reg)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 321, 221))
        self.lay = QVBoxLayout(self.verticalLayoutWidget)
        self.lay.setObjectName(u"lay")
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.new_user = QLabel(self.verticalLayoutWidget)
        self.new_user.setObjectName(u"new_user")
        self.new_user.setMinimumSize(QSize(140, 30))
        self.new_user.setMaximumSize(QSize(140, 30))
        self.new_user.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"margin-left: 3px;\n"
"margin-top: 3px;")

        self.lay.addWidget(self.new_user)

        self.reg_username_input = QLineEdit(self.verticalLayoutWidget)
        self.reg_username_input.setObjectName(u"reg_username_input")
        self.reg_username_input.setMinimumSize(QSize(160, 0))
        self.reg_username_input.setMaximumSize(QSize(200, 16777215))
        self.reg_username_input.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid rgb(24, 24, 24);\n"
"padding: 3px;\n"
"margin-left: 10px")
        self.reg_username_input.setMaxLength(32767)
        self.reg_username_input.setCursorPosition(0)

        self.lay.addWidget(self.reg_username_input)

        self.reg_mail_input = QLineEdit(self.verticalLayoutWidget)
        self.reg_mail_input.setObjectName(u"reg_mail_input")
        self.reg_mail_input.setMinimumSize(QSize(160, 0))
        self.reg_mail_input.setMaximumSize(QSize(200, 16777215))
        self.reg_mail_input.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid rgb(24, 24, 24);\n"
"padding: 3px;\n"
"margin-left: 10px")
        self.reg_mail_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.reg_mail_input.setEchoMode(QLineEdit.EchoMode.Normal)

        self.lay.addWidget(self.reg_mail_input)

        self.reg_phone_number_input = QLineEdit(self.verticalLayoutWidget)
        self.reg_phone_number_input.setObjectName(u"reg_phone_number_input")
        self.reg_phone_number_input.setMaximumSize(QSize(200, 16777215))
        self.reg_phone_number_input.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid rgb(24, 24, 24);\n"
"padding: 3px;\n"
"margin-left: 10px")

        self.lay.addWidget(self.reg_phone_number_input)

        self.reg_password_input = QLineEdit(self.verticalLayoutWidget)
        self.reg_password_input.setObjectName(u"reg_password_input")
        self.reg_password_input.setMaximumSize(QSize(200, 16777215))
        self.reg_password_input.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid rgb(24, 24, 24);\n"
"padding: 3px;\n"
"margin-left: 10px")
        self.reg_password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.lay.addWidget(self.reg_password_input)

        self.registration_button = QPushButton(self.verticalLayoutWidget)
        self.registration_button.setObjectName(u"registration_button")
        self.registration_button.setMaximumSize(QSize(150, 30))
        self.registration_button.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);\n"
"margin-left: 3px;\n"
"margin-top: 3px;")
        self.registration_button.setAutoDefault(True)

        self.lay.addWidget(self.registration_button)


        self.retranslateUi(Auth)

        QMetaObject.connectSlotsByName(Auth)
    # setupUi

    def retranslateUi(self, Auth):
        Auth.setWindowTitle(QCoreApplication.translate("Auth", u"Dialog", None))
        self.username_label.setText(QCoreApplication.translate("Auth", u"<html><head/><body><p align=\"center\">\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</p></body></html>", None))
        self.password_label.setText(QCoreApplication.translate("Auth", u"<html><head/><body><p align=\"center\">\u041f\u0430\u0440\u043e\u043b\u044c</p></body></html>", None))
        self.auth_button.setText(QCoreApplication.translate("Auth", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.to_reg_button.setText(QCoreApplication.translate("Auth", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.new_user.setText(QCoreApplication.translate("Auth", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.reg_username_input.setInputMask("")
        self.reg_username_input.setText("")
        self.reg_username_input.setPlaceholderText(QCoreApplication.translate("Auth", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.reg_mail_input.setText("")
        self.reg_mail_input.setPlaceholderText(QCoreApplication.translate("Auth", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.reg_phone_number_input.setText("")
        self.reg_phone_number_input.setPlaceholderText(QCoreApplication.translate("Auth", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.reg_password_input.setText("")
        self.reg_password_input.setPlaceholderText(QCoreApplication.translate("Auth", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.registration_button.setText(QCoreApplication.translate("Auth", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

