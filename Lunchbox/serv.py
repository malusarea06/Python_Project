from firebase import firebase

firebase = firebase.FirebaseApplication('https://lunchbox-8c6fc.firebaseio.com/', None)
result = firebase.get('/Users/8855940530', None)
print(result)