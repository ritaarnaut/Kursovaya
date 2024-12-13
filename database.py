import sqlite3

import datetime
from datetime import datetime


# Создание базы данных и соединение
with sqlite3.connect("restaurant.db") as conn:
    cursor = conn.cursor()

    # Таблица пользователей
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK (role IN ('admin', 'waiter', 'client')),
            first_name TEXT,
            last_name TEXT,
            phone TEXT,
            birth_date TEXT,
            email TEXT
        )
    """)

    # Таблица меню
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            price REAL NOT NULL CHECK (price > 0)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_login TEXT NOT NULL,
            order_details TEXT NOT NULL,
            total_price REAL NOT NULL CHECK (total_price >= 0),
            status TEXT NOT NULL CHECK (status IN ('active', 'completed')),
            order_date DATETIME,
            FOREIGN KEY (client_login) REFERENCES users (login) ON DELETE CASCADE
        )
    """)

    # Таблица отзывов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_login TEXT,
    order_id INTEGER,
    rating INTEGER,
    review_text TEXT,
    review_date DATETIME,  -- Добавлено поле для даты отзыва
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(client_login) REFERENCES users(login)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            dish_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
        )
    """)

    # Добавление тестовых данных
    try:
        # Пользователи
        cursor.executemany("""
            INSERT INTO users (login, password, role) VALUES (?, ?, ?)
        """, [
            ('admin', 'admin123', 'admin'),
            ('waiter', 'waiter123', 'waiter'),
            ('client1', 'clientpass', 'client'),
        ])

        # Меню
        cursor.executemany("""
            INSERT INTO menu (name, description, price) VALUES (?, ?, ?)
        """, [
            ('Пицца', 'Большая сырная пицца', 10.99),
            ('Бургер', 'Сочный бургер с картошкой', 8.99),
            ('Салат', 'Свежий овощной салат', 5.99),
            ('Паста', 'Паста с соусом Альфредо', 12.50),
            ('Стейк', 'Сочный стейк средней прожарки', 15.75),
            ('Ризотто', 'Ризотто с грибами', 14.99),
            ('Суп', 'Том Ям с креветками', 7.50),
            ('Пельмени', 'Домашние пельмени с мясом', 6.45),
            ('Котлета', 'Котлета по-киевски с гарниром', 9.30),
            ('Крабовые палочки', 'Крабовые палочки с соусом', 4.50),
            ('Чизкейк', 'Вкусный чизкейк с ягодами', 6.80),
            ('Мороженое', 'Ассорти мороженого', 3.20),
            ('Кофе', 'Кофе американо', 2.60),
            ('Чай', 'Чай зеленый', 1.99),
            ('Сок', 'Сок апельсиновый', 2.40),
            ('Пиво', 'Пиво светлое', 3.80),
            ('Вино', 'Красное вино', 12.40),
            ('Греческий салат', 'Салат с фетой и оливками', 8.99),
            ('Куриные крылышки', 'Жареные куриные крылышки', 7.20),
            ('Фалафель', 'Фалафель с соусом тахини', 5.60),
            ('Блинчики', 'Блинчики с мясом', 4.40),
            ('Сэндвич', 'Сэндвич с индейкой', 6.90),
            ('Лосось', 'Жареный лосось с картофелем', 17.50),
            ('Говядина', 'Говядина с овощами', 16.30),
            ('Краб', 'Салат с крабом и авокадо', 14.20),
            ('Мясо по-французски', 'Мясо с сыром в соусе', 13.60),
            ('Шашлык', 'Шашлык из свинины', 12.90),
            ('Торт', 'Торт шоколадный', 7.40),
            ('Лимонад', 'Домашний лимонад', 3.00),
            ('Коктейль', 'Коктейль «Мохито»', 6.70),
            ('Цезарь', 'Салат Цезарь с курицей', 9.90)
        ])
        conn.commit()

    except sqlite3.IntegrityError:
        # Игнорируем ошибки при повторной вставке данных
        pass

    from datetime import datetime

    # Получаем текущую дату
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Добавление заказов в таблицу
    with sqlite3.connect("restaurant.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("""
               INSERT INTO orders (client_login, order_details, total_price, status, order_date) VALUES (?, ?, ?, ?, ?)
           """, [
            ('client1', 'Пицца, Салат', 16.98, 'active', current_date),
            ('client2', 'Бургер', 8.99, 'completed', current_date),

        ])
        conn.commit()

    try:
        with sqlite3.connect("restaurant.db") as conn:
            cursor = conn.cursor()
            cursor.executemany("""
                INSERT INTO orders (client_login, order_details, total_price, status, order_date) VALUES (?, ?, ?, ?, ?)
            """, [
                ('client1', 'Пицца, Салат', 16.98, 'active', '2024-12-13'),
                ('client2', 'Бургер', 8.99, 'completed', '2024-12-13'),
                # Добавьте остальные данные заказов
            ])
            conn.commit()
    except sqlite3.IntegrityError:
        # Игнорируем ошибки при повторной вставке данных
        pass

    print("База данных успешно создана и инициализирована.")