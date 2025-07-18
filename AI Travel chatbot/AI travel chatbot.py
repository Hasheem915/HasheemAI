import re, random
from colorama import Fore, init

init(autoreset=True)
destination = {
    "beaches": ["Bali", "Maldives", "Phuket"]
    "mountains": ["Swiss", "Maldives", "Himalayas"]
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!"
    "Why did the computer go to the doctor? Because it had a virus"
    
]


def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def recommand():
    print(Fore.CYAN + "TravelBot:"
    "Beaches, Mountains, or Cities?")
    preference = input(Fore.BLUE + "You: ")
    preference = normalize_input(preference)

    if preference in destination: suggestion = random.choice(destination[preference)
                                                             print(Fore.YELLOW + f"TravelBot: How about {suggestion}?")
                                                             print(Fore.CYAN + f"TravelBot: Dou you like it? (yes/no)")


                                                             answer = input (Fore.GREEN + "You").lower()
                                                             if answer == "yes":
                                                             print(Fore.YELLOW + F"TravelBot: Awesome! Enjoy{suggestion}")
                                                             
 
