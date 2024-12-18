**Library management**
---

**Задача:**

Необходимо разработать REST API для управления библиотечным каталогом. 
API должно позволять работать с книгами, авторами и выдачей книг читателям.

---
**Технические требования:**

- Язык программирования:
  - Python 3.12
- Фреймворк:
  - FastAPI 0.115.6
- ORM:
  - SQLAlchemy 2.0 
- Хранение данных:
  - PostgreSQL
 
---
**Запуск проекта:**

- Клонируйте проект 
- Создайте файл .env в корне проекта по образцу (Файл .env.sample)
- Убедитесь, что на Вашем устройстве установлен Docker
- Осуществите сборку образов и запуск контейнеров (docker compose up -d --build)


---
**Структура базы данных:**

Таблица Author (Автор): 

- id,
- имя,
- фамилия,
- дата рождения.

Таблица Book (Книга):

- id,
- название,
- описание,
- id автора,
- количество доступных экземпляров.

Таблица Borrow (Выдача):

- id,
- id книги,
- имя читателя,
- дата выдачи,
- дата возврата.

---
**Функционал и бизнес-логика:**

Дата рождения автора не может быть раньше текущей даты.
Перед выдачей книги производится проверка наличия доступных экземпляров книги.
При выдаче книги количество доступных экземпляров уменьшается на один, а при возврате увеличивается.
По одной выдаче возможен только один возврат.


![image](https://github.com/user-attachments/assets/533ce321-e2ab-4b0c-9800-27ae26e11819)

