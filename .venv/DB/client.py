import sqlite3


# Создание базы данных и таблицы
def create_db():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # Создание таблицы, если она еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


# Функция для добавления клиента в базу данных
def add_client(name, age, hobby):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO clients (name, age, hobby)
        VALUES (?, ?, ?)
    ''', (name, age, hobby))

    conn.commit()
    conn.close()


# Функция для получения всех клиентов
def get_all_clients():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()

    conn.close()
    return clients


# Функция для обновления имени клиента по его id
def update_client_name(client_id, new_name):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE clients
        SET name = ?
        WHERE id = ?
    ''', (new_name, client_id))

    conn.commit()
    conn.close()


# Функция для удаления клиента по его id
def delete_client(client_id):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM clients
        WHERE id = ?
    ''', (client_id,))

    conn.commit()
    conn.close()


# Пример использования:
if __name__ == "__main__":
    create_db()  # Создаем таблицу (если не существует)

    # Добавление клиентов
    add_client("John Doe", 30, "Reading")
    add_client("Jane Smith", 25, "Cooking")
    add_client("Alice Brown", 28, "Hiking")

    # Получение всех клиентов
    clients = get_all_clients()
    print("Все клиенты:")
    for client in clients:
        print(client)

    # Обновление имени клиента с id = 1
    update_client_name(1, "Johnathan Doe")

    # Удаление клиента с id = 2
    delete_client(2)

    # Получение всех клиентов после изменений
    clients = get_all_clients()
    print("\nКлиенты после изменений:")
    for client in clients:
        print(client)
