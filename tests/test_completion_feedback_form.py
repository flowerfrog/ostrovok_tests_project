import allure
from data.users import UserFeedback
from pages.feedback_pade import FeedbackPage


@allure.tag("web")
@allure.label("owner", "flowerfrog")
@allure.feature("Checking that the feedback form is completed and sent")
def test_feedback_sending():
    feedback_page = FeedbackPage()

    # GIVEN
    feedback = UserFeedback(
        name_user='Alexandra',
        email_user='alxosenn@gmail.com',
        hotel_name='Nabokov Hotel',
        hotel_city='Rostov-on-Don',
        hotel_country='Russia',
        questions='Its question',
        successful_feedback='Thank you, your message has been sent!'
    )

    with allure.step("Open the feedback page"):
        feedback_page.open()

    with allure.step("Filling the feedback form"):
        feedback_page.filling_feedback_form(feedback)

    with allure.step("Checking that feedback has been sent"):
        feedback_page.feedback_form_should_sending(feedback)
