import requests
from urllib.parse import urlparse
from x_client_transaction.utils import handle_x_migration
from x_client_transaction import ClientTransaction

headers = {"Authority": "x.com",
           "Accept-Language": "en-US,en;q=0.9",
           "Cache-Control": "no-cache",
           "Referer": "https://x.com",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
           "X-Twitter-Active-User": "yes",
           "X-Twitter-Client-Language": "en"}

session = requests.Session()
session.headers = headers
response = handle_x_migration(session)

# Example 1
# replace the url and http method as per your use case
url = "https://x.com/i/api/1.1/jot/client_event.json"
method = "POST"
path = urlparse(url=url).path
# path will be /i/api/1.1/jot/client_event.json in this case

# Example 2
user_by_screen_name_url = "https://x.com/i/api/graphql/1VOOyvKkiI3FMmkeDNxM9A/UserByScreenName"
user_by_screen_name_http_method = "GET"
user_by_screen_name_path = urlparse(url=url).path
# path will be /i/api/graphql/1VOOyvKkiI3FMmkeDNxM9A/UserByScreenName in this case


ct = ClientTransaction(response)
transaction_id = ct.generate_transaction_id(method=method, path=path)
transaction_id_for_user_by_screen_name_endpoint = ct.generate_transaction_id(
    method=user_by_screen_name_http_method, path=user_by_screen_name_path)

print(transaction_id)
print(transaction_id_for_user_by_screen_name_endpoint)
