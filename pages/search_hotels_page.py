from selene import browser, have, be
from selene.support.shared.jquery_style import ss


class SearchHotelPage:
    def open_search_page(self):
        browser.open("hotel/russia/rostov-on-don/?dateless_form=yes")
        return self

    def changing_filters_and_researching_hotel(self):
        browser.element('button[data-testid="search-button"]').should(be.visible).click()
        browser.element('#apart').should(be.visible).execute_script('element.click()')
        browser.element('#has_internet').execute_script('element.scrollIntoView()')
        browser.element('#has_internet').should(be.visible).execute_script('element.click()')
        browser.element('#has_parking').should(be.visible).execute_script('element.click()')
        browser.element('#air-conditioning').should(be.visible).execute_script('element.click()')
        browser.element('#balcony').should(be.visible).execute_script('element.click()')
        browser.element('.zen-hotels-leftbar-regioninfo').execute_script('element.scrollIntoView()')
        return self

    def hotel_must_found(self, hotel):
        ss('.zen-hotelcard-address.link').element_by(have.text(hotel.address)).should(be.visible)
        browser.all(".zen-serpresultfilters").should(have.texts(f'{hotel.type}\n{hotel.services_in_the_hotel[0]}\n{hotel.services_in_the_hotel[1]}\n{hotel.services_in_the_room[0]}\n{hotel.services_in_the_room[1]}'))



