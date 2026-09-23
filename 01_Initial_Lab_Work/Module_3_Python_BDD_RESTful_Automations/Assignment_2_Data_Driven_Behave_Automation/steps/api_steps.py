from behave import given, when, then
import requests


@given('I send a GET request for user ID "{user_id}"')
def send_get_request(context, user_id):
    context.user_id = user_id
    context.response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )


@when("the API response is received")
def response_received(context):
    assert context.response is not None


@then("the response status code should be 200")
def verify_status_code(context):
    assert context.response.status_code == 200


@then('the response should contain user ID "{user_id}"')
def verify_user_id(context, user_id):
    data = context.response.json()
    assert data["id"] == int(user_id)