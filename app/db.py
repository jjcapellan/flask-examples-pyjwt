# db.py

# password in plain text is "1q2w3e4r"
users_table = {
    'john': {
        'name':'john',
        'rol':'admin',
        'password':'pbkdf2:sha256:150000$odpBdApk$edcb7f9a952e4330db6b624dfe67c552c533863e72f0e3162a3db4302a335470'
        },
    'oliver': {
        'name':'oliver',
        'rol':'user',
        'password':'pbkdf2:sha256:150000$odpBdApk$edcb7f9a952e4330db6b624dfe67c552c533863e72f0e3162a3db4302a335470'
        }
}