## Сервис управления рассылками

ЧАСТЬ 1. Разработка сервиса
1. Управление клиентами
Реализовать возможность добавлять, просматривать, редактировать и удалять получателей рассылки (клиентов).
Модель «Получатель рассылки»:
 * Email (строка, уникальное).
 * Ф. И. О. (строка).
 * Комментарий (текст).


2. Управление сообщениями
Реализовать возможность добавлять, просматривать, редактировать и удалять сообщения.
Модель «Сообщение»:
* Тема письма (строка).
* Тело письма (текст).


3. Управление рассылками
Реализовать возможность добавлять, просматривать, редактировать и удалять рассылки.
  Статусы рассылки:
    * Создана — рассылка была создана, но еще ни разу не была отправлена.
    * Запущена — рассылка активна и была отправлена хотя бы один раз.
    * Завершена — время окончания отправки рассылки прошло.

Модель «Рассылка»:
* Дата и время первой отправки (datetime).
* Дата и время окончания отправки (datetime).
* Статус (строка: 'Завершена', 'Создана', 'Запущена').
* Сообщение (внешний ключ на модель «Сообщение»).
* Получатели («многие ко многим», связь с моделью «Получатель»).


4. Отправка сообщений по требованию
Реализовать возможность отправки рассылки вручную через интерфейс пользователя и командную строку.


5. Попытки рассылок
Для каждой попытки отправки рассылки должны сохраняться следующие данные: дата и время попытки, статус
(успешно / не успешно), ответ почтового сервера.

```Попытка рассылки — это запись о каждой попытке отправки сообщения по рассылке. Она содержит информацию о том, была
ли попытка успешной, когда она произошла и какой ответ вернул почтовый сервер.
1. Инициация отправки.
Попытка рассылки создается каждый раз, когда запускается процесс отправки сообщений для конкретной рассылки.
2. Определение получателей.
Список клиентов, которым должно быть отправлено сообщение, определяется из выбранных клиентов для данной рассылки.
3. Отправка сообщения:
  * Для каждого клиента из списка выполняется отправка письма с помощью функции: send_mail() из Django.
  * В случае успешной отправки письма создается запись в модели "Попытка_рассылки" со статусом «успешно».
  * В случае ошибки отправки, например из-за недоступности почтового сервера, создается запись со статусом
  «не успешно» и текстом ошибки в поле «Ответ почтового сервера».
4. Сбор статистики.
Каждая попытка отправки письма фиксируется, что позволяет отслеживать успешные и неуспешные попытки, а также общее
количество попыток.
5. Анализ и отчетность.
Данные о попытках рассылок используются для формирования статистики и отчетности, предоставляя пользователю
информацию о статусе и результатах его рассылок.```

Модель «Попытка рассылки»:
* Дата и время попытки (datetime).
* Статус (строка: 'Успешно', 'Не успешно').
* Ответ почтового сервера (текст).
* Рассылка (внешний ключ на модель «Рассылка»).

6. Главная страница
На главной странице должно отображаться количество всех рассылок, количество активных рассылок (со статусом 'Запущена')
и количество уникальных получателей.

--------------------------------------------------------------------------------
## Стрктура проекта
БД - postpilot
### Управление клиентами
1. Модель «Получатель рассылки»:   - recipient
  * Email (строка, уникальное).                                    - email (unique)
  * Ф. И. О. (строка).                                             - full_name (char=100)
  * Комментарий (текст).                                           - comment (text)


2. Модель «Сообщение»:             - message
  * Тема письма (строка).                                           - subject (char=100)
  * Тело письма (текст).                                            - body_text (text)
  * Дата создания (datetime).                                       - created_at (datetime) -- Добавлено мной для удобства


3. Модель «Рассылка»:              - mailing
  * Дата и время первой отправки (datetime).                        - first_sent_at (datetime)
  * Дата и время окончания отправки (datetime).                     - sent_completed_at (datetime)
  * Статус (строка: 'Завершена', 'Создана', 'Запущена').            - status (char=10)
  * Сообщение (внешний ключ на модель «Сообщение»).                 - message (foreinkey to message)
  * Получатели («многие ко многим», связь с моделью «Получатель»).  - recipients (many-to-many key)


4. Модель «Попытка рассылки»:      - send_attempt
  * Дата и время попытки (datetime).                                - attempt_at (datetime)
  * Статус (строка: 'Успешно', 'Не успешно').                       - status (char=10)
  * Ответ почтового сервера (текст).                                - response (text)
  * Рассылка (внешний ключ на модель «Рассылка»).                   - mailing (foreinkey to mailing)
