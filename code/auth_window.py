from ui import ui_auth_reg_window
import data_base
from PySide6.QtWidgets import QDialog, QMessageBox
import arrow


# Окно авторизации
class AuthWindow(QDialog, ui_auth_reg_window.Ui_Auth):
    # Запуск окна авторизации
    def __init__(self, main, parent=None):
        super(AuthWindow, self).__init__(parent)
        self.main = main
        self.setupUi(self)
        self.exec()

    # Переопределение базовой функции класса с определением кнопок
    def setupUi(self, dialog):
        super().setupUi(dialog)
        self.auth_button.clicked.connect(self.authorization)
        self.to_reg_button.clicked.connect(self.reg_open)
        self.registration_button.clicked.connect(self.registration)
        self.reg.hide()

    # Кнопка регистрации в окне авторизации
    def reg_open(self):
        self.auth.hide()
        self.reg.show()

    # Кнопка авторизации
    def authorization(self):
        user_data = []
        us_name = self.username_input.text()
        us_password = self.password_input.text()

        connection, cursor = data_base.connect()
        check = cursor.execute(f"SELECT EXISTS(SELECT * FROM Users WHERE username_user = ?)", (us_name,)).fetchone()[0]
        if check:
            user_data = list(cursor.execute(f"SELECT id_user, type_user, password_user FROM Users WHERE username_user = ?",
                                            (us_name,)).fetchone())
            print(user_data)
            if user_data[2] == us_password:
                if user_data[1] == 1:
                    self.main.show_admin_window()

                    online = cursor.execute("SELECT COUNT(*) FROM Session WHERE online_session = 1").fetchone()[0]
                    cursor.execute("INSERT INTO Statistic (id_type_statistic, time_statistic, value_statistic)"
                                    "VALUES (?,?,?)", (2, arrow.utcnow().format("YYYY-MM-DD"), online))
                    data_base.close(connection, cursor)
                else:
                    self.main.show_clicker(user_data[0], us_name)
                self.close()
                return
            else:
                self.error_window("Ошибка", "Неверное имя пользователя или пароль")

    # Кнопка регистрации
    def registration(self):
        username = self.reg_username_input.text()
        mail = self.reg_mail_input.text()
        phone_number = self.reg_phone_number_input.text()
        password = self.reg_password_input.text()

        connection, cursor = data_base.connect()
        check = cursor.execute(f"SELECT EXISTS(SELECT * FROM Users WHERE username_user = ?)", (username,)).fetchone()[0]
        if not check:
            check = cursor.execute(f"SELECT EXISTS(SELECT * FROM Users WHERE mail_user = ?)", (mail,)).fetchone()[0]
            cursor.close()
            if not check:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO Users  "
                               "(type_user, username_user, password_user, mail_user, phone_number_user) "
                               "VALUES (?, ?, ?, ?, ?)",  (2, username, password, mail, phone_number))
                connection.commit()
                cursor.close()

                cursor = connection.cursor()
                id = cursor.execute("SELECT id_user FROM Users WHERE username_user = ?",
                                    (username,)).fetchone()[0]
                cursor.execute(f"INSERT INTO Leveling (id_user_leveling, souls_per_click_leveling) VALUES (?, "
                               f"?)", (id, 1))

                count_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0]
                cursor.execute(f"INSERT INTO Statistic (id_type_statistic, time_statistic, value_statistic)"
                               f" VALUES (?,?,?)", (1, arrow.utcnow().format("YYYY-MM-DD"), count_users))
                data_base.close(connection, cursor)
                print()

                accept = QMessageBox()
                accept.setWindowTitle("Успешно")
                accept.setText("Пользователь зарегистрирован")
                accept.setIcon(QMessageBox.Information)
                accept.addButton(accept.StandardButton.Ok)
                accept.exec_()
                self.reg.hide()
                self.auth.show()
                return
            else:
                self.error_window("Ошибка", "Адрес почты уже зарегистрирован")

        else:
            self.error_window("Ошибка", "Пользователь с таким никнеймом уже существует")

    # Окно-уведомление
    def error_window(self, title, message):
        error = QMessageBox()
        error.setWindowTitle(title)
        error.setText(message)
        error.setIcon(QMessageBox.Warning)
        error.addButton(error.StandardButton.Ok)
        error.exec_()