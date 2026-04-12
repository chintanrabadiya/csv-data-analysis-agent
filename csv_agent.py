"""
CSV Data Analysis Agent
A pandas-based agent for analyzing CSV datasets and answering questions about data.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any
import os


class CSVAnalysisAgent:
    """
    An intelligent agent that loads CSV files and performs exploratory data analysis.
    """
    
    def __init__(self, csv_path: Optional[str] = None):
        """
        Initialize the CSV Analysis Agent.
        
        Args:
            csv_path (str, optional): Path to the CSV file to analyze
        """
        self.df: Optional[pd.DataFrame] = None
        self.csv_path: Optional[str] = csv_path
        self.analysis_cache: Dict[str, Any] = {}
        
        if csv_path:
            self.load_csv(csv_path)
    
    def load_csv(self, csv_path: str, **kwargs) -> pd.DataFrame:
        """
        Load a CSV file into a pandas DataFrame.
        
        Args:
            csv_path (str): Path to the CSV file
            **kwargs: Additional arguments to pass to pd.read_csv()
        
        Returns:
            pd.DataFrame: Loaded dataframe
        
        Raises:
            FileNotFoundError: If the CSV file doesn't exist
            Exception: If there's an error reading the CSV
        """
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        
        try:
            self.df = pd.read_csv(csv_path, **kwargs)
            self.csv_path = csv_path
            self.analysis_cache.clear()  # Clear cache when new data is loaded
            print(f"✓ Successfully loaded CSV: {csv_path}")
            print(f"  Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
            return self.df
        except Exception as e:
            raise Exception(f"Error loading CSV: {str(e)}")
    
    def get_basic_info(self) -> Dict[str, Any]:
        """
        Get basic information about the dataset.
        
        Returns:
            Dict containing dataset information
        """
        if self.df is None:
            raise ValueError("No dataset loaded. Please load a CSV first.")
        
        if 'basic_info' in self.analysis_cache:
            return self.analysis_cache['basic_info']
        
        info = {
            'file_path': self.csv_path,
            'num_rows': len(self.df),
            'num_columns': len(self.df.columns),
            'column_names': self.df.columns.tolist(),
            'data_types': self.df.dtypes.to_dict(),
            'memory_usage': f"{self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"
        }
        
        self.analysis_cache['basic_info'] = info
        return info
    
    def get_summary_statistics(self) -> pd.DataFrame:
        """
        Generate summary statistics for numerical columns.
        
        Returns:
            pd.DataFrame: Summary statistics
        """
        if self.df is None:
            raise ValueError("No dataset loaded. Please load a CSV first.")
        
        if 'summary_stats' in self.analysis_cache:
            return self.analysis_cache['summary_stats']
        
        stats = self.df.describe(include='all').T
        self.analysis_cache['summary_stats'] = stats
        return stats
    
    def get_missing_values(self) -> pd.DataFrame:
        """
        Analyze missing values in the dataset.
        
        Returns:
            pd.DataFrame: Missing value analysis
        """
        if self.df is None:
            raise ValueError("No dataset loaded. Please load a CSV first.")
        
        if 'missing_values' in self.analysis_cache:
            return self.analysis_cache['missing_values']
        
        missing = pd.DataFrame({
            'column': self.df.columns,
            'missing_count': self.df.isnull().sum().values,
            'missing_percentage': (self.df.isnull().sum() / len(self.df) * 100).values
        })
        missing = missing[missing['missing_count'] > 0].sort_values('missing_count', ascending=False)
        
        self.analysis_cache['missing_values'] = missing
        return missing
    
    def get_column_info(self, column_name: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific column.
        
        Args:
            column_name (str): Name of the column
        
        Returns:
            Dict containing column information
        """
        if self.df is None:
            raise ValueError("No dataset loaded. Please load a CSV first.")
        
        if column_name not in self.df.columns:
            raise ValueError(f"Column '{column_name}' not found in dataset")
        
        col_data = self.df[column_name]
        
        info = {
            'name': column_name,
            'dtype': str(col_data.dtype),
            'unique_values': col_data.nunique(),
            'missing_values': col_data.isnull().sum(),
            'missing_percentage': f"{(col_data.isnull().sum() / len(col_data) * 100):.2f}%"
        }
        
        # Add statistics for numerical columns
        if pd.api.types.is_numeric_dtype(col_data):
            info.update({
                'mean': col_data.mean(),
                'median': col_data.median(),
                'std': col_data.std(),
                'min': col_data.min(),
                'max': col_data.max()
            })
        
        # Add value counts for categorical columns
        if col_data.nunique() < 20:  # Show value counts if less than 20 unique values
            info['value_counts'] = col_data.value_counts().to_dict()
        
        return info
    
    def answer_question(self, question: str) -> Any:
        """
        Answer simple questions about the dataset.
        
        Args:
            question (str): Natural language question about the data
        
        Returns:
            Answer to the question
        """
        if self.df is None:
            raise ValueError("No dataset loaded. Please load a CSV first.")
        
        question_lower = question.lower()
        
        # Question patterns
        if 'how many rows' in question_lower or 'number of rows' in question_lower:
            return f"The dataset has {len(self.df)} rows."
        
        elif 'how many columns' in question_lower or 'number of columns' in question_lower:
            return f"The dataset has {len(self.df.columns)} columns."
        
        elif 'column names' in question_lower or 'what columns' in question_lower:
            return f"Columns: {', '.join(self.df.columns.tolist())}"
        
        elif 'missing values' in question_lower or 'null values' in question_lower:
            total_missing = self.df.isnull().sum().sum()
            return f"Total missing values: {total_missing}"
        
        elif 'data types' in question_lower:
            return self.df.dtypes.to_dict()
        
        elif 'shape' in question_lower:
            return f"Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns"
        
        else:
            return "I couldn't understand that question. Try asking about: rows, columns, missing values, data types, or shape."
    
    def exploratory_analysis(self) -> Dict[str, Any]:
        """
        Perform comprehensive exploratory data analysis.
        
        Returns:
            Dict containing complete EDA results
        """
        if self.df is None:
            raise ValueError("No dataset loaded. Please load a CSV first.")
        
        eda = {
            'basic_info': self.get_basic_info(),
            'summary_statistics': self.get_summary_statistics(),
            'missing_values': self.get_missing_values(),
            'data_types': {
                'numerical': self.df.select_dtypes(include=[np.number]).columns.tolist(),
                'categorical': self.df.select_dtypes(include=['object']).columns.tolist(),
                'datetime': self.df.select_dtypes(include=['datetime']).columns.tolist()
            },
            'correlations': self.df.select_dtypes(include=[np.number]).corr() if len(self.df.select_dtypes(include=[np.number]).columns) > 1 else None
        }
        
        return eda
    
    def preview_data(self, n: int = 5) -> pd.DataFrame:
        """
        Preview the first n rows of the dataset.
        
        Args:
            n (int): Number of rows to preview
        
        Returns:
            pd.DataFrame: First n rows
        """
        if self.df is None:
            raise ValueError("No dataset loaded. Please load a CSV first.")
        
        return self.df.head(n)


def main():
    """
    Example usage of the CSV Analysis Agent.
    """
    print("=" * 60)
    print("CSV Data Analysis Agent")
    print("=" * 60)
    
    # Example: Create agent and load a sample CSV
    # agent = CSVAnalysisAgent('path/to/your/data.csv')
    
    # Or load later
    agent = CSVAnalysisAgent()
    
    print("\nTo use this agent:")
    print("1. agent = CSVAnalysisAgent('your_file.csv')")
    print("2. agent.get_basic_info()")
    print("3. agent.get_summary_statistics()")
    print("4. agent.answer_question('How many rows are there?')")
    print("5. agent.exploratory_analysis()")
    

if __name__ == "__main__":
    main()