import mysql.connector

conn = mysql.connector.connect(user="root", password="RT258387684z1", host="127.0.0.1", database="rtdb")
cursor = conn.cursor(buffered=True)
print('Подключение к БД прошло успешно.')

ip = '10.11.1.1'
name = 'London'
mac = 'cc:ff:ff:ff:ff:ff'

# Запись в базу данных
# add_unit = ("INSERT INTO unit "
#             "(unit_ip, unit_name, unit_mac) "
#             "VALUES ('%(ip)s', '%(name)s', '%(mac)s')" % {'ip': ip, 'name': name, 'mac': mac})
# cursor.execute(add_unit)

# Чтение из базы данных
cursor.execute("SELECT * FROM unit WHERE id = 6")
qw = cursor.fetchall()
for j in qw:
    print(j)
    print(j[2])
    
conn.commit()
conn.close()
