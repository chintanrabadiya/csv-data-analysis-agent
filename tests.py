"""
Unit tests for CSV Analysis Agent
"""

import unittest
import pandas as pd
import numpy as np
import os
import tempfile
from csv_agent import CSVAnalysisAgent


class TestCSVAnalysisAgent(unittest.TestCase):
    """Test cases for CSV Analysis Agent"""
    
    @classmethod
    def setUpClass(cls):
        """Create a temporary CSV file for testing."""
        cls.temp_dir = tempfile.mkdtemp()
        cls.test_csv = os.path.join(cls.temp_dir, 'test_data.csv')
        
        # Create test dataset
        np.random.seed(42)
        test_data = {
            'id': range(1, 51),
            'age': np.random.randint(20, 60, 50),
            'salary': np.random.randint(30000, 100000, 50),
            'department': np.random.choice(['IT', 'HR', 'Sales'], 50),
            'score': np.random.uniform(60, 100, 50).round(2)
        }
        
        df = pd.DataFrame(test_data)
        # Add some missing values
        df.loc[0:4, 'salary'] = np.nan
        df.to_csv(cls.test_csv, index=False)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up temporary files."""
        if os.path.exists(cls.test_csv):
            os.remove(cls.test_csv)
        os.rmdir(cls.temp_dir)
    
    def setUp(self):
        """Initialize agent before each test."""
        self.agent = CSVAnalysisAgent(self.test_csv)
    
    def test_load_csv(self):
        """Test CSV loading."""
        self.assertIsNotNone(self.agent.df)
        self.assertEqual(len(self.agent.df), 50)
        self.assertEqual(len(self.agent.df.columns), 5)
    
    def test_load_csv_file_not_found(self):
        """Test loading non-existent file."""
        agent = CSVAnalysisAgent()
        with self.assertRaises(FileNotFoundError):
            agent.load_csv('nonexistent_file.csv')
    
    def test_get_basic_info(self):
        """Test basic information retrieval."""
        info = self.agent.get_basic_info()
        
        self.assertEqual(info['num_rows'], 50)
        self.assertEqual(info['num_columns'], 5)
        self.assertIn('id', info['column_names'])
        self.assertIn('age', info['column_names'])
    
    def test_get_summary_statistics(self):
        """Test summary statistics generation."""
        stats = self.agent.get_summary_statistics()
        
        self.assertIsInstance(stats, pd.DataFrame)
        self.assertIn('age', stats.index)
        self.assertIn('salary', stats.index)
    
    def test_get_missing_values(self):
        """Test missing values analysis."""
        missing = self.agent.get_missing_values()
        
        self.assertIsInstance(missing, pd.DataFrame)
        # We added 5 missing values in salary
        salary_missing = missing[missing['column'] == 'salary']
        if len(salary_missing) > 0:
            self.assertEqual(salary_missing.iloc[0]['missing_count'], 5)
    
    def test_get_column_info(self):
        """Test column information retrieval."""
        col_info = self.agent.get_column_info('age')
        
        self.assertEqual(col_info['name'], 'age')
        self.assertIn('dtype', col_info)
        self.assertIn('unique_values', col_info)
        self.assertIn('mean', col_info)  # Age is numerical
    
    def test_get_column_info_invalid(self):
        """Test column info with invalid column name."""
        with self.assertRaises(ValueError):
            self.agent.get_column_info('nonexistent_column')
    
    def test_answer_question_rows(self):
        """Test question about number of rows."""
        answer = self.agent.answer_question("How many rows are there?")
        self.assertIn("50", str(answer))
    
    def test_answer_question_columns(self):
        """Test question about number of columns."""
        answer = self.agent.answer_question("How many columns?")
        self.assertIn("5", str(answer))
    
    def test_answer_question_column_names(self):
        """Test question about column names."""
        answer = self.agent.answer_question("What are the column names?")
        self.assertIn("id", answer)
        self.assertIn("age", answer)
    
    def test_answer_question_unknown(self):
        """Test unknown question."""
        answer = self.agent.answer_question("Tell me a joke")
        self.assertIn("couldn't understand", answer)
    
    def test_exploratory_analysis(self):
        """Test comprehensive EDA."""
        eda = self.agent.exploratory_analysis()
        
        self.assertIn('basic_info', eda)
        self.assertIn('summary_statistics', eda)
        self.assertIn('missing_values', eda)
        self.assertIn('data_types', eda)
        
        # Check data types categorization
        self.assertIn('numerical', eda['data_types'])
        self.assertIn('categorical', eda['data_types'])
    
    def test_preview_data(self):
        """Test data preview."""
        preview = self.agent.preview_data(5)
        
        self.assertEqual(len(preview), 5)
        self.assertIsInstance(preview, pd.DataFrame)
    
    def test_caching(self):
        """Test that analysis results are cached."""
        # First call
        info1 = self.agent.get_basic_info()
        
        # Second call should use cache
        info2 = self.agent.get_basic_info()
        
        self.assertEqual(info1, info2)
        self.assertIn('basic_info', self.agent.analysis_cache)
    
    def test_no_dataset_loaded(self):
        """Test operations without loaded dataset."""
        agent = CSVAnalysisAgent()
        
        with self.assertRaises(ValueError):
            agent.get_basic_info()
        
        with self.assertRaises(ValueError):
            agent.get_summary_statistics()


def run_tests():
    """Run all tests."""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == '__main__':
    run_tests()