"""
Flask application for managing financial transactions.

This module provides a web application for CRUD operations on transactions,
including creating, reading, updating, deleting, and searching transactions.
"""

# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


# Read operation
@app.route('/')
def get_transactions():
    """Display all transactions."""
    return render_template('transactions.html', transactions=transactions)


# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    """Add a new transaction via form submission."""
    if request.method == 'POST':
        try:
            # Validate form data
            if 'date' not in request.form or 'amount' not in request.form:
                return {"message": "Missing required fields"}, 400

            if not request.form['date'] or not request.form['amount']:
                return {"message": "Date and amount cannot be empty"}, 400

            transaction = {
                'id': len(transactions) + 1,
                'date': request.form['date'],
                'amount': float(request.form['amount'])
            }
            transactions.append(transaction)
            return redirect(url_for('get_transactions'))
        except ValueError:
            return {"message": "Invalid amount format"}, 400
        except (KeyError, TypeError) as e:
            return {"message": f"An error occurred: {str(e)}"}, 500
    return render_template('form.html')


# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    """Edit an existing transaction by ID."""
    if request.method == 'POST':
        # Validate form data
        if ('date' not in request.form or
                'amount' not in request.form or
                not request.form['date'] or
                not request.form['amount']):
            return {"message": "Missing or empty required fields"}, 400

        try:
            transaction_found = False
            for transaction in transactions:
                if transaction['id'] == transaction_id:
                    transaction['date'] = request.form['date']
                    transaction['amount'] = float(request.form['amount'])
                    transaction_found = True
                    break

            if transaction_found:
                return redirect(url_for('get_transactions'))
            return {"message": "Transaction not found"}, 404

        except ValueError:
            return {"message": "Invalid amount format"}, 400
        except (KeyError, TypeError) as e:
            return {"message": f"An error occurred: {str(e)}"}, 500

    transaction = next(
        (t for t in transactions if t['id'] == transaction_id),
        None
    )
    return (render_template('edit.html', transaction=transaction)
            if transaction
            else ({"message": "Transaction not found"}, 404))


# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    """Delete a transaction by ID."""
    try:
        transaction = next(
            (t for t in transactions if t['id'] == transaction_id),
            None
        )

        if not transaction:
            return {"message": "Transaction not found"}, 404

        transactions.remove(transaction)
        return redirect(url_for('get_transactions'))
    except (ValueError, KeyError) as e:
        return {"message": f"An error occurred: {str(e)}"}, 500


# Search operation
@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    """Search transactions by amount range."""
    if request.method == 'POST':
        try:
            # Validate form data
            min_key = 'min_amount'
            max_key = 'max_amount'
            if (min_key not in request.form or
                    max_key not in request.form or
                    not request.form[min_key] or
                    not request.form[max_key]):
                msg = "Missing or empty min/max amount fields"
                return {"message": msg}, 400

            min_amount = float(request.form[min_key])
            max_amount = float(request.form[max_key])

            if min_amount > max_amount:
                msg = "Min amount cannot be greater than max amount"
                return {"message": msg}, 400

            filtered_transactions = [
                transaction for transaction in transactions
                if min_amount <= transaction['amount'] <= max_amount
            ]
            return render_template(
                'transactions.html',
                transactions=filtered_transactions
            )
        except ValueError:
            return {"message": "Invalid amount format"}, 400
        except (KeyError, TypeError) as e:
            return {"message": f"An error occurred: {str(e)}"}, 500
    return render_template('search.html')


# Total balance operation
@app.route('/balance')
def total_balance():
    """Calculate and return the total balance of all transactions."""
    try:
        balance = sum(
            transaction['amount'] for transaction in transactions
        )
        return f"Total Balance: {balance}"
    except (KeyError, TypeError) as e:
        return {"message": f"An error occurred: {str(e)}"}, 500


# Error handlers
@app.errorhandler(404)
def not_found(_error):
    """Handle 404 errors."""
    return {"message": "Resource not found"}, 404


@app.errorhandler(500)
def internal_error(_error):
    """Handle 500 errors."""
    return {"message": "Internal server error"}, 500


@app.errorhandler(400)
def bad_request(_error):
    """Handle 400 errors."""
    return {"message": "Bad request"}, 400


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
