import httpx
import time

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

open_deposit_account_payload = {"userId": f"{user_id}"}
open_deposit_account_response = httpx.post('http://localhost:8003/api/v1/accounts/open-deposit-account', json=open_deposit_account_payload)
assert open_deposit_account_response.status_code == 200
open_deposit_account_response_data = open_deposit_account_response.json()
assert open_deposit_account_response_data
print(open_deposit_account_response_data)
print(open_deposit_account_response.status_code)
