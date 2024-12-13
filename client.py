import sqlite3
from idlelib import window
from tkinter import messagebox, ttk
import tkinter as tk
import datetime


def open_personal_data_window(username):
    personal_data_window = tk.Toplevel()
    personal_data_window.title("Личные данные")
    personal_data_window.geometry("400x400")  # Убедитесь, что окно имеет нормальные размеры

    # Заголовок
    tk.Label(personal_data_window, text="Заполните личные данные", font=("Arial", 14)).pack(pady=10)

    # Поля для ввода данных
    tk.Label(personal_data_window, text="Имя:").pack(pady=5)
    first_name_entry = tk.Entry(personal_data_window, width=30)
    first_name_entry.pack(pady=5)

    tk.Label(personal_data_window, text="Фамилия:").pack(pady=5)
    last_name_entry = tk.Entry(personal_data_window, width=30)
    last_name_entry.pack(pady=5)

    tk.Label(personal_data_window, text="Телефон:").pack(pady=5)
    phone_entry = tk.Entry(personal_data_window, width=30)
    phone_entry.pack(pady=5)

    tk.Label(personal_data_window, text="Дата рождения:").pack(pady=5)
    birth_date_entry = tk.Entry(personal_data_window, width=30)
    birth_date_entry.pack(pady=5)

    tk.Label(personal_data_window, text="Электронная почта:").pack(pady=5)
    email_entry = tk.Entry(personal_data_window, width=30)
    email_entry.pack(pady=5)

    # Функция загрузки данных
    def load_personal_data():
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT first_name, last_name, phone, birth_date, email
                    FROM users
                    WHERE login = ?
                """, (username,))
                data = cursor.fetchone()

                if data:
                    # Обрабатываем случай, если данные содержат None
                    first_name_entry.delete(0, tk.END)
                    first_name_entry.insert(0, data[0] if data[0] is not None else "")

                    last_name_entry.delete(0, tk.END)
                    last_name_entry.insert(0, data[1] if data[1] is not None else "")

                    phone_entry.delete(0, tk.END)
                    phone_entry.insert(0, data[2] if data[2] is not None else "")

                    birth_date_entry.delete(0, tk.END)
                    birth_date_entry.insert(0, data[3] if data[3] is not None else "")

                    email_entry.delete(0, tk.END)
                    email_entry.insert(0, data[4] if data[4] is not None else "")
                else:
                    messagebox.showwarning("Ошибка", f"Данные для пользователя {username} не найдены.")
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки данных: {e}")
    # Загружаем данные при открытии окна
    load_personal_data()

    # Функция сохранения данных
    def save_personal_data():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        phone = phone_entry.get()
        birth_date = birth_date_entry.get()
        email = email_entry.get()

        if not first_name or not last_name or not phone or not birth_date or not email:
            messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
            return

        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE users
                    SET first_name = ?, last_name = ?, phone = ?, birth_date = ?, email = ?
                    WHERE login = ?
                """, (first_name, last_name, phone, birth_date, email, username))
                conn.commit()
            messagebox.showinfo("Успех", "Личные данные успешно обновлены.")
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка обновления данных: {e}")

    # Кнопка сохранения данных
    save_button = tk.Button(personal_data_window, text="Сохранить данные", command=save_personal_data)
    save_button.pack(pady=10)

    # Кнопка назад
    back_button = tk.Button(personal_data_window, text="Назад", command=personal_data_window.destroy)
    back_button.pack(pady=10)

    personal_data_window.mainloop()  # Убедитесь, что mainloop() вызван в конце функцииdef open_personal_data_window(username):
    personal_data_window = tk.Toplevel()
    personal_data_window.title("Личные данные")
    personal_data_window.geometry("400x400")  # Убедитесь, что окно имеет нормальные размеры

    # Заголовок
    tk.Label(personal_data_window, text="Заполните личные данные", font=("Arial", 14)).pack(pady=10)

    # Поля для ввода данных
    tk.Label(personal_data_window, text="Имя:").pack(pady=5)
    first_name_entry = tk.Entry(personal_data_window, width=30)
    first_name_entry.pack(pady=5)

    tk.Label(personal_data_window, text="Фамилия:").pack(pady=5)
    last_name_entry = tk.Entry(personal_data_window, width=30)
    last_name_entry.pack(pady=5)

    tk.Label(personal_data_window, text="Телефон:").pack(pady=5)
    phone_entry = tk.Entry(personal_data_window, width=30)
    phone_entry.pack(pady=5)

    tk.Label(personal_data_window, text="Дата рождения:").pack(pady=5)
    birth_date_entry = tk.Entry(personal_data_window, width=30)
    birth_date_entry.pack(pady=5)

    tk.Label(personal_data_window, text="Электронная почта:").pack(pady=5)
    email_entry = tk.Entry(personal_data_window, width=30)
    email_entry.pack(pady=5)

    # Функция загрузки данных
    def load_personal_data():
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT first_name, last_name, phone, birth_date, email
                    FROM users
                    WHERE login = ?
                """, (username,))
                data = cursor.fetchone()
                if data:
                    # Заполняем поля данными
                    first_name_entry.delete(0, tk.END)  # Очищаем старое значение перед вставкой
                    first_name_entry.insert(0, data[0])
                    last_name_entry.delete(0, tk.END)
                    last_name_entry.insert(0, data[1])
                    phone_entry.delete(0, tk.END)
                    phone_entry.insert(0, data[2])
                    birth_date_entry.delete(0, tk.END)
                    birth_date_entry.insert(0, data[3])
                    email_entry.delete(0, tk.END)
                    email_entry.insert(0, data[4])
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки данных: {e}")

    # Загружаем данные при открытии окна
    load_personal_data()

    # Функция сохранения данных
    def save_personal_data():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        phone = phone_entry.get()
        birth_date = birth_date_entry.get()
        email = email_entry.get()

        if not first_name or not last_name or not phone or not birth_date or not email:
            messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
            return

        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE users
                    SET first_name = ?, last_name = ?, phone = ?, birth_date = ?, email = ?
                    WHERE login = ?
                """, (first_name, last_name, phone, birth_date, email, username))
                conn.commit()
            messagebox.showinfo("Успех", "Личные данные успешно обновлены.")
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка обновления данных: {e}")

    # Кнопка сохранения данных
    save_button = tk.Button(personal_data_window, text="Сохранить данные", command=save_personal_data)
    save_button.pack(pady=10)

    # Кнопка назад
    back_button = tk.Button(personal_data_window, text="Назад", command=personal_data_window.destroy)
    back_button.pack(pady=10)

    personal_data_window.mainloop()

