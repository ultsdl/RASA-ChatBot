import requests
import json

def get_response(recipient_id, message):
    data = json.dumps({"sender": recipient_id,"message": message, "metadata":{"name":"Just a name"}})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
    res = res.json()
    val = res[0]['text']
    return val

print(get_response("Arun Mohan", "total number of population"))

#import mysql.connector
#
#mydb = mysql.connector.connect(
#  host="database-1.cs2hezz6vd9p.ap-south-1.rds.amazonaws.com",
#  user="admin",
#  password="testenv116",
#  database="Transaction"
#)
#
#try:
#    cursor = mydb.cursor()
#    cursor.execute("""
#    SELECT * from Transaction
#    """)
#    result = cursor.fetchall()
#    print(result)
#finally:
#    mydb.close()

