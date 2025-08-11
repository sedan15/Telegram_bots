import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',#Который указывали при установке
    user='root',
    password='root',#Пароль который указывали при установке
    database = 'telegram_bot' #Название которое сделали в sql workbench
)

cursor = db.cursor() #С помощью этой переменной будем делать запросы к бд


# cursor.execute('SELECT * FROM users;') #Сам запрос
# result = cursor.fetchone() #Обработка запроса
# print(result)
