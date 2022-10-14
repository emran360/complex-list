quotes = [
{
"anime": "Avatar: The Last Airbender",
"character": "Zuko",
"quote": "Why am I so bad at being good?"
},
{
"anime": "K-ON!",
"character": "Sawako Yamanaka",
"quote": "No, she's hiding something. But what could it be? Snacks? Guitar? Wait, maybe ton-chan."
},
{
"anime": "Soul Eater",
"character": "Excalibur",
"quote": "This brings us to number 278 of the 1,000 provisions you must observe. I hate carrots. Never even think about putting them in my food, you get it?"
},
{
"anime": "Paradise Kiss",
"character": "Koizumi George",
"quote": "Stop rushing me. I want to take my time falling in love with you."
},
{
"anime": "Arakawa under the Bridge × Bridge",
"character": "Kou Ichinomiya",
"quote": "Waiting for you. Waiting for your knock. The only thing that stands between us is a single door. Shining\nmy shoes and placing a piece of eternally fresh bread in my pocket, I prepare for my journey.\nWhen you're ready, just look up at me.  Right now, I'm just waiting for you...Waiting for your knock."
},
{
"anime": "Hai to Gensou no Grimgar",
"character": "Haruhiro",
"quote": "I'm different from who I was yesterday. I wonder what I will be like tomorrow. Day by day, we live in the today and keep living to meet our future selves."
},
{
"anime": "Hanayamata",
"character": "Masaru Ōfuna",
"quote": "Coming together and working hard with everyone is a really fun thing!"
},
{
"anime": "Mayoiga",
"character": "Kamiyama",
"quote": "Lies are told prevent yourself from getting hurt."
},
{
"anime": "Fairy Tail",
"character": "Kagura Mikazuchi",
"quote": "I haven't relied on luck since the moment I was born. Everything has been the result of my choices. That is what leads my existence towards the future."
},
{
"anime": "Kagerou Days",
"character": "Kido Tsubomi",
"quote": "Meals are always better with lots of people at the table."
}
]

for quote in quotes:
    anime = quote.get('anime')
    character = quote.get('character')
    q = quote.get('quote')
    quote_template = f'{character} says, "{q}"'


    print(quote_template)

    print('*'* 10)
