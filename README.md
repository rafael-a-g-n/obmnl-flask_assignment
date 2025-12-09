# 💰 Flask Transaction Manager

A full-featured web application for managing financial transactions with CRUD operations, built with Flask and Python.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Code Quality](https://img.shields.io/badge/pylint-10.00%2F10-brightgreen.svg)](https://www.pylint.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📋 Table of Contents

- [Features](#-features)
- [Technologies](#-technologies)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Skills Demonstrated](#-skills-demonstrated)
- [Development](#-development)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [Credits](#-credits)
- [License](#-license)

## ✨ Features

### Core Functionality
- **Create** - Add new financial transactions with date and amount
- **Read** - View all transactions in a clean, organized table
- **Update** - Edit existing transaction details
- **Delete** - Remove unwanted transactions
- **Search** - Filter transactions by amount range
- **Balance** - Calculate and display total balance

### Technical Features
- ✅ Input validation and error handling
- ✅ RESTful API design
- ✅ Responsive HTML templates
- ✅ Custom error handlers (400, 404, 500)
- ✅ Smart number formatting (100 vs 100.0)
- ✅ PEP 8 compliant code
- ✅ 10/10 Pylint score
- ✅ Comprehensive docstrings

### Transaction List
View all your transactions at a glance with easy access to edit and delete operations.

### Add Transaction
Simple form to add new transactions with date and amount validation.

### Search Functionality
Filter transactions by specifying minimum and maximum amount ranges.

### Balance Calculation
Get instant total balance calculations across all transactions.

## 🛠 Technologies

### Backend
- **Python 3.13** - Core programming language
- **Flask 3.0** - Lightweight WSGI web application framework
- **Jinja2** - Template engine for dynamic HTML rendering

### Development Tools
- **Virtual Environment** - Isolated Python environment management
- **Pylint** - Static code analysis for quality assurance
- **Flake8** - Style guide enforcement
- **Git** - Version control

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Styling (via templates)
- **HTTP Methods** - GET, POST for form handling

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/rafael-a-g-n/obmnl-flask_assignment.git
   cd obmnl-flask_assignment
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   
   **Windows:**
   ```bash
   source venv/Scripts/activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install flask
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   
   Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

## 🚀 Usage

### Adding a Transaction
1. Navigate to `/add` or click "Add Transaction"
2. Enter the transaction date (YYYY-MM-DD format)
3. Enter the amount (positive or negative)
4. Submit the form

### Editing a Transaction
1. Click "Edit" next to any transaction
2. Modify the date or amount
3. Save changes

### Deleting a Transaction
1. Click "Delete" next to the transaction you want to remove
2. Transaction is immediately removed from the list

### Searching Transactions
1. Navigate to `/search`
2. Enter minimum and maximum amount values
3. View filtered results

### Viewing Balance
- Navigate to `/balance` to see the total balance of all transactions

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Display all transactions |
| `GET` | `/add` | Show add transaction form |
| `POST` | `/add` | Create new transaction |
| `GET` | `/edit/<id>` | Show edit form for transaction |
| `POST` | `/edit/<id>` | Update existing transaction |
| `GET` | `/delete/<id>` | Delete transaction by ID |
| `GET` | `/search` | Show search form |
| `POST` | `/search` | Filter transactions by amount range |
| `GET` | `/balance` | Display total balance |

### Response Codes
- `200` - Success
- `400` - Bad Request (validation errors)
- `404` - Not Found (transaction doesn't exist)
- `500` - Internal Server Error

## 📁 Project Structure

```
obmnl-flask_assignment/
│
├── app.py                  # Main Flask application
├── templates/              # HTML templates
│   ├── transactions.html   # Main transaction list view
│   ├── form.html          # Add transaction form
│   ├── edit.html          # Edit transaction form
│   └── search.html        # Search form
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
└── venv/                  # Virtual environment (not committed)
```

## 💡 Skills Demonstrated

### Backend Development
- RESTful API design and implementation
- Form data processing and validation
- Error handling and exception management
- Route parameter handling
- HTTP methods (GET, POST)
- Template rendering with dynamic data

### Python Programming
- List comprehensions for data filtering
- Generator expressions for efficient iteration
- Exception handling with specific exception types
- Type conversion and validation
- Docstring documentation
- PEP 8 style compliance

### Software Engineering
- Clean code principles
- DRY (Don't Repeat Yourself) methodology
- Separation of concerns
- Input validation and sanitization
- Error handling best practices
- Code documentation

### Web Development
- Flask framework mastery
- URL routing and dynamic URLs
- Template inheritance (Jinja2)
- Form handling
- Redirect flow control
- Status code management

### Code Quality
- Static code analysis (Pylint 10/10)
- PEP 8 compliance
- Comprehensive error handling
- Function documentation
- Code refactoring for maintainability

## 🔧 Development

### Running in Debug Mode
The application runs in debug mode by default for development:
```python
if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
```

### Code Quality Checks

**Run Pylint:**
```bash
pylint app.py
```

**Run Flake8:**
```bash
flake8 app.py
```

### Environment Variables
The application currently uses in-memory storage. For production, consider:
- Database integration (SQLite, PostgreSQL)
- Environment-based configuration
- Secret key management
- Production WSGI server (Gunicorn, uWSGI)

## 🧪 Testing

### Manual Testing
1. Test CRUD operations through the web interface
2. Verify validation by submitting empty/invalid forms
3. Test edge cases (negative amounts, future dates)
4. Verify error responses (404, 400, 500)

### Future Improvements
- Unit tests with pytest
- Integration tests
- Test coverage reporting
- Automated CI/CD pipeline

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 style guide
- Maintain Pylint score of 10/10
- Add docstrings to all functions
- Include error handling
- Write meaningful commit messages

## 👏 Credits

### Original Authors
This project is forked from the [IBM Developer Skills Network](https://github.com/ibm-developer-skills-network) Flask assignment template. Special thanks to the IBM team for providing the foundational structure and learning materials.

### Original Repository
- **Organization:** IBM Developer Skills Network
- **Original Repository:** `obmnl-flask_assignment`
- **Course:** IBM Python Flask Development

### Enhancements & Contributions
Enhanced and extended by [Rafael A. G. N.](https://github.com/rafael-a-g-n) with:
- Comprehensive error handling
- Search functionality
- Balance calculation feature
- Input validation
- Code quality improvements (Pylint 10/10)
- Smart number formatting
- Complete documentation
- Modern GitHub README

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Rafael A. G. N.**
- GitHub: [@rafael-a-g-n](https://github.com/rafael-a-g-n)
- Repository: [obmnl-flask_assignment](https://github.com/rafael-a-g-n/obmnl-flask_assignment)

## 🙏 Acknowledgments

- IBM Developer Skills Network for the initial project structure
- Coursera IBM Python Flask course materials
- Flask documentation and community
- Python community for excellent tools and libraries

---

⭐ **If you found this project helpful, please consider giving it a star!** ⭐

---

**Made with ❤️ and Python**
