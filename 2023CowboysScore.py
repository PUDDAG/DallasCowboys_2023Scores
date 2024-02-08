#Importing the needed Packages
import pandas as pd #Data Package
import matplotlib.pyplot as plt #Graphing
import seaborn as sns #statistical graphics 

#Dallas Cowboys Season Result Data
data = {
    'Date': ['Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week8', 'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week16', 'Week17', 'Week 18', 'Wild-Card'],
    'Opponent': ['Giants', 'Jets', 'Cardinals', 'Patroits', '49ners', 'Chargers', 'Rams', 'Eagles', 'Giants', 'Panthers', 'Commanders', 'Seahawks', 'Eagles', 'Bills', 'Dolphins', 'Lions', 'Commanders', 'Packers'],
    'Result': ['W', 'W', 'L', 'W', 'L', 'W', 'W', 'L', 'W', 'W', 'W', 'W', 'W', 'L', 'L', 'W', 'W', 'L'],
    'Dallas_Score': [40, 30, 16, 38, 10, 20, 43, 23, 49, 33, 45, 41, 33, 10, 20, 20, 38, 16,],
    'Opponent_Score': [0, 10, 28, 3, 42, 17, 20, 28, 17, 10, 10, 35, 13, 31, 22, 19, 10, 48],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the data
print(df)

#Creatinf the function
def analyze_data():
    # Summary statistics
    summary_stats = df.describe()

    # Visualization
    plt.figure(figsize=(20, 6))

    # Line plot for Dallas Cowboys scores
    sns.lineplot(x='Date', y='Dallas_Score', data=df, marker='o', label='Dallas Cowboys')

    # Line plot for Opponent scores
    sns.lineplot(x='Date', y='Opponent_Score', data=df, marker='o', label='Opponent', linestyle='dashed')

    # Annotate each data point with its value
    for i, row in df.iterrows():
        plt.annotate(row['Dallas_Score'], (row['Date'], row['Dallas_Score']), textcoords="offset points", xytext=(0, 5), ha='center')
        plt.annotate(row['Opponent_Score'], (row['Date'], row['Opponent_Score']), textcoords="offset points", xytext=(0, -15), ha='center')

    plt.title('Dallas Cowboys Game Scores vs. Opponent Over Time')
    plt.xlabel('Date')
    plt.ylabel('Score')
    plt.legend()
    plt.show()

   # Return summary statistics
    return summary_stats

# Run the analysis
summary_statistics = analyze_data()
# Print summary statistics outside the function
print("\nSummary Statistics:")
print(summary_statistics)


# Run The Program
analyze_data()
