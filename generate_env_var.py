import os

host = "MY_SECRET"
with open(os.environ["GITHUB_ENV"], "a") as env_file:
    env_file.write(f"host={host}")
