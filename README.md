#Blockchain

Django restframework project. 

Takes given bitcoin address, validates it and checks if address is in local database. If address exists shows details, all transactions and creates QRcode, if not connects to blockchain API, saves to database, shows details, all transactions and creates QRcode.

Project contains usage of:

- Django restframework API
- PostgreSQL database
- JSON data
- blockchain API
- pyqrcode
- Django static files
- custom made validators
- custom made templatetags
