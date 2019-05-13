import re
import string

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

IDIOME_LIST = {
    "A blessing in disguise": 1,
    "A dime a dozen": 0.3,
    "Break a leg": 0.5,
}

class SentimentAnalysis(object):

    def punctuation_amp(self, comment):
        ep_amp = 0
        qm_amp = 0
        ep_count = comment.count("!")
        ep_amp = ep_count * 0.2
        qm_count = comment.count("?")
        if qm_count > 1:
            qm_amp = qm_count * -0.2
        pun_amp = qm_amp + ep_amp
        if pun_amp > 0.8:
            pun_amp = 0.8
        elif pun_amp < -0.8:
            pun_amp = -0.8
        return pun_amp
    
    def sentimentOfKeywords(self, comment):
        
        lexicon = {}
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

    def idioms_check(self, comment):

        idioms = IDIOME_LIST
        iv = 0
        for idiom in idioms:
            n = len(idiom.split())
            ll = 0
            ul = n - 1
            while ul < len(comment):
                if idiom.split() == comment[ll:ul + 1]:
                    iv += idioms[idiom]
                    del comment[ll:ul + 1]
                ll += 1
                ul += 1
        return comment, iv

class Mentalsis(object):

    def calculatingSentiment(self, comment):
        
        pun_amp = 0.0
        emo_amp = 0.0
        sen_val = 0.0
        tot_val = 0.0
        idm_val = 0.0
        sac = SentimentAnalysis()
        comment_split = comment.split()
        comment_punremoved = re.compile('[{0}]'.format(re.escape(string.punctuation))).sub('', comment)
        comment_listed = []
        for w in comment_split:
            if len(w) > 2:
                comment_listed.append(w)
        comment_lowercase = [x.lower() for x in comment_listed]
        pun_amp = sac.punctuation_amp(comment_split)
        comment_lowercase, idm_val = sac.idioms_check(comment_lowercase)
        sen_val = sac.sentimentOfKeywords(comment_lowercase)
        tot_val = sac.total_value(pun_amp, emo_amp, sen_val+idm_val)
        return(tot_val)
