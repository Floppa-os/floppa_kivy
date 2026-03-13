"""
Модуль для сетевой коммуникации: отправка и приём сообщений.
"""

import socket
import threading
from config import PORT, BUFFER_SIZE, TIMEOUT

class NetworkManager:
    def __init__(self, on_message_received):
        self.on_message_received = on_message_received
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.settimeout(TIMEOUT)
        try:
            self.sock.bind(("", PORT))
        except Exception as e:
            print(f"[ОШИБКА] Не удалось привязаться к порту {PORT}: {e}")

    def send_message(self, message: str, target_ip: str):
        """Отправляет сообщение на указанный IP."""
        try:
            self.sock.sendto(message.encode('utf-8'), (target_ip, PORT))
            print(f"[ОТПРАВЛЕНО] {message} → {target_ip}")
        except Exception as e:
            print(f"[ОШИБКА при отправке] {e}")

    def start_listening(self):
        """Запускает поток для приёма сообщений."""
        threading.Thread(target=self._listen, daemon=True).start()

    def _listen(self):
        """Внутренний метод: слушает порт и передаёт сообщения обработчику."""
        while True:
            try:
                data, addr = self.sock.recvfrom(BUFFER_SIZE)
                message = data.decode('utf-8')
                sender_ip = addr[0]
                self.on_message_received(sender_ip, message)
            except socket.timeout:
                continue  # Просто продолжаем слушать
            except Exception as e:
                print(f"[ОШИБКА приёма] {e}")
                break
