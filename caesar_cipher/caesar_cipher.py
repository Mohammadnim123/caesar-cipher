import nltk
nltk.download('words')
original_words_list = nltk.corpus.words.words()
words_list = [word.lower() for word in original_words_list]


def encrypt(string, key):
    
    output = ''
    for letter in string:
        
        if ord(letter)>64 and ord(letter)<91:
            x = ord(letter) - 65
            new = x+key
            new = new%26 + 65
            output+=chr(new)            
        
        elif ord(letter)>96 and ord(letter)<123:
            x = ord(letter) - 97
            new = x+key
            new = new%26 + 97
            output+=chr(new)

        elif letter == ' ':
            output += letter


    return output

def decrypt(string, key):
    return encrypt(string, -key)

def hacking(string):
    trial_list = []
    for i in range(26):
        trial = decrypt(string,i)
        trial_list.append(trial)
    

    def count_words(sentence):
        sentence_words = sentence.split()
        en_word_count = 0

        for word in sentence_words:
            if word.lower() in words_list:
                en_word_count += 1

        return en_word_count

    def most_likely(sentences):
        _max = 0
        _max_sentence = ''

        for sentence in sentences:
            if count_words(sentence) > _max:
                _max_sentence = sentence
                _max = count_words(sentence)
        return _max_sentence

    return most_likely(trial_list)
        
    






if __name__ == "__main__":
    print(hacking('Sd gkc dro locd yp dswoc sd gkc dro gybcd yp dswoc'))

    print(encrypt('It was the best of times, it was the worst of times.',10))
    # print(decrypt('Npibnnbe', 1))