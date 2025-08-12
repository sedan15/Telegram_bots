import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',#Который указывали при установке
    user='root',
    password='root',#Пароль который указывали при установке
    database = 'telegram_bot' #Название которое сделали в sql workbench
)

db.autocommit = True #Свойство автоотправки запросов insert
cursor = db.cursor() #С помощью этой переменной будем делать запросы к бд

#Получить 1 запись по id
def get_one_by_id(table:str,id:int):
    query = f'''SELECT * FROM {table} WHERE id = {id}'''
    cursor.execute(query)
    record = cursor.fetchone() #Получение результатов запроса
    return record

#Сохранить 1 запись
def save_one(table:str,record:str,values:str):
    query = f'''INSERT INTO {table}({record}) VALUES({values})'''
    cursor.execute(query)
#Удалить 1 запись по id
def delete_one_by_id(table:str,id:int):
    query = f'''DELETE FROM {table} WHERE id = {id}'''
    cursor.execute(query)

# cursor.execute('SELECT * FROM users;') #Сам запрос
# result = cursor.fetchone() #Обработка запроса
# print(result)
