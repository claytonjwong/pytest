import pytest
import time

@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    '''Report the time at the end of a session'''
    yield
    now = time.time()
    print('--')
    print(f'Finished : {time.strftime("%d %b %X", time.localtime(now))}')

@pytest.fixture(autouse=True)
def footer_function_scope():
    '''Report test durations after each function'''
    beg = time.time()
    yield
    end = time.time()
    diff = end - beg
    print(f'\nTest duration : {diff}')

def test_1():
    time.sleep(1)

def test_2():
    time.sleep(1.25)
