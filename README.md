# LTX AI + ComfyUI (LTX-Video)

## Опис
Цей репозиторій дозволяє швидко розгорнути LTX AI з ComfyUI для генерації зображень та відео.
**Великі моделі не входять у репозиторій!** Їх потрібно завантажити окремо (див. нижче).

---

## Встановлення

### 1. Клонування репозиторію
```bash
git clone https://github.com/your-org/ltxAi.git
cd ltxAi
```

### 2. Створення та активація віртуального середовища
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Встановлення основних залежностей
```bash
pip install -r requirements.txt
```

### 4. Не потрібно клонувати ComfyUI вручну!
При першому запуску `python main.py` ComfyUI автоматично клонуються у вашу директорію, якщо її ще немає.

**Після цього обовʼязково виконайте:**
```bash
cd ComfyUI
pip install -r requirements.txt
cd ..
```

---

## Завантаження моделей

### 1. Перейдіть на [Hugging Face LTX-Video](https://huggingface.co/Lightricks/LTX-Video/tree/main)
Завантажте потрібні моделі (наприклад, `ltxv-2b-0.9.6-dev-04-25.safetensors`).

### 2. Розмістіть файли у відповідних папках:
- **Чекпойнти:**  
  `ComfyUI/models/checkpoints/`
- **VAE:**  
  `ComfyUI/models/vae/`
- **CLIP:**  
  `ComfyUI/models/clip/`
- (інші типи моделей — у відповідні папки)

> **УВАГА:** Не додавайте ці файли у git! Вони дуже великі.

---

## Запуск

```bash
python main.py
```
- Відкрийте браузер: http://127.0.0.1:8188

---

## Додатково

- Якщо при запуску з'являються помилки про відсутність залежностей — встановіть їх з `ComfyUI/requirements.txt` (ComfyUI буде клоновано автоматично при першому запуску).
- Якщо потрібна додаткова модель (наприклад, VAE для SD 1.5), завантажте її з Hugging Face і покладіть у відповідну папку.

---

## .gitignore (приклад)
```
venv/
__pycache__/
*.pyc
ComfyUI/
!ComfyUI/models/
!ComfyUI/models/checkpoints/.gitkeep
!ComfyUI/models/vae/.gitkeep
!ComfyUI/models/clip/.gitkeep
ComfyUI/output/
```

---

## Де брати моделі?
- [Hugging Face LTX-Video](https://huggingface.co/Lightricks/LTX-Video/tree/main)
- [Stable Diffusion 1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- [VAE для SD 1.5](https://huggingface.co/stabilityai/sd-vae-ft-mse-original)

---

## Підтримка
Якщо виникли питання — створіть issue або звертайтесь у командний чат.

## Використання

1. Відкрийте веб-інтерфейс ComfyUI
2. Завантажте робочий процес з папки `workflows`
3. Налаштуйте параметри відповідно до ваших потреб
4. Запустіть генерацію

## Структура проекту

```
ltxAi/
├── main.py              # Головний файл для запуску
├── requirements.txt     # Залежності проекту
├── scripts/            # Допоміжні скрипти
├── models/            # Моделі та ваги
├── workflows/         # Готові робочі процеси
└── config/           # Конфігураційні файли
```

## Додаткові інструкції для GPU

### Перевірка CUDA

1. Переконайтесь, що у вас встановлені драйвери NVIDIA. Для перевірки виконайте:
   ```bash
   nvidia-smi
   ```
   Ви побачите версію драйвера та підтримувану версію CUDA.

2. Встановіть CUDA Toolkit (якщо потрібно):
   - Для PyTorch з cu118 — встановіть CUDA Toolkit 11.8:  
     https://developer.nvidia.com/cuda-11-8-0-download-archive  
     (зазвичай достатньо драйверів, сам toolkit не обов'язковий)

3. Перевірте, чи PyTorch бачить вашу відеокарту:
   ```bash
   python -c "import torch; print(torch.cuda.is_available())"
   ```
   Має бути `True`.

### Встановлення PyTorch з CUDA

1. Видаліть старий torch:
   ```bash
   pip uninstall torch torchvision torchaudio
   ```

2. Встановіть PyTorch для CUDA 11.8 (найбільш стабільно для GTX 1050 Ti):
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

3. Перевірте ще раз:
   ```bash
   python -c "import torch; print(torch.cuda.is_available())"
   ```
   Має бути `True`.

### Якщо CUDA не працює

- Переконайтесь, що ви активували саме ваше venv (має бути (venv) на початку рядка).
- Перевірте, що Python, який ви запускаєте, — це саме той, що у venv:
  ```bash
  where python
  ```
  або
  ```bash
  which python
  ```
- Якщо все одно не працює — спробуйте перезавантажити комп'ютер після встановлення драйверів та torch.

### Примітки

- GTX 1050 Ti має лише 4GB відеопам'яті — для SDXL це дуже мало, можуть бути помилки Out of Memory. Для тесту краще спробувати простіші моделі (наприклад, SD 1.5). 