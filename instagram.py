# How to make a Simplest Instagram Bot in Python

# pip install instabot

from instabot import Bot
# first login our page
bot=Bot()
bot.login(username="your username",passwords="your passwords")
# if you follow anyone
bot.follow('virat.kohli')

# upload photo
bot.upload_photo("C:/Users/Dell/OneDrive/Pictures/jay.jpg",caption="wow___")

# if you want to unfollow any person then: 
bot.unfollow("virat.kohli")

# if you want to send message for multiple person in instagram
bot.send_message("hey how are you",["virat.kohli", "jaykumarsingh_01"])

# how to know your followers and following on the instagram:
followers =bot.get_user_followers("your user id")
for followers in followers:
    print(bot.get_user_info(follower))

# following
following=bot.get_user_following("your user id")
for Following in following:
    print(bot.get_user_info(Following))

