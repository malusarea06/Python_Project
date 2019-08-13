from firebase import Firebase
from Crypto.PublicKey import RSA
config = {
	"apiKey":" AIzaSyDOrwWBtIIy38h1ZfB6ipECuQMPQq2tqvI",
	"authDomain": "lunchbox-8c6fc.firebaseapp.com",
  "databaseURL": "https://lunchbox-8c6fc.firebaseio.com/",
  "storageBucket": "lunchbox-8c6fc.appspot.com"
}

firebase = Firebase(config)
#db = firebase.database()
#users = db.child("Users").get()
#print(users.val())