import httpx
import time

# Create user
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
assert create_user_response.status_code == 200
create_user_response_data = create_user_response.json()
assert create_user_response_data
user_id = create_user_response_data['user']['id']

# Open credit card account
open_credit_card_account_payload = {"userId": f"{user_id}"}
open_credit_card_account_response = httpx.post('http://localhost:8003/api/v1/accounts/open-credit-card-account',
                                               json=open_credit_card_account_payload)
assert open_credit_card_account_response.status_code == 200
open_credit_card_account_response_data = open_credit_card_account_response.json()
assert open_credit_card_account_response_data
account_id = open_credit_card_account_response_data['account']['id']
card_id = open_credit_card_account_response_data['account']['cards'][0]['id']

# Make purchase operation
make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": card_id,
    "accountId": account_id,
    "category": "taxi"
}
make_purchase_operation_response = httpx.post('http://localhost:8003/api/v1/operations/make-purchase-operation',
                                              json=make_purchase_operation_payload)
assert make_purchase_operation_response.status_code == 200
make_purchase_operation_response_data = make_purchase_operation_response.json()
assert make_purchase_operation_response_data
purchase_operation_id = make_purchase_operation_response_data['operation']['id']

# Get operation receipt
operation_receipt_response = httpx.get(
    f'http://localhost:8003/api/v1/operations/operation-receipt/{purchase_operation_id}')
assert operation_receipt_response.status_code == 200
operation_receipt_response_data = operation_receipt_response.json()
assert operation_receipt_response_data
print(operation_receipt_response_data)
