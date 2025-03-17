# Make an empty list for storing aliens.
aliens=[]

# Make 30 green aliens.
for alien_number in range(30):
    new_alien={'color': 'green','points':5,'speed':'slow'}
    aliens.append(new_alien)


# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")


# Show how many aliens have been created.
print(f"Total number of aliens:{len(aliens)}")

# Change the color of the first 3 to yellow and speed to medium
for alien in aliens[:3]:
    if alien['color'] =='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
