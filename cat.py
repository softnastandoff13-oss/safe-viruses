import cv2
import tkinter as tk
from tkinter import messagebox
import os
import sys
import ctypes
import keyboard  # Требуется: pip install keyboard

# Функция экстренного выхода
def emergency_exit():
    # Возвращаем мышь в нормальное состояние
    ctypes.windll.user32.ClipCursor(None)
    # Снимаем блокировку кнопок
    keyboard.unhook_all()
    cv2.destroyAllWindows()
    sys.exit(0)

def play_cat_video():
    if getattr(sys, 'frozen', False):
        current_dir = os.path.dirname(sys.executable)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    
    video_path = os.path.join(current_dir, "cat.mp4")

    if not os.path.exists(video_path):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Ошибка", f"Файл cat.mp4 не найден в папке:\n{current_dir}")
        return

    # Получаем размеры экрана
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    # --- ЗАПУСК БЛОКИРОВКИ ---
    
    # Секретная комбинация для выхода
    keyboard.add_hotkey('ctrl+alt+shift+q', emergency_exit)
    
    # Блокируем клавиши (без прав админа заблокирует почти всё, кроме Win и Ctrl+Alt+Del)
    for i in range(150):
        try:
            keyboard.block_key(i)
        except:
            pass

    # Запираем мышку в пикселе (0,0) в левом верхнем углу
    rect = (ctypes.c_long * 4)(0, 0, 1, 1)
    ctypes.windll.user32.ClipCursor(ctypes.byref(rect))
    
    # --- НАСТРОЙКА ВИДЕО ---

    cap = cv2.VideoCapture(video_path)
    window_name = "Cat Video"
    
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window_name, 0, 0)
    cv2.resizeWindow(window_name, screen_width, screen_height)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            # Зацикливаем видео
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        frame_resized = cv2.resize(frame, (screen_width, screen_height))
        cv2.imshow(window_name, frame_resized)

        # Клавиша Esc (код 27) для быстрого выхода
        key = cv2.waitKey(25) & 0xFF
        if key == 27:
            break

        # Проверяем окно ТОЛЬКО после того, как оно гарантированно создалось
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

    emergency_exit()

if __name__ == "__main__":
    # Запускаем напрямую без проверок на администратора
    play_cat_video()
