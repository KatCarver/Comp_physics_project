import pandas as pd

df = pd.read_csv('lidar_data.txt', delimiter='\t', skiprows=2)

# Display the DataFrame
print(df)