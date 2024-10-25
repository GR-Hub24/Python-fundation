banned_users = ['andrew', 'carolina', 'david']
user = 'david'

if user not in banned_users:
		print(f"{user.title()}, you can post a response if you wish.")
else:
	for banned_user in banned_users:
		if user in banned_user:
				print(f"{banned_user}, you cannot post any.")