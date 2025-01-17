#%%
import pandas as pd 
print(" play by play dataset file.")
path=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\play_by_play.csv"
data=pd.read_csv(path)
#%%

data.head()
data.isnull().sum()
# %%
data.describe()
# %%
print(len(data))
import pandas as pd
#%%
columns_to_drop = [
    "player3_name",
    "player3_team_id",
    "player3_team_city",
    "player3_team_nickname",
    "player3_team_abbreviation",
    "homedescription",
    "visitordescription",
    "score",
    "scoremargin",
    "neutraldescription",
    "player2_name",
    "player2_team_id",
    "player2_team_city",
    "player2_team_nickname",
    "player2_team_abbreviation"
]
data_player1 = data.drop(columns=columns_to_drop)
print(len(data_player1))
col_list = data_player1.columns.tolist()
print(col_list)
#%%
data_player1 = data_player1.dropna()
data_player1.isnull().sum()
print(len(data_player1))
#%%
print(" common player info ")
# %%
path_common_payer_info=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\common_player_info.csv"
data_common_payer_info= pd.read_csv(path_common_payer_info)
data_common_payer_info.isnull().sum()

print(len(data_common_payer_info))
print(data_common_payer_info.isnull().sum())
#%%
columns_to_drop = [
    "team_name",
    "team_abbreviation",
    "team_code",
    "team_city",
    "jersey"]

data_common_payer_info=data_common_payer_info.drop(columns=columns_to_drop)
data_common_payer_info=data_common_payer_info.dropna()
print(data_common_payer_info.isnull().sum())
print(len(data_common_payer_info))
#%%
print("combine stats ")
#%%
path_combine_stat=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\draft_combine_stats.csv"
data_path_combine_stat=pd.read_csv(path_combine_stat)
data_path_combine_stat.isnull().sum()
print(len(data_path_combine_stat))
# %%
columns_to_drop = [
    "hand_length",
    "hand_width",
    "modified_lane_agility_time",
    "bench_press",
    "spot_fifteen_corner_left",
    "spot_fifteen_break_left",
    "spot_fifteen_top_key",
    "spot_fifteen_break_right",
    "spot_fifteen_corner_right",
    "spot_college_corner_left",
    "spot_college_break_left",
    "spot_college_top_key",
    "spot_college_break_right",
    "spot_college_corner_right",
    "spot_nba_corner_left",
    "spot_nba_break_left",
    "spot_nba_top_key",
    "spot_nba_break_right",
    "spot_nba_corner_right",
    "off_drib_fifteen_break_left",
    "off_drib_fifteen_top_key",
    "off_drib_fifteen_break_right",
    "off_drib_college_break_left",
    "off_drib_college_top_key",
    "off_drib_college_break_right",
    "on_move_fifteen",
    "on_move_college"
]

data_path_combine_stat = data_path_combine_stat.drop(columns=columns_to_drop)

print(data_path_combine_stat.isnull().sum())
print(len(data_path_combine_stat))
data_path_combine_stat=data_path_combine_stat.dropna()
print(len(data_path_combine_stat))

# %%
print(" draft history ")
draft_history=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\draft_history.csv"
data_draft_history=pd.read_csv(draft_history)
data_draft_history.isnull().sum()
print(len(data_draft_history))
data_draft_history=data_draft_history.dropna()
print(len(data_draft_history))

#%%
print(" game ")
game=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\game.csv"
data_game=pd.read_csv(game)
data_game.isnull().sum()
len(data_game)
data_game=data_game.dropna()
len(data_game)
#%%
print(' game info ')
game_info=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\game_info.csv"
data_game_info1=pd.read_csv(game_info)
len(data_game_info1)
#%%
data_game_info1.isnull().sum()
len(data_game_info1)
#%%
columns_to_drop = ["game_time"]
data_game_info1=data_game_info1.drop(columns=columns_to_drop)
#%%
data_game_info1=data_game_info1.dropna()
len(data_game_info1)
print(data_game_info1.isnull().sum())
#%%
print(' game summary')
game_summary=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\game_summary.csv"
data_game_summary=pd.read_csv(game_summary)
len(data_game_summary)
#%%
data_game_summary.isnull().sum()
len(data_game_summary)
#%%
columns_to_drop = [
    "game_sequence",
    "game_status_text",
    "live_pc_time",
    "natl_tv_broadcaster_abbreviation"
]
data_game_summary=data_game_summary.drop(columns=columns_to_drop)
#%%
data_game_summary=data_game_summary.dropna()
len(data_game_summary)
print(data_game_summary.isnull().sum())

#%%
print(" inactive player dataset")
inactive=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\inactive_players.csv"
data_inactive_player=pd.read_csv(inactive)
len(data_inactive_player)
#%%
data_inactive_player.isnull().sum()
len(data_inactive_player)
#%%
data_inactive_player=data_inactive_player.dropna()
len(data_inactive_player)
print(data_inactive_player.isnull().sum())

#%%
print("line score ")
line_score=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\line_score.csv"
data_line_score=pd.read_csv(line_score)
len(data_line_score)
#%%
data_line_score.isnull().sum()
columns_to_drop = [
    "pts_ot1_away", "pts_ot2_away", "pts_ot3_away", "pts_ot4_away", "pts_ot5_away",
    "pts_ot6_away", "pts_ot7_away", "pts_ot8_away", "pts_ot9_away", "pts_ot10_away",
    "pts_ot1_home", "pts_ot2_home", "pts_ot3_home", "pts_ot4_home", "pts_ot5_home",
    "pts_ot6_home", "pts_ot7_home", "pts_ot8_home", "pts_ot9_home", "pts_ot10_home",
    "game_sequence"
]
data_line_score = data_line_score.drop(columns=columns_to_drop)
print(data_line_score.info())

len(data_line_score)
#%%
data_line_score=data_line_score.dropna()
len(data_line_score)
print(data_line_score.isnull().sum())
len(data_line_score)
#%%
print("officials ")
officials=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\officials.csv"
data_officials=pd.read_csv(officials)
len(data_officials)
#%%
data_officials.isnull().sum()

len(data_officials)
#%%
data_officials=data_officials.dropna()
len(data_officials)
print(data_officials.isnull().sum())

#%%
print("others stats ")
other_stats=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\other_stats.csv"
data_other_stat=pd.read_csv(other_stats)
len(data_other_stat)
#%%
data_other_stat.isnull().sum()

len(data_other_stat)
#%%
data_other_stat=data_other_stat.dropna()
len(data_other_stat)
print(data_other_stat.isnull().sum())

#%%
print("player dataset ")
player_data=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\player.csv"

data_player_data=pd.read_csv(player_data)
len(data_player_data) 
#%%
data_player_data.isnull().sum()

len(data_player_data)
#%%
data_player_data=data_player_data.dropna()
len(data_player_data)
print(data_player_data.isnull().sum())

#%%
print("team dataset")
team_dataset=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\team.csv"

data_team=pd.read_csv(team_dataset)
len(data_team) 
#%%
data_team.isnull().sum()

len(data_team)
#%%
data_team=data_team.dropna()
len(data_team)
print(data_team.isnull().sum())


#%%
print("team details")
team_details=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\team_details.csv"

data_team_details=pd.read_csv(team_details)
len(data_team_details) 
#%%
data_team_details.isnull().sum()

columns_to_drop=["arenacapacity"]
data_team_details=data_team_details.drop(columns=columns_to_drop)


len(data_team_details)
#%%
data_team_details=data_team_details.dropna()
len(data_team_details)
print(data_team_details.isnull().sum())

#%%
print("TEAM HISTORY")
team_history=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\team_history.csv"

data_team_history=pd.read_csv(team_history)
len(data_team_history)
#%%
data_team_history.isnull().sum()
len(data_team_history)
#%%

print("team common  info ")
team_info=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\team_info_common.csv"

data_team_info=pd.read_csv(team_info)
len(data_team_info)
####### we are not gonna use team info due to zero rows- length of dataset.#########
#%% 
######### now lets check common rows between all the dataset to combine as a one dataset#########
import pandas as pd


############################################################ above one  ##################

#%%

print("Player1 dataset columns:")
print(data_player1.columns)

print("Common player info columns:")
print(data_common_payer_info.columns)

print("Combine stats columns:")
print(data_path_combine_stat.columns)

print("Draft history columns:")
print(data_draft_history.columns)

print("Game dataset columns:")
print(data_game.columns)

print("Game info dataset columns:")
print(data_game_info1.columns)

print("Game summary dataset columns:")
print(data_game_summary.columns)

print("Inactive players dataset columns:")
print(data_inactive_player.columns)

print("Line score dataset columns:")
print(data_line_score.columns)

print("Officials dataset columns:")
print(data_officials.columns)

print("Other stats dataset columns:")
print(data_other_stat.columns)

print("Player dataset columns:")
print(data_player_data.columns)

print("Team dataset columns:")
print(data_team.columns)

print("Team details dataset columns:")
print(data_team_details.columns)

print("Team history dataset columns:")
print(data_team_history.columns)
############## combine the dataset - #################################
#%%

#%%
datasets = {
    "Player1": data_player1,
    "Common Player Info": data_common_payer_info,
    "Combine Stats": data_path_combine_stat,
    "Draft History": data_draft_history,
    "Game": data_game,
    "Game Info": data_game_info1,
    "Game Summary": data_game_summary,
    "Inactive Players": data_inactive_player,
    "Line Score": data_line_score,
    "Officials": data_officials,
    "Other Stats": data_other_stat,
    "Player": data_player_data,
    "Team": data_team,
    "Team Details": data_team_details,
    "Team History": data_team_history
}

for name, df in datasets.items():
    print(f"{name}: Rows = {len(df)}, Columns = {df.shape[1]}")

#%%
################# team ,team details team history ############# 
print(" combine dataset of team, team istory and team details  ")
data_team_combined = pd.merge(data_team, data_team_details, left_on='id', right_on='team_id', how='left')

data_team_combined = pd.merge(data_team_combined, data_team_history, left_on='id', right_on='team_id', how='left')

print(f"Combined Dataset Shape: {data_team_combined.shape}")
print(data_team_combined.head())

print(data_team_combined.columns)
unique_team_cities = data_team_combined['city'].unique()
print(unique_team_cities)

num_unique_team_cities = data_team_combined['city'].nunique()
print(f"Number of unique team cities: {num_unique_team_cities}")

