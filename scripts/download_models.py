import os
import sys
import requests
from tqdm import tqdm
from pathlib import Path

# Список моделей для завантаження
MODELS = {
    "sd_xl_base_1.0.safetensors": "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors",
    "sd_xl_refiner_1.0.safetensors": "https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors",
}

def download_file(url, filename):
    """Завантаження файлу з прогрес-баром"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(str(filename), 'wb') as file, tqdm(
        desc=str(filename),
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            pbar.update(size)

def main():
    """Головна функція"""
    # Створення директорії для моделей
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    print("Завантаження моделей...")
    
    for model_name, url in MODELS.items():
        model_path = models_dir / model_name
        
        if model_path.exists():
            print(f"Модель {model_name} вже існує, пропускаємо...")
            continue
        
        print(f"Завантаження {model_name}...")
        try:
            download_file(url, model_path)
            print(f"Модель {model_name} успішно завантажена!")
        except Exception as e:
            print(f"Помилка при завантаженні {model_name}: {e}")
            if model_path.exists():
                model_path.unlink()

if __name__ == "__main__":
    main() 