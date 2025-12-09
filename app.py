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
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
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
        except Exception as e:
            return {"message": f"An error occurred: {str(e)}"}, 500
    return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        try:
            # Validate form data
            if 'date' not in request.form or 'amount' not in request.form:
                return {"message": "Missing required fields"}, 400
            
            if not request.form['date'] or not request.form['amount']:
                return {"message": "Date and amount cannot be empty"}, 400
            
            transaction_found = False
            for transaction in transactions:
                if transaction['id'] == transaction_id:
                    transaction['date'] = request.form['date']
                    transaction['amount'] = float(request.form['amount'])
                    transaction_found = True
                    break
            
            if not transaction_found:
                return {"message": "Transaction not found"}, 404
            
            return redirect(url_for('get_transactions'))
        except ValueError:
            return {"message": "Invalid amount format"}, 400
        except Exception as e:
            return {"message": f"An error occurred: {str(e)}"}, 500
    
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction=transaction)
        
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    try:
        transaction_found = False
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transactions.remove(transaction)
                transaction_found = True
                break
        
        if not transaction_found:
            return {"message": "Transaction not found"}, 404
        
        return redirect(url_for('get_transactions'))
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500

# Search operation
@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    if request.method == 'POST':
        try:
            # Validate form data
            if 'min_amount' not in request.form or 'max_amount' not in request.form:
                return {"message": "Missing required fields"}, 400
            
            if not request.form['min_amount'] or not request.form['max_amount']:
                return {"message": "Min and max amount cannot be empty"}, 400
            
            min_amount = float(request.form['min_amount'])
            max_amount = float(request.form['max_amount'])
            
            if min_amount > max_amount:
                return {"message": "Min amount cannot be greater than max amount"}, 400
            
            filtered_transactions = [
                transaction for transaction in transactions 
                if min_amount <= transaction['amount'] <= max_amount
            ]
            return render_template('transactions.html', transactions=filtered_transactions)
        except ValueError:
            return {"message": "Invalid amount format"}, 400
        except Exception as e:
            return {"message": f"An error occurred: {str(e)}"}, 500
    return render_template('search.html')

# Total balance operation
@app.route('/balance')
def total_balance():
    try:
        balance = sum(transaction['amount'] for transaction in transactions)
        return f"Total Balance: {balance}"
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return {"message": "Resource not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"message": "Internal server error"}, 500

@app.errorhandler(400)
def bad_request(error):
    return {"message": "Bad request"}, 400

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
