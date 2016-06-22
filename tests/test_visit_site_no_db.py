# coding=utf-8
"""tests/visit_site.features feature tests."""

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from selenium import webdriver
from exampleapp.models import Example
from model_mommy import mommy


@pytest.mark.django_db
@scenario('visit_site.features', 'Visiting the site')
def test_visiting_the_site():
    """Visiting the site."""

@given('I create objects')
def objects():
    print('no db')
    objects = mommy.make(Example)
    print('Given')
    print(Example.objects.all())
    return objects
    


@given('I visit the site')
def browser():
    """I visit the site."""
    browser = webdriver.Firefox()
    return browser


@then('I see a window')
def i_see_a_window(live_server, browser):
    """I see a window."""
    print('Then')
    print('Objects: ', Example.objects.all())
    browser.get(live_server.url + '/no-db/')

