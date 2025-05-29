import os
import sys
import subprocess
from pathlib import Path

def check_requirements():
    """Перевірка наявності необхідних залежностей"""
    try:
        import torch
        import torchvision
        import numpy
        import PIL
        import cv2
        return True
    except ImportError as e:
        print(f"Помилка: {e}")
        print("Будь ласка, встановіть всі залежності з requirements.txt")
        return False

def setup_environment():
    """Налаштування середовища"""
    # Створення необхідних директорій
    directories = ['models', 'workflows', 'config']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)

def main():
    """Головна функція"""
    print("Запуск LTX AI з ComfyUI...")
    
    if not check_requirements():
        sys.exit(1)
    
    setup_environment()
    
    # Шлях до ComfyUI
    comfyui_path = os.path.join(os.path.dirname(__file__), 'ComfyUI')
    
    if not os.path.exists(comfyui_path):
        print("ComfyUI не знайдено. Клонуємо репозиторій...")
        subprocess.run(['git', 'clone', 'https://github.com/comfyanonymous/ComfyUI.git'])
    
    # Запуск ComfyUI
    os.chdir(comfyui_path)
    subprocess.run([sys.executable, 'main.py'])

if __name__ == "__main__":
    main() 