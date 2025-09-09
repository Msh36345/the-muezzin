from services.analyze_files.analyze_hostile_words import hostile_words,hostile_words_pairs,less_hostile_words,less_hostile_words_pairs

def detect_threat(raw_text):
    text = raw_text.lower().split()
    set_text = set(raw_text)
    mach_hostile = hostile_words & set_text
    mach_less_hostile = less_hostile_words & set_text
    mach_hostile_pairs = 0
    mach_less_hostile_pairs = 0
    for pair in hostile_words_pairs:
        for index,word in enumerate(text):
            if pair[0] == word and index != (len(hostile_words_pairs)) and pair[1]==hostile_words_pairs[index+1]:
                mach_hostile_pairs+=1
    for pair in less_hostile_words_pairs:
        for index,word in enumerate(text):
            if pair[0] == word and index != (len(less_hostile_words_pairs)) and pair[1]==less_hostile_words_pairs[index+1]:
                mach_less_hostile_pairs+=1


