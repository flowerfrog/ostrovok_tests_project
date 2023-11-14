import allure
from pages.main_page import MainPage


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Search for a hotel for business trips")
def test_searching_hotel_fo_business():
    main_page = MainPage()

    with allure.step("Open the main page"):
        main_page.open()

    # WHEN
    with allure.step("Click to button 'For business trips'"):
        main_page.click_to_tab_for_business_trips()

    # THEN
    with allure.step("Checking that open page https://corp.ostrovok.ru"):
        main_page.button_was_clicked()
