
#======================== JSON Notes ===============

#JSON stands for: JavaScript Object Notation
#despite this, it can read/translated across all languages, not just javascript

#- This makes it an incredibly useful language for APIs
#- It is also very lightweight making it easy to pass back and forth between server and client
#- Structered into objects that look like dictionaries

#---------------------- Status Codes ---------------

# - 200s are our successful request statuses
#--- 200 OK - request
#--- 201 - Successful creation 
#--- 204 No Content - Sent the request successfully, but didn't get any data back

# - 300s - Redirect
# - 301 - Moved around Permanantly: continuously redirected

# 400s - Client Error (Your Mistake)
# 400 - Bad Request: either malformed or missing data
# 401 - Unauthoraized: You don't have the proper credentials
# 404 - Not Found: The resource does not exit
# 429 - Too Many Request: exceeded the max amout of requests for a particular resource

# 500s - Server Error (Their Problem)

#- 500 - Internal Sever Error - something broke on their end
# 503 - Service Unavailable - Temporarily down for maintanence
# 504 - Gateway Timeout - Server took too long to respond