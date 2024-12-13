import sqlite3

def connect():
    cnx = sqlite3.connect("../database.db")
    cursor = cnx.cursor()
    return cnx, cursor


def close(connection, cursor):
    cursor.close()
    connection.commit()
    connection.close()


connection, curs = connect()

curs.execute('''CREATE TABLE IF NOT EXISTS `Users_types` (
  `type_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `user_type` VARCHAR(255) DEFAULT NULL)''')

curs.execute('''CREATE TABLE IF NOT EXISTS `Users` (
  `id_user` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `type_user` INTEGER NOT NULL,
  `username_user` VARCHAR(255) NOT NULL,
  `password_user` VARCHAR(255) NOT NULL,
  `mail_user` VARCHAR(255),
  `phone_number_user` VARCHAR(255),
  `clicks_amount` INTEGER NOT NULL DEFAULT '0',
  `pure_clicks_amount` INTEGER NOT NULL DEFAULT '0',
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`type_user`) REFERENCES `Users_types` (`type_id`))''')

curs.execute('''CREATE TABLE IF NOT EXISTS `Bans` (
  `id_bans` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `user_id_bans` INTEGER NOT NULL,
  `time_bans` TIME NOT NULL,
  `appeal_bans` INTEGER NOT NULL,
  `text_appeal_bans` INTEGER NOT NULL,
  `reason_bans` text NOT NULL,
  CONSTRAINT `bans_ibfk_1` FOREIGN KEY (`user_id_bans`) REFERENCES `Users` (`id_user`))''')

curs.execute('''CREATE TABLE IF NOT EXISTS `Leveling` (
  `id_leveling` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  `id_user_leveling` TINYINTEGER NOT NULL,
  `souls_per_click_leveling` INTEGER NOT NULL,
  `bottle_buy_leveling` TINYINTEGER NOT NULL DEFAULT '0',
  `eul_buy_leveling` TINYINTEGER NOT NULL DEFAULT '0',
  `blink_buy_leveling` TINYINTEGER NOT NULL DEFAULT '0',
  `bkb_buy_leveling` TINYINTEGER NOT NULL DEFAULT '0',
  CONSTRAINT `leveling_ibfk_1` FOREIGN KEY (`id_user_leveling`) REFERENCES `Users` (`id_user`))''')

curs.execute('''CREATE TABLE IF NOT EXISTS `Session` (
  `id_session` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  `user_id_session` INTEGER NOT NULL,
  `time_session` INTEGER NOT NULL DEFAULT '0',
  `pure_clicks_session` INTEGER NOT NULL DEFAULT '0',
  `online_session` INTEGER NOT NULL DEFAULT '1',
    CONSTRAINT `session_ibfk_1` FOREIGN KEY (`user_id_session`) REFERENCES `Users` (`id_user`))''')


curs.execute('''CREATE TABLE IF NOT EXISTS`Statistic_type` (
  `id_statistic_type` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `statistic_type` VARCHAR(255) NOT NULL)''')

curs.execute('''CREATE TABLE IF NOT EXISTS `Statistic` (
  `id_statistic` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `id_type_statistic` INTEGER NOT NULL,
  `time_statistic` DATE NOT NULL,
  `value_statistic` INTEGER NOT NULL)''')


