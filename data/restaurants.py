"""
This module interfaces to our restaraunts data
"""
import random

ID_LEN = 24
BIG_NUM = 100000000000000000000
RATING = "Rating"
MIN_Group_NAME_LEN = 2
MIN_RESTAURANT_NAME_LEN = 2
CUISINE = "Cuisine"
ADDRESS = "Address"
PRICE = "Price"


"""
Our Contract:
 - No arguments.
 - Returns a dictionary of restaraunts keyed on name (a str).
 - Each user name must be the key for a dictionary.
 - Each restaraunt must have a rating (int)
 """


restaurants = {
     "Shake Shack": {
         RATING: 4,
         PRICE: "$$",
         CUISINE: "American",
         ADDRESS: "123 E 6th Street"
     },
     "Caine's": {
         RATING: 5,
         PRICE: "$$",
         CUISINE: "American",
         ADDRESS: "223 E 4th Street"
     },
}


def get_restaurants():
    return restaurants


def _gen_id() -> str:
    _id = random.randint(0, BIG_NUM)
    _id = str(_id)
    _id = _id.rjust(ID_LEN, '0')
    return _id


def add_restaurant(name: str, rating: int, price: str, cuisine: str, address: str):
    if name in restaurants:
        raise ValueError(f'Duplicate Restaurant name: {name}')
    if not name:
        raise ValueError('Restaurant name may not be blank')
    restaurants[name] = {
         RATING: rating,
         PRICE: price,
         CUISINE: cuisine,
         ADDRESS: address}
    return _gen_id()


def get_restaurant_by_name(restaurant_name):
    """
    Get restaurant details by name.

    Parameters:
    - restaurant_name (str): The name of the restaurant to retrieve.

    Returns:
    - A dictionary containing the restaurant's information, e.g rating
    - Returns None if the restaurant is not found.
    """
    if restaurant_name in restaurants:
        return restaurants[restaurant_name]
    return "Restaurant does not exist"


def get_highly_rated_restaurants(min_rating=4):
    """
    Get a list of highly rated restaurants.

    Parameters:
    - min_rating (int): The minimum rating for a restaurant to be considered
    highly rated.

    Returns:
    - A list of dictionaries, each containing information about highly rated
    restaurants.
    """
    highly_rated_restaurants = [restaurant for restaurant, data in restaurants.items() if data[RATING] >= min_rating]
    return [{restaurant: restaurants[restaurant]} for restaurant in highly_rated_restaurants]


def get_restaurants_with_min_name_length(min_length=MIN_RESTAURANT_NAME_LEN):
    """
    Get a list of restaurants with names of at least a specified minimum length.

    Parameters:
    - min_length (int): The minimum length of restaurant names to include.

    Returns:
    - A list of dictionaries, each containing information about restaurants meeting the criteria.
    """
    valid_restaurants = {restaurant: data for restaurant, data in restaurants.items() if len(restaurant) >= min_length}
    return [{restaurant: valid_restaurants[restaurant]} for restaurant in valid_restaurants]


def search_restaurants(search_criteria, restaurants):
    """
    Search and filter restaurants based on user-defined criteria.

    Parameters:
    - search_criteria (dict): A dictionary containing user-defined search criteria.
        Example:
        {
            "cuisine": "Italian",
            "location": "New York",
            "min_rating": 4
        }
    - restaurants (dict): A dictionary of restaurants with their details.

    Returns:
    - A list of dictionaries, each containing information about restaurants that match the criteria.
    """
    matching_restaurants = []

    for restaurant, data in restaurants.items():
        cuisine = data.get("cuisine", "")
        location = data.get("location", "")
        rating = data.get("rating", 0)

        # Check if the restaurant meets the search criteria
        if (
            (not search_criteria.get("cuisine") or search_criteria["cuisine"].lower() == cuisine.lower()) and
            (not search_criteria.get("location") or search_criteria["location"].lower() == location.lower()) and
            rating >= search_criteria.get("min_rating", 0)
        ):
            matching_restaurants.append({
                "name": restaurant,
                "cuisine": cuisine,
                "location": location,
                "rating": rating
            })

    return matching_restaurants


def exists(name: str) -> bool:
    return name in get_restaurants()
