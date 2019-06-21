from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
from botconfig import NLU_CONFIG
import utils

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f220c8cdf836b8fcd4dab5fbd535c646"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		pricerange = tracker.get_slot('pricerange')
		cft = "1"
		if pricerange == '300':
			cft = "0"
		else:
		 	if pricerange == '700': cft = "2"
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'north indian':50,'south indian':85}
		results=zomato.restaurant_search_by_rating_desc("", lat, lon, str(cuisines_dict.get(cuisine)), cft , 20)
		response = utils.transformSearchOutput(json.loads(results), pricerange, "console")
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class ActionSearchCity(Action):
	def name(self):
		return 'action_city'
		
	def run(self, dispatcher, tracker, domain):
		city_name = tracker.get_slot('location')
		is_Valid_city = utils.isValidCity(city_name)
		resp = ""
		city_type = "tier1_2"
		if is_Valid_city == False:
			resp = "Service not available in this city"
			city_type = "tier3"	
		dispatcher.utter_message("-----"+resp)
		return [SlotSet('city_type',city_type)]	

class ActionSendEmail(Action):
	def name(self):
		return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f220c8cdf836b8fcd4dab5fbd535c646"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		pricerange = tracker.get_slot('pricerange')
		emailid = tracker.get_slot('emailaddress')
		cft = "1"
		if pricerange == '300':
			cft = "0"
		else:
		 	if pricerange == '700': cft = "2"
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'north indian':50,'south indian':85}
		results=zomato.restaurant_search_by_rating_desc("", lat, lon, str(cuisines_dict.get(cuisine)), cft , 20)
		data = utils.transformSearchOutput(json.loads(results), pricerange, "email")
		utils.sendBotEmail(emailid, data)
		print ("-- Email Sent")
		return [SlotSet('emailaddress',emailid)]	

