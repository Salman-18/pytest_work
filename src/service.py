import requests
database = {
    1: "salman",
    2 : "ahmed",
    3 : "anshal",
    4 : "ishaque"
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code  == 200:
        return response.json()
    raise requests.HTTPError("Failed to retrieve data from the API. Status code: {}".format(response.status_code))



