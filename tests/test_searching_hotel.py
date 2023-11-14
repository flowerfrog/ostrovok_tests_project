import allure

from data.hotels import SearchingHotel
from data.users import User
from pages.main_page import MainPage
from pages.search_hotels_page import SearchHotelPage


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Search for a hotel")
def test_searching_hotel_from_main_page():
    main_page = MainPage()

    # GIVEN
    user = User(
        destination_city='Rostov-on-Don',
        destination_country='Russia',
        arrival_date='22 Nov 2023',
        departure_date='29 Nov 2023',
        count_room=1,
        count_guests=3
    )

    with allure.step("Open the main page"):
        main_page.open()

    # WHEN
    with allure.step("Select values in filters and apply filters"):
        main_page.search_hotel(user)

    # THEN
    with allure.step("Checking that the hotel search result matches the user’s filters"):
        main_page.hotel_must_found(user)


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Search for a hotel")
def test_changing_filters_and_researching_hotel():
    search_hotels_page = SearchHotelPage()

    # GIVEN
    hotel = SearchingHotel(
        name='',
        address='Rostov-on-Don',
        type="Apartments",
        services_in_the_hotel=['Free Internet', 'Parking'],
        services_in_the_room=['Air conditioning', 'Balcony'],
    )

    with allure.step("Open the search hotels page"):
        search_hotels_page.open_search_page()

    # WHEN
    with allure.step("Select values in filters and apply filters"):
        search_hotels_page.changing_filters_and_researching_hotel(hotel)

    # THEN
    with allure.step("Checking that the hotel search result matches the user’s filters"):
        search_hotels_page.hotel_must_found(hotel)
