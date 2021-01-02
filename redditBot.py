import praw

def bot_login():
    print ("Logging in...")
    r = praw.Reddit(username = "nadoraa98",
                    password = "01150240104",
                    client_id = "7MEP5SG8xYtVWw",
                    client_secret = "SAp6UOjec6oQWgnVQI0UZQaoEG9dNw",
                    user_agent = "Students Comment Replier about Quizes v0.1")
    print("logged in!")
    return r

def run_bot(r):
    print("Obtaining comments...")
    for comment in r.subreddit('test').comments(limit=5):
        if "quiz " or "كويز" not in comment.body.lower():
            print("String with \"quiz\" found in comment " + comment.id)
            comment.reply("Yes, you do have one :)")
            print ("Replied to comment " + comment.id)

r = bot_login()
run_bot(r)