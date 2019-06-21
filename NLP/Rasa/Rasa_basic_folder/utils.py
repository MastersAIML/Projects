import botconfig
import email_service

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

def buildEmailData(formatted_result):
    """Responsible to frame email body"""
    msg = "\n"
    for obj in formatted_result:        
        msg = msg + ("==> \n\t\t Restaurant name: {name} \n\t\t Locality address: {address}"+
                "\n\t\t Average cost for two: {cft} \n\t\t User rating: {rating} \n\n").format(
                    name=str(obj["name"]), address=str(obj["locality_address"]), 
                    cft=str(obj["average_cost_for_two"]), rating=str(obj["user_rating"]))
    return msg

def sendBotEmail(to_address, search_result = []):
    """Responsible to send restuarent details to user"""
    email_config = botconfig.EMAIL_DETAILS
    body_msg = buildEmailData(search_result)
    body_msg = "Hello user, "+body_msg
    email_service.sendEmail(email_config["credentails"]["email"], email_config["credentails"]["password"], to_address,
                            email_config["default-header"], body_msg)

def transformSearchOutput(result, pricerange, dest):

    min = 300
    max = 700
    if pricerange == '300':
        min = 0
        max = 300
    else:   
        if pricerange == '300-700':
            min = 300
            max = 700
        else:
            min = 700
            max = 10000

    """Responsible to build formatted result"""
    data = []
    count = 0
    maxcount = 10
    if dest == "console":
        maxcount = 5
    response=""
    if result['results_found'] == 0:
        response= "no results found"
    else:
        for obj in result['restaurants']:
            if count == maxcount:
                break
            restaurant = obj['restaurant']
            if (restaurant['average_cost_for_two'] >= min and 
                restaurant['average_cost_for_two'] <= max):
                count = count + 1
                record = {}         
                record["id"] = restaurant['id']
                record["name"] = restaurant['name']
                record["locality_address"] = restaurant['location']["address"]
                record["average_cost_for_two"] = restaurant['average_cost_for_two']
                record["user_rating"] = restaurant['user_rating']["aggregate_rating"]
                response=response+ "Found "+ record["name"] + " in "+ record["locality_address"] + " has been rated "+ record["user_rating"] + " and  avg cost for two is Rs " + str(record["average_cost_for_two"])+"\n"
                data.append(record)
    if dest == "console":
        return response
    else: return data

def transformCuisineOutput(result):
    """Responsible to build dictionary where key is cuisine_id and value is cuisine_value"""
    data = []   
    for obj in result['cuisines']:
        record = {"id":obj["cuisine"]["cuisine_id"], "name":obj["cuisine"]["cuisine_name"]}
        data.append(record)
    return data

def isNotEmpty(s):
    return bool(s and s.strip())