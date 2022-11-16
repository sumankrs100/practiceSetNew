from config.database import Database


class DBHelper:

    def __init__(self, db):
        self.db = db

    def select(self, tab_name):
        sql = "select * from %s" % tab_name
        with self.db.cur() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def insert(self, tab_name, data):
        args = [tab_name]
        args.extend(data.keys())
        args.extend(data.values())
        sql = "insert into %s (%s, %s, %s, %s) values ('%s', '%s', '%s', '%s')" % tuple(args)
        with self.db.cur() as cursor:
            cursor.execute(sql)

    def update(self, tab_name, last_name):
        sql = "update %s set last_name = '%s'" % (tab_name, last_name)
        with self.db.cur() as cursor:
            cursor.execute(sql)