num_unique_other_stat=data_other_stat['team_city_home'].nunique()
print(f" no of unique team:{num_unique_other_stat }")

########### now , take a left join from data_team_combine and merge it with data_other_stats

#%%
data_team_combined.isnull().sum()
merged_data = data_other_stat.merge(
    data_team_combined,
    left_on='team_city_home',  
    right_on='city',          
    how='inner'               
)

print(merged_data.head())

merged_data.isnull().sum()
merged_data.columns
len(merged_data)

##### team , team details , team histroy and other stats is in one data frame - merge_data############


data_line_score
data_officials
len(data_officials )
len(data_line_score)

merged_data_line_officials = data_line_score.merge(
    data_officials,
    on='game_id',  
    how='inner'     
)

print(merged_data_line_officials.head())
len(merged_data_line_officials)
########## now we have two dataset 
###### merged_data -  team , team details , team histroy and other stats  
####### and merge_data_line_officials - include data_line score and data offocials 
merged_data_line_officials.columns
len(data_inactive_player)

len(data_player_data)


#%%
merged_data_player = data_inactive_player.merge(
    data_player_data,
    left_on='player_id', 
    right_on='id',       
    how='inner'          
)
len(merged_data_player)

unique_is_active_values = merged_data_player["is_active"].unique()
print(unique_is_active_values)


merged_data_player.isnull().sum()

########## now we have three dataset 
########## now we have 3 dataset 
###### merged_data -  team , team details , team histroy and other stats  
####### and merge_data_line_officials - include data_line score and data offocials 
### now merged_data_player - data_player_data and data_inactive_player 


# %%

len(data_game)
data_game.columns
data_game_info1.columns
data_game_info1.head()

len(data_game_info1)
len(data_game)
len(data_game_summary)

merge_temp = data_game_info1.merge(
    data_game,
    on='game_id',   
    how='inner'     
)

merge_game = merge_temp.merge(
    data_game_summary,
    on='game_id',  
    how='inner'     
)

print(merge_game.head())

len(merge_game)
merge_game.isnull().sum()
merge_game.columns
#%%
########## now we have 4 dataset 
###### merged_data -  team , team details , team histroy and other stats  
####### and merge_data_line_officials - include data_line score and data offocials 
### now merged_data_player - data_player_data and data_inactive_player 
#### merge game - data_game_summery , data_game_info and data_game 
#####
#%%
data_draft_history.columns
data_path_combine_stat.columns
len(data_path_combine_stat)
len(data_draft_history)

merged_draft_history_stat = data_draft_history.merge(
    data_path_combine_stat,
    on='player_name',   
    how='inner'        
)

print(merged_draft_history_stat.head())

########## now we have 5 dataset 
###### merged_data -  team , team details , team histroy and other stats  
####### and merge_data_line_officials - include data_line score and data offocials 
### now merged_data_player - data_player_data and data_inactive_player 
#### merge game - data_game_summery , data_game_info and data_game 
#### merge_draft_history_stat- draft history and draft combine stat. 

data_common_payer_info
data_player1
merged_data
merged_data_line_officials
merged_data_player
merge_game
merged_draft_history_stat

#%%
''' 
import os
save_path = r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset"

os.makedirs(save_path, exist_ok=True)

datasets = {
    "data_common_payer_info": data_common_payer_info,
    "data_player1": data_player1,
    "merged_data": merged_data,
    "merged_data_line_officials": merged_data_line_officials,
    "merged_data_player": merged_data_player,
    "merge_game": merge_game,
    "merged_draft_history_stat": merged_draft_history_stat
}

for name, df in datasets.items():
    file_path = os.path.join(save_path, f"{name}.csv")
    df.to_csv(file_path, index=False)

print(f"All datasets have been saved successfully to {save_path}")

'''
# %%

#%%
path1=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\data_common_payer_info.csv"

player_info=pd.read_csv(path1)

player_info.isnull().sum()
#%%
path2=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\data_player1.csv"

play_by_play=pd.read_csv(path2)
play_by_play.isnull().sum()
#%%
path3=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\merge_game.csv"

game=pd.read_csv(path3)
game.isnull().sum()
#%%

path4=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\merged_data.csv"
team=pd.read_csv(path4)
team.isnull().sum()
#%%

path5=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\merged_data_line_officials.csv"
game_score=pd.read_csv(path5)
game_score.isnull().sum()

#%%
path6=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\merged_data_player.csv"
player= pd.read_csv(path6)
player.isnull().sum()
#%%

path7=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\merged_draft_history_stat.csv"
stat_history=pd.read_csv(path6)

stat_history.isnull().sum()

#### 
''' 
1) player info - player_info
2) play by play data- play_by_play
3) game dataset - game 
4) team dataset - team 
5) game score dataset - game_score 
6) player dataset - player
7) stat history  - stat_history 
'''
########################## EDA  ########################
#%%
################ $ player info $ ############

player_info
print(player_info.shape)
print(player_info.info())
print(player_info.describe())


# %%
# player count by position 
import matplotlib.pyplot as plt

# Calculate position counts and percentages
position_counts = player_info['position'].value_counts()
total_players = position_counts.sum()
percentages = (position_counts / total_players) * 100

plt.figure(figsize=(8, 6))
bars = position_counts.plot(kind='bar', color='skyblue', alpha=0.8)

for i, (count, percentage) in enumerate(zip(position_counts, percentages)):
    plt.text(i, count + 5, f'{count} ({percentage:.1f}%)', ha='center', fontsize=10)

plt.title('Player Positions with Count and Percentage')
plt.xlabel('Position')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
#%%
# Group position by roster status - active vs inacive player 
grouped_positions = player_info.groupby(['position', 'rosterstatus']).size().unstack()

grouped_positions.plot(kind='bar', stacked=False, figsize=(10, 6), color=['skyblue', 'salmon'])
plt.title('Player Positions by Roster Status')
plt.xlabel('Position')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Roster Status')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#%%
# player height distrubution by count 
import matplotlib.pyplot as plt

height_counts = player_info['height'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
height_counts.plot(kind='bar', color='skyblue', alpha=0.7, label='Count', width=0.8)

plt.plot(range(len(height_counts)), height_counts.values, 
         color='red', marker='o', label='Line Overlay')

plt.title('Height Distribution with Line ')
plt.xlabel('Height')
plt.ylabel('Count')
plt.legend()
plt.show()


#%%
# player weight distrubution by weight 

import numpy as np
mean_weight = player_info['weight'].mean()
median_weight = player_info['weight'].median()
plt.figure(figsize=(10, 6))
sns.histplot(player_info['weight'], bins=20, kde=True, color='skyblue', alpha=0.7)

plt.axvline(mean_weight, color='red', linestyle='--', label=f'Mean: {mean_weight:.1f}')
plt.axvline(median_weight, color='green', linestyle='--', label=f'Median: {median_weight:.1f}')

plt.title('Weight Distribution with Mean and Median')
plt.xlabel('Weight (lbs)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
#%%
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [3, 1]})
sns.histplot(player_info['weight'], bins=20, kde=True, color='skyblue', alpha=0.7, ax=ax1)
ax1.set_title('Weight Distribution with Boxplot')
ax1.set_xlabel('Weight (lbs)')
ax1.set_ylabel('Frequency')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

sns.boxplot(x=player_info['weight'], ax=ax2, color='skyblue')
ax2.set_xlabel('Weight (lbs)')
ax2.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
#%%
# no player by country 
# Calculate average count of players
ax = country_counts.head(10).plot(kind='bar', color='skyblue', title='Top 10 Countries by Player Count')

for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 2, f'{i.get_height()}', 
            ha='center', va='bottom', fontsize=10, color='black')

# Customize the plot
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.tight_layout()
plt.show()


#%%
# A drafted player in the National Basketball League (NBL) 
# is a player who has been selected by an NBA team in the
# NBA draft. 
import matplotlib.pyplot as plt

plt.figure(figsize=(18, 28))
draft_year_counts.plot(
    kind='pie', 
    autopct='%1.1f%%', 
    startangle=90, 
    title='Draft Year Distribution', 
    legend=False
)
plt.ylabel('') 
plt.show()

plt.figure(figsize=(18, 8))
draft_round_counts.plot(
    kind='pie', 
    autopct='%1.1f%%', 
    startangle=90, 
    title='Draft Rounds Distribution', 
    legend=False
)
plt.ylabel('')  
plt.show()


print(f"Number of Undrafted Players: {undrafted_count}")

#%%
# player career distrubution  to year 

import matplotlib.pyplot as plt

career_bins = [0, 2, 5, 10, 15, 20, player_info['career_duration'].max()]
labels = ['0-2 years', '3-5 years', '6-10 years', '11-15 years', '16-20 years', '21+']

career_duration_distribution = pd.cut(player_info['career_duration'], bins=career_bins, labels=labels)
career_distribution_counts = career_duration_distribution.value_counts().sort_index()

plt.figure(figsize=(12, 18))
plt.pie(
    career_distribution_counts, 
    labels=labels, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=plt.cm.Paired.colors
)
plt.title('Player Career Duration Distribution')
plt.show()


#%%
# count of player by team - top 10 teams 
import matplotlib.cm as cm
import numpy as np
colors = cm.viridis(np.linspace(0.3, 0.8, len(team_counts.head(10))))
ax = team_counts.head(10).plot(kind='barh', color=colors, title='Top 10 Teams by Player Count')

plt.xlabel('Number of Players')
plt.ylabel('Team')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
#%%
ax = team_counts.head(10).plot(kind='bar', color='skyblue', title='Top 10 Teams by Player Count')

for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() / 2, f'{int(i.get_height())}', 
            ha='center', va='center', fontsize=10, color='white')

plt.xlabel('Team')
plt.ylabel('Number of Players')
plt.tight_layout()
plt.show()

# pie chart distrubution 
team_counts.head(10).plot(kind='pie', autopct='%1.1f%%', title='Top 10 Teams by Player Count', figsize=(8, 8))

plt.ylabel(' ')
plt.show()



#%%
# active and retired player by count 
roster_status_counts = player_info['rosterstatus'].value_counts()
roster_status_counts.plot(kind='pie', autopct='%1.1f%%', title='Active vs. Inactive Players')
plt.show()

#%%
# , a flag is used to indicate a flagrant foul, 
# which is a personal foul that involves excessive 
# or violent contact

games_played_counts = player_info['games_played_flag'].value_counts()
games_played_counts.plot(kind='pie', autopct='%1.1f%%', title='Games Played Flag')
plt.show()

