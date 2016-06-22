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
    print('Mock test')
    objects = mommy.prepare(Example)
    print('Given')
    print(Example.objects.all())
    return objects


@given('I visit the site')
def browser():
    """I visit the site."""
    browser = webdriver.Firefox()
    return browser


@then('I see a window')
def i_see_a_window(live_server, objects, browser, mocker):
    """I see a window."""
    mocker.patch('exampleapp.models.Example.objects.all', lambda: objects)
    print('Then')
    print(Example.objects.all())
    browser.get(live_server.url + '/db/')

