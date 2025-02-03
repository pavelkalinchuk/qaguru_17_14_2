# Проект luma-shop "https://magento.softwaretestingboard.com/"
___

### В разработке тестов использовался следующий стек:  
<img src="resources/macos.png" height="40" width="40" /><img src="resources/python.jpg" height="40" width="50" /><img src="resources/selenium.jpg" height="40" width="50" /><img src="resources/allure.png" height="40" width="40" /><img src="resources/jenkins.svg" height="40" width="40" /><img src="resources/github.png" height="40" width="40" /><img src="resources/telegram.png" height="40" width="40" /><img src="resources/selenoid.jpg" height="40" width="60" />
___

## Описание проекта
В данном проекте реализован автотест покупки толстовки "Marco Lightweight Active Hoodie" на сайте "https://magento.softwaretestingboard.com/"

Сайт:

<img src="resources/luma_shop.png" height="40" width="100" />

Покупаемый товар:

<img src="resources/hudies.png" height="170" width="270" />

На текущий момент реализован тест по следующиму сценарию:
- Открываем домашнюю страницу сайта
- Переходим в раздел товаров для мужчин
- Переходим в раздел "Худи и Свитшоты"
- Находим и открываем карточку с худи которое имеет название "Marco Lightweight Active Hoodie"
- Выбираем нужный размер
- Выбираем нужный цвет
- Добавляем выбранный товар в карзину
- Проверяем наличия сообщения об успешном добавлении товара в казину
- Открываем карзину
- Проверяем что в корзине содержится то, что было выбрано

___ 
### Примечание:
*Проект проверен на локальных запусках и с помощью Jenkins*
___

### Локальный запуск тестов

#### Запуск:
1. В терминале перейти в каталог с тестом *'/tests'*
2. Используя команду `pytest test_site_hh.py` выполнить запус тестов
#### Фомирование отчёта:
1. По завершению работы тестов находясь в том же каталоге, выполнить команду `allure generate`. В результате будет создан каталог 'allure-report' с данными отчёта
2. Далее запустить команду `allure open allure-report`. В результате будет открыта вэб-страница с allure-отчётом

> *Примечание!* 
> 
> *Если отчёт не открывается при выполнении команды описанной выше, то можно попробовать открыть отчёт командой:* 
> 
>`allure open -h localhost -p 8081`
> 
>*Данная проблема может встретится на ПК под управлением MacOS!*
___


### Запуск тестов в Jenkins

#### Запуск:
1. Откройте сраницу [проекта](https://jenkins.autotests.cloud/job/017-pavel_kalinchuk-test_hhru_unit14/)
2. В левом меню выберите пункт "Build now"
3. Дождитесь завершения работы тестов
5. После сборки, результат работы можно увидеть в ``Allure Report``

#### Просмотр отчёта:
1. В области "Build" *(левая нижняя часть экран)* кликните на пиктограмме *allure*
2. Дождитесь откытия страницы отчёта

## Примеры отчётов

### В Allure

#### Общий
<img src="resources/main_report_page.png" width="630" height="320"/>

#### Детальный

<img src="resources/detail_report_page.png" width="630" height="320"/>

#### Видеопрохождение теста

<img src="resources/luma_shop_test.gif" width="630" height="320"/>

### В Telegram

<img src="resources/telegram_report.png" width="350" height="450"/>

---

