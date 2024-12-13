from PySide6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon
from ui import ui_main_window
import data_base
from graph_window import Graph
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import time
import arrow


class MainWindow(QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.application = app
        self.this_window = self
        self.hide()
        self.setupUi(self)

    def setupUi(self, main):
        super().setupUi(main)
        self.setWindowTitle("Графики")
        self.setWindowIcon(QIcon("main.jpg"))
        self.bottle_button.clicked.connect(self.bottle_buy)
        self.eul_button.clicked.connect(self.eul_buy)
        self.blink_button.clicked.connect(self.blink_buy)
        self.bkb_button.clicked.connect(self.bkb_buy)
        self.graf_users.clicked.connect(self.graf_users_show)
        self.graf_online.clicked.connect(self.graf_online_show)
        self.graf_avg.clicked.connect(self.graf_avg_show)


        self.user_clicker.hide()
        self.admin_window.hide()

    # Функция отображения окна администратора
    def show_admin_window(self):
        self.user_clicker.setDisabled(True)
        self.user_clicker.close()
        self.show()
        self.admin_window.show()

        sort = self.sort_all_users()
        self.font2 = QFont()
        self.font2.setPointSize(14)
        self.font2.setBold(True)
        num_user = 0
        self.vert_layout = QVBoxLayout()
        self.vert_layout.addWidget(self.description)
        for i in sort:
            num_user += 1
            new_layout = QHBoxLayout()
            user = QWidget()
            label = QLabel()
            label.setFixedSize(228, 59)
            label.setText(str(num_user))
            label.setFont(self.font2)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            new_layout.addWidget(label)

            label2 = QLabel()
            label2.setFixedSize(228, 59)
            label2.setText(str(i[0]))
            label2.setFont(self.font2)
            label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            new_layout.addWidget(label2)

            label3 = QLabel()
            label3.setFixedSize(227, 59)
            label3.setText(str(i[1]))
            label3.setFont(self.font2)
            label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
            new_layout.addWidget(label3)

            label4 = QLabel()
            label4.setFixedSize(228, 59)
            label4.setText(str(i[2]))
            label4.setFont(self.font2)
            label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
            new_layout.addWidget(label4)

            user.setLayout(new_layout)
            self.vert_layout.addWidget(user)

        full = QWidget()
        full.setLayout(self.vert_layout)
        self.scrollArea_3.setWidget(full)

        # Сбор статистики пользователей
        connection, cursor = data_base.connect()

        amount_users = str(cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0])
        self.us_amount.setText(amount_users)

        online_us = str(cursor.execute("SELECT SUM(online_session) FROM Session").fetchone()[0])
        self.now_online.setText(online_us)

        avg_time = str(cursor.execute("SELECT AVG(time_session) FROM Session").fetchone()[0])
        self.avg_session_time.setText(avg_time)

        banned_users = str(cursor.execute("SELECT COUNT(*) FROM Bans").fetchone()[0])
        self.banned_users_amount.setText(banned_users)

        pure_clicks = str(cursor.execute("SELECT SUM(pure_clicks_amount) FROM Users").fetchone()[0])
        self.pure_clicks_amount.setText(pure_clicks)

        avg_pure = str(cursor.execute("SELECT AVG(pure_clicks_session) FROM Session").fetchone()[0])
        self.avg_pure_clicks.setText(avg_pure)

        sum_souls = str(cursor.execute("SELECT SUM(clicks_amount) FROM Users").fetchone()[0])
        self.all_souls.setText(sum_souls)

        bottle = str(cursor.execute("SELECT SUM(bottle_buy_leveling) FROM Leveling").fetchone()[0])
        self.bottle_bought.setText(bottle)

        eul = str(cursor.execute("SELECT SUM(eul_buy_leveling) FROM Leveling").fetchone()[0])
        self.euls_bought.setText(eul)

        blink = str(cursor.execute("SELECT SUM(blink_buy_leveling) FROM Leveling").fetchone()[0])
        self.blink_bought.setText(blink)

        bkb = str(cursor.execute("SELECT SUM(bkb_buy_leveling) FROM Leveling").fetchone()[0])
        self.bkb_bouth_amount.setText(bkb)

        data_base.close(connection, cursor)

        self.admin_window.show()

    def graf_users_show(self):
        Graph(1, "Пользователей")

    def graf_online_show(self):
        Graph(2, "Пользователей онлайн")

    def graf_avg_show(self):
        Graph(3, "Минут")

    # Функция отображения окна обычного пользователя
    def show_clicker(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.start_time = time.time()
        self.pure_click = 0
        self.admin_window.hide()

        print(f"Пользователь: {user_id}-{username}")

        # Получение данных о пользователе (кол-во игровой валюты, начисление игровой валюты за клик
        # и данные о прокачке
        connection, cursor = data_base.connect()
        cursor.execute(f"SELECT clicks_amount FROM `Users` WHERE id_user = {self.user_id}")
        self.clicks = int(cursor.fetchone()[0])
        cursor.execute(f"SELECT souls_per_click_leveling, bottle_buy_leveling, eul_buy_leveling, blink_buy_leveling, "
                       f"bkb_buy_leveling FROM Leveling WHERE id_user_leveling = {self.user_id}")
        level = cursor.fetchall()[0]
        self.soul_per_click = int(level[0])
        cursor.close()
        print(f"Всего кликов: {self.clicks} \t Душ за клик: {self.soul_per_click}")
        print(f"Прокачка: {level[1:]}")

        # Создание записи о сессии пользователя и получение id сессии
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Session (user_id_session) VALUES (?)", (self.user_id,))
        cursor.close()
        cursor = connection.cursor()
        cursor.execute("SELECT id_session FROM Session WHERE user_id_session = ? ORDER BY id_session DESC LIMIT 1",
                       (self.user_id,))
        self.id_session = int(cursor.fetchone()[0])
        data_base.close(connection, cursor)
        print(f"ID данной сессии: {self.id_session}")

        # Определение включения/отключения кнопок в магазине
        widgets_button = [self.bottle_button, self.eul_button, self.blink_button, self.bkb_button]
        for i in range(len(widgets_button)):
            if level[i + 1] == 1:
                widgets_button[i].setDisabled(True)
                widgets_button[i].setText("Куплено")
        self.clicks_amount.setText(str(self.clicks))
        self.click_button.clicked.connect(self.click)

        # Сортировка топа пользователей
        sort = self.sort_all_users()
        self.font2 = QFont()
        self.font2.setPointSize(14)
        self.font2.setBold(True)
        num_user = 0
        self.vert_layout = QVBoxLayout()
        self.vert_layout.addWidget(self.description)
        for i in sort:
            self.label_3.setTextFormat(Qt.TextFormat.AutoText)
            self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
            num_user += 1
            self.new_layout = QHBoxLayout()
            self.new_layout.addWidget(self.description)
            user = QWidget()
            label = QLabel()
            label.setFixedSize(228, 59)
            label.setText(str(num_user))
            label.setFont(self.font2)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.new_layout.addWidget(label)

            label2 = QLabel()
            label2.setFixedSize(228, 59)
            label2.setText(str(i[0]))
            label2.setFont(self.font2)
            label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.new_layout.addWidget(label2)

            label3 = QLabel()
            label3.setFixedSize(227, 59)
            label3.setText(str(i[1]))
            label3.setFont(self.font2)
            label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.new_layout.addWidget(label3)

            label4 = QLabel()
            label4.setFixedSize(228, 59)
            label4.setText(str(i[2]))
            label4.setFont(self.font2)
            label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.new_layout.addWidget(label4)

            user.setLayout(self.new_layout)
            self.vert_layout.addWidget(user)

        full = QWidget()
        full.setLayout(self.vert_layout)
        self.scrollArea.setWidget(full)
        self.show()
        self.user_clicker.show()

    # Засчитывание клика и обновление информации в базе
    def click(self):
        self.pure_click = 1
        self.clicks += self.soul_per_click
        self.clicks_amount.setText(str(self.clicks))

        connection, cursor = data_base.connect()
        cursor.execute(f"UPDATE Users SET pure_clicks_amount=pure_clicks_amount+1 WHERE id_user={self.user_id}")
        cursor.execute(f"UPDATE `Users` SET clicks_amount=clicks_amount+{self.soul_per_click} "
                       f"WHERE id_user={self.user_id}")
        data_base.close(connection, cursor)
        print(f"Клик засчитан \t Клики без модификаторов: {self.pure_click} \t Души: {self.soul_per_click}")

    def bottle_buy(self):

        if self.clicks >= 25:
            connection, cursor = data_base.connect()
            cursor.execute("UPDATE Leveling SET bottle_buy_leveling = ? WHERE id_user_leveling = ?",
                           (1, self.user_id))
            cursor.execute("UPDATE Leveling SET souls_per_click_leveling = souls_per_click_leveling + ? WHERE "
                           "id_user_leveling = ?", (1, self.user_id))
            cursor.execute(f"UPDATE Users SET clicks_amount = clicks_amount-{25}")
            data_base.close(connection, cursor)

            self.soul_per_click += 1
            self.clicks -= 25
            self.clicks_amount.setText(str(self.clicks))
            self.bottle_button.setDisabled(True)
            self.bottle_button.setText("Куплено")
            self.buy_widget_scroll.update()
        else:
            print("no")

    def eul_buy(self):

        if self.clicks >= 50:
            connection, cursor = data_base.connect()
            cursor.execute("UPDATE Leveling SET eul_buy_leveling = ? WHERE id_user_leveling = ?",
                           (1, self.user_id))
            cursor.execute("UPDATE Leveling SET souls_per_click_leveling = souls_per_click_leveling + ? WHERE "
                           "id_user_leveling = ?", (5, self.user_id))
            cursor.execute(f"UPDATE Users SET clicks_amount = clicks_amount-{50}")

            data_base.close(connection, cursor)
            self.soul_per_click += 5
            self.clicks -= 50
            self.clicks_amount.setText(str(self.clicks))
            self.eul_button.setDisabled(True)
            self.eul_button.setText("Куплено")
            self.buy_widget_scroll.update()

    def blink_buy(self):

        if self.clicks >= 100:
            connection, cursor = data_base.connect()
            cursor.execute("UPDATE Leveling SET blink_buy_leveling = ? WHERE id_user_leveling = ?",
                           (1, self.user_id))
            cursor.execute("UPDATE Leveling SET souls_per_click_leveling = souls_per_click_leveling + ? WHERE "
                           "id_user_leveling = ?", (10, self.user_id))
            cursor.execute(f"UPDATE Users SET clicks_amount = clicks_amount-{100}")

            data_base.close(connection, cursor)
            self.soul_per_click += 10
            self.clicks -= 100
            self.clicks_amount.setText(str(self.clicks))
            self.blink_button.setDisabled(True)
            self.blink_button.setText("Куплено")
            self.buy_widget_scroll.update()

    def bkb_buy(self):

        if self.clicks >= 1000:
            connection, cursor = data_base.connect()
            cursor.execute("UPDATE Leveling SET bkb_buy_leveling = ? WHERE id_user_leveling = ?",
                           (1, self.user_id))
            cursor.execute("UPDATE Leveling SET souls_per_click_leveling = souls_per_click_leveling + ? WHERE "
                           "id_user_leveling = ?", (50, self.user_id))
            cursor.execute(f"UPDATE Users SET clicks_amount = clicks_amount-{1000}")
            data_base.close(connection, cursor)

            self.soul_per_click += 50
            self.clicks -= 1000
            self.clicks_amount.setText(str(self.clicks))
            self.bkb_button.setDisabled(True)
            self.bkb_button.setText("Куплено")
            self.buy_widget_scroll.update()

    # События при закрытии окна
    def closeEvent(self, event):
        if self.user_clicker.isVisible():
            self.end_time = time.time()
            self.exe_time = int(self.end_time - self.start_time)

            connection, cursor = data_base.connect()

            cursor.execute("UPDATE Session SET time_session = ?, pure_clicks_session = ?, online_session = ? WHERE "
                           "user_id_session = ? AND id_session = ?",
                           (self.exe_time, self.pure_click, 0, self.user_id, self.id_session))
            connection.commit()

            cursor.execute("SELECT AVG(time_session) FROM Session")
            avg_time = int(cursor.fetchone()[0])
            cursor.execute("INSERT INTO Statistic (id_type_statistic, time_statistic, value_statistic) VALUES (?, "
                           "?, ?)", (3, arrow.utcnow().format(), avg_time))

            data_base.close(connection, cursor)
            event.accept()

    # Функция сортировки пользователей по количеству игровой валюты
    def sort_all_users(self):
        connection, cursor = data_base.connect()
        cursor.execute(f"SELECT Users.username_user, Users.clicks_amount, Leveling.souls_per_click_leveling FROM Users "
                       f"JOIN Leveling ON Leveling.id_user_leveling = Users.id_user")
        all_users = cursor.fetchall()
        data_base.close(connection, cursor)

        users = []
        for user in all_users:
            new_user = []
            for i in range(len(user)):
                new_user.append(user[i])
            users.append(new_user)

        sort = sorted(users, key=lambda clicks: clicks[1])
        sort.reverse()
        return sort

