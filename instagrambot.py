# How to make a Simplest Instagram Bot in pyhton

# pip install instabot
import os
import time
import schedule
from instabot import Bot

# Initialize bot
bot = Bot()

# Login Credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Remove previous session files (avoiding login issues)
if os.path.exists("config"):
    os.rmdir("config")

# Login to Instagram
bot.login(username=USERNAME, password=PASSWORD)

# Function: Follow a user
def follow_user(username):
    bot.follow(username)
    print(f"Followed {username}")

# Function: Unfollow a user
def unfollow_user(username):
    bot.unfollow(username)
    print(f"Unfollowed {username}")

# Function: Upload a photo with a caption
def upload_photo():
    image_path = "C:/Users/Dell/OneDrive/Pictures/jay.jpg"
    caption = "Wow! 😍 #awesome"
    bot.upload_photo(image_path, caption=caption)
    print("Photo uploaded!")

# Function: Like and comment on a user's latest post
def like_and_comment(username, comment_text="Nice post!"):
    user_id = bot.get_user_id_from_username(username)
    media_ids = bot.get_last_user_medias(user_id, 1)
    if media_ids:
        bot.like(media_ids[0])
        bot.comment(media_ids[0], comment_text)
        print(f"Liked & commented on {username}'s post")

# Function: Auto-like posts by hashtag
def like_by_hashtag(hashtag, amount=5):
    bot.like_hashtag(hashtag, amount)
    print(f"Liked {amount} posts from #{hashtag}")

# Function: Follow users who posted using a hashtag
def follow_by_hashtag(hashtag):
    users = bot.get_hashtag_users(hashtag)
    bot.follow_users(users)
    print(f"Followed users posting under #{hashtag}")

# Function: Send messages
def send_message():
    bot.send_message("Hey, how are you?", ["virat.kohli", "jaykumarsingh_01"])
    print("Message sent!")

# Function: Get followers and following list
def get_followers_following():
    followers = bot.get_user_followers(USERNAME)
    following = bot.get_user_following(USERNAME)

    print("Followers:")
    for follower in followers[:5]:  # Display only first 5 followers
        print(bot.get_user_info(follower))

    print("\nFollowing:")
    for person in following[:5]:  # Display only first 5 followings
        print(bot.get_user_info(person))

# Function: Remove inactive followers (who don’t follow you back)
def remove_inactive_followers():
    non_followers = set(bot.following) - set(bot.followers)
    for user in non_followers:
        bot.unfollow(user)
    print("Unfollowed inactive followers!")

# Function: Fetch user bio and post count
def fetch_user_info(username):
    user_info = bot.get_user_info(username)
    print(f"Bio: {user_info['biography']}")
    print(f"Posts Count: {user_info['media_count']}")

# Function: Download photos from a user
def download_user_photos(username):
    bot.download_user(username, profile_pic=True)
    print(f"Downloaded {username}'s photos")

# Function: Scheduled posting
def schedule_post():
    schedule.every().day.at("09:00").do(upload_photo)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Execute functions
follow_user("virat.kohli")
like_and_comment("virat.kohli")
like_by_hashtag("fitness", amount=3)
follow_by_hashtag("cricket")
send_message()
get_followers_following()
remove_inactive_followers()
fetch_user_info("virat.kohli")
download_user_photos("virat.kohli")


# Logout after execution
bot.logout()
print("Bot logged out successfully!")


                                        #Jay Kumar Singh


