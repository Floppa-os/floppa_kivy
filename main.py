"""
Основная логика мессенджера: ввод сообщений, отправка, вывод полученных.
"""

from network import NetworkManager
from message_handler import handle_message
from config import LOCAL_IP, PORT
def main():
    print("=== Floppa Kivy — Мессенджер для локальной сети ===")
    print(f"Ваш IP: {LOCAL_IP}:{PORT}")
    print("Ожидание сообщений... (для отправки введите IP и сообщение через пробел)")
    print("Пример: 192.168.1.100 Привет!")

    # Создаём сетевой менеджер
    nm = NetworkManager(on_message_received=handle_message)
    nm.start_listening()

    # Основной цикл: ввод и отправка сообщений
    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue

            # Разбираем ввод: IP и сообщение
            parts = user_input.split(" ", 1)
            if len(parts) < 2:
                print("Формат: <IP> <сообщение>")
                continue

            target_ip, message = parts[0], parts[1]
            nm.send_message(message, target_ip)

        except KeyboardInterrupt:
            print("\nЗавершение работы...")
            break
        except Exception as e:
            print(f"[ОШИБКА] {e}")

if __name__ == "__main__":
    main()
