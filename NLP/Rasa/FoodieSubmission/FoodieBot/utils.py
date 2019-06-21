import botconfig
import email_service
import re

def isValidCity(city_name):
    """Responsible to verify provided city name"""
    if city_name is not None:
        all_cities = []
        all_cities.extend(botconfig.CITIES_CONFIG['tier-1'])
        all_cities.extend(botconfig.CITIES_CONFIG['tier-2'])
        all_cities = [city.lower() for city in all_cities]
        if city_name in all_cities:
            return True
        else:
            return False
    else:
        return False

def isValidEmailId(emailid):
	"""Responsible to verify provided provided emailid"""
	pattern = "^[\\w\.]+@[a-zA-Z_]+?\\.[a-zA-Z]{2,3}"
#	print("email id to validate: ", emailid)
	isvalid = False
	if emailid is not None:
		if re.match(pattern,emailid) is not None : 
			isvalid = True
#	print("is mail id valid ? ", isvalid)
	return isvalid

def sendBotEmail(to_address, bodyMsgParams = None):
	"""Responsible to send restuarent details to user"""
	email_config = botconfig.EMAIL_DETAILS
	bodyMsgParams = email_config["default-body-template"] + "\n" + bodyMsgParams

	email_service.sendEmail(
		email_config["credentails"]["email"],
		email_config["credentails"]["password"],
		to_address,
		email_config["default-header"],
		bodyMsgParams)