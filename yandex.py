import keyboard
import winsound
import threading
import time
import tkinter as tk

# Секретная комбинация для выхода
EXIT_HOTKEY = 'ctrl+alt+k'

# Переменная для остановки потоков
running = True

# Функция звука "тыдыдыды"
def play_sound():
    frequencies = [400, 600, 800, 1000]
    while running:
        for freq in frequencies:
            if not running: 
                break
            winsound.Beep(freq, 70)
        time.sleep(0.05)

# Функция выхода из пранка
def unlock():
    global running
    running = False
    keyboard.unhook_all()
    root.destroy()

# Блокируем ВСЕ клавиши, кроме комбинации выхода
def lock_keyboard():
    for i in range(150):
        try:
            keyboard.block_key(i)
        except:
            pass
    keyboard.add_hotkey(EXIT_HOTKEY, unlock)

# Запуск звука
threading.Thread(target=play_sound, daemon=True).start()
lock_keyboard()

# Создаем полноэкранное окно
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.config(bg='black')

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

try:
    # Загружаем картинку yandex.png из папки со скриптом
    bg_image = tk.PhotoImage(file="yandex.png")
    
    # Создаем холст и рисуем картинку во весь экран
    canvas = tk.Canvas(root, width=screen_w, height=screen_h, bg='black', highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    # Важное исправление: закрепляем ссылку на картинку внутри canvas, чтобы она не исчезала
    canvas.bg_image = bg_image 
    canvas.create_image(screen_w // 2, screen_h // 2, image=bg_image)
except Exception:
    # Если картинки нет, просто оставляем черный экран без надписей
    pass

root.mainloop()