def insert_on_create():
    curs.execute("INSERT INTO Users(type_user, username_user, password_user, mail_user, phone_number_user) "
                 "VALUES (?,?,?,?,?)", (1, 2, 2, 2, 2))
    curs.execute("""INSERT INTO Statistic_type (statistic_type) VALUES (?)""", ("Общее кол-во пользователей",))
    curs.execute("""INSERT INTO Statistic_type (statistic_type) VALUES (?)""", ("Текущий онлайн",))
    curs.execute("""INSERT INTO Statistic_type (statistic_type) VALUES (?)""", ("Среднее время онлайна",))
    curs.execute('''INSERT INTO Users_types (user_type) VALUES (?)''', ("admin",))
    curs.execute('''INSERT INTO Users_types (user_type) VALUES (?)''', ("user",))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
    """,(1,"2024-12-15", 1))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-12-15", 10))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-12-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-12-21", 40))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-12-08", 21))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-12-08", 2))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-11-15", 1))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-11-15", 10))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-11-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2024-12-21", 40))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-12-08", 21))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2024-12-08", 2))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-10-15", 1))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-10-15", 10))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-10-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-10-21", 32))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2023-10-15", 42))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2023-10-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2023-10-21", 100))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (1, "2022-10-15", 42))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (1, "2022-10-21", 24))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (1, "2022-10-21", 123))
    curs.execute("INSERT INTO Users(type_user, username_user, password_user, mail_user, phone_number_user) "
                 "VALUES (?,?,?,?,?)", (1, 2, 2, 2, 2))
    curs.execute("""INSERT INTO Statistic_type (statistic_type) VALUES (?)""", ("Общее кол-во пользователей",))
    curs.execute("""INSERT INTO Statistic_type (statistic_type) VALUES (?)""", ("Текущий онлайн",))
    curs.execute("""INSERT INTO Statistic_type (statistic_type) VALUES (?)""", ("Среднее время онлайна",))
    curs.execute('''INSERT INTO Users_types (user_type) VALUES (?)''', ("admin",))
    curs.execute('''INSERT INTO Users_types (user_type) VALUES (?)''', ("user",))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
    """,(1,"2024-12-15", 1))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-12-15", 10))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-12-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-12-21", 40))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-12-08", 21))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-12-08", 2))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-11-15", 1))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-11-15", 10))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-11-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2024-12-21", 40))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-12-08", 21))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2024-12-08", 2))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (1, "2024-10-15", 1))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-10-15", 10))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-10-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (1, "2024-10-21", 32))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2023-10-15", 42))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2023-10-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (1, "2023-10-21", 100))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (1, "2022-10-15", 42))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (1, "2022-10-21", 24))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (1, "2022-10-21", 123))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
        """, (2, "2024-12-15", 1))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (2, "2024-12-15", 2))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (2, "2024-12-21", 3))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (2, "2024-12-21", 12))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (2, "2024-12-08", 11))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (2, "2024-12-08", 3))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (2, "2024-11-15", 4))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (2, "2024-11-15", 5))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (2, "2024-11-21", 6))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (2, "2024-12-21", 7))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (2, "2024-12-08", 8))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (2, "2024-12-08", 9))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (2, "2024-10-15", 5))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (2, "2024-10-15", 3))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (2, "2024-10-21", 10))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (2, "2024-10-21", 12))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (2, "2023-10-15", 10))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (2, "2023-10-21", 3))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (2, "2023-10-21", 11))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                        """, (2, "2022-10-15", 11))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                        """, (2, "2022-10-21", 22))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                        """, (2, "2022-10-21", 32))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
            """, (3, "2024-12-15", 21))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (3, "2024-12-15", 21))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (3, "2024-12-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (3, "2024-12-21", 33))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (3, "2024-12-08", 53))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (3, "2024-12-08", 43))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (3, "2024-11-15", 11))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (3, "2024-11-15", 11))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (3, "2024-11-21", 11))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                        """, (3, "2024-12-21", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (3, "2024-12-08", 32))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                        """, (3, "2024-12-08", 12))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                """, (3, "2024-10-15", 55))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (3, "2024-10-15", 53))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (3, "2024-10-21", 24))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                    """, (3, "2024-10-21", 32))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                        """, (3, "2023-10-15", 14))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                        """, (3, "2023-10-21", 42))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                        """, (3, "2023-10-21", 50))

    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                            """, (3, "2022-10-15", 11))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                            """, (3, "2022-10-21", 22))
    curs.execute("""INSERT INTO Statistic(id_type_statistic, time_statistic, value_statistic) VALUES (?,?,?)
                            """, (3, "2022-10-21", 32))

close(connection, curs)




