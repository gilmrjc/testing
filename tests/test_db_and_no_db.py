import pytest

from selenium import webdriver
from exampleapp.models import Example

from model_mommy import mommy

@pytest.mark.django_db()
def test_db(live_server):
    objecto = mommy.make(Example)
    browser = webdriver.Firefox()
    print('Db view test')
    print(Example.objects.all())
    browser.get(live_server.url + '/db')

@pytest.mark.django_db()
def test_no_db(live_server):
    objeto = mommy.make(Example)
    browser = webdriver.Firefox()
    print('No db view test')
    print(Example.objects.all())
    browser.get(live_server.url + '/no-db')
