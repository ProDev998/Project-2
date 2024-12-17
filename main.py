import os
import random
import time
from datetime import datetime
import wikipedia
import webbrowser
import math

def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def tell_time():
    print(f"The current local time is {datetime.now().strftime('%H:%M:%S')}.")

def open_application(app_name):
    try:
        os.system(f'start {app_name}')
        return f"Opening {app_name}."
    except Exception as e:
        return "Could not open the application."

def open_website(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        webbrowser.open(url)
        return f"Opening {url}."
    except Exception as e:
        return "Could not open the website."

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except Exception as e:
        return "Could not retrieve data from Wikipedia."

def solve_math(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
    except Exception as e:
        return "Invalid math expression."
    
def presidents():
    presidents = [
        "Prime Minister of India is Narendra Modi",
        "President of the USA is Joe Biden",
        "Prime Minister of the UK is Rishi Sunak",
        "President of Brazil is Luiz Inácio Lula da Silva",
        "President of Russia is Vladimir Putin",
        "Prime Minister of Canada is Justin Trudeau",
        "President of China is Xi Jinping",
        "Prime Minister of Japan is Fumio Kishida",
        "President of France is Emmanuel Macron",
        "Prime Minister of Australia is Anthony Albanese",
        "President of Mexico is Andrés Manuel López Obrador",
        "Prime Minister of Italy is Giorgia Meloni",
        "President of Germany is Frank-Walter Steinmeier",
        "Prime Minister of South Korea is Han Duck-soo",
        "President of Argentina is Alberto Fernández",
        "Prime Minister of Israel is Benjamin Netanyahu",
        "President of Turkey is Recep Tayyip Erdoğan",
        "Prime Minister of Spain is Pedro Sánchez",
        "President of South Africa is Cyril Ramaphosa",
        "Prime Minister of Greece is Kyriakos Mitsotakis",
        "Prime Minister of New Zealand is Chris Hipkins",
        "President of Ukraine is Volodymyr Zelenskyy",
        "Prime Minister of Malaysia is Anwar Ibrahim",
        "President of Egypt is Abdel Fattah el-Sisi",
        "Prime Minister of Sweden is Ulf Kristersson",
        "President of Indonesia is Joko Widodo",
        "Prime Minister of Singapore is Lee Hsien Loong",
        "President of South Korea is Yoon Suk-yeol",
        "Prime Minister of Belgium is Alexander De Croo",
        "President of Saudi Arabia is Salman bin Abdulaziz Al Saud",
        "Prime Minister of Pakistan is Anwar-ul-Haq Kakar",
        "President of Iran is Ebrahim Raisi",
        "Prime Minister of Norway is Jonas Gahr Støre",
        "President of Vietnam is Võ Văn Thưởng",
        "Prime Minister of Denmark is Mette Frederiksen",
        "President of Poland is Andrzej Duda",
        "Prime Minister of Portugal is António Costa",
        "President of the Philippines is Ferdinand Marcos Jr.",
        "Prime Minister of Finland is Petteri Orpo",
        "President of Colombia is Gustavo Petro",
        "Prime Minister of Switzerland is Alain Berset",
        "President of Hungary is Katalin Novák",
        "Prime Minister of Slovenia is Robert Golob",
        "President of Chile is Gabriel Boric",
        "Prime Minister of Iceland is Katrín Jakobsdóttir",
        "President of Egypt is Abdel Fattah el-Sisi",
        "Prime Minister of Bangladesh is Sheikh Hasina",
        "President of Pakistan is Arif Alvi",
        "Prime Minister of Armenia is Nikol Pashinyan",
        "President of Tunisia is Kais Saied",
        "Prime Minister of Nepal is Pushpa Kamal Dahal",
        "President of Kenya is William Ruto",
        "Prime Minister of Sri Lanka is Dinesh Gunawardena",
        "President of Rwanda is Paul Kagame",
        "Prime Minister of Bangladesh is Sheikh Hasina",
        "President of Algeria is Abdelmadjid Tebboune",
        "Prime Minister of Ethiopia is Abiy Ahmed",
        "President of Kazakhstan is Kassym-Jomart Tokayev",
        "Prime Minister of Myanmar is Min Aung Hlaing",
        "President of Belarus is Alexander Lukashenko",
        "Prime Minister of Zimbabwe is Emmerson Mnangagwa"
        "President of Nigeria is Bola Tinubu",
        "Prime Minister of Bhutan is Lotay Tshering",
        "President of Uzbekistan is Shavkat Mirziyoyev",
        "Prime Minister of Bangladesh is Sheikh Hasina",
        "President of Kyrgyzstan is Sadyr Japarov",
        "Prime Minister of Mauritius is Pravind Jugnauth",
        "President of Nepal is Ram Chandra Poudel",
        "Prime Minister of Maldives is Mohamed Shareef",
        "President of Ivory Coast is Alassane Ouattara",
        "Prime Minister of Montenegro is Dritan Abazović",
        "President of Bosnia and Herzegovina is Šefik Džaferović",
        "Prime Minister of North Macedonia is Dimitar Kovačevski",
        "President of Serbia is Aleksandar Vučić",
        "Prime Minister of Albania is Edi Rama",
        "President of Mozambique is Filipe Nyusi",
        "Prime Minister of Latvia is Krišjānis Kariņš",
        "President of Latvia is Egils Levits",
        "Prime Minister of Estonia is Kaja Kallas",
        "President of Estonia is Kersti Kaljulaid",
        "Prime Minister of Luxembourg is Xavier Bettel",
        "President of Paraguay is Santiago Peña",
        "Prime Minister of Malta is Robert Abela",
        "President of Bolivia is Luis Arce",
        "Prime Minister of Mauritius is Pravind Jugnauth",
        "President of Liberia is George Weah",
        "Prime Minister of Cambodia is Hun Sen",
        "President of Belarus is Alexander Lukashenko",
        "Prime Minister of Seychelles is Wavel Ramkalawan",
        "President of Rwanda is Paul Kagame",
        "Prime Minister of Sri Lanka is Dinesh Gunawardena",
        "President of Guinea is Mamadi Doumbouya",
        "Prime Minister of Zambia is Hakainde Hichilema",
        "President of Georgia is Salome Zourabichvili",
        "Prime Minister of Kenya is William Ruto",
        "President of Ivory Coast is Alassane Ouattara",
        "Prime Minister of Malawi is Lazarus Chakwera",
        "President of Tanzania is Samia Suluhu Hassan",
        "Prime Minister of Lesotho is Samuel Matekane",
        "President of Burkina Faso is Ibrahim Traoré",
    ]
    return random.choice(presidents)

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why was the math book sad? Because it had too many problems.",
        "What do you call fake spaghetti? An impasta!",
        "Why do cows wear bells? Because their horns do not work.",
        "Why do chicken coops only have two doors? Because if they had four, they would be chicken sedans.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What do you call fake spaghetti? An impasta.",
        "I could not figure out why the baseball kept getting bigger. Then it hit me.",
        "I used to play piano by ear, but now I use my hands.",
        "I could not remember how to throw a boomerang, but then it came back to me.",
        "Why do seagulls fly over the ocean? Because if they flew over the bay, they would be bagels.",
        "I used to have a job as a professional cricket player, but I was stung by a wasp.",
        "Why dont skeletons fight each other? They do not have the guts.",
        "What did the ocean say to the beach? Nothing, it just waved.",
        "I was going to tell you a joke about a pencil, but it was pointless.",
        "How does a penguin build its house? Igloos it together.",
        "Why could not the bicycle stand up by itself? It was two-tired.",
        "What did one wall say to the other wall? I will meet you at the corner.",
        "Why do elephants never use computers? They are afraid of the mouse.",
        "What do you call cheese that is not yours? Nacho cheese.",
        "I told my computer I needed a break, and now it wont stop sending me Kit-Kats.",
        "Why do vampires always seem sick? Because they are always coffin.",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "I had a joke about construction, but I am still working on it.",
        "Why dont oysters share their pearls? Because they are shellfish.",
        "What did the grape do when it got stepped on? Nothing but let out a little wine.",
        "I asked the librarian if the library had any books on paranoia. She whispered, They are right behind you.",
        "I tried to catch some fog yesterday, but I mist.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "I told my dog to play dead. Now it is just acting like a rug.",
        "What do you call a pile of cats? A meow-tain.",
        "Why do cows make great musicians? They have great moosical talent.",
        "I could not find my sunglasses, but then I realized I was looking for them in the dark.",
        "Why did the tomato turn red? Because it saw the salad dressing.",
        "I am reading a book on anti-gravity. It is impossible to put down.",
        "Why do elephants never get invited to parties? They are always too busy stamping on things.",
        "What do you call an alligator in a vest? An investigator.",
        "I once heard a joke about a pencil, but it was too drawn out.",
        "Why do fish never play basketball? Because they are afraid of the net.",
        "What do you call a can opener that does not work? A cant opener.",
        "I had to sell my vacuum cleaner because it was just gathering dust.",
        "Why dont skeletons ever go trick or treating? Because they have no body to go with.",
        "What do you call a fake noodle? An impasta.",
        "I used to be a baker, but I could not make enough dough.",
        "Why was the math book sad? Because it had too many problems.",
        "I am reading a book about anti-gravity, but it is impossible to put down.",
        "Why dont skeletons ever fight each other? They do not have the guts.",
        "What do you call a dog magician? A labracadabrador.",
        "Why did the coffee file a police report? It got mugged.",
        "I am on a whiskey diet. I have lost three days already.",
        "Why dont ants get sick? Because they have tiny ant-bodies.",
        "I once got into a fight with a broken pencil. It was pointless.",
        "Why do frogs have so much fun? They never let anything get under their skin.",
        "What is the hardest part about writing a book? The editing, unless it is a mystery novel, in which case, it is finding the plot.",
        "I was going to make a pun about the wind, but it blew away.",
        "Why do birds fly south in the winter? It is faster than walking.",
        "I bought a belt the other day. It was a waist of money.",
        "Why did the bicycle fall over? It was two-tired.",
        "I used to be a baker, but I could not make enough dough.",
        "Why dont some couples go to the gym? Because some relationships do not work out.",
        "I would tell you a joke about a roof, but it might go over your head.",
        "Why do bears have sticky fur? Because they use honeycombs.",
        "What do you call a lazy kangaroo? A pouch potato.",
        "Why did the man put his money in the blender? Because he wanted to make some liquid assets.",
        "What do you call a lazy dog? A sloth.",
        "Why did the banana go to the doctor? Because it was not peeling well.",
        "What did one plate say to the other plate? Lunch is on me.",
        "Why do pigs make terrible baseball players? They are always hogging the ball.",
        "What is orange and sounds like a parrot? A carrot.",
        "I could not figure out why the baseball kept getting bigger. Then it hit me.",
        "Why did the math book look so sad? Because it had too many problems.",
        "Why was the broom late? It swept in.",
        "I could not remember how to throw a boomerang, but then it came back to me."
    ]
    return random.choice(jokes)

def countries():
    countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica", "Côte d’Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia, Federated States of", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", "Sudan, South", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
    return random.choice(countries)

def thoughts():
    thoughts = [
        "happiness is a choice you make every day",  
        "every problem is an opportunity in disguise",  
        "small steps lead to great journeys",  
        "kindness costs nothing but means everything",  
        "mistakes are proof you’re trying",  
        "your attitude determines your altitude",  
        "believe you can, and you’re halfway there",  
        "success is the sum of small efforts repeated daily",  
        "be the reason someone smiles today",  
        "change begins at the end of your comfort zone",  
        "focus on the possibilities, not the obstacles",  
        "learn from yesterday, live for today, hope for tomorrow",  
        "a positive mindset brings positive outcomes",  
        "progress, not perfection, is the goal",  
        "your mind is a garden; cultivate it wisely",  
        "challenges make you stronger, not weaker",  
        "self-discipline is the bridge between goals and achievement",  
        "life is 10% what happens and 90% how you react",  
        "don’t count the days, make the days count",  
        "grit and perseverance beat talent without effort",  
        "you are stronger than you think",  
        "every great journey starts with a single step",  
        "gratitude turns what you have into enough",  
        "dream big, start small, act now",  
        "the future depends on what you do today",  
        "stay curious, stay hungry",  
        "failure is not the opposite of success; it’s part of success",  
        "your vibe attracts your tribe",  
        "action is the foundational key to success",  
        "each sunrise brings new opportunities",  
        "never let fear decide your future",  
        "embrace the glorious mess that you are",  
        "don’t watch the clock; do what it does—keep going",  
        "you don’t have to be perfect to be amazing",  
        "what you think, you become",  
        "choose courage over comfort",  
        "stay focused and never give up",  
        "energy flows where attention goes",  
        "be the change you want to see in the world",  
        "be yourself; everyone else is already taken",  
        "start where you are, use what you have, do what you can",  
        "don’t let yesterday take up too much of today",  
        "your potential is endless",  
        "trust the timing of your life",  
        "let your dreams be bigger than your fears",  
        "success is a journey, not a destination",  
        "don’t stop until you’re proud",  
        "your only limit is you",  
        "focus on the good, and the good gets better",  
        "persistence is the key to success",  
        "choose joy even in the chaos",  
        "don’t wait for opportunity; create it",  
        "you grow through what you go through",  
        "the harder you work, the luckier you get",  
        "be fearless in the pursuit of what sets your soul on fire",  
        "it’s never too late to be what you might have been",  
        "each day is a new chance to improve",  
        "wake up with determination, go to bed with satisfaction",  
        "don’t compare your chapter 1 to someone else’s chapter 20",  
        "what consumes your mind controls your life",  
        "take the risk or lose the chance",  
        "every day is a second chance",  
        "if it doesn’t challenge you, it won’t change you",  
        "your dreams don’t work unless you do",  
        "make peace with your past to shape a better future",  
        "you can’t pour from an empty cup; take care of yourself first",  
        "stars can’t shine without darkness",  
        "don’t wait; the time will never be just right",  
        "life rewards action, not intention",  
        "learn to rest, not quit",  
        "the best way out is always through"  
    ]
    return random.choice(thoughts)

def stories():
    stories = [
        "On a quiet, rainy evening, Amelia discovered an old music box in her grandmother’s attic. As she wound it up, a soft, haunting melody filled the room. Suddenly, the air shimmered, and Amelia found herself standing in a bustling 18th-century ballroom. The people around her were dressed in ornate costumes, and they all seemed to know her name. Amelia wasn’t sure if she was dreaming, but one thing was certain—she didn’t know how to get back.",  

        "Every night, under the cover of darkness, Liam visited the abandoned lighthouse at the edge of town. Everyone said it was haunted, but Liam didn’t care. He was drawn to the flickering light that shouldn’t have been there. One night, he climbed to the top and found a woman dressed in tattered 19th-century clothing. She smiled at him and whispered, ‘You’re late.’ Before he could respond, she vanished into the mist.",  

        "Eva had always loved stargazing, but one night, something strange happened. A star seemed to pulse and grow brighter as she watched. The next morning, she woke up to find a small, glowing crystal on her bedside table. The crystal hummed when she touched it, filling her mind with visions of other worlds. Eva realized she’d been chosen for something extraordinary, though she had no idea what.",  

        "In a hidden grove deep in the forest, Noah stumbled upon a tree with golden leaves. He plucked one, and as it crumbled in his hand, he felt a surge of energy. For the next week, everything he touched turned to gold. At first, he thought he was blessed, but soon, the weight of his newfound power began to crush him. How could he undo what had been done?",  

        "Isla was walking home when she found a small, leather-bound book lying on the sidewalk. Inside were detailed entries about her life—things no one else could possibly know. The last entry, however, described a decision she hadn’t made yet, one that would change her future forever. As she read it, she realized she was being watched by someone who knew her better than she knew herself.",  

        "Jason hated the old clock his uncle left him. It was loud, creaky, and always seemed to be running fast. One night, as he tried to wind it, the hands spun wildly, and Jason was thrown into the past—his own past. He was standing in his childhood home, watching his younger self make the very mistakes that had haunted him for years. This was his chance to change everything.",  

        "Underneath the city, in a maze of forgotten tunnels, Sophie found a door with her name etched into it. She pushed it open and entered a room filled with glowing orbs. Each orb contained a memory—some hers, some not. As she touched one, she was pulled into a scene from centuries ago. She realized the orbs weren’t just memories—they were pieces of history she was meant to protect.",  

        "Mark had always been able to hear whispers in the wind, but he never understood them until the day he found the old flute buried in his backyard. When he played it, the whispers turned into voices, guiding him to hidden places filled with treasure and danger. But the voices were demanding, and Mark began to wonder if he was their master or their pawn.",  

        "Mia’s cat, Shadow, had always been strange, but she didn’t realize how strange until the day he brought home a glowing, blue stone. That night, Shadow sat on the windowsill, staring at the moon, and then he spoke. ‘The portal opens tonight,’ he said. ‘We have to go.’ Before Mia could protest, Shadow leapt through the air, and the stone erupted into a swirling vortex.",  

        "After moving into the old farmhouse, Emma started hearing footsteps at night. At first, she thought it was the creaky floorboards, but one evening, she followed the sound to the basement. There, she found a little girl crying. ‘I can’t find my doll,’ the girl said. When Emma handed her the doll she’d found earlier, the girl smiled and faded away, leaving Emma to wonder if she’d just helped a ghost.",  

        "Tom’s grandfather had always told stories about a hidden treasure in the mountains, but no one believed him. When Tom inherited his grandfather’s map, he decided to follow it, more for fun than anything else. After days of searching, he found a chest filled with gold and jewels. But there was also a letter addressed to him, warning him of a curse that came with the treasure.",  

        "In the heart of the desert, Leah discovered a small oasis. At its center was a mirror that didn’t reflect her image—it showed her deepest fears instead. As she stared into it, she saw herself alone, her dreams shattered. But when she turned away, the mirror cracked, and Leah felt a surge of courage she’d never known before. She realized that facing her fears was the only way forward.",  

        "Ben loved the stars, so when he was offered a chance to train for a space mission, he jumped at it. But during the voyage, something went wrong. His ship was pulled into a wormhole, and Ben found himself on a planet with creatures that communicated through light. They taught him about their world and showed him how small and connected the universe truly was.",  

        "Olivia’s grandmother had always worn the same silver ring, saying it was a family heirloom. After her grandmother passed, Olivia found a note hidden in the jewelry box. It read, ‘The ring grants one wish, but choose wisely.’ Olivia hesitated for days before making her wish. When it came true, she realized the cost was higher than she could have imagined.",  

        "At the edge of the ocean, Daniel found a bottle with a message inside. It was written in a language he didn’t recognize, but as he touched it, the words rearranged themselves. ‘Help us,’ it said. Daniel felt a pull toward the horizon, as if the ocean itself was calling him. He knew he had to follow, even though he didn’t know what he would find."  
    ]
    return random.choice(stories)

def poems():
    poems = [
        "the stars whispered secrets to the night,  a tale of love, a tale of fright,  the moon, a witness, silver and cold,  watched as dreams and stories unfold",  

        "in the forest, where shadows play,  the trees hold secrets of another day,  their whispers blend with the evening breeze, a symphony sung by the ancient trees",  

        "beneath the waves, the ocean sighs,  a melody sung to the open skies,  its depths conceal treasures untold,  a world of wonder, fierce and bold",  

        "the mountain stood, proud and high,  its peak kissed softly by the sky,  it watched the world in stoic grace,  a timeless guardian of this place",  

        "the wind carried whispers of the past,  memories fleeting, yet meant to last,  they danced through fields, soft and free,  a chorus sung by the wandering sea",  

        "the flower bloomed in the crack of stone,  a sign of life where none was known,  its petals bright, defying despair,  a reminder that beauty can grow anywhere",  

        "the river flows with endless might,  carving paths through day and night,  its journey long, its purpose clear,  to carry dreams both far and near",  

        "the flame flickered in the darkened room,  a single spark in the endless gloom,  it spoke of hope, it spoke of light,  a beacon shining through the night",  

        "the child laughed, a melody sweet,  their joy a world no pain could defeat,  in their eyes, the stars took flight,  a universe born in pure delight",  

        "the storm raged, wild and free,  its fury roaring across the sea,  yet within the chaos, a peace resides,  a calm that the tempest cannot hide",  

        "the sun rose with a golden hue,  painting the world in colors anew,  its warmth embraced the waking land,  a gentle touch, a guiding hand",  

        "the rain fell soft, a soothing song,  a lullaby for the weary throng,  each drop a kiss, a gentle plea,  to cleanse the earth, to set it free",  

        "in the mirror, a face stared back,  a tale of strength, of what we lack,  its eyes held truths, both dark and bright,  a reflection of the inner fight",  

        "the moonlit path was silent and still,  its glow a guide over valley and hill,  beneath its light, the wanderer roamed,  searching for a place to call home",  

        "the clock ticked on, its hands unkind,  marking the passage of fleeting time,  yet within each tick, a story lay,  of moments lived and dreams that stay",  

        "the bird took flight at break of dawn,  its wings a brushstroke on the morn,  it sang a song of boundless skies,  a hymn to freedom, bold and wise",  

        "in the heart of winter, a fire burned,  its heat a gift for the lost and spurned,  it spoke of warmth, of brighter days,  a promise made in its dancing blaze",  

        "the desert stretched, a sea of gold,  its sands a story of ages old,  the wind its voice, the sun its crown,  a realm where silence wears a gown",  

        "the city slept, its streets at peace,  a moment’s breath, a sweet release,  beneath the stars, its heart beat slow,  a secret rhythm few would know",  

        "the clouds gathered, a painter’s dream,  their shapes and hues a fleeting scheme,  they danced with light, both bold and shy,  a masterpiece upon the sky",  

        "the forest floor was soft and green,  a world of life, both felt and seen,  its creatures thrived in harmony,  a song of balance, wild and free",  

        "the candle’s flame, a gentle glow,  a quiet friend in the evening’s flow,  it cast its warmth, it shared its light,  a guardian through the long, dark night",  

        "the waves embraced the sandy shore,  a timeless dance, forevermore,  their rhythm spoke of endless time,  a story told in fluid rhyme",  

        "the flower leaned toward the sun,  its battle fought, its victory won,  its colors bright, its spirit strong,  a quiet triumph all day long",  

        "the wind sang soft, a lullaby,  its melody soothing the evening sky,  it carried dreams on unseen wings,  a song of hope that gently clings",  

        "the bridge stretched out across the stream,  a path of stone, a builder’s dream,  it carried hearts from side to side,  a link unbroken, long and wide",  

        "the sky at dusk, a canvas vast,  its colors fading, shadows cast,  it spoke of endings, soft and true,  and whispered promises of something new",  

        "the river whispered to the stones,  its voice a hum, a sacred tone,  it told of journeys, old and new,  of lands it loved, of skies it knew",  

        "the sunrise kissed the morning dew,  a fleeting moment, pure and true,  it brought the day with gentle grace,  a gift of light for every place",  

        "the snow fell soft, a blanket white,  transforming the world in quiet light,  each flake a promise, soft and small,  that even winter holds beauty for all'"

    ]
    return random.choice(poems)

def tell_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not.",
        "Water makes up about 60 percent of the human body",
        "The human brain contains around 100 billion neurons",
        "A honeybee can fly up to 15 miles per hour",
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion",
        "Sharks have been around for more than 400 million years",
        "A group of flamingos is called a 'flamboyance'",
        "Bananas are berries, but strawberries are not",
        "The shortest war in history lasted 38 to 45 minutes",
        "An octopus has three hearts",
        "Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs",
        "The longest recorded flight of a chicken is 13 seconds",
        "Jellyfish are 95 percent water",
        "The tallest building in the world is the Burj Khalifa in Dubai, standing at 828 meters",
        "A day on Venus is longer than a year on Venus",
        "Cows have best friends and get stressed when separated from them",
        "Humans share 60 percent of their DNA with bananas",
        "There are more stars in the universe than grains of sand on all the Earth’s beaches",
        "The Great Wall of China is not visible from space with the naked eye",
        "A snail can sleep for three years",
        "It takes approximately 8 minutes and 20 seconds for light from the Sun to reach the Earth",
        "There are more microorganisms in a human’s mouth than there are people on Earth",
        "The Mona Lisa has no eyebrows because it was the fashion in Renaissance Florence to shave them",
        "A single bolt of lightning can contain up to one billion volts of electricity",
        "A year on Mars is 687 Earth days",
        "Elephants are the only animals that cannot jump",
        "There are more possible iterations of a game of chess than there are atoms in the known universe",
        "A cloud can weigh more than a million pounds",
        "The fastest-growing plant in the world is bamboo, which can grow up to 35 inches in a day",
        "The longest-lived species on Earth is the immortal jellyfish, which can revert to its juvenile form after reaching adulthood",
        "The world’s largest desert is not the Sahara, but Antarctica",
        "An adult human has fewer bones than a baby; a baby has around 270 bones, while an adult has 206",
        "A chameleon’s tongue is twice the length of its body",
        "In Japan, there is a tradition of 'forest bathing' or 'Shinrin-yoku', which involves walking in forests for stress reduction",
        "The total weight of ants on Earth once equaled the total weight of humans",
        "It would take a person 17 years to walk to the Moon, if they could walk in space",
        "Honey never spoils, even after thousands of years",
        "In ancient Rome, urine was used as a cleaning agent due to its ammonia content",
        "The moon is slowly drifting away from the Earth at a rate of about 1.5 inches per year",
        "The average person walks the equivalent of three times around the world in a lifetime",
        "The tongue is the strongest muscle in the human body relative to its size",
        "More people are killed by donkeys each year than by airplane crashes",
        "The longest time a person has gone without sleep is 11 days",
        "It rains diamonds on Saturn and Jupiter",
        "An adult human body contains about 100,000 miles of blood vessels",
        "The only letter that does not appear in any U.S. state name is 'Q'",
        "A cow can produce up to 6.5 gallons of milk each day",
        "The Eiffel Tower can be 15 cm taller in the summer due to thermal expansion",
        "Peanuts are not nuts; they are legumes",
        "A blue whale's tongue alone can weigh as much as an elephant",
        "The longest word in the English language without a vowel is 'rhythms'",
        "The world's smallest dog breed is the Chihuahua",
        "Coca-Cola was originally green in color",
        "A crocodile cannot stick its tongue out",
        "The longest hiccuping spree lasted 68 years",
        "Sloths can hold their breath for up to 40 minutes underwater",
        "Cleopatra lived closer to the first Moon landing than to the construction of the Great Pyramid",
        "The average person spends six months of their life waiting for red lights to turn green",
        "The Guinness World Record for the most children born to one woman is 69",
        "Sharks have been around for more than 400 million years, longer than trees",
        "The shortest commercial flight in the world is just 47 seconds long, between two islands in Scotland",
        "You burn more calories sleeping than you do watching television",
        "The first computer virus was created in 1983",
        "A goldfish’s memory span is actually longer than three seconds – it can last months",
        "The longest time anyone has ever survived without food is 382 days",
        "A volcano can produce an ash cloud that is up to 30 kilometers high",
        "A day on Mercury lasts 59 Earth days",
        "The longest human fingernail ever recorded was over 8 feet long",
        "Jupiter’s Great Red Spot is a massive storm that has been raging for at least 350 years",
        "The Eiffel Tower was initially intended to be a temporary structure",
        "The average cloud weighs about a million pounds"
    ]
    return random.choice(facts)

