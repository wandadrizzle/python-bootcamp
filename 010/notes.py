#Day 009 Continued,

travel_log = {}

travel_log = [
    {
        "country":"France", 
        "cities_visited": ["Paris", "Lille","Dijon"],
        "total_visits": 12
    },
    {  
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg","Stuttgart"],
        "total_visits": 3
    }
]

#Day 010 - Functions with Outputs
'''
pythontutor.com
'''

def format_name(f_name, l_name):
    '''
    Takes first and last name and formats them to return a title case equivalent.
    '''
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()

    return f"{f_name} {l_name}"

print(format_name("wanda", "DRizzLe"))
print("wanda DRiZzle".title())