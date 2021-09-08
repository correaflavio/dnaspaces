# dnaspaces

This is a repo with tools to be used with Cisco DNA Spaces (http://dnaspaces.io) product.

**activate_get_api_key.py** -  python script to activate your on-prem DNA Spaces APP and get the API Key to access the data streaming.

With the API Key you can do the first try using curl:

curl "https://partners.dnaspaces.io/api/partners/v1/firehose/events" -H "X-API-Key: <Your-API-Key>"

**Note:** If you are in europe the URL of DNA Spaces ends with _eu_ instead of _io_.

-----------------------

If you are looking for more DNA Spaces related code, I recommend visiting Simon Light github (https://github.com/SimonLight001)

