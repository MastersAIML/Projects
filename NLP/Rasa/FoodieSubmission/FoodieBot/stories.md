## Generated Story 3884163192287029647
* goodbye
    - utter_greet
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
* restaurant_search
    - export

## Generated Story 3526466347112259377
* greet
    - export

## Generated Story 7796198434620052377
* greet
* greet
    - export

## Generated Story 1453138857447164698
* greet
    - utter_greet
* restaurant_search
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
* affirm{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
* restaurant_search{"location": "range"}
    - slot{"location": "range"}
* restaurant_search
    - export

## Generated Story -2814829874628903759
* greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
* restaurant_search
    - utter_ask_price_range
* restaurant_search
* restaurant_search
    - export

## Generated Story 694903493758605683
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "300-700"}
    - slot{"pricerange": "300-700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "False"}
    - slot{"sendemail": "False"}
    - utter_goodbye
    - export

## Generated Story -2879278848138566604
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True"}
    - slot{"sendemail": "True"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - action_email
    - utter_mailsent
    - utter_enjoy
    - export

## Generated Story -4556702529894254123
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "300-700"}
    - slot{"pricerange": "300-700"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True", "emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"sendemail": "True"}
    - action_email
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - utter_mailsent
    - utter_enjoy
    - export

