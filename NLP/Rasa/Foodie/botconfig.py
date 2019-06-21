CITIES_CONFIG = {
	"tier-1":["Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Pune"],
	"tier-2":["Agra", "Ajmer", "Aligarh", "Allahabad", "Amravati", "Amritsar", "Asansol", "Aurangabad", "Bareilly", "Belgaum", 
		"Bhavnagar", "Bhiwandi", "Bhopal", "Bhubaneswar", "Bikaner", "Bokaro Steel City", "Chandigarh", "Coimbatore", 
		"Cuttack", "Dehradun", "Dhanbad", "Durg-Bhilai Nagar", "Durgapur", "Erode", "Faridabad", "Firozabad", "Ghaziabad", 
		"Gorakhpur", "Gulbarga", "Guntur", "Gurgaon", "Guwahati", "Gwalior", "Hubli-Dharwad", "Indore", "Jabalpur", "Jaipur",
		"Jalandhar", "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Kannur", "Kanpur", "Kakinada", "Kochi", "Kottayam", 
		"Kolhapur", "Kollam", "Kota", "Kozhikode", "Kurnool", "Lucknow", "Ludhiana", "Madurai", "Malappuram", "Mathura", "Goa", "Mangalore",
		"Meerut", "Moradabad", "Mysore", "Nagpur", "Nanded", "Nashik", "Nellore", "Noida", "Palakkad", "Patna", "Pondicherry", "Raipur", "Rajkot", 
		"Rajahmundry", "Ranchi", "Rourkela", "Salem", "Sangli", "Siliguri", "Solapur", "Srinagar", "Sultanpur", "Surat", "Thiruvananthapuram", 
		"Thrissur", "Tiruchirappalli", "Tirunelveli", "Tiruppur", "Ujjain", "Vijayapura", "Vadodara", "Varanasi", "Vasai-Virar City", "Vijayawada", 
		"Visakhapatnam", "Warangal"]
}

EMAIL_DETAILS = {
	"credentails":{
		"email":"smtp.restaurant.bot59@gmail.com",
		"password":"Duck-tales@6:30pm"
	},
	"default-header":"Greetings from bot",
	"default-body-template":"Hello user, \n Find restaurants details \
							below."
}

NLU_CONFIG = {
	"fixed_modal_name":"restaurant_nlu",
	"nlu_modal_generic_path":"./models/nlu",
	"train_data_location":"./data/data.json",
	"spacy_config_location":"config_spacy.json"
}