#%%
# count of plyer by coleeges 
avg_count = college_counts.head(10).mean()

ax = college_counts.head(10).plot(kind='bar', color='skyblue', title='Top 10 Colleges by Player Count')

plt.axhline(y=avg_count, color='red', linestyle='--', label=f'Average: {avg_count:.0f}')
plt.legend()

for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 2, f'{int(i.get_height())}', 
            ha='center', va='bottom', fontsize=10, color='black')

plt.xlabel('College')
plt.ylabel('Number of Players')
plt.tight_layout()
plt.show()


#%%
# Pie chart for top 10 colleges by player count
college_counts.head(10).plot(kind='pie', autopct='%1.1f%%', title='Top 10 Colleges by Player Count', figsize=(8, 8))

plt.ylabel('')
plt.show()

#%%
active_players = player_info[player_info['rosterstatus'] == 'Active']
inactive_players = player_info[player_info['rosterstatus'] == 'Inactive']

active_college_counts = active_players['school'].value_counts()
inactive_college_counts = inactive_players['school'].value_counts()

college_status_counts = pd.DataFrame({
    'Active Players': active_college_counts,
    'Inactive Players': inactive_college_counts
}).fillna(0)  # Fill NaN values with 0 for colleges with only one type of player

ax = college_status_counts.head(10).plot(kind='bar', width=0.8, title='Active vs Inactive Players by University', color=['green', 'red'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2, p.get_height() + 0.5),
                ha='center', va='bottom', fontsize=10, color='black')

plt.xlabel('University')
plt.ylabel('Number of Players')
plt.tight_layout()
plt.show()

#%%
# count of active player by university

active_players = player_info[player_info['rosterstatus'] == 'Active']

active_college_counts = active_players['school'].value_counts()

active_college_counts.head(10).plot(kind='bar', color='green', title='Top 10 Universities by Active Player Count')

for i in plt.gca().patches:
    plt.gca().text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, f'{int(i.get_height())}', 
                   ha='center', va='bottom', fontsize=10, color='black')

plt.xlabel('University')
plt.ylabel('Number of Active Players')
plt.tight_layout()
plt.show()

# %%

inactive_players = player_info[player_info['rosterstatus'] == 'Inactive']

Inactive_college_counts = inactive_players['school'].value_counts()

Inactive_college_counts.head(10).plot(kind='bar', color='green', title='Top 10 Universities by Active Player Count')

for i in plt.gca().patches:
    plt.gca().text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, f'{int(i.get_height())}', 
                   ha='center', va='bottom', fontsize=10, color='black')

plt.xlabel('University')
plt.ylabel('Number of Inactive Players')
plt.tight_layout()
plt.show()

#%%

import pandas as pd

def convert_height_to_inches(height):
    try:
        if isinstance(height, str) and '-' in height:
            feet, inches = height.split('-')
            return int(feet) * 12 + int(inches)
        else:
            return float(height)  
    except:
        return None  

player_info['height_in_inches'] = player_info['height'].apply(convert_height_to_inches)

player_info['career_duration'] = player_info['to_year'] - player_info['from_year']

height_correlation = player_info['height_in_inches'].corr(player_info['career_duration'])
weight_correlation = player_info['weight'].corr(player_info['career_duration'])

