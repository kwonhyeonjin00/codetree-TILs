secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

secret = Secret(secret_code, meeting_point, time)

print(f"secret code : {secret.secret_code}")
print(f"meeting point : {secret.meeting_point}")
print(f"time : {secret.time}")