"""
Example script demonstrating the CSV Analysis Agent
"""

from csv_agent import CSVAnalysisAgent
import pandas as pd
import numpy as np


def create_sample_data():
    """Create a sample CSV file for demonstration."""
    np.random.seed(42)
    
    data = {
        'customer_id': range(1, 101),
        'age': np.random.randint(18, 70, 100),
        'income': np.random.randint(30000, 120000, 100),
        'purchase_amount': np.random.uniform(10, 500, 100).round(2),
        'category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], 100),
        'satisfaction': np.random.choice(['High', 'Medium', 'Low', None], 100, p=[0.4, 0.3, 0.2, 0.1])
    }
    
    df = pd.DataFrame(data)
    df.to_csv('examples/sample_data.csv', index=False)
    print("✓ Sample dataset created: examples/sample_data.csv")
    return df


def demo_agent():
    """Demonstrate all features of the CSV Analysis Agent."""
    
    print("=" * 70)
    print("CSV Data Analysis Agent - Demo")
    print("=" * 70)
    
    # Create sample data
    import os
    os.makedirs('examples', exist_ok=True)
    create_sample_data()
    
    print("\n" + "=" * 70)
    print("STEP 1: Initialize Agent and Load CSV")
    print("=" * 70)
    
    agent = CSVAnalysisAgent('examples/sample_data.csv')
    
    print("\n" + "=" * 70)
    print("STEP 2: Preview the Data")
    print("=" * 70)
    print(agent.preview_data(5))
    
    print("\n" + "=" * 70)
    print("STEP 3: Get Basic Information")
    print("=" * 70)
    info = agent.get_basic_info()
    for key, value in info.items():
        print(f"{key}: {value}")
    
    print("\n" + "=" * 70)
    print("STEP 4: Summary Statistics")
    print("=" * 70)
    print(agent.get_summary_statistics())
    
    print("\n" + "=" * 70)
    print("STEP 5: Missing Values Analysis")
    print("=" * 70)
    missing = agent.get_missing_values()
    if len(missing) > 0:
        print(missing)
    else:
        print("No missing values found!")
    
    print("\n" + "=" * 70)
    print("STEP 6: Analyze Specific Column")
    print("=" * 70)
    col_info = agent.get_column_info('age')
    for key, value in col_info.items():
        print(f"{key}: {value}")
    
    print("\n" + "=" * 70)
    print("STEP 7: Ask Natural Language Questions")
    print("=" * 70)
    
    questions = [
        "How many rows are there?",
        "How many columns are in the dataset?",
        "What are the column names?",
        "How many missing values are there?",
        "What is the shape of the dataset?"
    ]
    
    for question in questions:
        answer = agent.answer_question(question)
        print(f"\nQ: {question}")
        print(f"A: {answer}")
    
    print("\n" + "=" * 70)
    print("STEP 8: Complete Exploratory Data Analysis")
    print("=" * 70)
    eda = agent.exploratory_analysis()
    
    print("\nNumerical Columns:", eda['data_types']['numerical'])
    print("Categorical Columns:", eda['data_types']['categorical'])
    
    print("\n" + "=" * 70)
    print("Demo Complete!")
    print("=" * 70)
    print("\nTry it yourself:")
    print("  agent = CSVAnalysisAgent('your_file.csv')")
    print("  agent.exploratory_analysis()")


if __name__ == "__main__":
    demo_agent()