print(f"Correlation between Height (in inches) and Career Duration: {height_correlation:.2f}")
print(f"Correlation between Weight and Career Duration: {weight_correlation:.2f}")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(player_info['height_in_inches'], player_info['career_duration'], alpha=0.6, color='blue')
plt.title('Height vs Career Duration')
plt.xlabel('Height (in inches)')
plt.ylabel('Career Duration (Years)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(player_info['weight'], player_info['career_duration'], alpha=0.6, color='green')
plt.title('Weight vs Career Duration')
plt.xlabel('Weight (lbs)')
plt.ylabel('Career Duration (Years)')
plt.grid(True)

plt.tight_layout()
plt.show()
#%%
#  height vs position
plt.figure(figsize=(12, 6))
sns.violinplot(x='position', y='height', data=player_info, palette='Set2')
plt.title('Height Distribution by Position')
plt.xlabel('Position')
plt.ylabel('Height (in inches)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#%%
#  weight vs position
plt.figure(figsize=(12, 6))
sns.violinplot(x='position', y='weight', data=player_info, palette='Set2')
plt.title('Weight Distribution by Position')
plt.xlabel('Position')
plt.ylabel('Weight (in pounds)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#%%
active_players = player_info[player_info['rosterstatus'] == 'Active']
plt.figure(figsize=(12, 6))
sns.boxplot(x='position', y='season_exp', data=active_players, palette='Set2')
plt.title('Season Experience Distribution by Position (Active Players)')
plt.xlabel('Position')
plt.ylabel('Season Experience')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# %%
# D-League and NBA participation
# Games played flag count
# greatest_75_flag- Indicates whether the player was
# included in the NBA’s list of the "75 Greatest NBA Players"
# released to commemorate the league's 75th anniversary.


# draft_number - The pick number by which the player was 
# selected in the draft.

# games_played_flag:ndicates whether the player has played games in the NBA 

# dleague_flag:Indicates whether the player has participated in the NBA’s Development League

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 4, figsize=(16, 6))

games_played_counts.plot(kind='bar', color=['skyblue', 'lightcoral'], title="Games Played vs Not Played", ax=ax[0])
ax[0].set_xlabel('Games Played')
ax[0].set_ylabel('Count')
ax[0].tick_params(axis='x', rotation=0)

dleague_counts = player_info['dleague_flag'].value_counts()
dleague_counts.plot(kind='bar', color=['lightgreen', 'orange'], title="D-League Participation", ax=ax[1])
ax[1].set_xlabel('D-League Participation')
ax[1].set_ylabel('Count')
ax[1].tick_params(axis='x', rotation=0)

nba_counts = player_info['nba_flag'].value_counts()
nba_counts.plot(kind='bar', color=['lightblue', 'salmon'], title="NBA Participation", ax=ax[2])
ax[2].set_xlabel('NBA Participation')
ax[2].set_ylabel('Count')
ax[2].tick_params(axis='x', rotation=0)

games_played_nba_counts = player_info.groupby(['games_played_flag', 'nba_flag']).size().unstack()
games_played_nba_counts.plot(kind='bar', stacked=False, title="Games Played vs NBA Participation", ax=ax[3])
ax[3].set_xlabel('Games Played vs NBA Participation')
ax[3].set_ylabel('Count')
ax[3].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%%
import matplotlib.pyplot as plt
import seaborn as sns

# for the greatest 75 players
greatest_75_players = player_info[player_info['greatest_75_flag'] == 'Y']

# 1. Schools of Greatest 75 Players
school_counts = greatest_75_players['school'].value_counts().head(10)

plt.figure(figsize=(12, 6))
school_counts.plot(kind='bar', color='skyblue', title="Top Schools of Greatest 75 Players")
plt.xlabel('School')
plt.ylabel('Number of Players')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Heights of Greatest 75 Players
def convert_height(height):
    try:
        feet, inches = height.split('-')
        return int(feet) * 12 + int(inches)
    except:
        return None

greatest_75_players['height_numeric'] = greatest_75_players['height'].apply(convert_height)

plt.figure(figsize=(10, 6))
sns.histplot(greatest_75_players['height_numeric'], kde=True, bins=10, color='green')
plt.title("Height Distribution of Greatest 75 Players")
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 3. Weights of Greatest 75 Players
plt.figure(figsize=(10, 6))
sns.histplot(greatest_75_players['weight'], kde=True, bins=10, color='purple')
plt.title("Weight Distribution of Greatest 75 Players")
plt.xlabel('Weight (lbs)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Career Duration (Total Years Played)
greatest_75_players['career_duration'] = greatest_75_players['to_year'] - greatest_75_players['from_year']

plt.figure(figsize=(10, 6))
sns.histplot(greatest_75_players['career_duration'], kde=True, bins=10, color='orange')
plt.title("Career Duration of Greatest 75 Players")
plt.xlabel('Career Duration (Years)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 5. Average Career Duration and Other Stats
average_career_duration = greatest_75_players['career_duration'].mean()
average_height = greatest_75_players['height_numeric'].mean()
average_weight = greatest_75_players['weight'].mean()

print(f"Average Career Duration of Greatest 75 Players: {average_career_duration:.2f} years")
print(f"Average Height of Greatest 75 Players: {average_height:.2f} inches")
print(f"Average Weight of Greatest 75 Players: {average_weight:.2f} lbs")

# 6. Comparing Career Duration vs Height (Violin Plot)
plt.figure(figsize=(10, 6))
sns.violinplot(x='height_numeric', y='career_duration', data=greatest_75_players, color='lightblue')
plt.title("Career Duration vs Height of Greatest 75 Players")
plt.xlabel('Height (inches)')
plt.ylabel('Career Duration (Years)')
plt.tight_layout()
plt.show()

# 7. Comparing Career Duration vs Weight (Violin Plot)
plt.figure(figsize=(10, 6))
sns.violinplot(x='weight', y='career_duration', data=greatest_75_players, color='salmon')
plt.title("Career Duration vs Weight of Greatest 75 Players")
plt.xlabel('Weight (lbs)')
plt.ylabel('Career Duration (Years)')
plt.tight_layout()
plt.show()


#%%
# Filter the data for Active and Inactive Players of greast 75 player lsit 
active_players = greatest_75_players[greatest_75_players['rosterstatus'] == 'Active']
inactive_players = greatest_75_players[greatest_75_players['rosterstatus'] == 'Inactive']

active_position_counts = active_players['position'].value_counts()

inactive_position_counts = inactive_players['position'].value_counts()

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

active_position_counts.plot(kind='bar', color='green', ax=ax[0], title="Active Players by Position")
ax[0].set_xlabel('Position')
ax[0].set_ylabel('Number of Players')

inactive_position_counts.plot(kind='bar', color='red', ax=ax[1], title="Inactive Players by Position")
ax[1].set_xlabel('Position')
ax[1].set_ylabel('Number of Players')

plt.tight_layout()
plt.show()
#%%
import seaborn as sns
import matplotlib.pyplot as plt
filtered_data = player_info.dropna(subset=['position', 'rosterstatus'])
filtered_data['rosterstatus'] = filtered_data['rosterstatus'].astype('category')
plt.figure(figsize=(12, 6))
sns.violinplot(x='position', y='weight', hue='rosterstatus', data=filtered_data, split=True)
plt.title('Weight Distribution by Position and Roster Status (Active vs Inactive)')
plt.xlabel('Position')
plt.ylabel('Weight')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#%%
import seaborn as sns

# Combine Active and Inactive Players' position counts into a single dataframe
position_counts = pd.DataFrame({
    'Active': active_position_counts,
    'Inactive': inactive_position_counts
}).fillna(0)

# Plot Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(position_counts.T, annot=True, cmap='YlGnBu', cbar=True, fmt='g', linewidths=0.5)
plt.title("Heatmap: Active vs Inactive Players by Position")
plt.xlabel('Position')
plt.ylabel('Roster Status')
plt.tight_layout()
plt.show()
#%%
# year wise distrubution of thr  the greatest 75 players
greatest_75_players = player_info[player_info['greatest_75_flag'] == 'Y']
yearly_distribution = greatest_75_players['draft_year'].value_counts()

plt.figure(figsize=(8, 8))
yearly_distribution.plot(kind='pie', autopct='%1.1f%%', title="Year-wise Distribution of Greatest 75 Players")
plt.ylabel('')  
plt.show()

#%%
# correlation plot 

numeric_columns = player_info.select_dtypes(include=['number']).columns

correlation_matrix = player_info[numeric_columns].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True, linewidths=0.5)
plt.title("Correlation Heatmap of All Numeric Columns")
plt.tight_layout()
plt.show()

# %%
##### $$$ play_by_play - dataset contain inf of every game $$$ ########

path2=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\data_player1.csv"

play_by_play=pd.read_csv(path2)
play_by_play.isnull().sum()
play_by_play

'''
# game_id: 
Description: Unique identifier for each game.
Usefulness: Helps in identifying and grouping events
related to a specific game.

eventnum:
Description: Sequential number of the event within a game.
Usefulness: Useful for understanding the sequence of
events during the game.

eventmsgtype:
Description: Code representing the type of
event (e.g., shot, foul, turnover).
Usefulness: Useful for analyzing specific

types of game actions and patterns.
Made Shot (1): A successful field goal.
Missed Shot (2): An unsuccessful field goal attempt.
Free Throw (3): Free throw attempts.
Rebound (4): Either offensive or defensive rebounds.
Turnover (5): Loss of possession without attempting a shot.
Foul (6): Personal, technical, or team fouls.
Violation (7): Includes traveling, double dribble, or other infractions.
Substitution (8): Player changes during the game.
Timeout (10): Timeout called by a team or official.
Game End/Other (11): Marks the end of a period or other miscellaneous events


eventmsgactiontype:
Description: Code providing more details about the event type.
Usefulness: Provides granularity for event analysis,
such as differentiating between types of fouls.

0: Generic or unspecified action (e.g., general fouls or turnovers).
1: Specific actions like layups, dunks, or steals depending on the eventmsgtype.
2: Jump shots or specific shot types.
5: Defensive rebounds or specific turnovers.
11: Personal fouls or technical fouls.
12: Offensive fouls or team-specific actions.
Higher numbers (e.g., 42, 79): Represent less common or 
specialized actions, such as flagrant fouls, specific
violations, or unusual game scenarios.

By combining eventmsgtype and eventmsgactiontype, 
you can precisely determine what occurred in the game.
For example:
eventmsgtype = 1 (Made Shot) and eventmsgactiontype = 2 could signify a made jump shot.
eventmsgtype = 6 (Foul) and eventmsgactiontype = 11 might indicate a personal foul.
eventmsgtype = 8 (Substitution) and eventmsgactiontype = 0 shows a substitution occurred.



period:
Description: Game period (e.g., 1 for the first quarter, 2 for the second quarter).
Usefulness: Helps analyze events by quarter or overtime.

1: The first quarter of the game (Q1).
2: The second quarter of the game (Q2).
3: The third quarter of the game (Q3).
4: The fourth quarter of the game (Q4).
5 or higher: Represents overtime periods. For example:
5: First overtime (OT1).
6: Second overtime (OT2), and so on.




wctimestring:
Description: Wall-clock time (actual time during the game).
Usefulness: Useful for mapping events to real-world time.


pctimestring:
Description: Time remaining in the period (game clock).
Usefulness: Helps analyze the timing of critical events in a game.

person1type:
Description: Type of person involved in the event
(e.g., player, coach).
Usefulness: Helps identify who was primarily involved in the event.

 the values 4 and 5 are common and can be interpreted as follows, based on the NBA's event categorization:

4: Player – This typically refers to an actual player on the court involved in the event (e.g., scoring, fouling, assisting).
5: Opponent/Other – This could refer to another type of entity involved, such as the opposing player or 
another non-player entity like a coach or referee, depending on the event.




player1_id:
Description: Unique identifier for the primary
player involved in the event.
Usefulness: Enables tracking of player-specific actions.

player1_name:
Description: Name of the primary player involved in the event.
Usefulness: Provides readable context to player1_id.

player1_team_id:
Description: Unique identifier for the player’s team.
Usefulness: Helps in team-specific analyses.

player1_team_city:
Description: City of the player’s team.
Usefulness: Adds geographical context to team-specific events.

player1_team_nickname:
Description: Nickname of the player’s team (e.g., Lakers, Suns).
Usefulness: Makes team information more relatable.

player1_team_abbreviation:
Description: Abbreviated form of the team name (e.g., LAL, PHX).
Usefulness: Convenient for visualizations and compact displays.

person2type:
Description: Type of the second person involved in the event.
Usefulness: Useful for events involving multiple participants.

5: Opponent/Other – Similar to person1type, this could refer
to the opposing player or another type of non-player entity 
involved in the event (e.g., referee or coach).
0: None or No Interaction – This likely indicates that there
is no second participant for this event. It could be an event
involving only one player, such as a solo action.
4: Player – This indicates the second player involved in 
the event (for example, a player receiving a pass or assisting
another player).




player2_id:
Description: Unique identifier for the secondary player involved in the event.
Usefulness: Allows deeper analysis of interactions between players.

person3type:
Description: Type of a third person involved in the event.
Usefulness: Relevant for complex events involving three participants.

player3_id:
Description: Unique identifier for the tertiary player involved in the event.
Usefulness: Extends granularity for multi-person events.

5: Opponent/Other – This likely refers to the third
player (or other entity) involved in the event, possibly
an opposing player or a non-player role, such as a referee
or coach.
0: None or No Interaction – This indicates that there is
no third participant for the event. It suggests the event 
involved fewer than three people (such as a solo action or
a two-player interaction).
4: Player – This indicates that the third participant is
a player, which could be part of an event with multiple 
players involved (e.g., a play with three players 
interacting, such as a pass or screen).



video_available_flag: 
Description: Indicates if a video of the event is available (0 = no, 1 = yes).
Usefulness: Useful for identifying events with supplementary video content.
'''
# %%
import pandas as pd
summary_stats = play_by_play.describe(include='all')  # Includes all columns

unique_games = play_by_play['game_id'].nunique()
unique_players = play_by_play['player1_name'].nunique()
unique_teams = play_by_play['player1_team_id'].nunique()
total_events = len(play_by_play)

summary = {
    "Number of Unique Games": unique_games,
    "Number of Unique Players": unique_players,
    "Number of Unique Teams": unique_teams,
    "Total Events": total_events,
}

summary_stats, summary

# %%

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

print(play_by_play.head())

print(play_by_play.info())

print(play_by_play.describe())

print(play_by_play.isnull().sum())


print(play_by_play.dtypes)
#%%
print("Unique values in eventmsgtype: ", play_by_play['eventmsgtype'].unique())
print("Unique values in period: ", play_by_play['period'].unique())
print("Unique values in person1type: ", play_by_play['person1type'].unique())
print("Unique values in player1_team_abbreviation: ", play_by_play['player1_team_abbreviation'].unique())
#%%
plt.figure(figsize=(10, 6))
sns.histplot(play_by_play['eventnum'], kde=True)
plt.title('Distribution of Event Numbers')
plt.xlabel('Event Number')
plt.ylabel('Frequency')
plt.show()
#%%

plt.figure(figsize=(10, 6))
sns.histplot(play_by_play['eventmsgtype'], kde=True)
plt.title('Distribution of Event Numbers')
plt.xlabel('Event Number')
plt.ylabel('Frequency')
plt.show()
#%%
plt.figure(figsize=(10, 6))
sns.countplot(data=play_by_play, x='period', palette='viridis')
plt.title('Distribution of Events Across Periods')
plt.xlabel('Period')
plt.ylabel('Count of Events')
plt.show()
#%%
plt.figure(figsize=(12, 6))
sns.countplot(data=play_by_play, x='eventmsgtype', palette='Set2')
plt.title('Distribution of Event Types')
plt.xlabel('Event Type')
plt.ylabel('Count of Events')
plt.show()
#%%


#%%
player_event_count = play_by_play['player1_id'].value_counts().head(10)

player_names = play_by_play.drop_duplicates(subset='player1_id')[['player1_id', 'player1_name']]
player_names_dict = dict(zip(player_names['player1_id'], player_names['player1_name']))

top_10_players_names = [player_names_dict.get(player_id, 'Unknown') for player_id in player_event_count.index]


plt.figure(figsize=(12, 6))
sns.barplot(x=player_event_count.index, y=player_event_count.values, palette='magma')


for i, value in enumerate(player_event_count.values):
    plt.text(i, value + 5, top_10_players_names[i], ha='center', va='bottom', fontsize=10)

plt.title('Top 10 Players by Number of Events')
plt.xlabel('Player ID')
plt.ylabel('Number of Events')
plt.xticks(rotation=90)
plt.show()


#%%
# corr plot for numerical dtype 
play_by_play_numeric = play_by_play.select_dtypes(include=[np.number])
corr = play_by_play_numeric.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.show()


# %%

# univarient analysis for numeric col like period and event num

# Statistics for numerical features
numerical_cols = ['eventnum', 'period']  # Add other numerical columns if necessary
numerical_summary = play_by_play[numerical_cols].describe()
print(numerical_summary)
#%%
plt.figure(figsize=(14, 6))
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(1, len(numerical_cols), i)
    sns.histplot(play_by_play[col], kde=True, color='skyblue', bins=20)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
#%%
plt.figure(figsize=(14, 6))
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(1, len(numerical_cols), i)
    sns.boxplot(x=play_by_play[col], color='lightgreen')
    plt.title(f'Box plot of {col}')
    plt.xlabel(col)
plt.tight_layout()
plt.show()

# %%
# univerent analysis for catagorical columns 
# # Categorical features to analyze
#%%
categorical_cols = ['person1type', 'person2type', 'person3type']  
#%%
for col in categorical_cols:
    print(f"Frequency distribution of {col}:")
    print(play_by_play[col].value_counts())
    print("\n")
#%%

plt.figure(figsize=(14, 6))
for i, col in enumerate(categorical_cols, 1):
    plt.subplot(1, len(categorical_cols), i)
    sns.countplot(x=play_by_play[col], palette='muted')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
plt.tight_layout()
plt.show()

#%%
###########


#%%
#  count for periods (quarters and overtime)
period_count = play_by_play['period'].value_counts()
print(period_count)

#%%
# Time analysis: regeular VS overtime 
#  
play_by_play['overtime'] = play_by_play['period'].apply(lambda x: 'Overtime' if x > 4 else 'Regular')
plt.figure(figsize=(5, 6))
sns.countplot(x='overtime', data=play_by_play, palette='Set2')
plt.title('Event Distribution: Regular vs Overtime')
plt.xlabel('Period Type')
plt.ylabel('Event Count')
plt.show()

#%%
plt.figure(figsize=(12, 6))
sns.violinplot(
    x='period', 
    y='eventmsgtype', 
    data=play_by_play, 
    palette='magma', 
    scale='width', 
    inner='quartile'
)
plt.title('Event Distribution by Game Period')
plt.xlabel('Period (Quarter/Overtime)')
plt.ylabel('Event Type')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



#%%
player_involvement = play_by_play.groupby(['player1_id', 'player2_id', 'player3_id', 'eventmsgtype']).size().reset_index(name='count')

top_player_involvement = player_involvement.groupby(['player1_id', 'eventmsgtype']).sum().reset_index().head(10)

plt.figure(figsize=(12, 6))
ax = sns.barplot(x='player1_id', y='count', hue='eventmsgtype', data=top_player_involvement, palette='Set2')
plt.title('Player Involvement in Event Types')
plt.xlabel('Player ID')
plt.ylabel('Event Count')
plt.xticks(rotation=90)


for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                fontsize=10, color='black', 
                xytext=(0, 5), textcoords='offset points')

plt.show()

#%%
# team performanece by evenrt type 
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

outer_data = team_performance.groupby('player1_team_id')['count'].sum().sort_values(ascending=False)
inner_data = team_performance.groupby(['player1_team_id', 'eventmsgtype'])['count'].sum().reset_index()

team_colors = plt.cm.viridis(np.linspace(0, 1, len(outer_data)))
event_type_colors = plt.cm.coolwarm(np.linspace(0, 1, len(inner_data['eventmsgtype'].unique())))

team_color_map = dict(zip(outer_data.index, team_colors))
event_type_color_map = dict(zip(inner_data['eventmsgtype'].unique(), event_type_colors))

fig, ax = plt.subplots(figsize=(10, 10))
wedges_outer, texts_outer = ax.pie(
    outer_data, 
    labels=outer_data.index, 
    startangle=140, 
    colors=[team_color_map[team] for team in outer_data.index], 
    radius=1, 
    wedgeprops={'width': 0.3, 'edgecolor': 'w'}
)

inner_startangle = 140
for team_id in outer_data.index:
    subset = inner_data[inner_data['player1_team_id'] == team_id]
    wedges_inner, _ = ax.pie(
        subset['count'], 
        startangle=inner_startangle, 
        radius=0.7, 
        colors=[event_type_color_map[event] for event in subset['eventmsgtype']], 
        wedgeprops={'width': 0.3, 'edgecolor': 'w'}
    )
    inner_startangle += 360 / len(outer_data) 

center_circle = Circle((0, 0), 0.5, color='white')
ax.add_artist(center_circle)

legend_elements = (
    [Line2D([0], [0], color=team_color_map[team], lw=4, label=f'Team {team}') for team in outer_data.index] +
    [Line2D([0], [0], color=event_type_color_map[event], lw=4, label=f'Event Type {event}') for event in inner_data['eventmsgtype'].unique()]
)
plt.legend(handles=legend_elements, bbox_to_anchor=(1, 1), loc='upper left', title='Legend', fontsize='small')

plt.title('Donut-in-Donut Chart: Team Performance by Event Type')
ax.set_aspect('equal')
plt.tight_layout()
plt.show()



#%%
# Aggregate the total count of events by team
team_total_events = team_performance.groupby('player1_team_id')['count'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(team_total_events)))

plt.pie(
    team_total_events, 
    labels=team_total_events.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops={'width': 0.4}
)

plt.title('Team Comparison: Total Event Counts (Donut Chart)')
plt.gca().set_aspect('equal')  
plt.show()


# %%
#  performance data per event msg type 
team_event_data = team_performance.pivot_table(index='player1_team_id', columns='eventmsgtype', values='count', aggfunc='sum', fill_value=0)

team_event_data.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')
plt.title('Comparison of Event Types by Team')
plt.xlabel('Team ID')
plt.ylabel('Event Count')
plt.xticks(rotation=90)
plt.show()

#%%
#  by period and event type to analyze event distribution by period
period_event_counts = play_by_play.groupby(['period', 'eventmsgtype']).size().reset_index(name='count')
donut_data = play_by_play.groupby('eventmsgtype').size().reset_index(name='count')

plt.figure(figsize=(8, 8))
plt.pie(
    donut_data['count'],
    labels=donut_data['eventmsgtype'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('coolwarm', len(donut_data))
)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

plt.title('Event Type Distribution Across All Periods (Donut Chart)')
plt.show()


#%%
# Group by person type and event type
person_interactions = play_by_play.groupby(['person1type', 'person2type', 'person3type', 'eventmsgtype']).size().reset_index(name='count')

plt.figure(figsize=(12, 6))
sns.countplot(x='eventmsgtype', hue='person1type', data=person_interactions, palette='magma')
plt.title('Person Type Interactions by Event Type')
plt.xlabel('Event Type')
plt.ylabel('Count')
plt.show()

#%%

path2=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\data_player1.csv"

play_by_play=pd.read_csv(path2)


#%%
###################### $$$$$$$$$  ################################
# Identify key events: Successful shots (eventmsgtype = 1), fouls (eventmsgtype = 6), turnovers (eventmsgtype = 5)
key_events = play_by_play[play_by_play['eventmsgtype'].isin([1, 5, 6])]
#%%
# Group by player and team to find involvement in key events
hotspot_players = key_events.groupby(['player1_id', 'player1_name']).size().reset_index(name='count').sort_values(by='count', ascending=False).head(10)
hotspot_teams = key_events.groupby(['player1_team_id', 'player1_team_nickname']).size().reset_index(name='count').sort_values(by='count', ascending=False).head(10)
#%%
#  top players in key events
plt.figure(figsize=(12, 6))
sns.barplot(data=hotspot_players, x='player1_name', y='count', palette='coolwarm')
plt.title('Top Players Involved in Key Events')
plt.xlabel('Player Name')
plt.ylabel('Count of Key Events')
plt.xticks(rotation=45)
plt.show()
#%%
#  top teams in key events
plt.figure(figsize=(12, 6))
sns.barplot(data=hotspot_teams, x='player1_team_nickname', y='count', palette='magma')
plt.title('Top Teams Involved in Key Events')
plt.xlabel('Team Name')
plt.ylabel('Count of Key Events')
plt.xticks(rotation=45)
plt.show()

# %%

############ %%% $$$$$$$$$$$$$$ %%%% ######################
## top playerr eda 

print(play_by_play['pctimestring'].unique())
#%%

play_by_play['pctimestring'] = play_by_play['pctimestring'].apply(lambda x: str(x).strip())
#%%
player1_events = play_by_play.groupby(['game_id', 'pctimestring', 'player1_id', 'player1_name']).size().reset_index(name='event_count')
player2_events = play_by_play.groupby(['game_id', 'pctimestring', 'player2_id', 'player1_name']).size().reset_index(name='event_count')
player3_events = play_by_play.groupby(['game_id', 'pctimestring', 'player3_id', 'player1_name']).size().reset_index(name='event_count')
#%%
all_player_events = pd.concat([player1_events, player2_events, player3_events])

player_event_summary = all_player_events.groupby(['player1_name']).agg({'event_count': 'sum'}).reset_index()
#%%
top_players = player_event_summary.sort_values(by='event_count', ascending=False).head(75)

print(top_players[['player1_name', 'event_count']])

top_time_players = all_player_events.groupby(['pctimestring', 'player1_name']).agg({'event_count': 'sum'}).reset_index()
#%%
top_time_players_sorted = top_time_players.sort_values(by='event_count', ascending=False).head(10)
print(top_time_players_sorted[['pctimestring', 'player1_name', 'event_count']])

# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
# Plot the Top 75  Players by Event Count 
plt.figure(figsize=(10, 16))
top_players_plot = sns.barplot(data=top_players, x='event_count', y='player1_name', palette='viridis')
top_players_plot.set_title("Top 75 Players by Event Count", fontsize=16)
top_players_plot.set_xlabel("Event Count", fontsize=12)
top_players_plot.set_ylabel("Player Name", fontsize=12)
plt.tight_layout()
plt.show()
#%%
# Top 10  Players by Event Count at Specific reaming 0 to 12 pc  Time Intervals
plt.figure(figsize=(10, 6))
top_time_players_plot = sns.barplot(data=top_time_players_sorted, x='event_count', y='player1_name', hue='pctimestring', palette='coolwarm')
top_time_players_plot.set_title("Top Players by Event Count at Specific Time Intervals", fontsize=16)
top_time_players_plot.set_xlabel("Event Count", fontsize=12)
top_time_players_plot.set_ylabel("Player Name", fontsize=12)
plt.tight_layout()
plt.show()
#%%
####### $$$$$$$$$ ############################################
##### $$ merge_game $$ ############


path3=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\merge_game.csv"

game=pd.read_csv(path3)
game.isnull().sum()
game.head(10)
game.tail(10)
#%%
"""

######      $$ Column Descriptions $$      ###########

game_id:
Meaning: Unique identifier for each game.
Unique Values: Each value is distinct, representing a specific game.

game_date_x:
Meaning: The date when the game was played.
Unique Values: Unique dates (e.g., 2023-05-22, 2023-06-12). Likely the same as game_date_y.

attendance:
Meaning: The number of people who attended the game.
Unique Values: Numeric values like 18997, 19528, etc., showing attendance for different games.

season_id:
Meaning: Identifier for the NBA season (e.g., 2022 season games = 42022).
Unique Values: Likely a single value for a dataset covering one season (e.g., 42022).

team_id_home:
Meaning: Unique identifier for the home team.
Unique Values: Numeric IDs (e.g., 1610612747 for Los Angeles Lakers, 1610612748 for Miami Heat).

team_abbreviation_home:
Meaning: Abbreviation for the home team name.
Unique Values: LAL, MIA, BOS, DEN, etc.

team_name_home:
Meaning: Full name of the home team.
Unique Values: Los Angeles Lakers, Miami Heat, Boston Celtics, Denver Nuggets, etc.

game_date_y:
Meaning: Duplicate or alternative format for game_date_x.
Unique Values: Same as game_date_x.

matchup_home:
Meaning: A string showing the matchup, indicating home vs. away teams (e.g., LAL vs. DEN).
Unique Values: Combinations like LAL vs. DEN, MIA vs. BOS.

wl_home:
Meaning: Win/Loss indicator for the home team.
Unique Values: W for Win, L for Loss.
Other Columns (hidden by ...):
These columns were not fully displayed but could include statistics, metadata, or team/player details.

season_type:
Meaning: Indicates the type of NBA season (e.g., Regular Season, Playoffs).
Unique Values: Playoffs (in the provided data).

game_date_est:
Meaning: Game date in Eastern Standard Time (duplicate of game_date_x).
Unique Values: Same as game_date_x.

game_status_id:
Meaning: Status of the game (likely 3 = Completed).
Unique Values: 3.

gamecode:
Meaning: A code identifying the game, formatted as <date>/<teams>.
Unique Values: Strings like 20230522/DENLAL, 20230612/MIADEN.

home_team_id:
Meaning: ID of the home team (similar to team_id_home).
Unique Values: Matches team_id_home.

visitor_team_id:
Meaning: ID of the visiting team.
Unique Values: IDs like 1610612743, 1610612748.

season:
Meaning: The NBA season year (e.g., 2022).
Unique Values: Likely one value (e.g., 2022).

live_period:
Meaning: Indicates the game's progress (e.g., quarter or overtime).
Unique Values: 4 for the fourth quarter.

live_period_time_bcast:
Meaning: Time left in the game, as broadcast (e.g., Q4 - ESPN).
Unique Values: Strings like Q4 - ESPN, Q4 - TNT, Q4 - ABC.

wh_status:
Meaning: Status indicator for data (likely 1 = Available/Finalized).
Unique Values: 1




"""
#%%
#### start for game dataset 

#%%

import pandas as pd


print("Dataset Info:")
print(game.info())

missing_values = game.isnull().sum()
print("\nMissing Values:")
print(missing_values)


if 'attendance' in game.columns:
    median_attendance = game['attendance'].median()
    game['attendance'].fillna(median_attendance, inplace=True)
    print(f"\nMissing 'attendance' values filled with median: {median_attendance}")

# 2. Verify Data Types
print("\nData Types Before Conversion:")
print(game.dtypes)

if 'game_date_x' in game.columns:
    game['game_date_x'] = pd.to_datetime(game['game_date_x'], errors='coerce')
    print("\nConverted 'game_date_x' to datetime.")

duplicates_count = game.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates_count}")
game.drop_duplicates(inplace=True)
print("Duplicates removed.")

# 4. Standardize Formats
# Example: Ensuring `team_abbreviation` is in uppercase
if 'team_abbreviation_home' in game.columns:
    game['team_abbreviation_home'] = game['team_abbreviation_home'].str.upper()
    print("\nStandardized 'team_abbreviation_home' to uppercase.")

# 5. Handle Outliers (Example for 'attendance')
if 'attendance' in game.columns:
    Q1 = game['attendance'].quantile(0.25)
    Q3 = game['attendance'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify and flag outliers
    outliers = game[(game['attendance'] < lower_bound) | (game['attendance'] > upper_bound)]
    print(f"\nNumber of outliers in 'attendance': {len(outliers)}")
    
   
    game = game[(game['attendance'] >= lower_bound) & (game['attendance'] <= upper_bound)]
    print("Outliers removed from 'attendance'.")

print("\nDataset Info After Cleaning:")
print(game.info())



#%%

# Calculate the average attendance
average_attendance = game['attendance'].mean()
print(f"Average Attendance: {average_attendance}")

high_attendance_games = game[game['attendance'] > average_attendance]

high_attendance_games_sorted = high_attendance_games.sort_values(by='attendance', ascending=False)

# Display the top 10 games with the highest attendance
print("Top 10 Games with Attendance Higher than Average:")
print(high_attendance_games_sorted[['game_id', 'attendance', 'team_name_home', 'team_name_away', 'game_date_x']].head(10))

# Group by home team to see average attendance for each team
team_attendance = high_attendance_games_sorted.groupby('team_name_home')['attendance'].mean().sort_values(ascending=False)

# Display top 10 teams with the highest average attendance for high-attendance games
print("\nTop 10 Teams by Average Attendance in High-Attendance Games:")
print(team_attendance.head(10))




#%%

# Attendance Analysis

average_attendance = game['attendance'].mean()
print(f"\nAverage Attendance: {average_attendance}")

# Top 10 Games with Attendance Higher than Average
top_games = game[game['attendance'] > average_attendance]
top_games_sorted = top_games.sort_values(by='attendance', ascending=False).head(10)

print("\nTop 10 Games with Attendance Higher than Average:")
print(top_games_sorted[['game_id', 'attendance', 'team_name_home', 'team_name_away', 'game_date_x']])
#%%
# Top 10 Teams by Average Attendance
top_teams_attendance = game.groupby('team_name_home')['attendance'].mean()
top_teams_attendance_sorted = top_teams_attendance.sort_values(ascending=False).head(10)

print("\nTop 10 Teams by Average Attendance in High-Attendance Games:")
print(top_teams_attendance_sorted)
#%%
#
#  Distribution of Attendance
plt.figure(figsize=(10, 6))
sns.histplot(game['attendance'], bins=30, kde=True)
plt.title('Distribution of Attendance')
plt.xlabel('Attendance')
plt.ylabel('Frequency')
plt.show()

#%%
#  Top 10 Teams by Average Attendance
plt.figure(figsize=(12, 6))
sns.barplot(x=top_teams_attendance_sorted.index, y=top_teams_attendance_sorted.values)
plt.title('Top 10 Teams by Average Attendance')
plt.xlabel('Team Name')
plt.ylabel('Average Attendance')
plt.xticks(rotation=45, ha='right')
plt.show()
#%%

# 3. Attendance Over Time (by Game Date)
game['game_date_x'] = pd.to_datetime(game['game_date_x'])

attendance_over_time = game.groupby('game_date_x')['attendance'].mean()

plt.figure(figsize=(12, 6))
attendance_over_time.plot(kind='line', color='blue')
plt.title('Average Attendance Over Time')
plt.xlabel('Game Date')
plt.ylabel('Average Attendance')
plt.xticks(rotation=45)
plt.show()

#%%%
numerical_summary = game.describe()
print("\nSummary Statistics for Numerical Columns:")
print(numerical_summary)

#%%
categorical_columns = ['team_name_home', 'team_name_away', 'game_date_x']  # Example categorical columns
categorical_summary = game[categorical_columns].describe(include=['object'])
print("\nSummary Statistics for Categorical Columns:")
print(categorical_summary)

# 3. Attendance Specific Summary (only numerical summary for 'attendance' column)
attendance_summary = game['attendance'].describe()
print("\nAttendance Summary:")
print(attendance_summary)

#%%
# 4. Frequency of Unique Teams (Home and Away)
home_team_freq = game['team_name_home'].value_counts()
away_team_freq = game['team_name_away'].value_counts()

print("\nFrequency of Home Teams:")
print(home_team_freq.head(10))  # Display top 10 home teams by frequency

print("\nFrequency of Away Teams:")
print(away_team_freq.head(10))  # Display top 10 away teams by frequency



#%%
## top 10 team by  frequency  
plt.figure(figsize=(12, 6))
sns.barplot(x=home_team_freq.head(10).index, y=home_team_freq.head(10).values)
plt.title('Top 10 Home Teams by Frequency')
plt.xlabel('Team Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.show()
#%%
##top 10 tems away frequency 

plt.figure(figsize=(12, 6))
sns.barplot(x=away_team_freq.head(10).index, y=away_team_freq.head(10).values)
plt.title('Top 10 Away Teams by Frequency')
plt.xlabel('Team Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.show()

#%%

#### games overs the year eda part 


# Convert 'game_date_x' to datetime format
game['game_date_x'] = pd.to_datetime(game['game_date_x'])

# Extract year, month, and day of week from 'game_date_x'
game['year'] = game['game_date_x'].dt.year
game['month'] = game['game_date_x'].dt.month
game['day_of_week'] = game['game_date_x'].dt.day_name()

# Count number of games per year
games_per_year = game['year'].value_counts().sort_index()

# Count number of games per month
games_per_month = game['month'].value_counts().sort_index()

# Count number of games per day of the week
games_per_day_of_week = game['day_of_week'].value_counts()

print("\nGames per Year:", games_per_year)
print("\nGames per Month:", games_per_month)
print("\nGames per Day of Week:", games_per_day_of_week)

# Compare Regular Season vs Playoffs games
season_type_count = game['season_type'].value_counts()
print("\nGames by Season Type:", season_type_count)

#%%

# Assuming there's a column 'home_team_win' indicating whether the home team won
# Home Team Performance: wins and losses
home_team_performance = game.groupby('team_name_home')['home_team_win'].value_counts().unstack().fillna(0)

# Top 10 Winning Teams
top_teams_by_wins = game.groupby('team_name_home')['home_team_win'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Teams by Wins:", top_teams_by_wins)

# Team Performance (Home Team Win/Loss)
print("\nHome Team Performance (Wins/Losses):")
print(home_team_performance)

#%%

# Check the column names in the game dataset
print(game.columns)

#%%

# Analyze game outcomes (Win/Loss) for home and away teams
home_team_results = game.groupby('team_name_home')['wl_home'].value_counts().unstack().fillna(0)
away_team_results = game.groupby('team_name_away')['wl_away'].value_counts().unstack().fillna(0)

print("\nHome Team Results (Wins/Losses):")
print(home_team_results)

print("\nAway Team Results (Wins/Losses):")
print(away_team_results)

#%%
# Calculate average performance for home and away teams (points, rebounds, assists, etc.)
home_team_performance = game.groupby('team_name_home')[['pts_home', 'reb_home', 'ast_home']].mean()
away_team_performance = game.groupby('team_name_away')[['pts_away', 'reb_away', 'ast_away']].mean()

# Display the top 10 teams by points scored
top_home_teams_points = home_team_performance.sort_values('pts_home', ascending=False).head(10)
top_away_teams_points = away_team_performance.sort_values('pts_away', ascending=False).head(10)

print("\nTop 10 Home Teams by Average Points Scored:")
print(top_home_teams_points[['pts_home']])

print("\nTop 10 Away Teams by Average Points Scored:")
print(top_away_teams_points[['pts_away']])

#%%
# Convert game_date_x to datetime format
game['game_date_x'] = pd.to_datetime(game['game_date_x'])

# Analyze attendance trends over years and months
attendance_by_year = game.groupby(game['game_date_x'].dt.year)['attendance'].mean()
attendance_by_month = game.groupby(game['game_date_x'].dt.month)['attendance'].mean()
attendance_by_day_of_week = game.groupby(game['game_date_x'].dt.dayofweek)['attendance'].mean()

# Plot attendance over the years
plt.figure(figsize=(10, 6))
attendance_by_year.plot(kind='line', color='blue')
plt.title('Average Attendance by Year')
plt.xlabel('Year')
plt.ylabel('Average Attendance')
plt.xticks(rotation=45)
plt.show()

# Plot attendance by month
plt.figure(figsize=(10, 6))
attendance_by_month.plot(kind='bar', color='green')
plt.title('Average Attendance by Month')
plt.xlabel('Month')
plt.ylabel('Average Attendance')
plt.xticks(rotation=45)
plt.show()

# Plot attendance by day of the week
plt.figure(figsize=(10, 6))
attendance_by_day_of_week.plot(kind='bar', color='orange')
plt.title('Average Attendance by Day of Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Attendance')
plt.xticks(rotation=45)
plt.show()


#%%
# Compare attendance between regular season and playoff games
attendance_by_season_type = game.groupby('season_type')['attendance'].mean()

# Plot the comparison
plt.figure(figsize=(8, 6))
attendance_by_season_type.plot(kind='bar', color='purple')
plt.title('Average Attendance by Season Type (Regular Season vs Playoffs)')
plt.xlabel('Season Type')
plt.ylabel('Average Attendance')
plt.xticks(rotation=45)
plt.show()

#%%

# Calculate correlations between performance metrics for home and away teams
home_team_corr = home_team_performance.corr()
away_team_corr = away_team_performance.corr()

print("\nCorrelation Matrix for Home Team Performance:")
print(home_team_corr)

print("\nCorrelation Matrix for Away Team Performance:")
print(away_team_corr)
#%%

# corr()- with the team home and team aways corr 
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate correlations between performance metrics for home and away teams
home_team_corr = home_team_performance.corr()
away_team_corr = away_team_performance.corr()

# Plotting the Correlation Matrix for Home Team Performance
plt.figure(figsize=(8, 6))
sns.heatmap(home_team_corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix for Home Team Performance')
plt.show()

# Plotting the Correlation Matrix for Away Team Performance
plt.figure(figsize=(8, 6))
sns.heatmap(away_team_corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix for Away Team Performance')
plt.show()

#%%

######## $$ %% plyaer analysis %% $$ #########

# Top 5 Most Frequent Home and Away Teams
print("\nTop 5 Most Frequent Home Teams:")
print(game['team_name_home'].value_counts().head(5))

print("\nTop 5 Most Frequent Away Teams:")
print(game['team_name_away'].value_counts().head(5))

# Compare performance between home and away teams
home_away_performance = game[['pts_home', 'pts_away', 'reb_home', 'reb_away', 'ast_home', 'ast_away']].mean()
print("\nHome vs Away Team Performance Comparison:")
print(home_away_performance)
#%%
## code in error 

# Calculate win percentages for home and away teams
home_win_percentage = game.groupby('team_name_home')['home_team_win'].mean()
away_win_percentage = game.groupby('team_name_away')['away_team_win'].mean()

print("\nHome Team Win Percentages:")
print(home_win_percentage)

print("\nAway Team Win Percentages:")
print(away_win_percentage)

print(game.columns)

game.head(10)
#%%
# Correlation between Attendance and Performance
performance_columns = ['attendance', 'pts_home', 'pts_away', 'reb_home', 'reb_away', 'ast_home', 'ast_away']
attendance_performance_corr = game[performance_columns].corr()
print("\nCorrelation Between Attendance and Performance Metrics:")
print(attendance_performance_corr)

# Plot correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(attendance_performance_corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix: Attendance vs Performance')
plt.show()


#%%





#### above some work remaning 



""" 

$$$$$$$$$$$$$$$$$










%%%%%%%%


"""


##########################

# %%
################## %% $$$$ game score data $$$$$ %% ##############

path5=r"C:\GWU\Projects\Data_warehosuing_sql\NBA\csv\final_dataset\merged_data_line_officials.csv"
game_score=pd.read_csv(path5)
#%%

game_score

#%%
"""

game_date_est: Date of the game (Eastern Standard Time).
Use: Temporal analysis to explore trends over time,
such as season-specific performance or year-by-year analysis.



game_id: Unique identifier for each game.
Use: Ensures data integrity and acts as a key for
joining datasets.



team_id_home, team_id_away: Unique identifiers for the home
and away teams.
Use: Identifying specific team performances and trends.


team_abbreviation_home, team_abbreviation_away: Abbreviations
for the teams (e.g., CHI for Chicago Bulls).
Use: Labels in visualizations and filtering specific teams.



team_city_name_home, team_city_name_away: Names of cities
the teams are based in.
Use: Geospatial analysis or regional performance trends.



team_nickname_home, team_nickname_away: Nicknames of the
teams (e.g., Bulls, Pistons).
Use: Adding context or personalization in reports.



team_wins_losses_home, team_wins_losses_away: Current
win-loss record for each team.
Use: Analyzing performance trends and team success.


pts_qtr1_home, pts_qtr2_home, pts_qtr3_home, 
pts_qtr4_home: Points scored by the home team in each quarter.
Use: Analyzing game flow and momentum changes.



pts_qtr1_away, pts_qtr2_away, pts_qtr3_away, 
pts_qtr4_away: Points scored by the away team in each quarter.
Use: Same as above for away teams.



pts_home, pts_away: Total points scored by home and away teams.
Use: Determining game outcomes, average scoring trends,
and margin-of-victory analysis.



official_id, first_name, last_name, jersey_num: Details 
of game officials.
Use: Analyzing officiating patterns, potential biases,
or referee impact.

"""

#%%


import pandas as pd

# Check for missing values
print("Missing values:\n", game_score.isnull().sum())

game_score['pts_home'] = game_score['pts_home'].fillna(game_score['pts_home'].mean())
game_score['pts_away'] = game_score['pts_away'].fillna(game_score['pts_away'].mean())
game_score['team_city_name_home'] = game_score['team_city_name_home'].fillna(game_score['team_city_name_home'].mode()[0])
game_score['team_city_name_away'] = game_score['team_city_name_away'].fillna(game_score['team_city_name_away'].mode()[0])

#%%
# Check data types
print("Data types before conversion:\n", game_score.dtypes)

# Convert columns to appropriate data types
game_score['game_date_est'] = pd.to_datetime(game_score['game_date_est'])  # Convert to datetime
numeric_cols = ['pts_home', 'pts_away']  # Example of numeric columns
game_score[numeric_cols] = game_score[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Confirm changes
print("Data types after conversion:\n", game_score.dtypes)

#%%
print("Number of duplicate rows:", game_score.duplicated().sum())
game_score = game_score.drop_duplicates()
print("Duplicate rows after removal:", game_score.duplicated().sum())

#%%
# Standardize text columns for team names : 
text_columns = ['team_city_name_home', 'team_city_name_away']
for col in text_columns:
    game_score[col] = game_score[col].str.lower().str.strip()

print(game_score[text_columns].head())

#%%
# Create 'margin_of_victory' column: 
game_score['margin_of_victory'] = game_score['pts_home'] - game_score['pts_away']
print(game_score[['pts_home', 'pts_away', 'margin_of_victory']].head())
#%%

# Descriptive statistics
print("Descriptive statistics:\n", game_score.describe())

# Frequency counts for categorical columns
categorical_cols = ['team_city_name_home', 'team_city_name_away']
for col in categorical_cols:
    print(f"Frequency counts for {col}:\n", game_score[col].value_counts())

#%%

# Calculate win/loss
game_score['home_win'] = game_score['pts_home'] > game_score['pts_away']

# Analyze margin of victory
print("Margin of victory statistics:\n", game_score['margin_of_victory'].describe())

# Home-court advantage analysis :
home_avg = game_score['pts_home'].mean()
away_avg = game_score['pts_away'].mean()
print(f"Home Average Score: {home_avg}, Away Average Score: {away_avg}")
#%%
# extract year , mont and day from the dataset 

game_score['year'] = game_score['game_date_est'].dt.year
game_score['month'] = game_score['game_date_est'].dt.month
game_score['day'] = game_score['game_date_est'].dt.day

yearly_scores = game_score.groupby('year')[['pts_home', 'pts_away']].mean()
print("Yearly Scoring Trends:\n", yearly_scores)

#%%
import matplotlib.pyplot as plt
import seaborn as sns
# Plot margin of victory distribution : 
sns.histplot(game_score['margin_of_victory'], kde=True)
plt.title('Margin of Victory Distribution')
plt.xlabel('Margin of Victory')
plt.ylabel('Frequency')
plt.show()
#%%
# Time series of average home/away scores
# time series analysis by year tread 
yearly_scores.plot(kind='line', marker='o', title='Yearly Scoring Trends')
plt.xlabel('Year')
plt.ylabel('Average Score')
plt.show()

#%%

game_score.head(10)
#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = game_score.copy()
#%%
### Descriptive Statistics

# Descriptive statistics for numeric columns
numeric_stats = data.describe()

numeric_variance = data.var(numeric_only=True)

numeric_median = data.median(numeric_only=True)

# Display results :
print("Descriptive Statistics:\n", numeric_stats)
print("\nVariance:\n", numeric_variance)
print("\nMedian:\n", numeric_median)
#%%
###  Score Distribution

# Distribution of Home and Away Scores
plt.figure(figsize=(16, 8))

plt.subplot(1, 3, 1)
sns.histplot(data['pts_home'], kde=True, bins=20, color='blue')
plt.title('Distribution of Home Scores')
plt.xlabel('Points Scored by Home Team')
#%%
plt.subplot(1, 3, 2)
sns.histplot(data['pts_away'], kde=True, bins=20, color='red')
plt.title('Distribution of Away Scores')
plt.xlabel('Points Scored by Away Team')
#%%
plt.subplot(1, 3, 3)
sns.histplot(data['margin_of_victory'], kde=True, bins=20, color='green')
plt.title('Distribution of Margin of Victory')
plt.xlabel('Margin of Victory')

plt.tight_layout()
plt.show()
#%%

#  plot for pts_home, pts_away, and margin_of_victory
plt.figure(figsize=(12, 8))
sns.violinplot(data=data[['pts_home', 'pts_away', 'margin_of_victory']], palette="muted", scale="width")
plt.title('Violin Plot of Home Scores, Away Scores, and Margin of Victory', fontsize=16)
plt.xlabel('Metrics', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.xticks(ticks=[0, 1, 2], labels=['Home Scores', 'Away Scores', 'Margin of Victory'], fontsize=10)
plt.show()

#%%
### Frequency Counts

# Frequency of Home Team Cities :
home_team_city_freq = data['team_city_name_home'].value_counts()
print("\nFrequency of Home Team Cities:\n", home_team_city_freq)

# Frequency of Wins (True/False in home_win column) :
home_win_freq = data['home_win'].value_counts()
print("\nFrequency of Home Wins:\n", home_win_freq)

# Frequency of Years:
year_freq = data['year'].value_counts().sort_index()
print("\nFrequency of Games by Year:\n", year_freq)

# Frequency of Months:
month_freq = data['month'].value_counts().sort_index()
print("\nFrequency of Games by Month:\n", month_freq)

# Frequency of Days:
day_freq = data['day'].value_counts().sort_index()
print("\nFrequency of Games by Day:\n", day_freq)


#%%
# Simple Pie Chart for Frequency of Games by Year
plt.figure(figsize=(8, 8))
plt.pie(
    year_freq_sorted.values, 
    labels=year_freq_sorted.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=sns.color_palette('Set3', len(year_freq_sorted))
)
plt.title('Pie Chart for Frequency of Games by Year')
plt.show()



#%%
# Line Plot for Frequency of Games by Year
plt.figure(figsize=(10, 6))
sns.lineplot(x=year_freq_sorted.index, y=year_freq_sorted.values, marker='o', color='purple')
plt.title('Line Plot for Frequency of Games by Year')
plt.xlabel('Year')
plt.ylabel('Number of Games')
plt.grid(True)
plt.show()




#%%


#%%














#%%
# Calculate frequency of games by month
month_freq = data['month'].value_counts().sort_index()

plt.figure(figsize=(8, 8))
colors = sns.color_palette('coolwarm', len(month_freq))
plt.pie(
    month_freq.values, 
    labels=month_freq.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors,
    wedgeprops={'width': 0.4}  # This creates the "hole" for the donut effect
)
plt.title('Frequency of Games by Month', fontsize=16)
plt.show()




#%%



#%%


#%%%


#%%


# Extract day, month, and year from 'game_date_est'
data['game_date_est'] = pd.to_datetime(data['game_date_est'])
data['day'] = data['game_date_est'].dt.day
data['month'] = data['game_date_est'].dt.month
data['year'] = data['game_date_est'].dt.year
data['day_of_week'] = data['game_date_est'].dt.day_name()

# Display the updated dataset with extracted features
data.head()


#%%


# Compare average scores by day of the week
day_of_week_scores = data.groupby('day_of_week')[['pts_home', 'pts_away']].mean()

# Plot average scores by day of the week
plt.figure(figsize=(10, 6))
day_of_week_scores.plot(kind='bar', colormap='viridis')
plt.title('Average Home and Away Scores by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Points')
plt.xticks(rotation=45)
plt.show()

#%%
# Create a new column to indicate weekend vs weekday games
data['weekend'] = data['day_of_week'].isin(['Saturday', 'Sunday'])

# Analyze scores based on weekend/weekday
weekend_scores = data.groupby('weekend')[['pts_home', 'pts_away']].mean()

# Violin plot for home and away scores during weekend vs weekday games
plt.figure(figsize=(8, 6))
sns.violinplot(x='weekend', y='pts_home', data=data, palette='coolwarm', inner='quart')
sns.violinplot(x='weekend', y='pts_away', data=data, palette='coolwarm', inner='quart')
plt.title('Violin Plot: Home vs Away Scores on Weekend vs Weekday')
plt.xlabel('Weekend vs Weekday')
plt.ylabel('Points')
plt.show()


#%%
# Pairplot for weekend vs weekday games showing home and away scores
sns.pairplot(data, hue='weekend', vars=['pts_home', 'pts_away'], palette='coolwarm')
plt.title('Pairplot: Weekend vs Weekday Scores')
plt.show()


#%%
# Calculate the frequency of games by year
game_count_by_year = data.groupby('year').size()

# Plot number of games per year
plt.figure(figsize=(12, 6))
game_count_by_year.plot(kind='line', marker='o', color='b')
plt.title('Number of Games Played by Year')
plt.xlabel('Year')
plt.ylabel('Number of Games')
plt.grid(True)
plt.show()



#%%

# Calculate the frequency of games by month
game_count_by_month = data.groupby('month').size()

# Plot number of games per month
plt.figure(figsize=(10, 6))
game_count_by_month.plot(kind='bar', color='seagreen')
plt.title('Number of Games Played by Month')
plt.xlabel('Month')
plt.ylabel('Number of Games')
plt.xticks(rotation=45)
plt.show()


#%%

# Calculate average home and away scores by month
monthly_scores = data.groupby('month')[['pts_home', 'pts_away']].mean()

# Plot average home and away scores by month
plt.figure(figsize=(10, 6))
monthly_scores.plot(kind='line', marker='o', color=['orange', 'purple'])
plt.title('Average Home and Away Scores by Month')
plt.xlabel('Month')
plt.ylabel('Average Points')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#%%

# Calculate win rate for home teams by year
data['home_win'] = data['pts_home'] > data['pts_away']
win_rate_by_year = data.groupby('year')['home_win'].mean()

# Plot win rate by year
plt.figure(figsize=(12, 6))
win_rate_by_year.plot(kind='line', marker='o', color='blue')
plt.title('Home Team Win Rate by Year')
plt.xlabel('Year')
plt.ylabel('Win Rate')
plt.grid(True)
plt.show()


#%%%

# Calculate win/loss records
data['home_win'] = data['pts_home'] > data['pts_away']
data['away_win'] = data['pts_home'] < data['pts_away']

# Win/loss record by team (home games)
team_win_loss_home = data.groupby('team_nickname_home').agg(
    home_wins=('home_win', 'sum'),
    home_losses=('home_win', lambda x: (~x).sum())
).reset_index()

# Win/loss record by team (away games)
team_win_loss_away = data.groupby('team_nickname_home').agg(
    away_wins=('away_win', 'sum'),
    away_losses=('away_win', lambda x: (~x).sum())
).reset_index()

# Combine home and away records
team_win_loss = pd.merge(team_win_loss_home, team_win_loss_away, on='team_nickname_home', how='outer')
team_win_loss['total_wins'] = team_win_loss['home_wins'] + team_win_loss['away_wins']
team_win_loss['total_losses'] = team_win_loss['home_losses'] + team_win_loss['away_losses']
team_win_loss['win_loss_ratio'] = team_win_loss['total_wins'] / (team_win_loss['total_wins'] + team_win_loss['total_losses'])

team_win_loss = team_win_loss.sort_values(by='win_loss_ratio', ascending=False)
print(team_win_loss)


#%%

# Calculate average home and away points for each team by city
team_performance = data.groupby('team_city_name_home').agg(
    avg_home_points=('pts_home', 'mean'),
    avg_away_points=('pts_away', 'mean')
).reset_index()

# Plotting average points for each city
plt.figure(figsize=(14, 6))
sns.barplot(x='team_city_name_home', y='avg_home_points', data=team_performance, color='orange', label='Home')
sns.barplot(x='team_city_name_home', y='avg_away_points', data=team_performance, color='purple', label='Away')
plt.title('Average Home and Away Points by Team City')
plt.xlabel('Team City')
plt.ylabel('Average Points')
plt.xticks(rotation=90)
plt.legend()
plt.show()



#%%


# Pie chart of win/loss distribution for top 10 teams
team_win_loss = top_teams.set_index('team_nickname_home')['win_loss_ratio']
team_win_loss = team_win_loss / team_win_loss.sum()  # Normalize to create proportions

plt.figure(figsize=(8, 8))
team_win_loss.plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis', legend=False)
plt.title('Top 10 Performing Teams: Win/Loss Ratio Distribution')
plt.ylabel('')
plt.show()
#%%
# radar chart to check their perfomance 
import numpy as np
import matplotlib.pyplot as plt

# Define radar chart metrics (e.g., points, assists, rebounds)
metrics = ['Points', 'Assists', 'Rebounds', 'Steals', 'Blocks']
values = [80, 22, 15, 8, 4]  # Example team data

# Prepare the data for radar chart
angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
values += values[:1]  # Close the radar chart
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='orange', alpha=0.25)
ax.plot(angles, values, color='orange', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics)

plt.title('Team Performance Metrics')
plt.show()


#%%

# Group data by year and team for performance over time
team_performance_over_time = data.groupby(['year', 'team_nickname_home']).agg(
    avg_home_points=('pts_home', 'mean'),
    avg_away_points=('pts_away', 'mean')
).reset_index()

# Plotting team performance over time
plt.figure(figsize=(14, 8))
sns.lineplot(x='year', y='avg_home_points', hue='team_nickname_home', data=team_performance_over_time, marker='o')
sns.lineplot(x='year', y='avg_away_points', hue='team_nickname_home', data=team_performance_over_time, marker='o', linestyle='--')
plt.title('Team Performance Over Time (Average Home and Away Points)')
plt.xlabel('Year')
plt.ylabel('Average Points')
plt.legend(title='Teams')
plt.show()


#%%


#%%


#%%


#%%


#%%

#%%


#%%