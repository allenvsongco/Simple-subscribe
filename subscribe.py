import urllib.parse
import urllib.request

# -------------------------- You need to set these -------------------------- #
your_installation_url = 'http://sendy.coursebank.ph'  # Your Sendy installation (without the trailing slash)
list_id = 'C8vWaerC4JWGukRwMkoYAw'  # Can be retrieved from "View all lists" page
api_key = 'KizFCsS60lGWRcQh5eqN '  # Can be retrieved from your Sendy's main settings
success_url = 'http://google.com'  # URL user will be redirected to if successfully subscribed
fail_url = 'http://yahoo.com'  # URL user will be redirected to if subscribing fails
# --------------------------------------------------------------------------- #

# POST variables
email = input('Enter email: ')
boolean = 'true'

# Check fields
if email == '':
    print('Please fill in all fields.')
    exit()

# Subscribe
data = urllib.parse.urlencode({
    'email': email,
    'list': list_id,
    'api_key': api_key,
    'boolean': boolean
}).encode('utf-8')

req = urllib.request.Request(your_installation_url + '/subscribe', data=data)
try:
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
except urllib.error.HTTPError as e:
    result = ''

# Check result and redirect
if result:
    print('Location: ' + success_url)
else:
    print('Location: ' + fail_url)
