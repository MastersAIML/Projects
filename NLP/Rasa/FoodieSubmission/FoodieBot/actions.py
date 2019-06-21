from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import AllSlotsReset
from rasa_core.events import SlotSet
import zomatopy
import json
from botconfig import NLU_CONFIG
import utils

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"4246fccd5eab15a8c276179641863325"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		pricerange = tracker.get_slot('pricerange')
		cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'north indian':50,'south indian':85}
		
		if cuisine is None:
			cuisine = ""
		
		print("INFO: Looking for restaurants in '" + loc + "' serving '" + cuisine + "' cuisine with average budget for 2 people in range " + pricerange + ".")
		cft = "1"
		if pricerange == '300':
			cft = "0"
		else:
		 	if pricerange == '700': cft = "2"
		
		
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		results=zomato.restaurant_search_by_rating_desc("", lat, lon, str(cuisines_dict.get(cuisine)), cft , 20)
		d = json.loads(results)
		response=""
		count = 0
		if d['results_found'] == 0:
			response= "Sorry. No results found. You can try some other combinations."
		else:
			for restaurant in d['restaurants']:
				if count == 5:
					break
				if pricerange == '300':
					if restaurant['restaurant']['average_cost_for_two'] <= 300: 
						count = count + 1
						response=response+ str(count)+". "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] + " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating'] + ". And the average price for two people here is Rs " + str(restaurant['restaurant']['average_cost_for_two'])+"\n"
				else:
					if pricerange == '700':
						if restaurant['restaurant']['average_cost_for_two'] > 700: 
							count = count + 1
							response=response+ str(count)+". "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] + " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+ ". And the average price for two people here is Rs " + str(restaurant['restaurant']['average_cost_for_two'])+"\n"
					else: 
						if restaurant['restaurant']['average_cost_for_two'] > 300 and restaurant['restaurant']['average_cost_for_two'] <= 700: 
							count = count + 1
							response=response+ str(count)+". "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] + " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+ ". And the average price for two people here is Rs " + str(restaurant['restaurant']['average_cost_for_two'])+"\n"
		dispatcher.utter_message("\nShowing you top rated restaurants:\n\n" + response)
		return [SlotSet('location',loc)]

class ActionSearchCity(Action):
	def name(self):
		return 'action_city'
		
	def run(self, dispatcher, tracker, domain):
		city_name = tracker.get_slot('location')
		is_Valid_city = utils.isValidCity(city_name)
		city_type = "tier1_2"
		if is_Valid_city == False:
			city_type = "tier3"	
		return [SlotSet('city_type',city_type)]	

class ActionSendEmail(Action):
	def name(self):
		return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		emailid = tracker.get_slot('emailaddress')
		emailbody = ""
		#print ("sending email on ", emailid)
		if utils.isValidEmailId(emailid) :
			print("INFO: mail id is valid")
			config={ "user_key":"4246fccd5eab15a8c276179641863325"}
			zomato = zomatopy.initialize_app(config)
			loc = tracker.get_slot('location')
			cuisine = tracker.get_slot('cuisine')
			pricerange = tracker.get_slot('pricerange')
			budget = "Rs. 300 to 700"

			if cuisine is None:
				cuisine = ""
			
			cft = "1"
			if pricerange == '300':
				cft = "0"
				budget = "lesser than Rs. 300"
			elif pricerange == '700':
					cft = "2"
					budget = "more than Rs. 700"
			
			emailbody = "As per your search criteria you were looking for restaurants in '" + loc + "' serving '" + cuisine + "' cuisine with average budget for 2 people in " + budget + " range.\n"
			
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'north indian':50,'south indian':85}
			results=zomato.restaurant_search_by_rating_desc("", lat, lon, str(cuisines_dict.get(cuisine)), cft , 20)
			d = json.loads(results)
			response=""
			count = 0
			if d['results_found'] == 0:
				response= "\nSorry. No results found. You can try some other combinations."
			else:
				response=response+ "\nS.No.\t | \t"+ "Restaurant Name" + "\t | \t"+ "Restaurant Location" + "\t | \t"+ "Restaurant Rating" + "\t | \t" + "Average Cost for 2 people" +"\n"
				for restaurant in d['restaurants']:
					if count == 10:
						break
					if pricerange == '300':
						if restaurant['restaurant']['average_cost_for_two'] <= 300: 
							count = count + 1
							response=response+ str(count)+".\t | \t"+ restaurant['restaurant']['name']+ "\t | \t"+ restaurant['restaurant']['location']['address'] + "\t | \t"+ restaurant['restaurant']['user_rating']['aggregate_rating'] + "\t | \t" + str(restaurant['restaurant']['average_cost_for_two'])+"\n"
					else:
						if pricerange == '700':
							if restaurant['restaurant']['average_cost_for_two'] > 700: 
								count = count + 1
								response=response+ str(count)+".\t | \t"+ restaurant['restaurant']['name']+ "\t | \t"+ restaurant['restaurant']['location']['address'] + "\t | \t"+ restaurant['restaurant']['user_rating']['aggregate_rating']+ "\t | \t" + str(restaurant['restaurant']['average_cost_for_two'])+"\n"
						else: 
							if restaurant['restaurant']['average_cost_for_two'] > 300 and restaurant['restaurant']['average_cost_for_two'] <= 700: 
								count = count + 1
								response=response+ str(count)+".\t | \t"+ restaurant['restaurant']['name']+ "\t | \t"+ restaurant['restaurant']['location']['address'] + "\t | \t"+ restaurant['restaurant']['user_rating']['aggregate_rating']+ "\t | \t" + str(restaurant['restaurant']['average_cost_for_two'])+"\n"
			
			emailbody = emailbody + "\nResults:\n\n" + response
			
			utils.sendBotEmail(emailid, bodyMsgParams = emailbody)
        
		else:
			emailid = None
			
		return [SlotSet('emailaddress',emailid)]	

class ActionResetSlots(Action):
	def name(self):
		return 'action_slot_reset'
	
	def run(self, dispatcher, tracker, domain):
			return[AllSlotsReset()]