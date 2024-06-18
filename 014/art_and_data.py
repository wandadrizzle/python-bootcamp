logo = r'''
                                                                                                                         
88          88             88                                   88                                                       
88          ""             88                                   88                                                       
88                         88                                   88                                                       
88,dPPYba,  88  ,adPPYb,d8 88,dPPYba,   ,adPPYba, 8b,dPPYba,    88  ,adPPYba,  8b      db      d8  ,adPPYba, 8b,dPPYba,  
88P'    "8a 88 a8"    `Y88 88P'    "8a a8P_____88 88P'   "Y8    88 a8"     "8a `8b    d88b    d8' a8P_____88 88P'   "Y8  
88       88 88 8b       88 88       88 8PP""""""" 88            88 8b       d8  `8b  d8'`8b  d8'  8PP""""""" 88          
88       88 88 "8a,   ,d88 88       88 "8b,   ,aa 88            88 "8a,   ,a8"   `8bd8'  `8bd8'   "8b,   ,aa 88          
88       88 88  `"YbbdP"Y8 88       88  `"Ybbd8"' 88            88  `"YbbdP"'      YP      YP      `"Ybbd8"' 88          
                aa,    ,88                                                                                               
                 "Y8bbdP"                                                                                                
'''

vs = '''
 +-+ +-+  
 |V| |S|  
 +-+ +-+
'''

instagram = '''

⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⢹⣿⣆
⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠛⠻⢿⣿⣿⣷⣶⣾⣿⣿
⣿⣿⣿⣿⣿⡿⠋⠀⠀⣀⣠⣄⣀⠀⠀⠙⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠁⠀⢠⣾⣿⣿⣿⣿⣷⡄⠀⠈⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⢾⣿⣿⣿⣿⣿⣿⡷⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡀⠀⠘⢿⣿⣿⣿⣿⡿⠃⠀⢀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣄⠀⠀⠉⠙⠋⠉⠀⠀⣠⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀
'''

#These are called ANSI colors or something
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

