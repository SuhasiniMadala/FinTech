import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

# Input
name = input("Enter NBA Player: ")
line = float(input(f"Enter O/U line for {name}: "))

# Player ID
all_players = players.get_players()
p_id = [p for p in all_players if p['full_name'].lower() == name.lower()][0]['id']

# Last 20 games data
log = playergamelog.PlayerGameLog(player_id=p_id, season='2025-26')
df = log.get_data_frames()[0].head(20)

# Home/Away Splits
df['is_home'] = df['MATCHUP'].str.contains('vs.')
home_avg = df[df['is_home']]['PTS'].mean()
away_avg = df[~df['is_home']]['PTS'].mean()

# FCS and Probability
pts = df['PTS'].astype(int)
cv = pts.std() / pts.mean()
fcs = (1 - cv) * 5  
prob = (pts > line).mean() * 100

# Report
print(f"{name.upper()} ANALYSIS")
print(f"Consistency Score: {fcs:.1f}/5")
print(f"Prob of Over {line}: {prob:.1f}%")
print(f"Home Avg: {home_avg:.1f} Vs. Away Avg: {away_avg:.1f}")

# Plot
sns.kdeplot(df[df['is_home']]['PTS'], fill=True, label='Home', color='blue')
sns.kdeplot(df[~df['is_home']]['PTS'], fill=True, label='Away', color='orange')
plt.axvline(line, color='red', linestyle='--')
plt.title(f"{name} Scoring Distribution")
plt.legend()
plt.show()