def play_word_game():
    words = {
        "Python": "A programming language named after a comedy group.",
        "Gravity": "A force that attracts objects toward each other.",
        "Electron": "A negatively charged subatomic particle.",
        "Quantum": "A discrete quantity of energy or matter in physics.",
        "Holography": "The science of creating three-dimensional images using light.",
        "Cell": "The basic structural and functional unit of living organisms.",
        "Atom": "The smallest unit of matter, consisting of protons, neutrons, and electrons.",
        "Osmosis": "The movement of water molecules through a semipermeable membrane.",
        "Molecule": "Two or more atoms bonded together.",
        "Chlorophyll": "A green pigment found in plants that helps in photosynthesis.",
        "Velocity": "The speed of something in a specific direction.",
        "Fusion": "The process of combining two atomic nuclei to form a heavier nucleus.",
        "Friction": "The resistance that one surface or object encounters when moving over another.",
        "Bioluminescence": "The production and emission of light by living organisms.",
        "Tectonics": "The study of the structure and movement of Earths crust.",
        "Covalent": "A type of bond where atoms share electrons.",
        "Photosynthesis": "The process by which plants convert light energy into chemical energy.",
        "Turbine": "A machine that converts fluid energy into mechanical energy.",
        "Bacteria": "Microscopic, single-celled organisms that can be harmful or beneficial.",
        "Antibody": "A protein produced by the immune system to neutralize pathogens.",
        "Genetics": "The study of heredity and the variation of inherited characteristics.",
        "Symbiosis": "A relationship between two different species living closely together.",
        "Melanin": "A pigment responsible for the color of skin, hair, and eyes.",
        "Neutron": "A subatomic particle with no charge found in an atoms nucleus.",
        "Celsius": "A temperature scale where water freezes at 0°C and boils at 100°C.",
        "Solar": "Relating to or derived from the Sun.",
        "Chromosome": "A thread-like structure made of DNA that carries genetic information.",
        "Vortex": "A flow pattern in which a fluid moves in a spiral around a central point.",
        "Nucleus": "The central part of an atom or a cell that contains genetic material.",
        "Metabolism": "The chemical processes that occur within a living organism to maintain life.",
        "Virus": "A microscopic agent that infects living cells and reproduces inside them.",
        "Lymphocyte": "A type of white blood cell involved in immune responses.",
        "Acid": "A substance that donates protons or accepts electrons in reactions.",
        "Base": "A substance that accepts protons or donates electrons in reactions.",
        "Magnetism": "The force exerted by magnets when they attract or repel each other.",
        "Kinetics": "The study of the motion of objects and the forces that cause that motion.",
        "Refraction": "The bending of light as it passes from one medium to another.",
        "Magma": "Molten rock beneath Earths surface.",
        "Tissue": "A group of cells that work together to perform a specific function.",
        "Hormone": "A signaling molecule produced by glands to regulate physiological processes.",
        "Ecosystem": "A community of interacting organisms and their environment.",
        "Plasma": "A state of matter consisting of ionized particles, found in stars and lightning.",
        "Zoology": "The scientific study of animals and their behavior.",
        "Botany": "The scientific study of plants and their processes.",
        "Astronomy": "The study of celestial bodies and the universe beyond Earth.",
        "Geology": "The study of Earths physical structure, its history, and its processes.",
        "Biome": "A large ecological area with distinct plant and animal life.",
        "Biochemistry": "The study of the chemical processes and substances in living organisms.",
        "Anatomy": "The study of the structure of organisms and their parts.",
        "Psychology": "The study of the mind and behavior.",
        "Seismology": "The study of earthquakes and the propagation of seismic waves.",
        "Geography": "The study of Earths physical features and the distribution of life.",
        "Meteorology": "The study of weather patterns and atmospheric phenomena.",
        "Ecology": "The study of the relationships between organisms and their environment.",
        "Laws": "Rules established by authorities to govern behavior.",
        "Rhythm": "A pattern of sounds and silences in music or speech.",
        "Volcano": "A rupture in Earths crust that allows molten rock, ash, and gases to escape.",
        "Toxin": "A poisonous substance produced by living organisms.",
        "Isotope": "Atoms of the same element with different numbers of neutrons.",
        "Inductor": "A device used in electrical circuits to store energy in a magnetic field.",
        "Circuit": "A complete path through which electric current can flow.",
        "Amplifier": "An electronic device used to increase the strength of a signal.",
        "Spectroscopy": "The study of the interaction between light and matter.",
        "Alloy": "A mixture of two or more metals.",
        "Momentum": "The quantity of motion an object has, dependent on its mass and velocity.",
        "Spectrometer": "An instrument used to measure the properties of light.",
        "Reflex": "An automatic response to a stimulus.",
        "Reactor": "A vessel or device in which a chemical reaction occurs, often for energy production.",
        "Algorithm": "A step-by-step procedure for solving a problem or performing a task."
    }
    word, hint = random.choice(list(words.items()))
    print(f"Hint: {hint}")
    guess = input("Your guess: ").strip()
    if guess.lower() == word.lower():
        return "Correct!"
    else:
        return f"Incorrect! The word was {word}."

