import mysql.connector

from app.datos.Connector import Connector


class MysqlConnection(Connector):
    
    def __init__(self):
        self.__connector = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", # Aqui va la contraseña del root de la instalacion de MySql
            database="rotonda"
        )
        self.__cursor = self.__connector.cursor(dictionary=True)


    def select(self, fields=["*"], tables=[], where='', values={} , order_by=[], group_by=[], from_s=0, limit=None):
        sql = "SELECT " + (','.join(fields)) + " FROM " + (','.join(tables)) 
        
        if where != '':
            sql += " WHERE " + where
        if len(group_by) > 0:
            sql += " GROUP BY " + (','.join(group_by))
        if len(order_by) > 0:
            sql += " ORDER BY " + (','.join(order_by))
        if limit is not None:
            sql += " LIMIT " + str(limit)
        if from_s > 0:
            sql += " OFFSET " + str(from_s)
        self.__cursor.execute(sql, values)

        return self.__cursor.fetchall()


    def update(self, table, update=[], where='', values={}):
        try:
            sql = "UPDATE " + table + " SET " + (','.join(upd+"=%("+upd+")s" for upd in update)) + " WHERE " + where
            self.__cursor.execute(sql, values)
            return {'success':True, 'filas_afectadas': self.__cursor.rowcount}
        except mysql.connector.Error as e:
            
            return {'success':False, 'error' : str(e)}


    def insert(self, table, insert={}):
        try:
            sql = "INSERT INTO " + table + " (" + (','.join(insert.keys())) + ") VALUES(" +\
                (','.join("%("+ins+")s" for ins in insert.keys())) + ")"
            self.__cursor.execute(sql, insert)
            
            return {'success':True}
        except mysql.connector.Error as e:
            return {'success':False, 'error' : str(e)}

    def delete(self, table, where='', values={}):
        try:
            sql = "DELETE FROM " + table + " WHERE " + where
            self.__cursor.execute(sql, values)
            return {'success':True, 'filas_afectadas': self.__cursor.rowcount}
        except mysql.connector.Error as e:
            return {'success':False, 'error' : str(e)}

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

    def get_last_id(self):
        return self.__cursor.lastrowid


