"""
Конфигурационные параметры мессенджера.
"""

import socket

# Порт для обмена сообщениями
PORT = 5000

# Время ожидания ответа (сек)
TIMEOUT = 2

# Размер буфера для приёма сообщений
BUFFER_SIZE = 1024

# Получаем локальный IP-адрес
def get_local_ip():
    try:
        # Создаём UDP-сокет, чтобы узнать локальный IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # Google DNS
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

LOCAL_IP = get_local_ip()
