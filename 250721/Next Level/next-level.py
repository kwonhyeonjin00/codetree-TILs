user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Member:
    def __init__(self, user_id, user_level):
        self.user_id = user_id
        self.user_level = user_level

member_1 = Member("codetree", 10)
member_2 = Member(user2_id, user2_level)

print(f"user {member_1.user_id} lv {member_1.user_level}")
print(f"user {member_2.user_id} lv {member_2.user_level}")