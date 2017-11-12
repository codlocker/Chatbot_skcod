# CONSUMER
# consumer = {
#     "name": "Batman",
#     "email": "batman@gotham.com"
# }


# PIPELINE
'''
Other Pipeline modules available:
{
    "module": "ner",
    "library": "spacy"
},
{
    "module": "pos",
    "library": "spacy"
},
{
    "module": "parsetree",
    "library": "spacy"
},
{
    "module": "spell_check",
    "library": "botman_textblob"
},
{
    "module": "word_tokenization",
    "library": "spacy"
},
{
    "module": "sentence_tokenization",
    "library": "nltk"
},
{
    "module": "sentence_tokenization",
    "library": "spacy"
},
{
    "module": "lemmatization",
    "library": "spacy"
},
{
    "module": "chunking",
    "library": "spacy"
},
{
    "module": "texttospeech",
    "library": "azure"
},
{
    "module": "texttospeech",
    "library": "amazon"
},
{
    "module": "texttospeech",
    "library": "google"
},
{
    "module": "speechtotext",
    "library": "google"
}
'''

'''
Default and Recommended Pipeline:
'''

pipeline = [
    {
        "module": "spell_check",
        "library": "azure"
    },
    {
        "module": "word_tokenization",
        "library": "nltk"
    },
    {
        "module": "pos",
        "library": "google"
    },
    {
        "module": "parsetree",
        "library": "google"
    },
    {
        "module": "timedate",
        "library": "botman"
    },
    {
        "module": "units",
        "library": "botman"
    },
    {
        "module": "numbers",
        "library": "botman"
    },
    {
        "module": "commonsense",
        "library": "botman"
    },
    {
        "module": "custom_ners",
        "library": "botman"
    }
]
