<h1> Проект по тестированию веб-сервиса бронирования отелей "Островок"</h1>

> <a target="_blank" href="https://ostrovok.ru">Ссылка на сайт</a>

![This is an image](design/image/mainpage.png)

#### Список проверок, реализованных в автотестах:
- [x] Поиск отелей по заданным фильтрам с главной страницы сайта
- [x] Изменение фильтров и повторный поиск отеля по заданным фильтрам
- [x] Добавление отеля в избранное
- [x] Удаление отеля из избранного
- [x] Открытие страницы Островок Командировки

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

### Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/008-oddfrog-python-8-15/">Ссылка на проект в Jenkins</a>

#### Параметры сборки

* environment (default stage). Параметр определяет окружение для запуска тестов


### Для запуска автотестов в Jenkins

#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/008-oddfrog-python-8-15/">проект</a>

![This is an image](design/image/jenkins_project.png)

#### 2. Выбрать пункт **Build with Parameters**
#### 3. В случае необходимости изменить параметры, выбрав значение из выпадающего списков
#### 4. Указать комментарий
#### 5. Нажать **Build**
#### 6. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](design/image/jenkins_build.png)



