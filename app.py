import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames


def create_widgets():
    """Создание виджета приложения"""
    label_from_email = Label(root, text='Ваш email : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_from_email.grid(row=0, column=0, pady=5, padx=5)
    root.entry_from_email = Entry(root, width=50)
    root.entry_from_email.grid(row=0, column=1, pady=5, padx=5)
    
    label_password_email = Label(root, text='Пароль : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_password_email.grid(row=1, column=0, pady=5, padx=5)
    root.entry_password_email = Entry(root, width=50, show='*')
    root.entry_password_email.grid(row=1, column=1, pady=5, padx=5)
    root.show_hide_btn = Button(root, text='Показать', width=10, command=show_password)
    root.show_hide_btn.grid(row=1, column=2, pady=5, padx=5)
    
    label_to_email = Label(root, text='Email получателя : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_to_email.grid(row=2, column=0, pady=5, padx=5)
    root.entry_to_email = Entry(root, width=50)
    root.entry_to_email.grid(row=2, column=1, pady=5, padx=5)
    
    label_subject_email = Label(root, text='Тема письма : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_subject_email.grid(row=3, column=0, pady=5, padx=5)
    root.entry_subject_email = Entry(root, width=50)
    root.entry_subject_email.grid(row=3, column=1, pady=5, padx=5)
    
    label_attachment_email = Label(root, text='Выберите файл : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_attachment_email.grid(row=4, column=0, pady=5, padx=5)
    root.entry_attachment_email = Text(root, width=65, height=5)
    root.entry_attachment_email.grid(row=4, column=1, pady=5, padx=5)
    attachment_btn = Button(root, text='Обзор', width=10, command=file_browse)
    attachment_btn.grid(row=4, column=2, pady=5, padx=5)
    
    label_body_email = Label(root, text='Сообщение : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_body_email.grid(row=5, column=0)
    root.body_email = Text(root, width=100, height=20)
    root.body_email.grid(row=6, column=0, columnspan=3, pady=5, padx=5)
    
    send_email_btn = Button(root, text='Отпраить email', width=13)
    send_email_btn.grid(row=7, column=2, padx=5, pady=5)
    exit_btn = Button(root, text='Выход', width=10, command=email_exit)
    exit_btn.grid(row=7, column=0, padx=5, pady=5)
    


def show_password():
    """Отображает замаскированный пароль"""
    # Настройка кнопки для отображения текста Скрыть и запуска функции hide_password() при нажатии
    root.show_hide_btn.config(text='Скрыть', command=hide_password)
    # Установка атрибута show в пустую строку для отображения пароля
    root.entry_password_email.config(show='')


def hide_password():
    """Маскирует пароль звездочками"""
    # Настройка кнопки для отображения текста Показать и запуска функции show_password() при нажатии
    root.show_hide_btn.config(text='Показать', command=show_password)
    # Установка атрибута show равным * для маскировки пароля
    root.entry_password_email.config(show='*')


def file_browse():
    """Отображает диалоговое окно для выбора файлов, которые будут отправлены в качестве вложений"""
    # Предоставляет пользователю диалоговое окно для выбора файлов
    # функция askopenfilenames() может использоваться для выбора нескольких файлов
    # Настройка initialdir необязательна
    root.filename = askopenfilenames(initialdir='YOUR DIRECTORY PATH')
    # Перебор выбранных файлов и отображение их в виджете attacment_entry
    for files in root.filename:
        # Извлекает только имена файлов из пути, используя метод os.path.basename()
        filename = os.path.basename(files)
        root.entry_attachment_email.insert('1.0', filename + '\n')
        
        
def email_exit():
    """Выход из приложения"""
    # Получить подтверждение от пользователя с помощью messagebox
    msg_box = messagebox.askquestion('Выход из Email Sender', 'Вы действительно хотите выйти?')
    if msg_box == 'yes':
        # Закрыть окно приложения
        root.destroy()



# Создание объекта класса tk
root = tk.Tk()

# Настройка цвета заголовка и фона, отключение свойства изменения размера
root.title('Email Sender')
root.config(background='darkslategray4')
root.resizable(False, False)
root.geometry('850x700')

# Создание переменных tkinter
to_email = StringVar()
from_email = StringVar()
password_email = StringVar()
subject_email = StringVar()

# Вызвать функцию create_widgets с парматрами bgColor
create_widgets()

# Бесконечный цикл для запуска приложения
root.mainloop()