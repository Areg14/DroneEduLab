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

word = input("Enter word you want to find in the lyrics: ")
separate_lyrics = lyrics.split()
for n, i in enumerate(separate_lyrics):
    if word == i:
        print(f"I found it: at {n}th word")