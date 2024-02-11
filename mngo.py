from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://comamikra:<9!-tLLE9_CcHT.2>@atlascluster.djuouag.mongodb.net/?retryWrites=true&w=majority"

# Replace special characters with actual username and password
username = "com.am.ikra@gmail.com"
password = "9!-tLLE9_CcHT.2"
uri = uri.replace("<9!-tLLE9_CcHT.2>", password).replace("com.am.ikra@gmail.com", username)

# Convert MongoDB URI into a link
mongodb_link = f"<a href='{uri}' target='_blank'>{uri}</a>"

print(mongodb_link)
