"""Класс для работы с базой данных"""
import sqlite3


class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с бд"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем наличие юзера в БД"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Получаем id юзера в БД по его user_id в телеграмм"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchall()[0]

    def add_user(self, user_id):
        """Добавляем юзера в БД"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_record(self, user_id, operation, value):
        """Создаём запись операции расхода/дохода"""
        self.cursor.execute("INSERT INTO `records` (`user_id`, `operation`, `value`) VALUES (?, ?, ?)",
                            (user_id,
                             operation == "+",
                             value,))
        return self.conn.commit()

    def get_history(self, user_id, within = 'all'):
        """Получаем историю за день, месяц или год"""

        if within == 'day':
            result = self.cursor.execute(
                "SELECT * "
                "FROM `records` "
                "WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of day')"
                "AND datetime('now', 'localtime')"
                "ORDER BY `date`",
                (user_id,)
            )
        elif within == 'month':
            result = self.cursor.execute(
                "SELECT * "
                "FROM `records` "
                "WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of month')"
                "AND datetime('now', 'localtime')"
                "ORDER BY `date`",
                (user_id,)
            )
        elif within == 'year':
            result = self.cursor.execute(
                "SELECT * "
                "FROM `records` "
                "WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of year')"
                "AND datetime('now', 'localtime')"
                "ORDER BY `date`",
                (user_id,)
            )
        else:
            result = self.cursor.execute(
                "SELECT * "
                "FROM `records` "
                "WHERE `user_id` = ? "
                "ORDER BY `date`",
                (user_id,)
            )
        return result.fetchall()

    def close(self):
        """Завершение работы с БД"""
        self.conn.close()
