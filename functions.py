
get_city_country={}

def city_country(city_name, country_name):
    """Return a city and country """
    full_city = f"{city_name}, {country_name}"
    return full_city.title()

while True:
    print("\n Please tell me the city and country...")
    print("(enter 'q' to quit)")

    ci_name = input("City: ")
    if ci_name.lower() == 'q':
        break

    cou_name = input("Country: ")
    if cou_name.lower() == 'q':
        break
    
    get_city_country[ci_name] = cou_name

print("\nThis are the countries in the dictionary:")

for ci_name, cou_name in get_city_country.items():
    print(f"{ci_name.title()}, {cou_name.title()}")


