import os
import smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def create_widgets():
    """Создание виджета приложения"""
    label_from_email = Label(root, text='Ваш email : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_from_email.grid(row=0, column=0, pady=5, padx=5)
    root.entry_from_email = Entry(root, width=50, textvariable=from_email)
    root.entry_from_email.grid(row=0, column=1, pady=5, padx=5)
    
    label_password_email = Label(root, text='Пароль : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_password_email.grid(row=1, column=0, pady=5, padx=5)
    root.entry_password_email = Entry(root, width=50, show='*', textvariable=password_email)
    root.entry_password_email.grid(row=1, column=1, pady=5, padx=5)
    root.show_hide_btn = Button(root, text='Показать', width=10, command=show_password)
    root.show_hide_btn.grid(row=1, column=2, pady=5, padx=5)
    
    label_to_email = Label(root, text='Email получателя : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_to_email.grid(row=2, column=0, pady=5, padx=5)
    root.entry_to_email = Entry(root, width=50, textvariable=to_email)
    root.entry_to_email.grid(row=2, column=1, pady=5, padx=5)
    
    label_subject_email = Label(root, text='Тема письма : ', bg='darkslategray4', font=('', 15, 'bold'))
    label_subject_email.grid(row=3, column=0, pady=5, padx=5)
    root.entry_subject_email = Entry(root, width=50, textvariable=subject_email)
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
    
    send_email_btn = Button(root, text='Отпраить email', width=13, command=send_email)
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
        

def send_email():
    """Отправка электронной почты"""
    # Получение всех введенных пользователем параметров и сохранение их в соответствующих переменных
    from_email_1 = from_email.get()
    password_email_1 = password_email.get()
    to_email_1 = to_email.get()
    subject_email_1 = subject_email.get()
    body_email_1 = root.body_email.get('1.0', END)
    
    # Создание экземпляра класса MimeMultipart()
    message = MIMEMultipart()
    # Сохранение данных электронной почты в соответствующих полях
    message['from'] = from_email_1
    message['to'] = to_email_1
    message['subject'] = subject_email_1
    # Прикрепить сообщение с помощью экземпляра MIME
    message.attach(MIMEText(body_email_1))

    try:
        # Перебор файлов в списке вложений
        for files in root.filename:
            # Открытие и чтение файла во вложении
            attachment = open(files, 'rb').read()
            # Создаем экземпляр MIMEBase и присваиваем ему имя email_attach
            email_attach = MIMEBase('application', 'octet-stream')
            # Изменение полезной нагрузки в закодированном виде
            email_attach.set_payload(attachment)
            # Кодирование вложения в base64
            encoders.encode_base64(email_attach)
            # Добавление заголовков к файлам
            email_attach.add_header('Content-Disposition', 'attachment; filename= %s' % os.path.basename(files))
            # Прикрепление instane email_attach к экземпляру сообщения
            message.attach(email_attach)

    except AttributeError:
        pass

    # Отправка электронного письма с вложениями
    try:
        # Создание smtp-сессии
        smtp = smtplib.SMTP('smtp.yandex.ru', 587)
        # Запуск TLS для обеспечения безопасности
        smtp.starttls()
        # Аутентификация пользователя
        smtp.login(from_email_1, password_email_1)
        # Отправка электронного письма с Mulitpart сообщением, преобразованным в строку
        smtp.sendmail(from_email_1, to_email_1, message.as_string())
        messagebox.showinfo('Успех', 'Письмо успешно отправлено! ' + str(to_email_1))
        # Завершение сессии
        smtp.quit()

    # Перехват ошибки аутентификации
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror('Ошибка', 'Неверно указан email или пароль')
    # Обнаружение ошибки подключения
    except smtplib.SMTPConnectError:
        messagebox.showerror('Ошибка', 'Пожалуйста, попробуйте позже')



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