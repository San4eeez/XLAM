import os
from bs4 import BeautifulSoup

# Запрос на ввод пути к папке
folder_path = input("Введите путь к папке с HTML файлами: ")

# Преобразование в абсолютный и экранированный путь
folder_path = os.path.abspath(folder_path)

# Ненужный код для удаления
unwanted_code = '''
<section class="u-backlink u-clearfix u-grey-80">
    <a class="u-link" href="https://nicepage.com/templates" target="_blank">
        <span>Template</span>
    </a>
    <p class="u-text">
        <span>created with</span>
    </p>
    <a class="u-link" href="https://nicepage.com/static-site-generator" target="_blank">
        <span>Static Website Generator</span>
    </a>. 
</section>
'''

# Проверка существования папки
if not os.path.exists(folder_path):
    print(f"Папка {folder_path} не существует.")
else:
    # Проход по всем файлам в указанной папке
    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                # Чтение содержимого файла
                content = file.read()
            
            # Используем BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(content, 'html.parser')
            
            # Находим и удаляем ненужный код
            unwanted_section = soup.find('section', class_='u-backlink u-clearfix u-grey-80')
            if unwanted_section:
                unwanted_section.extract()
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(str(soup))
                print(f'Ненужный код удален из файла: {filename}')
            else:
                print(f'Ненужный код не был найден в файле: {filename}')
