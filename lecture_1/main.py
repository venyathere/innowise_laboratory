from colorama import init, Fore, Back, Style

init()

print(f"{Fore.RED}{Back.YELLOW}Hello world!{Style.RESET_ALL}")
print(f"{Fore.GREEN}Hello world in green {Style.RESET_ALL}")
print(f"{Fore.BLUE}{Style.BRIGHT}Hello world in bright blue {Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{Back.CYAN}Hello world with manageenta with cyan background!{Style.RESET_ALL}")
