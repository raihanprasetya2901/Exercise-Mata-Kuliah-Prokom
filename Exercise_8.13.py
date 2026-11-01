# Exercise 8-13: User Profile
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('mahasiswa', 'uns', location='surakarta', field='industrial engineering')
print(my_profile)