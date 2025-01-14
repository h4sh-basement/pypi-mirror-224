import torch
import torch.nn as nn

from Janex import *

import numpy as np
import nltk
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

import numpy as np
import random
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out

class ChatDataset(Dataset):

    def __init__(self, X_train, y_train):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

class JanexPT:
    def __init__(self, intents_file_path, thesaurus_file_path, UIName):
        self.intents_file_path = intents_file_path
        self.thesaurus_file_path = thesaurus_file_path
        self.FILE = "data.pth"
        self.UIName = UIName
        self.IntentMatcher = IntentMatcher(intents_file_path, thesaurus_file_path)
        self.intents = self.IntentMatcher.train()
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')

    def pattern_compare(self, input_string, user):
        try:
            self.data = torch.load(self.FILE)
        except:
            self.trainpt()
            self.data = torch.load(self.FILE)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.input_size = self.data["input_size"]
        self.hidden_size = self.data["hidden_size"]
        self.output_size = self.data["output_size"]
        self.all_words = self.data['all_words']
        self.tags = self.data['tags']
        self.model_state = self.data["model_state"]
        self.model = NeuralNet(self.input_size, self.hidden_size, self.output_size).to(self.device)
        self.intents = self.IntentMatcher.train()
        self.model.load_state_dict(self.model_state)
        self.model.eval()
        sentence = input_string

        sentence = self.IntentMatcher.tokenize(sentence)

        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(self.device)

        output = self.model(X)
        _, predicted = torch.max(output, dim=1)

        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        probs = probs[0][predicted.item()]

        for intent in self.intents['intents']:
            if tag == intent["tag"]:
                return intent

    def response_compare(self, input_string, classification):
        print(classification.get("tag"))
        BestResponse = self.IntentMatcher.response_compare(input_string, classification)
        return BestResponse

    def ResponseGenerator(self, response):
        synonyms = []

        response_list = self.IntentMatcher.tokenize(response)

        for token in response_list:
            for syn in wordnet.synsets(token):
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name())

        synonyms = list(set(synonyms))

        synonyms = [s for s in synonyms if s != token]

        new_response = " ".join(synonyms)

        return new_response

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # Default to Noun

    def generate_response_with_synonyms(self, response, strength):
        response_list = word_tokenize(response)
        tagged_response = pos_tag(response_list)
        new_response = []
        prestrength = 0

        for word, tag in tagged_response:
            if prestrength > strength:
                break
            og_word = word
            synsets = wordnet.synsets(word, pos=self.get_wordnet_pos(tag))
            if synsets:
                synonyms = synsets[0].lemmas()  # Use the first synonym
                new_word = synonyms[0].name() if synonyms else word
                if og_word.istitle():
                    new_word = new_word.capitalize()
            else:
                new_word = word
                if og_word.istitle():
                    new_word = new_word.capitalize()

            response = response.replace(og_word, new_word)
            prestrength = prestrength + 1

        response = self.IntentMatcher.ResponseGenerator(response)

        return response

    def trainpt(self):
        try:
            open("train.py", "r")
            os.system("python3 train.py")
        except:
            print("Janex-PyTorch: Train program not detected, downloading from Github.")
            os.system(f"curl -o train.py https://raw.githubusercontent.com/Cipher58/Janex-PyTorch/main/Stock/train.py -#")
            os.system("python3 train.py")
