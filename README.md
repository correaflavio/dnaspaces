# dnaspaces

This is a repo with tools to be used with Cisco DNA Spaces (http://dnaspaces.io) product.


**activate_get_api_key.py** -  python script to activate your on-prem DNA Spaces APP and get the API Key to access the data streaming.

When running this script, you will be requested to enter your token. This token can be obtained in your DNA Spaces Portal (http://dnaspaces.io), at the Partner APPs area, clicking in your APP Settings => New Activation => Select Location and Devices => Generate Activation Key => Copy Token.

With the API Key you can do the first try using curl:

curl "https://partners.dnaspaces.io/api/partners/v1/firehose/events" -H "X-API-Key: <Your-API-Key>"

  
**Notes:** 
  - If you are in europe the URL of DNA Spaces ends with _eu_ instead of _io_.
  - If you have a Cloud DNA Spaces APP instead of an on-prem, the activation and API key access is made in a different way.

Complete DNA Spaces Firehose API documentation available at http://partners.dnaspaces.io. This is also the location to create your APP and select the type of DNA Spaces you want to receive via the Firehose API.
To have access to the API, you need to have DNA Spaces license and it's required to ask support to activate it. It's not enabled by default.
  
-----------------------

If you are looking for more DNA Spaces related code, I recommend visiting Simon Light github (https://github.com/SimonLight001)

