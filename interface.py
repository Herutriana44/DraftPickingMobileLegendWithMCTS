import json
import pandas as pd
import random as rd
from operator import itemgetter

def sort_dictionary_by_value(input_dict, reverse=False):
    sorted_dict = dict(sorted(input_dict.items(), key=itemgetter(1), reverse=reverse))
    return sorted_dict

def flatten_list_recursive(input_list):
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(flatten_list_recursive(item))
        else:
            result.append(item)
    return result

def minmaxselect(num, min, max):
    if num < min:
        return min
    if num > max:
        return max
    return num

def hero_power_func(team, player, hero):
    df = pd.read_excel('DraftPickHeroML.xlsx')
    df = df[(df['Tim'] == team) & (df['Player'] == player)]
    try:
        hero_power = df[hero][0]

        return hero_power
    except:
        return 0

def all_hero_pool_in_team(team):
    df = pd.read_excel('DraftPickHeroML.xlsx')
    df = df[df['Tim'] == team]
    players = df['Player'].tolist()
    all_hero_pool = json.load(open('hero pool.json'))
    hero_pool_team = []
    for player in players:
        hero_pool_team.append(all_hero_pool[player])
    hero_pool_team = flatten_list_recursive(hero_pool_team)
    hero_pool_team = list(set(hero_pool_team))

    return hero_pool_team
    

def hero_pool_with_power(team, player, banned):
    # df = pd.read_excel('DraftPickHeroML.xlsx')
    # df = df[df['Tim'] == team and df['Player'] == player]
    all_hero_pool = json.load(open('hero pool.json'))
    hero_pool = all_hero_pool[player]
    hero_pool = [hero for hero in hero_pool if hero not in banned]
    hero_pool_power = [hero_power_func(team, player, hero) for hero in hero_pool]
    hero_pool_res = {}
    for i in range(len(hero_pool)):
        hero_pool_res[hero_pool[i]] = hero_pool_power[i]

    hero_pool_res = sort_dictionary_by_value(hero_pool_res, reverse=True)
    # hero_select = next(iter(hero_pool_res))
    return hero_pool_res#, hero_select

def select_hero_by_highest_power(hero_pool):
    hero_select = next(iter(hero_pool))
    return hero_select, hero_pool[hero_select]

def banned_foe_hero_team(foe_team):
    foe_hero_pool_team = all_hero_pool_in_team(foe_team)
    return rd.choice(foe_hero_pool_team)


# hero_pool_ex = hero_pool_with_power("Alter Ego", "Pai", ["Uranus", "Terizla"])
# print(hero_pool_ex)
# print(select_hero_by_highest_power(hero_pool_ex))
# print(all_hero_pool_in_team("Alter Ego"))
print(banned_foe_hero_team('Alter Ego'))

# ban_team_1 = []
# ban_team_2 = []

# garis = "="*30
# def header():
#     print(garis)
#     print("List Tim Mobile Legends")
#     print(garis)
#     dataDraft = json.load(open('draft.json')) # load file draft.json
#     # print list tim
#     for ind, tim in enumerate(dataDraft['Tim']):
#         print(f"{ind}). {tim}")

#     selectedTeam1 = minmaxselect(int(input("Masukkan Tim 1 sesuai Angka yang ada : ")), 0, len(dataDraft['Tim']) - 1)
#     selectedTeam1 = dataDraft['Tim'][selectedTeam1]
#     selectedTeam2 = minmaxselect(int(input("Masukkan Tim 2 sesuai Angka yang ada : ")), 0, len(dataDraft['Tim']) - 1)
#     selectedTeam2 = dataDraft['Tim'][selectedTeam2]
#     hero_pool = pd.read_excel("Hero Pool.xlsx")
#     hero_pool = hero_pool[hero_pool['Tim'] == selectedTeam1]
#     all_player = list(hero_pool['Player'].tolist())
#     all_hero_pool = json.load(open('hero pool.json')) # load file draft.json

#     print(f"Semua Hero Pool Player dari Tim {selectedTeam1}")
#     all_selected_hero1 = []
#     for player in all_player:
#         print(f"{player} : {all_hero_pool[player]}")
#     #     try:
#     #         all_selected_hero1.append(rd.choice(all_hero_pool[player]))
#     #     except:
#     #         all_selected_hero1.append(0)

#     # print(f"Semua Hero Player Yang Dipilih secara acak dari Tim {selectedTeam1}")
#     # for i, player in enumerate(all_player):
#     #     print(f"{player} : {all_selected_hero1[i]}")

#     hero_power = pd.read_excel('DraftPickHeroML.xlsx')
#     hero_power = hero_power[hero_power['Tim'] == selectedTeam1]

#     all_hero_power_selected1 = []
#     for j, player in enumerate(all_player):
#         try:
#             hero_power_selected = [hero_power[i] for i in all_selected_hero1]
#             all_hero_power_selected1.append(hero_power_selected)
#         except:
#             all_hero_power_selected1.append(0)

#     print(all_hero_power_selected1)

#     print(f"Semua Hero Pool Player dari Tim {selectedTeam2}")
#     all_selected_hero2 = []
#     for player in all_player:
#         print(f"{player} : {all_hero_pool[player]}")
#     #     try:
#     #         all_selected_hero2.append(rd.choice(all_hero_pool[player]))
#     #     except:
#     #         all_selected_hero2.append(0)

#     # print(f"Semua Hero Player Yang Dipilih secara acak dari Tim {selectedTeam2}")
#     # for i, player in enumerate(all_player):
#     #     print(f"{player} : {all_selected_hero2[i]}")

#     hero_power = pd.read_excel('DraftPickHeroML.xlsx')
#     hero_power = hero_power[hero_power['Tim'] == selectedTeam2]

#     all_hero_power_selected2 = []
#     for j, player in enumerate(all_player):
#         try:
#             hero_power_selected = [hero_power[i] for i in all_selected_hero2]
#             all_hero_power_selected2.append(hero_power_selected)
#         except:
#             all_hero_power_selected2.append(0)

#     print(all_hero_power_selected1)
    

    
# header()