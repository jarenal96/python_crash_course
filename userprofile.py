def build_profiles(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first name']= first
    user_info['last name'] = last
    return user_info

user_profile = build_profiles('jorge','arenal', job = 'Operational Excellence', company = 'Pilgrims Pride')

print(user_profile)