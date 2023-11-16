<h1> Проект по тестированию веб-сервиса бронирования отелей "Островок"</h1>

> <a target="_blank" href="https://ostrovok.ru">Ссылка на сайт</a>

![This is an image](design/image/mainpage.png)

#### Список проверок, реализованных в автотестах:
- [x] Поиск отелей по заданным фильтрам с главной страницы сайта
- [x] Изменение фильтров и повторный поиск отеля по заданным фильтрам
- [x] Добавление отеля в избранное
- [x] Удаление отеля из избранного
- [x] Заполнение и отправка формы обратной связи
- [x] Открытие страницы Островок Командировки

----
### Проект реализован с использованием:

<table border="2">
  <tbody>
    <tr>
        <td>Python</td>
        <td>Pytest</td>
        <td>Selene</td>
        <td>Selenium</td>
        <td>Selenoid</td>
        <td>Jenkins</td>
        <td>Allure Reports</td>
        <td>Allure TestOps</td>
        <td>Jira</td>
    </tr>
  </tbody>
</table>

<img src="design/icons/python-original.svg" width="50"> <img src="design/icons/pytest.png" width="50"> <img src="design/icons/intellij_pycharm.png" width="50"> <img src="design/icons/selene.png" width="50"> <img src="design/icons/selenium.png" width="50"> <img src="design/icons/selenoid.png" width="50"> <img src="design/icons/jenkins.png" width="50"> <img src="design/icons/allure_report.png" width="50"> <img src="design/icons/allure_testops.png" width="50"> <img src="design/icons/tg.png" width="50"> <img src="design/icons/jira.png" width="50">

----
### Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/OstrovokSiteAutoTest/">Ссылка на проект в Jenkins</a>

#### Параметры сборки

* `environment` - параметр определяет окружение для запуска тестов
* `comment` - комментарий


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/OstrovokSiteAutoTest/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](design/image/jenkins_build.png)

----
### Allure отчет


#### Общие результаты
![This is an image](design/image/allure_report_overview.png)
#### Список тест кейсов
![This is an image](design/image/allure_report.png)
#### Пример отчета о прохождении теста
![This is an image](design/image/example_test_allure.png)

----

### Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3786/dashboards">Ссылка на проект в AllureTestOps</a> (запрос доступа `admin@qa.guru`)

#### Тест-планы проекта
![This is an image](design/image/allure_TestOps_test_plans.png)

#### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
![This is an image](design/image/allure_TestOps_test_cases.png)

#### Пример отчёта выполнения одного из автотестов
![This is an image](design/image/example_autotests_allure_TestOps.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](design/image/allure_TestOps_dashboard.png)

----
### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-955">Ссылка на проект в Jira</a>

![This is an image](design/image/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](design/image/tg_notification.png)

----
### Пример видео прохождения автотеста
![autotest_gif](design/image/autotest_gif.gif)







