import hashlib 
import json
import requests

# Get the object from server
# json_entry = '{"numero_casas": 10,"token":"token_do_usuario","cifrado": "az texto criptografado","decifrado": "aqui vai o texto decifrado","resumo_criptografico": "aqui vai o resumo"}'
json_entry = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token= **SEU TOKEN**')

# Load JSON to get the target text
response = json_entry.json()

# Put target text in a variable
text = response['cifrado']
# Put the text in lowercase
text = text.lower() 

# Put target text shift in a variable
shift = -response['numero_casas']

# View target text just for DEBUG
# print(text)

# creates a list of numbers
numbers = []

# For each letter in text
for i in range(len(text)):
	# Get the letter number
	number = ord(text[i])
	number_shifted = number
	if (number >= 97 and number <= 122):
		number_shifted = number + shift

		if (number_shifted > 122):
			number_shifted = number_shifted - 26

		if (number_shifted < 97):
			number_shifted = number_shifted + 26

	numbers.append(number_shifted)

# Display numbers list just for DEBUG
# print(numbers)


# creates a list of numbers
new_text = ""

# For each letter in text
for i in range(len(text)):
	# Get the char from number
	letter = chr(numbers[i])
	new_text = new_text + letter

response['decifrado'] = new_text
response['resumo_criptografico'] = hashlib.sha1(new_text.encode()).hexdigest() 


# convert into JSON:
response_json = json.dumps(response)

# the result is a JSON string:
print(response_json)



# Load JSON to post the target processed text data
posted = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=f429699844626afddfc6e759398026b0311b0561', files=dict(answer=response_json))

# Load JSON to get the target text
posted_json_return = posted.json()
print(posted_json_return)
