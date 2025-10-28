import tkinter as tk
from tkinter import *


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
    root.show_hide_btn = Button(root, text='Показать', width=10)
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
    attachment_btn = Button(root, text='Обзор', width=10)
    attachment_btn.grid(row=4, column=2, pady=5, padx=5)
    
    label_body_email = Label(root, text='Сообщение : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_body_email.grid(row=5, column=0)
    root.body_email = Text(root, width=100, height=20)
    root.body_email.grid(row=6, column=0, columnspan=3, pady=5, padx=5)
    
    send_email_btn = Button(root, text='Отпраить email', width=13)
    send_email_btn.grid(row=7, column=2, padx=5, pady=5)
    exit_btn = Button(root, text='Выход', width=10)
    exit_btn.grid(row=7, column=0, padx=5, pady=5)
    

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