#This dictionary was created using wikipedia, on the 18th of June 2024, https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts
accounts = [
    #Note: the counts are in millions
    {"name":"Instagram", "handle":"@instagram","description": "Social media platform","follower_count": 673, "country":"United States 🇺🇸"},
    {"name":"Cristiano Ronaldo","handle":"@cristiano","description": "Footballer","follower_count": 632, "country":"Portugal 🇵🇹"},
    {"name":"Lionel Messi", "handle":"@leomessi","description": "Footballer","follower_count": 503, "country":"Argentina 🇦🇷"},
    {"name":"Selena Gomez", "handle":"@selenagomez","description": "Musician and actress","follower_count": 427, "country":"United States 🇺🇸"},  
    {"name":"Kylie Jenner", "handle":"@kyliejenner","description": "Media personality","follower_count": 399, "country":"United States 🇺🇸"},
    {"name":"Dwayne Johnson", "handle":"@therock","description": "Actor and professional wrestler","follower_count": 396, "country":"United States 🇺🇸"},
    {"name":"Ariana Grande", "handle":"@arianagrande","description": "Musician and actress","follower_count": 378, "country":"United States 🇺🇸"},
    {"name":"Kim Kardashian", "handle":"@kimkardashian","description": "Media personality","follower_count": 362, "country":"United States 🇺🇸"},
    {"name":"Beyoncé", "handle":"@beyonce","description": "Musician and actress","follower_count": 318, "country":"United States 🇺🇸"},
    {"name":"Khloé Kardashian", "handle":"@khloekardashian","description": "Media personality","follower_count": 308, "country":"United States 🇺🇸"},

    {"name":"Nike", "handle":"@nike","description": "Sportswear multinational","follower_count": 306, "country":"United States 🇺🇸"},
    {"name":"Justin Beiber", "handle":"@justinbieber","description": "Musician","follower_count": 293.5, "country":"Canada"},
    {"name":"Kendall Jenner", "handle":"@kendalljenner","description": "Media personality","follower_count": 293.1, "country":"United States 🇺🇸"},
    {"name":"Taylor Swift", "handle":"@taylorswift","description": "Musician","follower_count": 283.76, "country":"United States 🇺🇸"},
    {"name":"National Geographic", "handle":"@natgeo","description": "Magazine","follower_count": 283.03, "country":"United States 🇺🇸"},
    {"name":"Virat Kohli", "handle":"@virat.kohli","description": "Cricketer","follower_count": 269, "country":"India"},
    {"name":"Jennifer Lopez", "handle":"@jlo","description": "Musician and actress","follower_count": 252, "country":"United States 🇺🇸"},
    {"name":"Nicki Minaj", "handle":"@nickiminaj","description": "Musician","follower_count": 229, "country":"United States 🇺🇸 & Trinidad and Tobago"},
    {"name":"Kourtney Kardashian", "handle":"@kourtneykardash","description": "Media personality","follower_count": 223, "country":"United States 🇺🇸"},
    {"name":"Neymar", "handle":"@neymarjr","description": "Footballer","follower_count": 222, "country":"Brazil"},


    {"name":"Miley Cyrus", "handle":"@mileycyrus","description": "Musician and actress","follower_count": 216, "country":"United States"},
    {"name":"Katy Perry", "handle":"@katyperry","description": "Musician","follower_count": 206, "country":"United States"},
    {"name":"Zendaya", "handle":"@zendaya","description": "Actress and singer","follower_count": 183, "country":"United States"},
    {"name":"Kevin Hart", "handle":"@kevinhart4real","description": "Comedian and actor","follower_count": 179, "country":"United States"},
    {"name":"Cardi B", "handle":"@iamcardib","description": "Musician and actress","follower_count": 167, "country":"United States"},
    {"name":"Real Madrid FC", "handle":"@realmadrid","description": "Football club","follower_count": 162, "country":"Spain"},
    {"name":"LeBron James", "handle":"@kingjames","description": "Basketball player","follower_count": 159, "country":"United States"},
    {"name":"Demi Lovato", "handle":"@ddlovato","description": "Musician and actress","follower_count": 156, "country":"United States"},
    {"name":"Rihanna", "handle":"@badgalriri","description": "Musician","follower_count": 151, "country":"Barbados"},
    {"name":"Drake", "handle":"@champagnepapi","description": "Musician","follower_count": 146, "country":"Canada & United States"},

    {"name":"Chris Brown", "handle":"@chrisbrownofficial","description": "Musician","follower_count": 145, "country":"United States"},
    {"name":"Ellen DeGeneres", "handle":"@ellendegeneres","description": "Comedian and television host","follower_count": 138, "country":"United States"},
    {"name":"FC Barcelona", "handle":"@fcbarcelona","description": "Football club","follower_count": 127, "country":"Spain"},
    {"name":"Billie Eilish", "handle":"@billieeilish","description": "Musician","follower_count": 119, "country":"United States"},
    {"name":"Kylian Mbappé", "handle":"@k.mbappe","description": "Footballer","follower_count": 118, "country":"France"},
    {"name":"EUFA Champions League", "handle":"@championsleague","description": "Club football competition","follower_count": 115, "country":"Europe"},
    {"name":"Gal Gadot", "handle":"@gal_gadot","description": "Actress","follower_count": 108, "country":"Israel"},
    {"name":"Lisa", "handle":"@lalalalisa_m","description": "Musician","follower_count": 103, "country":"Thailand"},
    {"name":"Vin Diesel", "handle":"@vindiesel","description": "Actor","follower_count": 102, "country":"United States"},
    {"name":"NASA", "handle":"@nasa","description": "Space agency","follower_count": 97.9, "country":"United States"},

    {"name":"Priyanka Chopra", "handle":"@priyankachopra","description": "Actress","follower_count": 91.3, "country":"India 🇮🇳"},
    {"name":"Narendra Modi", "handle":"@narendramodi","description": "Prime Minister of India","follower_count": 90.7, "country":"India 🇮🇳"},
    {"name":"Shakira", "handle":"shakira","description": "Musician","follower_count": 90.5, "country":"Columbia"},
    {"name":"Shraddha Kapoor", "handle":"@shraddhakapoor","description": "Actress","follower_count": 89.9, "country":"India 🇮🇳"},
    {"name":"NBA", "handle":"@nba","description": "Professional basketball league","follower_count": 88.2, "country":"United States & Canada"},
    {"name":"Dua Lipa", "handle":"@dualipa","description": "Musician","follower_count": 88.1, "country":"United Kingdom & Albania 🇦🇱"},
    {"name":"David Beckham", "handle":"@davidbeckham","description": "Former footballer","follower_count": 88, "country":"United Kingdom 🇬🇧"},
    {"name":"Snoop Dogg", "handle":"@snoopdogg","description": "Musician","follower_count": 87.5, "country":"United States"},
    {"name":"Jennie", "handle":"@jennierubyjane","description": "Musician","follower_count": 84.8, "country":"South Korea 🇰🇷"},
    {"name":"Alia Bhatt", "handle":"@aliaabhatt","description": "Actress","follower_count": 84.7, "country":"United Kingdom 🇬🇧 & India"},
]