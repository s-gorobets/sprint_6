import pytest
from pages.main_page import MainPage
from conftest import *
from urls import URL_BASE
from data.text_ans import question_text
class Test_Questions:
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])

    def test_FAQ(self, driver, num):
        main_page = MainPage(driver)
        main_page.go_to_url()

        main_page.click_to_cookie()
        answer = main_page.get_question_and_answer(num)

        expected_text = question_text[num]
        assert expected_text in answer
