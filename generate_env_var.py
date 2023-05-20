import os

env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("host=MY_SECRET")
    myfile.write("\n")
    myfile.write("work_secret=MY_SECRET_WORK")
