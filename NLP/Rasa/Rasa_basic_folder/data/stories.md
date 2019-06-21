## Generated Story 1.1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"Yes"}
    - slot{"sendemail":"Yes"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress":"montygupta@gmail.com"}
    - slot{"emailaddress":"montygupta@gmail.com"}
    - action_email
    - utter_goodbye

## Generated Story 1.2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bandipur"}
    - action_city
    - slot{"city_type": "tier3"}
    - utter_ask_location
* restaurant_search{"location": "abc"}
    - action_city
    - slot{"city_type": "tier3"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"Yes"}
    - slot{"sendemail":"Yes"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress":"montygupta@gmail.com"}
    - slot{"emailaddress":"montygupta@gmail.com"}
    - action_email
    - utter_goodbye

## Generated Story 1.3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"No"}
    - slot{"sendemail":"No"}
    - utter_goodbye

## Generated Story 1.4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "300-700"}
    - slot{"pricerange": "300-700"}
    - action_restaurant
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"Yes"}
    - slot{"sendemail":"Yes"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress":"montygupta@gmail.com"}
    - slot{"emailaddress":"montygupta@gmail.com"}
    - action_email
    - utter_goodbye

## Generated Story 1.5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - action_city
    - slot{"city_type": "tier3"}
	- utter_ask_location
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"No"}
    - slot{"sendemail":"No"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress":"montygupta@gmail.com"}
    - slot{"emailaddress":"montygupta@gmail.com"}
    - action_email
    - utter_goodbye