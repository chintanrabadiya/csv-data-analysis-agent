# CSV Data Analysis Agent 📊

A Python-based intelligent agent that analyzes CSV datasets using pandas. Upload your CSV file and ask questions about your data!

## 🌟 Features

- **Load CSV files** with automatic error handling
- **Exploratory Data Analysis (EDA)** - comprehensive dataset overview
- **Summary Statistics** - mean, median, std, min, max for numerical columns
- **Missing Value Analysis** - identify and quantify missing data
- **Column Information** - detailed stats for any column
- **Natural Language Questions** - ask questions about your data in plain English
- **Performance Optimized** - caching mechanism for faster repeated queries

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/chintanrabadiya/csv-data-analysis-agent.git
cd csv-data-analysis-agent

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from csv_agent import CSVAnalysisAgent

# Initialize agent with a CSV file
agent = CSVAnalysisAgent('your_data.csv')

# Get basic information
info = agent.get_basic_info()
print(info)

# Get summary statistics
stats = agent.get_summary_statistics()
print(stats)

# Ask questions
answer = agent.answer_question("How many rows are there?")
print(answer)

# Perform full exploratory analysis
eda = agent.exploratory_analysis()
```

## 📖 Detailed Examples

### Example 1: Load and Explore a Dataset

```python
from csv_agent import CSVAnalysisAgent

# Load your CSV
agent = CSVAnalysisAgent('sales_data.csv')

# Preview the data
print(agent.preview_data(10))  # Show first 10 rows

# Get dataset information
info = agent.get_basic_info()
print(f"Dataset has {info['num_rows']} rows and {info['num_columns']} columns")
```

### Example 2: Analyze Missing Values

```python
# Check for missing values
missing = agent.get_missing_values()
print(missing)

# Output:
#           column  missing_count  missing_percentage
# 0          age             45               15.2
# 1       salary            12                4.1
```

### Example 3: Get Column Details

```python
# Analyze a specific column
col_info = agent.get_column_info('price')
print(col_info)

# Output:
# {
#     'name': 'price',
#     'dtype': 'float64',
#     'unique_values': 234,
#     'missing_values': 5,
#     'mean': 45.67,
#     'median': 39.99,
#     'std': 12.34,
#     'min': 10.00,
#     'max': 150.00
# }
```

### Example 4: Ask Questions

```python
# Natural language questions
questions = [
    "How many rows are there?",
    "How many columns are in the dataset?",
    "What are the column names?",
    "How many missing values are there?",
    "What is the shape of the dataset?"
]

for q in questions:
    print(f"Q: {q}")
    print(f"A: {agent.answer_question(q)}\n")
```

### Example 5: Complete EDA

```python
# Comprehensive exploratory analysis
eda = agent.exploratory_analysis()

# Access different parts
print("Basic Info:", eda['basic_info'])
print("Summary Stats:", eda['summary_statistics'])
print("Missing Values:", eda['missing_values'])
print("Numerical Columns:", eda['data_types']['numerical'])
print("Categorical Columns:", eda['data_types']['categorical'])
```

## 🔧 API Reference

### Class: `CSVAnalysisAgent`

#### Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `load_csv(csv_path, **kwargs)` | Load a CSV file | DataFrame |
| `get_basic_info()` | Get dataset overview | Dict |
| `get_summary_statistics()` | Generate summary stats | DataFrame |
| `get_missing_values()` | Analyze missing data | DataFrame |
| `get_column_info(column_name)` | Get column details | Dict |
| `answer_question(question)` | Answer NL questions | Any |
| `exploratory_analysis()` | Complete EDA | Dict |
| `preview_data(n=5)` | Preview first n rows | DataFrame |

## 🎯 Use Cases

1. **Quick Data Exploration** - Understand your dataset in seconds
2. **Data Quality Checks** - Identify missing values and data issues
3. **Automated Reporting** - Generate stats for reports automatically
4. **Educational Tool** - Learn data analysis step-by-step
5. **Data Pipeline Validation** - Verify data before processing

## 📊 Supported Questions

The agent can answer:
- "How many rows are there?"
- "How many columns are in the dataset?"
- "What are the column names?"
- "How many missing values are there?"
- "What is the shape of the dataset?"
- "What are the data types?"

## 🛠️ Requirements

- Python 3.7+
- pandas >= 1.3.0
- numpy >= 1.21.0

## 📝 Example Dataset

Try the agent with the included sample dataset:

```python
# Use the sample dataset
agent = CSVAnalysisAgent('examples/sample_data.csv')
agent.exploratory_analysis()
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution

- [ ] Add visualization capabilities (matplotlib/seaborn)
- [ ] Support for more file formats (Excel, JSON, Parquet)
- [ ] Advanced NLP for better question answering
- [ ] Statistical tests (t-test, ANOVA, chi-square)
- [ ] Data cleaning suggestions
- [ ] Export analysis reports (PDF, HTML)
- [ ] Integration with LLMs for smarter insights

## 🙏 Acknowledgments

- Built with [pandas](https://pandas.pydata.org/)
- Inspired by the data science community

## 📧 Contact

Chintan Rabadiya - [@chintanrabadiya](https://www.linkedin.com/in/chintan-rabadiya/)

Project Link: [git remote add origin https://github.com/chintanrabadiya/csv-data-analysis-agent.git]

## 🗺️ Roadmap

- [x] Basic CSV loading
- [x] Summary statistics
- [x] Missing value analysis
- [x] Question answering system
- [ ] Data visualization
- [ ] ML model recommendations
- [ ] Web interface
- [ ] REST API
- [ ] Docker support

---

**Made with ❤️ for the Data Science Community**
