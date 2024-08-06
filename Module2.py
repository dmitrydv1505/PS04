# Эта программа выполняет:
# 1. Поиск статьи на Википедии по запросу пользователя.
# 2. Позволяет листать параграфы текущей статьи.
# 3. Позволяет переходить на связанные страницы.
# 4. Предлагает пользователю выйти из программы.




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Настройка драйвера
browser = webdriver.Firefox()
#browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

# Функция для поиска статьи на Википедии
def search_wikipedia(query):
    browser.get("https://wikipedia.org/"                "")
    search_box = browser.find_element(By.NAME, value="search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Ждем, пока загрузится страница

# Функция для листания параграфов текущей статьи
def read_paragraphs():
    paragraphs = browser.find_elements(By.CSS_SELECTOR, 'p')
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i+1}: {paragraph.text}")
        input("Нажмите Enter для продолжения...")

# Функция для перехода на связанные страницы
def navigate_links():
    links = browser.find_elements(By.CSS_SELECTOR, 'a')
    link_texts = [link.text for link in links if link.text.strip()]

    for i, text in enumerate(link_texts):
        print(f"{i+1}. {text}")

    choice = int(input("Введите номер ссылки, на которую хотите перейти: ")) - 1
    links[choice].click()
    time.sleep(3)  # Ждем, пока загрузится новая страница

# Основная функция программы
def main():
    query = input("Введите запрос для поиска на Википедии: ")
    search_wikipedia(query)

    while True:
        print("\nЧто вы хотите сделать дальше?")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Введите номер вашего выбора:")

        if choice == '1':
            read_paragraphs()
        elif choice == '2':
            navigate_links()
        elif choice == '3':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

        browser.quit()

if __name__ == "__main__":
    main()

