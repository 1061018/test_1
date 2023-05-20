import os

secret = os.environ.get('HOSTNAME')
print(f'my secret is{secret}')
with open('secrets.sh', 'w') as f:
    f.write(f'export MY_SECRET="{secret}"')
