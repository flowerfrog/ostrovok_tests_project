import allure
from data.hotels import Hotel
from pages.hotel_page import HotelPage


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Moving hotel from favorites")
def test_adding_hotel_to_favorites():
    hotel_page = HotelPage()

    # GIVEN
    hotel = Hotel(
        name='Nabokov Hotel',
        address='Krasnoarmejskaya ulitsa, 168/99, Rostov-on-Don'
    )

    with allure.step("Open the hotel page"):
        hotel_page.open()

    # WHEN
    with allure.step("Adding hotel to favorites"):
        hotel_page.adding_hotel_to_favorites()

    # THEN
    with allure.step("Checking that the hotel was added to favorites"):
        hotel_page.hotel_must_be_added_to_favorites(hotel)


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Moving hotel from favorites")
def test_removing_hotel_to_favorites():
    hotel_page = HotelPage()

    # GIVEN
    hotel = Hotel(
        name='Nabokov Hotel',
        address='Krasnoarmejskaya ulitsa, 168/99, Rostov-on-Don'
    )

    with allure.step("Open the hotel page"):
        hotel_page.open()

    with allure.step("Adding hotel to favorites"):
        hotel_page.adding_hotel_to_favorites()
        hotel_page.hotel_must_be_added_to_favorites(hotel)

    # WHEN
    with allure.step("Remove the hotel from favorites"):
        hotel_page.open()
        hotel_page.remove_hotel_to_favorites()

    # THEN
    with allure.step("Checking that the hotel was removed from favorites"):
        hotel_page.hotel_must_be_removed_from_favorites()
