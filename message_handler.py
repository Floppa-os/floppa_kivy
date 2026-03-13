"""
Обработчик входящих сообщений.
"""

from datetime import datetime

def handle_message(sender_ip: str, message: str):
    """
    Обрабатывает полученное сообщение.
    Выводит в консоль с меткой времени.
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {sender_ip}: {message}")
