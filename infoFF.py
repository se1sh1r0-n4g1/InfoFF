# Creado por: n4g1

#Descripción:
#        Sencillo script en python para obtener información
#        sobre una cuenta de Free Fire, el clan en el que esta unido del jugador e info del lider de su clan

import requests,argparse
from colorama import Fore, Style, Back

url = "https://free-ff-api-src-5plp.onrender.com/api/v1/"

parser = argparse.ArgumentParser(description='Este script te muestra información sobre tu cuenta de Free Fire')

parser.add_argument('-r', '--region_cuenta', type=str, required=True, help='Region de la cuenta (US,IND,BR...)')
parser.add_argument('-id', '--id_cuenta', type=int, required=True, help='ID de tu cuenta')

args = parser.parse_args()
id = args.id_cuenta
region = args.region_cuenta

def get_info(region, id):
    info = requests.get(f'https://free-ff-api-src-5plp.onrender.com/api/v1/account?region={region}&uid={id}')
    
    info_json = info.json()
    
    # Principal info
    basic_info = info_json['basicInfo']
    
    
    account_id = basic_info['accountId']
    name = basic_info['nickname']
    level = basic_info['level']
    br_points = basic_info['rankingPoints']
    likes = basic_info['liked']
    description = info_json['socialInfo']['signature']
    
    # Informacion del clan
    
    clan_info = info_json['clanBasicInfo']
    
    clan_id = clan_info['clanId']
    clan_name = clan_info['clanName']
    clan_level = clan_info['clanLevel']
    clan_members = clan_info['memberNum']
    
    # Informacion del lidel del clan
    
    captain_clan_info = info_json['captainBasicInfo']
    
    captain_clan_id = captain_clan_info['accountId']
    captain_clan_name = captain_clan_info['nickname']
    captain_clan_level = captain_clan_info['level']
    captain_clan_br_points = captain_clan_info['rankingPoints']
    captain_clan_likes = captain_clan_info['liked']
    
    # Mostrar información
    
    print(Fore.RED + Style.BRIGHT + """
  ___        __       _____ _____ 
 |_ _|_ __  / _| ___ |  ___|  ___|
  | || '_ \| |_ / _ \| |_  | |_   
  | || | | |  _| (_) |  _| |  _|  
 |___|_| |_|_|  \___/|_|   |_|    
""")
    print(Style.RESET_ALL)
    
    print('Creado por: ' + Fore.RED + Style.BRIGHT + 'n4g1')
    print(Style.RESET_ALL)
    
    print(f'{Fore.CYAN}[+] {Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT} Información principal ')
    print(Style.RESET_ALL)
    
    print(f'{Fore.GREEN}Id: {Fore.BLUE}{Style.BRIGHT}{account_id}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Nombre: {Fore.BLUE}{Style.BRIGHT}{name}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Nivel: {Fore.BLUE}{Style.BRIGHT}{level}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Puntos en BR: {Fore.BLUE}{Style.BRIGHT}{br_points}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Likes: {Fore.BLUE}{Style.BRIGHT}{likes}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Descripción: {Fore.BLUE}{Style.BRIGHT}{description}')
    print(Style.RESET_ALL)
    
    print(f'{Fore.CYAN}[+] {Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT} Información del clan ')
    print(Style.RESET_ALL)
    
    print(f'{Fore.GREEN}Id: {Fore.BLUE}{Style.BRIGHT}{clan_id}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Nombre: {Fore.BLUE}{Style.BRIGHT}{clan_name}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Nivel: {Fore.BLUE}{Style.BRIGHT}{clan_level}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Miembros actuales: {Fore.BLUE}{Style.BRIGHT}{clan_members}')
    print(Style.RESET_ALL)
    
    print(f'{Fore.CYAN}[+] {Back.LIGHTWHITE_EX}{Fore.BLACK}{Style.BRIGHT} Información del lidel del clan ')
    print(Style.RESET_ALL)
    
    print(f'{Fore.GREEN}Id: {Fore.BLUE}{Style.BRIGHT}{captain_clan_id}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Nombre: {Fore.BLUE}{Style.BRIGHT}{captain_clan_name}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Puntos en BR: {Fore.BLUE}{Style.BRIGHT}{captain_clan_br_points}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Nivel: {Fore.BLUE}{Style.BRIGHT}{captain_clan_level}')
    print(Style.RESET_ALL)
    print(f'{Fore.GREEN}Likes: {Fore.BLUE}{Style.BRIGHT}{captain_clan_likes}')
    print(Style.RESET_ALL)
    

get_info(region, id)