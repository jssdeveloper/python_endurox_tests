from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/create_transaction', methods=['POST'])
def create():
    data = {
        "access_token": "23421adad12321adssd",
        "token_type": "Bearer",
        "expires_in": 2399,
        "status": "awaiting_authorisation",
        "creation_date": 1231313131,
        "expiration_date": 1231313431,
        "consent_id": "id",
        "account_id": "account_id",
        "account_type": "Personal",
        "account_subtype": "Current",
        "nickname": "Bills",
        "bank_name": "bank_name",
        "verified": False,
        "countries": ["EU"],
        "developer_portal": "testbank.com",
        "label": "transaction init",
        "premium": False,
        "categories": "accounts",
        "documentation_url": "docurl.com",
        "blocked": False,
        "bank_swift": "bank_swift",
        "balance_available": 259.33,
        "limit": 750,
        "amount": 39.95,
        "currency": "EUR",
        "transaction_details": "transaction_details",
        "country": "DE",
        "city": "city",
        "street": "street",
        "street_number": "street_number",
        "apt_number": 4,
        "debit_response_code": 0,
        "credit_respoonse_code": 0,
        "test": False,
        "fee": 0,
        "source_order_id": None,
        "credit_exceeded": False,
        "merchant": "Example Mart",
        "account_number": "**** **** **** 1234",
        "transaction_type": "Debit",
        "category": "Retail",
        "location": "Berlin, DE",
        "payment_method": "Credit Card",
        "card_type": "Visa",
        "card_last_digits": "4321",
        "authorization_code": "AUTH500",
        "is_expense_reported": True,
        "is_receipt_attached": True,
        "is_pending": True,
        "is_duplicate": False,
        "is_recurring": False,
        "is_anomaly": False,
        "is_flagged": False,
        "beneficiary_name": "Test Customer",
        "beneficiary_account": "Test account",
        "beneficiary_bank": "Example Bank",
        "tax_amount": 2.39,
        "tax_rate": 19,
        "fee_amount": 2.50,
        "fee_description": "Transaction Fee",
        "insurance_policy": "pol23",
        "device_type": "mobile",
        "ip_address": "192.168.2.1",
        "browser": "mobile",
        "os": "android",
        "is_fraudulent": False,
        "related_transactions": ["TRANS1", "TRANS2"],
        "test_field2": "value2",
        "test_field1": "value1",
        "test_field3": "value3",
        "test_field4": "value4",
        "test_field5": "value5",
        "test_field6": "value6",
        "test_field7": "value7",
        "test_field8": "value8",
        "test_field9": "value9",
        "test_field10": "value10",
        "test_field11": "value11",
        "test_field12": "value12",
        "test_field13": "value13",
        "test_field14": "value14",
        "test_field15": "value15",
        "test_field16": "value16",
        "test_field17": "value17",
        "test_field18": "value18",
        "test_field19": "value19",
        "test_field20": "value20",
        "test_field21": "value1",
        "test_field22": "value2",
        "test_field23": "value3",
        "test_field24": "value4",
        "test_field25": "value5",
        "test_field26": "value6",
        "test_field27": "value7",
        "test_field28": "value8",
        "test_field29": "value9",
        "test_field30": "value10",
        "test_field31": "value11",
        "test_field32": "value12",
        "test_field33": "value13",
        "test_field34": "value14",
        "test_field35": "value15",
        "test_field36": "value16",
        "test_field37": "value17",
        "test_field38": "value18",
        "test_field39": "value19",
        "test_field40": "value20",
    }
    try:
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/creditdebit', methods=['POST'])
def send_post_request():
    try:
        # Get request body as JSON
        data = request.get_json()

        if data is None:
            return jsonify({'error': 'Invalid JSON in request body'}), 400

        print("Got transaction data, sending request to Credit")

        headers = {"Content-type": "application/json"}

        # Send transaction to Credit
        credit = requests.post(
            "http://127.0.0.1:3001/credit", data=json.dumps(data), headers=headers)
        creditResponse = credit.json()

        if creditResponse["credit"] == "passed":
            print("Credit verified, sending request to debit")

        # Send transaction to Debit
        debit = requests.post("http://127.0.0.1:3002/debit", data=json.dumps(
            creditResponse), headers=headers)

        return debit.json()
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# if __name__ == '__main__':
#     app.run()

# gunicorn --bind 0.0.0.0:3000 -w 8 wsgi:app
