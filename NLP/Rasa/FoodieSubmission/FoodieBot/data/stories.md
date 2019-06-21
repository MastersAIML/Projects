## Generated Story 1.1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"True"}
    - slot{"sendemail":"True"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress":"montygupta@gmail.com"}
    - slot{"emailaddress":"montygupta@gmail.com"}
    - action_email
	- slot{"emailaddress":"montygupta@gmail.com"}
	- utter_mailsent
    - utter_enjoy
	- action_slot_reset

## Generated Story 1.2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bandipur"}
    - slot{"location": "bandipur"}
    - action_city
    - slot{"city_type": "tier3"}
	- utter_deny
    - utter_ask_location
* restaurant_search{"location": "abc"}
    - slot{"location": "abc"}
    - action_city
    - slot{"city_type": "tier3"}
	- utter_deny
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"True"}
    - slot{"sendemail":"True"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress":"montygupta@gmail.com"}
    - slot{"emailaddress":"montygupta@gmail.com"}
    - action_email
    - slot{"emailaddress":"montygupta@gmail.com"}
	- utter_mailsent
    - utter_enjoy
	- action_slot_reset

## Generated Story 1.3
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
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location":"delhi"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"False"}
    - slot{"sendemail": "False"}
    - utter_goodbye
    - utter_enjoy
	- action_slot_reset
	
## Generated Story 1.4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location":"delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "300-700"}
    - slot{"pricerange": "300-700"}
    - action_restaurant
    - slot{"location":"delhi"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"True"}
    - slot{"sendemail":"True"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress":"montygupta@gmail.com"}
    - slot{"emailaddress":"montygupta@gmail.com"}
    - action_email
    - slot{"emailaddress":"montygupta@gmail.com"}
	- utter_mailsent
    - utter_enjoy
	- action_slot_reset

## Generated Story 1.5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location":"italy"}
    - action_city
    - slot{"city_type": "tier3"}
	- utter_deny
	- utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location":"lucknow"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "300"}
    - slot{"pricerange": "300"}
    - action_restaurant
    - slot{"location":"lucknow"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"False"}
    - slot{"sendemail":"False"}
    - utter_goodbye
	- utter_enjoy
	- action_slot_reset

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
	- utter_enjoy
	- action_slot_reset


## Generated Story 1.6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bandipur"}
    - slot{"location": "bandipur"}
    - action_city
    - slot{"city_type": "tier3"}
	- utter_deny
    - utter_ask_location
* restaurant_search{"location": "abc"}
    - slot{"location": "abc"}
    - action_city
    - slot{"city_type": "tier3"}
	- utter_deny
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail":"False"}
    - slot{"sendemail":"False"}
    - utter_goodbye
	- utter_enjoy
	- action_slot_reset

	
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
	- action_slot_reset

## Generated Story -4556702529894254123
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_city
    - slot{"city_type": "tier1_2"}
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
	- action_slot_reset

## Generated Story -4556702529894254123_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "300-700"}
    - slot{"pricerange": "300-700"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "False"}
    - slot{"sendemail": "False"}
    - utter_goodbye
    - utter_enjoy
	- action_slot_reset

## Generated Story -4556702529894254123_2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True", "emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"sendemail": "True"}
    - action_email
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - utter_mailsent
    - utter_enjoy
	- action_slot_reset

## Generated Story -4556702529894254123_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh", "pricerange": "300-700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - slot{"pricerange": "300-700"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "False"}
    - slot{"sendemail": "False"}
    - utter_goodbye
    - utter_enjoy
	- action_slot_reset

## Generated Story -4556702529894254123_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh", "pricerange": "300-700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - slot{"pricerange": "300-700"}
    - action_city
    - slot{"city_type": "tier1_2"}
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
	- action_slot_reset

## Generated Story -4556702529894254123_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "bangalore", "pricerange": "300"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bangalore"}
    - slot{"pricerange": "300"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True", "emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"sendemail": "True"}
    - action_email
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - utter_mailsent
    - utter_enjoy
	- action_slot_reset

## Generated Story -4556702529894254123_6
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bangalore", "pricerange": "700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - slot{"pricerange": "700"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "False"}
    - slot{"sendemail": "False"}
    - utter_goodbye
    - utter_enjoy
	- action_slot_reset

## Generated Story -4556702529894254123_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bangalore", "pricerange": "700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - slot{"pricerange": "700"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True"}
    - slot{"sendemail": "True"}
    - utter_ask_emailaddress
* emailconfirmation{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - action_email
    - utter_mailsent
    - utter_enjoy
	- action_slot_reset

## Generated Story -4556702529894254123_8
* greet
    - utter_greet
* restaurant_search{"location": "bandipur"}
    - slot{"location": "bandipur"}
    - action_city
    - slot{"city_type": "tier3"}
	- utter_deny
	- utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "lucknow"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True", "emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"sendemail": "True"}
    - action_email
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - utter_mailsent
    - utter_enjoy
	- action_slot_reset
	

## Generated Story -4556702529894254123_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
	- utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - utter_ask_price_range
* restaurant_search{"pricerange": "700"}
    - slot{"pricerange": "700"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True", "emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"sendemail": "True"}
    - action_email
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - utter_mailsent
    - utter_enjoy
	- action_slot_reset

## Generated Story -4556702529894254123_11
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "pricerange": "700"}
    - slot{"cuisine": "north indian"}
    - slot{"pricerange": "700"}
	- utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True", "emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"sendemail": "True"}
    - action_email
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - utter_mailsent
    - utter_enjoy
	- action_slot_reset

## Generated Story -4556702529894254123_12
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "pricerange": "700"}
    - slot{"cuisine": "north indian"}
    - slot{"pricerange": "700"}
	- utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_city
    - slot{"city_type": "tier3"}
	- utter_deny
	- utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"city_type": "tier1_2"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_sendemail
* emailconfirmation{"sendemail": "True", "emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - slot{"sendemail": "True"}
    - action_email
    - slot{"emailaddress": "rohitash.kainth@gmail.com"}
    - utter_mailsent
    - utter_enjoy
	- action_slot_reset
