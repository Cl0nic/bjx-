import json
import os

STORAGE = "cloud.json"

def load():
    if os.path.exists(STORAGE):
        with open(STORAGE, "r", encoding="utf-8") as f:
            return json.load(f)

def save(data):
    with open(STORAGE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def upload(filename, content):
    data = load()
    if not filename.endswith(".png"):
        print("file not is png , poshel naxyi")
        return

    data[filename] = content
    save(data)
    print(f"гааа, {filename}")

def download(filename):
    data = load()
    if not filename.endswith(".png"): 
        print("скачать можно токо фото .Png  ")  
        return

        data = load()
        filename in data
        print(f"{filename}:")
        print(data[filename])
    else:
        print("файл не найден")

def delete(filename):
    data = load()
    if filename in data:
        del data[filename]
        save(data)
        print(f"файл удален {filename}")
    else:
        print("файла ниту")

def list_files():
    data = load()

    if not data: 
        print("облоко пустое загурите файлы ")
        return

    print(f"в облоке файлов {len(data)} Файлов: ")
    for name  in data:
        print(f"-{name}")

       # --- ФИНАЛЬНЫЙ ТЕСТ ---
print("1. Загружаем новую картинку:")
upload("meme.png", "смешной мем")

print("\n2. Смотрим, что в облаке:")
list_files()

print("\n3. Пробуем скачать meme.png:")
download("meme.png")

print("\n4. Удаляем meme.png:")
delete("meme.png")

print("\n5. Смотрим список (meme.png должен исчезнуть, а старые файлы остаться):")
list_files()

list_files()
delete("kartinka.png")
list_files()