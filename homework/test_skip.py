"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser as window

@pytest.fixture(params=["mobile", "desktop"])
def browser(request):
    if request.param == "mobile":
        window.driver.set_window_size(640, 960)
    if request.param == "desktop":
        window.driver.set_window_size(1920, 1080)

@pytest.mark.parametrize("browser", ["desktop"], indirect=True)
def test_github_desktop(browser):
    pass

@pytest.mark.parametrize("browser", ["mobile"], indirect=True)
def test_github_mobile(browser):
    pass
