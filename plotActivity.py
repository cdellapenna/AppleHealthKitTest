import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# create element tree object
tree = ET.parse('export.xml') 
# for every health record, extract the attributes
root = tree.getroot()

# Extracting data and creating a DataFrame
data = []
for activity in root.findall('ActivitySummary'):
    data.append(activity.attrib)

df = pd.DataFrame(data)

# Convert dateComponents to datetime
df['dateComponents'] = pd.to_datetime(df['dateComponents'])

# Convert relevant columns to numeric type for plotting
numeric_cols = ['activeEnergyBurned', 'appleExerciseTime', 'appleStandHours']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

plt.figure(figsize=(10, 6))
plt.plot(df['dateComponents'], df['activeEnergyBurned'], marker='o', linestyle='-', color='b')
plt.title('Active Energy Burned Over Time')
plt.xlabel('Date')
plt.ylabel('Active Energy Burned (Cal)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
