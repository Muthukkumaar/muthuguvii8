import requests

# Function to fetch data from BreweryDB API
def fetch_breweries(state):
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    url = f'https://sandbox-api.brewerydb.com/v2/breweries?key={api_key}&region={state}'
    response = requests.get(url)
    data = response.json()
    return data

# Task 1: List names of all breweries in Alaska, Maine, and New York
def list_breweries_names(states):
    breweries_names = []
    for state in states:
        data = fetch_breweries(state)
        breweries = data['data']
        for brewery in breweries:
            breweries_names.append(brewery['name'])
    return breweries_names

# Task 2: Count of breweries in each state
def count_breweries(states):
    breweries_count = {}
    for state in states:
        data = fetch_breweries(state)
        breweries_count[state] = data['totalResults']
    return breweries_count

# Task 3: Count number of types of breweries in individual cities
def count_brewery_types(states):
    brewery_types_count = {}
    for state in states:
        data = fetch_breweries(state)
        breweries = data['data']
        for brewery in breweries:
            city = brewery.get('city', 'Unknown')
            brewery_type = brewery.get('breweryType', 'Unknown')
            if city not in brewery_types_count:
                brewery_types_count[city] = {}
            if brewery_type in brewery_types_count[city]:
                brewery_types_count[city][brewery_type] += 1
            else:
                brewery_types_count[city][brewery_type] = 1
    return brewery_types_count

# Task 4: Count and list how many breweries have websites
def count_breweries_with_websites(states):
    breweries_with_websites = {}
    for state in states:
        data = fetch_breweries(state)
        breweries = data['data']
        count = 0
        for brewery in breweries:
            if 'website' in brewery:
                count += 1
        breweries_with_websites[state] = count
    return breweries_with_websites

# States of interest
states_of_interest = ['AK', 'ME', 'NY']

# Execute tasks
print("1. List of all brewery names:")
brewery_names = list_breweries_names(states_of_interest)
for name in brewery_names:
    print(name)

print("\n2. Count of breweries in each state:")
breweries_count = count_breweries(states_of_interest)
for state, count in breweries_count.items():
    print(f"{state}: {count}")

print("\n3. Count of brewery types in individual cities:")
brewery_types_count = count_brewery_types(states_of_interest)
for city, types in brewery_types_count.items():
    print(f"{city}:")
    for brewery_type, num in types.items():
        print(f"  {brewery_type}: {num}")

print("\n4. Count of breweries with websites in each state:")
breweries_with_websites = count_breweries_with_websites(states_of_interest)
for state, count in breweries_with_websites.items():
    print(f"{state}: {count}")
