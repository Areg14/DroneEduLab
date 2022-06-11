lyrics = """Spotlight, uh, moonlight, uh
Nigga, why you trippin'? Get your mood right, uh
Shawty look good in the moonlight
All these pussy niggas so bad mind
Spotlight, moonlight
Nigga, why you trippin'? Get your mood right
Shawty look good in the moonlight
All these pussy niggas so bad mind
Spotlight, uh, moonlight, uh
Nigga, why you trippin'? Get your mood right, uh
Shawty look good in the moonlight
All these pussy niggas so bad mind
Spotlight, moonlight
Nigga, why you trippin'? Get your mood right
Shawty look good in the moonlight
All these pussy niggas so bad mind
Feel like I'm destined
I don't need no Smith & Wesson, no
Boy, who you testin'?
Fuck a Scantron, here's your lesson, oh
Knife in intestine
Takin' shots at all your bredrin, oh
Feel like I'm damaged
Girl, I know you fuckin' planned this
All alone, call my phone, make me feel right
Girl, you know when you call, make me feel right
All alone, call my phone, make me feel right
Girl, you know when you call, make me feel right
Spotlight, uh, moonlight, uh
Nigga, why you trippin'? Get your mood right, uh
Shawty look good in the moonlight
All these pussy niggas so bad mind
Spotlight, moonlight
Nigga, why you trippin'? Get your mood right
Shawty look good in the moonlight
All these pussy niggas so bad mind
Spotlight, uh, moonlight, uh
Nigga, why you trippin'? Get your mood right, uh
Shawty look good in the moonlight
All these pussy niggas so bad mind
Spotlight, moonlight
Nigga, why you trippin'? Get your mood right
Shawty look good in the moonlight
All these pussy niggas so bad mind"""

print(lyrics)
print("\n\n")

letter = input("Enter letter to get its count in the lyrics: ")
letters = []
count = 0

for i in lyrics:
    letters.append(i)

for i in letters:
    if i == letter:
        count = count + 1

print(count)