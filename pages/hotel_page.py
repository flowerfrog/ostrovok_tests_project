from selene import browser, have


class HotelPage:
    def open(self):
        browser.open("hotel/russia/rostov-on-don/mid6718553/loftotel_nabokov")
        return self

    def adding_hotel_to_favorites(self):
        browser.element('.PopupSearchForm_close__kMbOA').execute_script('element.click()')
        browser.element('.HotelHeader_favorite__RVb7z').click()
        return self

    def hotel_must_be_added_to_favorites(self, hotel):
        browser.open("sp/favorite/")
        browser.element(".HotelCard__hotelInfo--1hN4g > a").should(have.text(hotel.name))
        browser.element(".HotelCard__hotelInfo--1hN4g > span").should(have.text(hotel.address))
        return self

    def remove_hotel_to_favorites(self):
        browser.element('.HotelHeader_favorite__RVb7z').click()
        return self

    def hotel_must_be_removed_from_favorites(self):
        browser.open("sp/favorite/")
        browser.element(".FavoriteHotels__favoriteHotelsText--kAcEs").should(have.text("You have no favorite hotels yet. Start adding the hotels you liked by clicking the heart icon, and they'll appear here."))
        return self