def open_orders_history(parent_window, username):
    history_window = tk.Toplevel(parent_window)
    history_window.title("История заказов")
    history_window.geometry("500x500")

    tk.Label(history_window, text=f"История заказов: {username}", font=("Arial", 14)).pack(pady=10)

    orders_list = tk.Listbox(history_window, width=70, height=20)
    orders_list.pack(pady=10)

    try:
        with sqlite3.connect("restaurant.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, order_details, total_price, status
                FROM orders
                WHERE client_login = ?
            """, (username,))
            orders = cursor.fetchall()

            if orders:
                for order in orders:
                    order_id, order_details, total_price, status = order
                    orders_list.insert(
                        tk.END,
                        f"№{order_id} | {order_details} - {total_price} руб. | Статус: {status}"
                    )
                    cursor.execute("""
                        SELECT dish_name, quantity FROM order_items
                        WHERE order_id = ?
                    """, (order_id,))
                    items = cursor.fetchall()

                    for item in items:
                        dish_name, quantity = item
                        orders_list.insert(tk.END, f"  {dish_name} x{quantity}")

                    # Добавим вывод отзывов с датой
                    cursor.execute("""
                        SELECT review_text, review_date FROM reviews
                        WHERE order_id = ?
                    """, (order_id,))
                    reviews = cursor.fetchall()

                    if reviews:
                        for review in reviews:
                            review_text, review_date = review
                            orders_list.insert(tk.END, f"  Отзыв: {review_text} (Дата: {review_date})")
                    else:
                        orders_list.insert(tk.END, "  Отзывов нет.")
            else:
                orders_list.insert(tk.END, "Заказы отсутствуют.")
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", f"Ошибка загрузки истории заказов: {e}")

    tk.Button(history_window, text="Назад", command=history_window.destroy).pack(pady=10)


def open_orders_window():
    """Окно для отображения заказов со статусом 'active'."""
    orders_win = tk.Toplevel()
    orders_win.title("Активные заказы")
    orders_win.geometry("600x600")

    # Список заказов
    orders_list = tk.Listbox(orders_win, width=70, height=15)
    orders_list.pack(pady=10)

    def load_orders():
        """Загрузка активных заказов с датой."""
        orders_list.delete(0, tk.END)
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, client_login, order_details, total_price, date FROM orders WHERE status = 'active'")
                orders = cursor.fetchall()
                if orders:
                    for order in orders:
                        order_info = f"Заказ #{order[0]} - Клиент: {order[1]} - {order[2]} - {order[3]} руб. - Дата: {order[4]}"
                        orders_list.insert(tk.END, order_info)
                else:
                    orders_list.insert(tk.END, "Нет активных заказов.")
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки заказов: {e}")

    load_orders()

    def deliver_order():
        """Выдача заказа (смена статуса на 'completed')."""
        selected_order = orders_list.curselection()
        if not selected_order:
            messagebox.showwarning("Ошибка", "Выберите заказ для выдачи.")
            return
        order_id = orders_list.get(selected_order[0]).split(" ")[1][1:]  # Извлекаем номер заказа
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE orders SET status = 'completed' WHERE id = ?", (order_id,))
                conn.commit()
                messagebox.showinfo("Успех", f"Заказ #{order_id} был выдан.")
                load_orders()  # Обновляем список заказов
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка при выдаче заказа: {e}")

    # Кнопка для выдачи заказа
    tk.Button(orders_win, text="Выдать заказ", command=deliver_order).pack(pady=5)

    # Кнопка для возвращения в главное меню
    tk.Button(orders_win, text="Назад", command=orders_win.destroy).pack(pady=10)

def open_write_review_window(username):
    review_window = tk.Toplevel()
    review_window.title("Написать отзыв")
    review_window.geometry("400x400")

    # Заголовок
    tk.Label(review_window, text="Оставьте свой отзыв", font=("Arial", 14)).pack(pady=10)

    # Поле для ввода оценки
    tk.Label(review_window, text="Оценка (1-5):").pack(pady=5)
    rating_entry = tk.Entry(review_window, width=10)
    rating_entry.pack(pady=5)

    # Поле для ввода текста отзыва
    tk.Label(review_window, text="Ваш отзыв:").pack(pady=5)
    review_text = tk.Text(review_window, width=30, height=10)
    review_text.pack(pady=10)

    # Получаем список заказов пользователя
    order_combobox = ttk.Combobox(review_window, state="readonly", width=30)
    order_combobox.pack(pady=5)

    try:
        with sqlite3.connect("restaurant.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, order_date FROM orders WHERE client_login = ?
            """, (username,))
            orders = cursor.fetchall()

            if orders:
                order_combobox['values'] = [f"№{order[0]} - {order[1]}" for order in orders]
            else:
                messagebox.showwarning("Ошибка", "У вас нет заказов.")
                return
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", f"Ошибка базы данных: {e}")

    def save_review_action():
        # Получаем оценку
        try:
            rating = int(rating_entry.get())
            if rating < 1 or rating > 5:
                messagebox.showwarning("Ошибка", "Оценка должна быть от 1 до 5.")
                return
        except ValueError:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите корректную оценку.")
            return

        # Получаем текст отзыва
        review = review_text.get("1.0", tk.END).strip()
        if not review:
            messagebox.showwarning("Ошибка", "Пожалуйста, напишите отзыв!")
            return

        # Получаем номер заказа из строки
        selected_order = order_combobox.get()
        if not selected_order:
            messagebox.showwarning("Ошибка", "Пожалуйста, выберите заказ.")
            return

        order_id = int(selected_order.split(" - ")[0][1:])

        # Сохраняем отзыв
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO reviews (order_id, client_login, rating, review_text)
                    VALUES (?, ?, ?, ?)
                """, (order_id, username, rating, review))
                conn.commit()
            messagebox.showinfo("Успех", "Отзыв успешно добавлен.")
            review_window.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка сохранения отзыва: {e}")

    # Кнопка отправить отзыв
    send_button = tk.Button(review_window, text="Отправить отзыв", command=save_review_action)
    send_button.pack(pady=10)

    # Кнопка назад
    back_button = tk.Button(review_window, text="Назад", command=review_window.destroy)
    back_button.pack(pady=10)

    review_window.mainloop()

def open_orders_window():
    """Окно для отображения заказов со статусом 'active'."""
    orders_win = tk.Toplevel()
    orders_win.title("Активные заказы")
    orders_win.geometry("600x600")

    # Список заказов
    orders_list = tk.Listbox(orders_win, width=70, height=15)
    orders_list.pack(pady=10)

    def load_orders():
        """Загрузка активных заказов с датой и временем."""
        orders_list.delete(0, tk.END)
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, client_login, order_details, total_price, date FROM orders WHERE status = 'active'")
                orders = cursor.fetchall()
                if orders:
                    for order in orders:
                        # Преобразование даты из формата YYYY-MM-DD HH:MM:SS в ДД.ММ.ГГГГ ЧЧ:ММ:СС
                        date_obj = datetime.strptime(order[4], "%Y-%m-%d %H:%M:%S")  # предполагается, что в базе дата с временем
                        formatted_date = date_obj.strftime("%d.%m.%Y %H:%M:%S")
                        order_info = f"Заказ #{order[0]} - Клиент: {order[1]} - {order[2]} - {order[3]} руб. - Дата: {formatted_date}"
                        orders_list.insert(tk.END, order_info)
                else:
                    orders_list.insert(tk.END, "Нет активных заказов.")
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки заказов: {e}")

    load_orders()

    def deliver_order():
        """Выдача заказа (смена статуса на 'completed')."""
        selected_order = orders_list.curselection()
        if not selected_order:
            messagebox.showwarning("Ошибка", "Выберите заказ для выдачи.")
            return
        order_id = orders_list.get(selected_order[0]).split(" ")[1][1:]  # Извлекаем номер заказа
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE orders SET status = 'completed' WHERE id = ?", (order_id,))
                conn.commit()
                messagebox.showinfo("Успех", f"Заказ #{order_id} был выдан.")
                load_orders()  # Обновляем список заказов
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка при выдаче заказа: {e}")

    # Кнопка для выдачи заказа
    tk.Button(orders_win, text="Выдать заказ", command=deliver_order).pack(pady=5)

    # Кнопка для возвращения в главное меню
    tk.Button(orders_win, text="Назад", command=orders_win.destroy).pack(pady=10)


import tkinter as tk
from tkinter import messagebox
import sqlite3


def open_menu_window():
    menu_window = tk.Toplevel()
    menu_window.title("Меню")
    menu_window.geometry("500x500")

    # Шрифт, который будет использоваться везде
    font = ("Arial", 12)

    tk.Label(menu_window, text="Меню", font=("Arial", 14)).pack(pady=10)

    # Поле для поиска блюд
    search_entry = tk.Entry(menu_window, width=30, font=font)
    search_entry.pack(pady=5)

    # Создание канвы с прокруткой
    canvas = tk.Canvas(menu_window)
    scroll_y = tk.Scrollbar(menu_window, orient="vertical", command=canvas.yview)
    canvas.config(yscrollcommand=scroll_y.set)

    # Фрейм для прокручиваемого списка
    menu_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=menu_frame, anchor="nw")

    # Размещение канвы и прокрутки
    canvas.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")

    menu_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Поле для отображения меню (с прокруткой)
    menu_text = tk.Text(menu_frame, height=20, width=50, wrap="word", font=font, state="disabled")
    menu_text.pack(pady=10, padx=10)

    def show_all_dishes():
        """Загрузка всех блюд из базы данных и отображение в списке."""
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name, description, price FROM menu")
                dishes = cursor.fetchall()

                # Очистка старого текста в поле
                menu_text.config(state="normal")  # Разрешаем редактирование
                menu_text.delete(1.0, tk.END)  # Очищаем поле

                # Добавление блюд в текстовое поле
                for dish in dishes:
                    dish_info = f"{dish[0]} - {dish[1]} - {dish[2]} руб.\n"
                    menu_text.insert(tk.END, dish_info)

                menu_text.config(state="disabled")  # Запрещаем редактирование
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка базы данных: {e}")

    def search_menu():
        """Поиск блюд по имени."""
        search_query = search_entry.get().strip()
        try:
            with sqlite3.connect("restaurant.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name, description, price FROM menu WHERE name LIKE ?", (f"%{search_query}%",))
                dishes = cursor.fetchall()

                # Очистка старого текста в поле
                menu_text.config(state="normal")  # Разрешаем редактирование
                menu_text.delete(1.0, tk.END)  # Очищаем поле

                # Если блюда найдены, отображаем их
                if dishes:
                    for dish in dishes:
                        dish_info = f"{dish[0]} - {dish[1]} - {dish[2]} руб.\n"
                        menu_text.insert(tk.END, dish_info)
                else:
                    menu_text.insert(tk.END, "Блюда не найдены.\n")

                menu_text.config(state="disabled")  # Запрещаем редактирование
        except sqlite3.Error as e:
            messagebox.showerror("Ошибка", f"Ошибка базы данных: {e}")

    # Кнопка для поиска
    tk.Button(menu_window, text="Найти", command=search_menu, font=font).pack(pady=5)

    # Кнопка для отображения всех блюд
    tk.Button(menu_window, text="Показать все", command=show_all_dishes, font=font).pack(pady=5)

    # Кнопка для закрытия окна
    tk.Button(menu_window, text="Назад", command=menu_window.destroy, font=font).pack(pady=10)

    # Показать все блюда по умолчанию при открытии окна
    show_all_dishes()