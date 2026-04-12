# Contributing to CSV Data Analysis Agent

Thank you for considering contributing to CSV Data Analysis Agent! 🎉

## 🚀 How to Contribute

### 1. Fork the Repository
Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/csv-data-analysis-agent.git
cd csv-data-analysis-agent
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
- Write clean, readable code
- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Include type hints where appropriate

### 5. Test Your Changes
```bash
# Run the test suite
python tests.py

# Test the example
python example.py
```

### 6. Commit Your Changes
```bash
git add .
git commit -m "Add: Description of your changes"
```

**Commit Message Format:**
- `Add:` for new features
- `Fix:` for bug fixes
- `Update:` for updates to existing features
- `Docs:` for documentation changes
- `Test:` for test-related changes

### 7. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 8. Create a Pull Request
Go to the original repository and click "New Pull Request"

## 📝 Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include screenshots for UI changes
- Ensure all tests pass
- Update documentation if needed

## 🐛 Reporting Bugs

Create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Error messages/stack traces

## 💡 Feature Requests

We welcome feature requests! Please:
- Check if the feature already exists
- Describe the use case
- Explain why it would be valuable
- Suggest implementation if possible

## 🎯 Areas for Contribution

### Beginner-Friendly
- [ ] Fix typos in documentation
- [ ] Add more examples to README
- [ ] Improve error messages
- [ ] Add more test cases
- [ ] Add docstring examples

### Intermediate
- [ ] Add data visualization (matplotlib/seaborn)
- [ ] Support Excel files (.xlsx)
- [ ] Add more statistical functions
- [ ] Improve question answering
- [ ] Add data cleaning suggestions

### Advanced
- [ ] Build a web interface (Flask/Streamlit)
- [ ] Add ML model recommendations
- [ ] Create REST API
- [ ] Integration with LLMs
- [ ] Performance optimization

## 🔍 Code Style

We follow PEP 8 with these additions:
- Maximum line length: 100 characters
- Use type hints
- Write descriptive docstrings
- Use meaningful variable names

### Example:
```python
def get_column_info(self, column_name: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific column.
    
    Args:
        column_name (str): Name of the column to analyze
    
    Returns:
        Dict[str, Any]: Dictionary containing column statistics
    
    Raises:
        ValueError: If column doesn't exist in dataset
    
    Example:
        >>> agent = CSVAnalysisAgent('data.csv')
        >>> info = agent.get_column_info('age')
        >>> print(info['mean'])
    """
    # Implementation here
```

## ✅ Testing

All contributions should include tests:

```python
def test_new_feature(self):
    """Test the new feature works correctly."""
    # Arrange
    agent = CSVAnalysisAgent(self.test_csv)
    
    # Act
    result = agent.new_feature()
    
    # Assert
    self.assertEqual(result, expected_value)
```

## 📚 Documentation

Update documentation when:
- Adding new features
- Changing existing functionality
- Adding new dependencies
- Fixing bugs

## 🤝 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy toward others

### Not Acceptable
- Harassment or discrimination
- Trolling or insulting comments
- Publishing private information
- Unprofessional conduct

## 💬 Questions?

Feel free to:
- Open an issue for discussion
- Ask in pull request comments
- Contact maintainers

## 🏆 Recognition

Contributors will be:
- Listed in the README
- Credited in release notes
- Thanked in the community

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