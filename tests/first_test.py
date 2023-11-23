from pytest_steps import test_steps
import requests

@test_steps('test_first')
def test_get_user_request():
    url = "https://google.com"
    session = requests.session()
    response = session.get(url)
    
    assert (response.status_code == 200), f"Status Code validation failed for {response.request.url}"
    yield