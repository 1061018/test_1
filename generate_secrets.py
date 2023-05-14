import os

secret = os.environ.get('MY_SECRET')

with open('secrets.sh', 'w') as f:
    f.write(f'export MY_SECRET="{secret}"')
