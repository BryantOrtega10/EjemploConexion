from app.datos.Connector import Connector
import mysql.connector

class MysqlConnection(Connector):
    
    def __init__(self):
        self.__connector = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="rotonda"
        )
        self.__cursor = self.__connector.cursor()


    def select(self, fields=["*"], tables=[], where="", values={} , order_by=[], group_by=[], from_s=0, limit=None):
        sql = "SELECT " + (','.join(fields)) + " FROM " + (','.join(tables)) 
        
        if where != "":
            sql += " WHERE " + where
        if len(group_by) > 0:
            sql += " GROUP BY " + (','.join(group_by))
        if len(order_by) > 0:
            sql += " ORDER BY " + (','.join(order_by))
        if limit is not None:
            sql += " LIMIT " + str(limit)
        if from_s > 0:
            sql += " OFFSET " + str(from_s)
        print(sql)
        self.__cursor.execute(sql,values)

        return self.__cursor.fetchall()


    def update(self, table, update=[], where="", values={}):
        sql = "UPDATE " + table + " SET " + (','.join(upd+"=%("+upd+")s" for upd in update)) + " WHERE " + where
        self.__cursor.execute(sql, values)
        return self.__cursor.rowcount


    def insert(self, table, insert={}):
        sql = "INSERT INTO " + table + " (" + (','.join(insert.keys())) + ") VALUES(" +\
               (','.join("%("+ins+")s" for ins in insert.keys())) + ")"

        print(sql, insert)
        self.__cursor.execute(sql, insert)
        return self.__cursor.rowcount


    def delete(self, table, where="", values={}):
        sql = "DELETE FROM " + table + " WHERE " + where
        self.__cursor.execute(sql, values)
        return self.__cursor.rowcount


    def raw_select(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()


    def raw_update(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.rowcount


    def commit(self):
        self.__connector.commit()


    def rollback(self):
        self.__connector.rollback()


    def set_autocommit(self, value):
        self.__connector.autocommit = value