def chatbot():
    todo_lists = {}  # A dictionary to store user to-do lists

    def create_todo_list(list_name):
        if list_name in todo_lists:
            return f"To-do list '{list_name}' already exists."
        todo_lists[list_name] = []
        return f"To-do list '{list_name}' created successfully."

    def add_task(list_name, task):
        if list_name not in todo_lists:
            return f"To-do list '{list_name}' does not exist. Please create it first."
        todo_lists[list_name].append(task)
        return f"Task '{task}' added to '{list_name}' successfully."

    def remove_task(list_name, task):
        if list_name not in todo_lists:
            return f"To-do list '{list_name}' does not exist."
        if task not in todo_lists[list_name]:
            return f"Task '{task}' not found in '{list_name}'."
        todo_lists[list_name].remove(task)
        return f"Task '{task}' removed from '{list_name}' successfully."

    def view_todo_list(list_name):
        if list_name not in todo_lists:
            return f"To-do list '{list_name}' does not exist."
        tasks = todo_lists[list_name]
        if not tasks:
            return f"To-do list '{list_name}' is empty."
        return f"Tasks in '{list_name}': " + "\n".join(tasks)

    def delete_todo_list(list_name):
        if list_name not in todo_lists:
            return f"To-do list '{list_name}' does not exist."
        del todo_lists[list_name]
        return f"To-do list '{list_name}' deleted successfully."
    
    def play_rock_paper_scissors():
        options = ['rock', 'paper', 'scissors']
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in options:
            return "Invalid choice! Please choose rock, paper, or scissors."
        
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!"
    
    print(get_greeting())
    print("I am your chatbot. How can I assist you today?")

    while True:
        user_input = input("Type(Exit OR Bye To Stop):"+"").lower()

        if "time" in user_input:
            print(tell_time())

        elif "open" in user_input and "website" in user_input:
            url = input("Enter website URL: ")
            print(open_website(url))

        elif "what can you do?" in user_input:
            print("I'm Max, your personalized AI Chatbot Assistant. I can open apps and websites for you, tell you jokes, stories, facts and poems, search wikipedia for you, play mini-games with you and much more.")

        elif "open" in user_input:
            app_name = input("Enter application name: ")
            print(open_application(app_name))

        elif "joke" in user_input:
            print(tell_joke())

        elif "thought of the day" in user_input:
            print(thoughts())

        elif "stories" in user_input:
            print(stories())

        elif "poems" in user_input:
            print(poems())

        elif "todo" in user_input:
            if "create" in user_input:
                list_name = input("Enter the name of the To-Do list: ")
                print(create_todo_list(list_name))

        elif "add" in user_input:
            list_name = input("Enter the name of the To-Do list: ")
            task = input("Enter the task to add: ")
            print(add_task(list_name, task))

        elif "remove" in user_input:
            list_name = input("Enter the name of the To-Do list: ")
            task = input("Enter the task to remove: ")
            print(remove_task(list_name, task))

        elif "view" in user_input:
                list_name = input("Enter the name of the To-Do list: ")
                print(view_todo_list(list_name))

        elif "rock paper scissors" in user_input:
            print(play_rock_paper_scissors())

        elif "delete" in user_input:
            list_name = input("Enter the name of the To-Do list: ")
            print(delete_todo_list(list_name))

        elif "country name" in user_input:
            print(countries())

        elif "fact" in user_input:
            print(tell_fact())

        elif "ocean names" in user_input:
            print("The 5 Ocean Names are Pacific, Indian, Arctic, Antarctic and Southern ocean.")

        elif "leader name" in user_input:
            print(presidents())

        elif "math" in user_input or "calculate" in user_input:
            expression = input("Enter the math expression: ")
            print(solve_math(expression))

        elif "wikipedia" in user_input or "search" in user_input:
            query = input("Enter your search query: ")
            print(search_wikipedia(query))

        elif "play" in user_input and "game" in user_input:
            print(play_word_game())

        elif "bye" in user_input or "exit" in user_input:
            print("Goodbye! Have a great day!")
            break

        else:
            print("I'm sorry, I don't understand that command. Please try again.")

chatbot()