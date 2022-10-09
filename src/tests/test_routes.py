from httpx import post, get

url_healthcheck = "http://localhost:5000/"
url_shipping = "http://localhost:5000/shipping"

def test_get_healthcheck_200():
    request = get(url_healthcheck)
    assert request.status_code == 200

def test_post_shipping_201():
    request = post(url_shipping)
    assert request.status_code == 308 or 201
    