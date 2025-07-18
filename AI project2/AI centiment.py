import colorama
from colorama import Fore, Style
from textblob import Textblob

#Intialialze colorama for coloured output
colourama.Init()

#Emojis for the start of the coloured output
print(f"{Fore.CYAN} Welcome to Sentiment Spy! {Style.RESET_ALL}")

user_name = input(f"{For.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"


conversation_history = []

print(f"\n{Fare.CYAN})Hello, Agent {user_name}!")
print(f"Type amesssage and I will analyze your sentence with Textblob and show you the sentiment")
print(f"Type{Fore.YELLOW}'rest'{Fore.CYAN}, {Fore.YELLOW}'history' {Fore.CYAN}"
      f"or{Fore.YELLOW}'exit'{Fore.CYAN} to quit,{Style.RESET_ALL}")

while True:
     user_input=input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    
     if not user_input:
          print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
          continue
     
         #Check for commands
          if user_input.lower() = "exit":
           print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewall, Agent {user_name}! {Style.RESET_ALL}")
           break
     
          elif user_name.lower() = "reset":
              conversation_history.clear()
              print(f"\n{Fore.CYAN} All conversation history cleared!{Style.RESET_ALL}")
              continue
          elif user_input.lower() = "history":
              if not conversation_history:
                  print(f"{Fore.YELLOW} No conversation history yet.{Style.RESET_ALL}")
              else:
                  print(f"{Fore.CYAN} ")
          

     
    


