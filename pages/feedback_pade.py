from selene import browser, be, have, query


class FeedbackPage:
    def open(self):
        browser.open("feedback")
        return self

    def filling_feedback_form(self, feedback):
        browser.element('//form/div[2]/div/div/div[1]/label/div[2]').should(be.visible).click()
        browser.element('input[name="name-hotel"]').should(be.visible).type(feedback.hotel_name)
        browser.element('input[name="contry-city-link"]').should(be.visible).type(feedback.hotel_city)
        browser.element('textarea[name="comment"]').should(be.visible).type(feedback.questions)
        browser.element('input[name="name"]').should(be.visible).type(feedback.name_user)
        browser.element('input[name="email"]').should(be.visible).type(feedback.email_user)
        browser.element('button[type="submit"]').should(be.visible).click()
        return self

    def feedback_form_should_sending(self, feedback):
        browser.element('.zenfeedback-success').should(be.visible).should(have.text(feedback.successful_feedback))
        return self

