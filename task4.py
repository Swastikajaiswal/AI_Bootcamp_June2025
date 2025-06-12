import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df_csv = pd.read_csv('LoksabhaData.csv')

# Clean column names
df_csv.columns = df_csv.columns.str.strip()

# Print actual column names to verify
print(df_csv.columns.tolist())

# Plot using exact column names
plt.figure(figsize=(12, 6))
plt.bar(df_csv['States and Union Territories'], df_csv['No. Of Phases'], color='#FF9933')
plt.title('Number of Election Phases by State/UT')
plt.xlabel('States and Union Territories')
plt.ylabel('Number of Phases')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
