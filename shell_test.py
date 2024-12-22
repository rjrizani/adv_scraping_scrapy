import impersonate
from scrapy.http import Request

# Set up impersonate
impersonate.start()

# Create a request with impersonate headers
url = 'https://sg.iherb.com/pr/california-gold-nutrition-gold-c-usp-grade-vitamin-c-1-000-mg-60-veggie-capsules/61864'
headers = impersonate.headers()
request = Request(url, headers=headers)

# Fetch the page
fetch(request)

# View the response
response.body