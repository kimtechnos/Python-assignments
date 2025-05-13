# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Task 1: Load and Explore the Dataset
def load_and_explore_data():
    try:
        # Load the Iris dataset
        iris = load_iris()
        
        # Create a DataFrame
        iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        iris_df['species'] = iris.target
        iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
        
        # Display the first few rows
        print("First 5 rows of the dataset:")
        print(iris_df.head())
        print("\n")
        
        # Explore data structure
        print("Dataset information:")
        print(iris_df.info())
        print("\n")
        
        # Check for missing values
        print("Missing values per column:")
        print(iris_df.isnull().sum())
        print("\n")
        
        # Since Iris dataset is clean, we'll demonstrate cleaning anyway
        # (Normally you'd only do this if there were missing values)
        cleaned_df = iris_df.dropna()  # Would drop rows with missing values if any existed
        
        return cleaned_df
    
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

# Task 2: Basic Data Analysis
def perform_data_analysis(df):
    try:
        # Basic statistics
        print("Basic statistics for numerical columns:")
        print(df.describe())
        print("\n")
        
        # Group by species and calculate means
        print("Mean values by species:")
        species_means = df.groupby('species').mean()
        print(species_means)
        print("\n")
        
        # Interesting finding
        print("Interesting finding:")
        print("Setosa has significantly smaller petal dimensions compared to other species.")
        print("\n")
        
        return species_means
    
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return None

# Task 3: Data Visualization
def create_visualizations(df, species_means):
    try:
        # Set style for better looking plots
        sns.set(style="whitegrid")
        
        # 1. Line chart (simulating trends over time - we'll use index as pseudo-time)
        plt.figure(figsize=(10, 6))
        df['sepal length (cm)'].plot(title='Sepal Length Trend (by index)')
        plt.xlabel('Index (simulated time)')
        plt.ylabel('Sepal Length (cm)')
        plt.show()
        
        # 2. Bar chart (average sepal length by species)
        plt.figure(figsize=(10, 6))
        species_means['sepal length (cm)'].plot(kind='bar', color=['blue', 'green', 'red'])
        plt.title('Average Sepal Length by Species')
        plt.xlabel('Species')
        plt.ylabel('Average Sepal Length (cm)')
        plt.xticks(rotation=0)
        plt.show()
        
        # 3. Histogram (distribution of petal length)
        plt.figure(figsize=(10, 6))
        df['petal length (cm)'].plot(kind='hist', bins=20, edgecolor='black')
        plt.title('Distribution of Petal Length')
        plt.xlabel('Petal Length (cm)')
        plt.ylabel('Frequency')
        plt.show()
        
        # 4. Scatter plot (sepal length vs petal length)
        plt.figure(figsize=(10, 6))
        colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
        for species, group in df.groupby('species'):
            plt.scatter(group['sepal length (cm)'], group['petal length (cm)'], 
                        color=colors[species], label=species)
        plt.title('Sepal Length vs Petal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend()
        plt.show()
        
        # Bonus: Pair plot using seaborn
        print("Bonus: Pair plot showing all variable relationships")
        sns.pairplot(df, hue='species', height=2.5)
        plt.show()
        
    except Exception as e:
        print(f"An error occurred during visualization: {e}")

# Main execution
if __name__ == "__main__":
    print("=== Data Analysis with Pandas and Visualization with Matplotlib ===")
    print("Task 1: Loading and exploring the Iris dataset\n")
    iris_df = load_and_explore_data()
    
    if iris_df is not None:
        print("\nTask 2: Performing basic data analysis\n")
        species_means = perform_data_analysis(iris_df)
        
        if species_means is not None:
            print("\nTask 3: Creating visualizations\n")
            create_visualizations(iris_df, species_means)