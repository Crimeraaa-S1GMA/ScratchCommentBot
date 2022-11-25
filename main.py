import scratchclient
import random
import time
import json

print("  __                        _                               _         ")
print(" (_   _ ._ _. _|_  _ |_    /   _  ._ _  ._ _   _  ._ _|_   |_)  _ _|_ ")
print(" __) (_ | (_|  |_ (_ | |   \_ (_) | | | | | | (/_ | | |_   |_) (_) |_ ")
print("By Crimeraaa")
print("Warning: I AM NOT RESPONSIBLE FOR ANY BANS FROM THE USAGE OF THIS")

config = open("config.json", "r")
config_loaded = json.loads(config.read())

comments = open("comments.txt", "r").readlines()
project_ids = open("projectid.txt", "r").readlines()
session = scratchclient.ScratchSession(config_loaded["userName"], config_loaded["password"])

session.login(config_loaded["password"])

if config_loaded["inclFeaturedProjects"]:
    for frontProj in session.get_front_page()["featured_projects"]:
        project_ids.append(frontProj.id)

while True:
    for p in project_ids:
        project = session.get_project(int(p))
        try:
            if project.comments_allowed:
                project.post_comment(
                    random.choice(comments) + " " + str(random.randint(100, 999)))
                print("Comment posted!\n\nThere's a 60 second delay + comment posting duration due to Scratch's limits")
                time.sleep(60)
        except:
            pass

