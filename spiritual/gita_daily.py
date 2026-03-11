import random

GITA_SLOKAS = [

"कर्मण्येवाधिकारस्ते मा फलेषु कदाचन",

"योगस्थः कुरु कर्माणि",

"न जायते म्रियते वा कदाचित"
]

def daily_slok():

    return random.choice(GITA_SLOKAS)
