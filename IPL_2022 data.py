#######################################################################################
#                                IPL 2022 DATA ANALYSIS                               #
#                                Date: 08th February 2025                             #
#######################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2022.csv")

# Display basic information
df.info()
df.isnull().sum()
df.describe()

print(df.duplicated().sum())
print(df.isnull().sum())

print(df.drop_duplicates().dropna())
df['player_of_the_match'].fillna('unknown', inplace=True)

sns.set_style("darkgrid")

# ==================================================================================== #
#                            1.  Plot bar chart of matches won per team
# ==================================================================================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2022.csv")
team_wins = df['match_winner'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=team_wins.index, y=team_wins.values, palette="viridis")
plt.xticks(rotation=45, fontsize=12, fontweight='bold', color='darkblue')
plt.xlabel("Team", fontsize=14, fontweight='bold', color='darkred')
plt.ylabel("Matches Won", fontsize=14, fontweight='bold', color='darkred')
plt.title("1. IPL 2022: Matches Won by Each Team", fontsize=16, fontweight='bold', color='black')
plt.show()


# ==================================================================================== #
#                           2. Top scorers bar chart
# ==================================================================================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2022.csv")
top_scorers = df.groupby("top_scorer")["highscore"].max().nlargest(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_scorers.index, y=top_scorers.values, palette="coolwarm")
plt.xticks(rotation=45, fontsize=12, fontweight='bold', color='darkblue')
plt.xlabel("Player", fontsize=14, fontweight='bold', color='darkred')
plt.ylabel("Highest Score", fontsize=14, fontweight='bold', color='darkred')
plt.title("2. Top 10 Highest Scores in IPL 2022", fontsize=16, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                            3. Toss decision analysis
# ==================================================================================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2022.csv")
toss_decisions = df['toss_decision'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(toss_decisions, labels=toss_decisions.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'])
plt.title("3. Toss Decisions: Bat vs Bowl", fontsize=16, fontweight='bold', color='black')
plt.show()


# ==================================================================================== #
#                             4.  Matches per venue
# ==================================================================================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2022.csv")
venue_counts = df['venue'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=venue_counts.index, y=venue_counts.values, palette="magma")
plt.xticks(rotation=90, fontsize=12, fontweight='bold', color='darkblue')
plt.xlabel("Venue", fontsize=14, fontweight='bold', color='darkred')
plt.ylabel("Matches Played", fontsize=14, fontweight='bold', color='darkred')
plt.title("4. IPL 2022: Matches Played at Each Venue", fontsize=16, fontweight='bold', color='black')
plt.show()


# ==================================================================================== #
#                            5.  Runs distribution
# ==================================================================================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2022.csv")
plt.figure(figsize=(8, 6))
sns.histplot(df['first_ings_score'], bins=20, kde=True, color='blue')
plt.xlabel("First Innings Score", fontsize=14, fontweight='bold', color='darkred')
plt.ylabel("Frequency", fontsize=14, fontweight='bold', color='darkred')
plt.title("5. Distribution of First Innings Scores", fontsize=16, fontweight='bold', color='black')
plt.show()


# ==================================================================================== #
#                           6.  Win by runs analysis
# ==================================================================================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2022.csv")
plt.figure(figsize=(10, 6))
sns.histplot(df['won_by'], bins=15, kde=True, color='green')
plt.xlabel("Win by Runs", fontsize=14, fontweight='bold', color='darkred')
plt.ylabel("Frequency", fontsize=14, fontweight='bold', color='darkred')
plt.title("6. Win Margin (by Runs) Distribution", fontsize=16, fontweight='bold', color='black')
plt.show()

# ==================================================================================== #
#                            7.  First innings vs second innings scores
# ==================================================================================== #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2022.csv")
plt.figure(figsize=(10, 6))
sns.lineplot(x=df.index, y=df['first_ings_score'], label="First Innings Score", marker="o", color='blue')
sns.lineplot(x=df.index, y=df['second_ings_score'], label="Second Innings Score", marker="s", color='red')
plt.xlabel("Match Index", fontsize=14, fontweight='bold', color='darkred')
plt.ylabel("Runs", fontsize=14, fontweight='bold', color='darkred')
plt.title("10. First vs Second Innings Scores", fontsize=16, fontweight='bold', color='black')
plt.legend()
plt.show()

# ==================================================================================== #
#                                 END OF ANALYSIS                                     #
# ==================================================================================== #