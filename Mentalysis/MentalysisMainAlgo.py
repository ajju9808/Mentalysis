import re
import string

"""NEGATION_LIST will help to check if a word is negated or not, if negated then polarity of the word is reversed"""
NEGATION_LIST = {
    "nahi"
    "na"
    "aint",
    "arent",
    "cannot",
    "cant",
    "couldnt",
    "darent",
    "didnt",
    "doesnt",
    "ain't",
    "aren't",
    "can't",
    "couldn't",
    "daren't",
    "didn't",
    "doesn't",
    "dont",
    "hadnt",
    "hasnt",
    "havent",
    "isnt",
    "mightnt",
    "mustnt",
    "neither",
    "don't",
    "hadn't",
    "hasn't",
    "haven't",
    "isn't",
    "mightn't",
    "mustn't",
    "neednt",
    "needn't",
    "never",
    "none",
    "nope",
    "nor",
    "not",
    "nothing",
    "nowhere",
    "oughtnt",
    "shant",
    "shouldnt",
    "uhuh",
    "wasnt",
    "werent",
    "oughtn't",
    "shan't",
    "shouldn't",
    "uh-uh",
    "wasn't",
    "weren't",
    "without",
    "wont",
    "wouldnt",
    "won't",
    "wouldn't",
    "rarely",
    "seldom",
    "despite",
}

"""
This function will help to calculate the punctuation amphilification of the comment
There are two types of punctuation amphilifers ? and !
"""


class SentimentAnalysis(object):

    def punctuation_amp(self, comment):
        ep_amp = 0
        qm_amp = 0
        """first calculating the ! mark amphilification factor"""
        ep_count = comment.count("!")
        ep_amp = ep_count * 0.2
        """Second calculating the ? mark amphilificaiton factor"""
        qm_count = comment.count("?")
        if qm_count > 1:
            qm_amp = qm_count * -0.2
        """Calculating the total punctuation amphilification score"""
        pun_amp = qm_amp + ep_amp
        if pun_amp > 0.8:
            pun_amp = 0.8
        elif pun_amp < -0.8:
            pun_amp = -0.8
        return pun_amp

    '''
    """
    This function will help to detect and calculate any emoticons in the comment
    The emoticons are stored in a seprate file ???
    """
    def emojis_amp(comment_split):
        emoji_file = open("emoji_file.txt","r")
        data
        for word in comment:
            if word in 
        return (emo_amp)
    '''

    """This function will determine the base sentiment value of the comment"""

    def sentimentOfKeywords(self, comment):
        """lexicon will be the dictionary of all the lexicons and their values"""
        lexicon = {}

        """intens will hold the submation of intensity of the words in the sentence"""
        intens = 0.00

        with open('vader_lexicon.txt') as f:
            lexicon_file = [line.rstrip('\n') for line in f]
        for line in lexicon_file:
            (word, measure) = line.strip().split('\t')[0:2]
            lexicon[word] = float(measure)

        count = 0
        for word in comment:
            for lex in lexicon:
                if word == lex:
                    if comment[count - 1] in NEGATION_LIST:
                        intens = intens + (lexicon[lex] * -1)
                    else:
                        intens = intens + lexicon[lex]
            count += 1
        return (intens)

    def total_value(self, pun, emo, sen):
        if sen / 6 > 1:
            sen = 1
        else:
            if sen / 6 < -1:
                sen = -1
            else:
                sen = sen / 6

        if emo / 3 > 1:
            emo = 1
        else:
            if emo / 3 < -1:
                emo = -1
            else:
                emo = emo / 3
        if pun != 0:
            sen = sen + sen * pun
            if sen > 1:
                sen = 1
            else:
                if sen < -1:
                    sen = -1
        if emo != 0:
            tot = (sen * 0.8) + (emo * 0.2)
        else:
            tot = sen
        return (tot)


class Mentalsis(object):

    def calculatingSentiment(self, comment):

        """pun_amp and emo_amp will applied on the sentence"""
        pun_amp = 0.0
        emo_amp = 0.0
        sen_val = 0.0
        tot_val = 0.0

        """diffrent formats of the comment. used in diffrent forms"""
        comment_split = comment.split()
        comment_punremoved = re.compile('[{0}]'.format(re.escape(string.punctuation))).sub('', comment)
        comment_listed = []
        for w in comment_split:
            if len(w) > 2:
                comment_listed.append(w)
        comment_lowercase = [x.lower() for x in comment_listed]

        """creating the object of SentimentAnalysis Class"""
        sac = SentimentAnalysis()

        """Calculating the punctuation amphilification of the comment and storeing"""
        pun_amp = sac.punctuation_amp(comment)

        '''
        """Calculating the emoticons amphilification of the comment and storeing"""
        emo_amp = emojis_amp(comment_split)
        '''

        """Calculating the base sentiment value of the comment"""
        sen_val = sac.sentimentOfKeywords(comment_lowercase)

        """Calculating the total sentiment value if the comment"""
        tot_val = sac.total_value(pun_amp, emo_amp, sen_val)

        return(tot_val)
