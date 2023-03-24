#!/usr/bin/env python
# coding: utf-8

# In[400]:


import pandas as pd
import numpy as np
import scipy.stats as st


# In[401]:


raw_data = pd.read_csv(r"C:\Users\Adam\Desktop\2023 - FIRST CAD\Scouting - WI2023\Copy of WarriorWATCH2023_Pro_Wisconsin_528 - MatchData (1).csv")


# In[402]:


raw_data[raw_data["Team Number"] == 93]


# In[403]:


def parse_data(data_set, team_number):
    team_data = data_set[data_set["Team Number"] == team_number]
    
    auto_cubes_total = team_data["Auto Cubes - Top"].sum() + team_data["Auto Cubes - Middle"].sum() + team_data["Auto Cubes - Bottom"].sum()
    auto_cones_total = team_data["Auto Cones - Top"].sum() + team_data["Auto Cones - Middle"].sum() + team_data["Auto Cones - Bottom"].sum()
    
    average_auto_cubes = (auto_cubes_total) / team_data.shape[0]
    average_auto_cones = (auto_cones_total) / team_data.shape[0]
    
    stdev_auto_cubes = np.std(auto_cones_total)
    stdev_auto_cones = np.std(auto_cubes_total)
    
    auto_balance_attempts_percentage = 0,
    foo = team_data["Auto Balance"].value_counts().to_dict()

    auto_balance_attempts_percentage = 0
    if('"Attempted & No Balance"' in team_data["Auto Balance"].value_counts().to_dict().keys()):
        auto_balance_attempts_percentage = (team_data["Auto Balance"].value_counts().to_dict()['"Attempted & No Balance"'] / team_data["Auto Balance"].shape[0])*100
    auto_balance_percentage = 0
    if('"Balanced"' in team_data["Auto Balance"].value_counts().to_dict().keys()):
        auto_balance_percentage = (team_data["Auto Balance"].value_counts().to_dict()['"Balanced"'] / team_data["Auto Balance"].shape[0])*100
    
    tele_cubes_total = team_data["Tele Cubes - Top"].sum() + team_data["Tele Cubes - Middle"].sum() + team_data["Tele Cubes - Bottom"].sum()
    tele_cones_total = team_data["Tele Cones - Top"].sum() + team_data["Tele Cones - Middle"].sum() + team_data["Tele Cones - Bottom"].sum()
    
    average_tele_cubes = (tele_cubes_total) / team_data.shape[0]
    average_tele_cones = (tele_cones_total) / team_data.shape[0]
    
    tele_balance_attempts_percentage = 0
    if('"Attempted & No Balance"' in team_data["Tele Balance"].value_counts().to_dict().keys()):
        tele_balance_attempts_percentage = (team_data["Tele Balance"].value_counts().to_dict()['"Attempted & No Balance"'] / team_data["Tele Balance"].shape[0])*100
    tele_balance_percentage = 0
    if('"Balanced"' in team_data["Tele Balance"].value_counts().to_dict().keys()):
        tele_balance_percentage = (team_data["Tele Balance"].value_counts().to_dict()['"Balanced"'] / team_data["Tele Balance"].shape[0])*100


    parsed_data = {
        "team_number": f"{team_number}",
        "total_auto_game_objects": average_auto_cubes + average_auto_cones,
        "average_auto_cubes": average_auto_cubes,
        "average_auto_cones": average_auto_cones,
#         "confidence_interval": st.t.interval(alpha = 0.9, df = len(team_data) - 1, loc = average_auto_cones, scale=stdev_auto_cones)
        "auto_balance_fail_percentage": f"{auto_balance_attempts_percentage}%",
        "auto_balance_success_percentage": f"{auto_balance_percentage}%",
        "total_tele_game_objects": average_tele_cubes + average_tele_cones,
        "average_tele_cubes": average_tele_cubes,
        "average_tele_cones": average_tele_cones,
        "tele_balance_fail_percentage": f"{tele_balance_attempts_percentage}%",
        "tele_balance_success_percentage": f"{tele_balance_percentage}%",
        "number_of_matches": f"{team_data.shape[0]}",
#         "confidence_interval"
    }
    
    return parsed_data    


# In[404]:


parse_data(raw_data, 93)


# In[405]:


team_numbers = raw_data["Team Number"].unique()


# In[406]:


parsed_data = pd.DataFrame()
for i in team_numbers:
    dict_new = parse_data(raw_data, i)
    parsed_data = parsed_data.append(dict_new, ignore_index=True)
parsed_data.set_index('team_number', inplace=True)
print(parsed_data)


# In[408]:


parsed_data.to_csv(r"C:\Users\Adam\Desktop\2023 - FIRST CAD\Scouting - WI2023\WarriorWATCH2023_Pro_Wisconsin - ProcessedMatchData.csv")


# In[ ]:




