from selene import browser, be, have


class MainPage:
    def open(self):
        browser.open("")
        return self

    def search_hotel(self, user):
        browser.element('input[data-testid="destination-input"]').should(be.visible).type(f'{user.destination_city}, {user.destination_country}')
        browser.element('div[title="Rostov-on-Don, Russia"]').should(be.visible).click()
        browser.element('div[data-testid="date-start-input"]').should(be.visible).click()
        browser.element('div.Grid-module__months--2K2vv > div:nth-child(1) > div:nth-child(5) > div:nth-child(4)').should(be.visible).click()
        browser.element('div.Grid-module__months--2K2vv > div:nth-child(1) > div:nth-child(6) > div:nth-child(4)').should(be.visible).click()
        browser.element('div[data-testid="guests-input"]').should(be.visible).click()
        browser.element('div.Counter-module__wrapper--2E40x > button:nth-child(3)').should(be.visible).click()
        browser.element('.Button-module__button--MR2Ly.Button-module__button_size_m--184Hw.Button-module__button_wide--eV274.Form-module__button--3EXOP').should(be.visible).click()
        browser.element('button[data-testid="search-button"]').should(be.visible).click()
        return self

    def hotel_must_found(self, user):
        browser.all(".zenregioninfo").should(have.texts(
            f'{user.destination_city}, {user.destination_country}\n{user.arrival_date} — {user.departure_date}\n{user.count_room} room for {user.count_guests} guests'))
        return self
