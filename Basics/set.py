room_friends = {'KP', 'Jephin', 'Rekhin'}
room2 = {'jibu', 'shab'}
room_friends.add('jibu')

print(room_friends)
#Sets are case sensitive, here the name Jibu is added because its case sensitive
room2.add('Jibu')
print(room2)

art_friends = {'Jibu', 'Rekhin', 'sambhu'}
science = {'Rekhin', 'Jephin'}

art_friends_not_science = art_friends.difference(science)
science_not_art = science.difference(art_friends)

print(art_friends_not_science)
print(science_not_art)

all_friends = art_friends.union(science)
print(all_friends)

art_and_science = art_friends.intersection(science)
print(art_and_science)


