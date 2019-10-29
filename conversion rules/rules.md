#                                           Spoken English - Written English Conversion         
                    

* A sentence must adhere to specific "grammar rules". These rules are pretty basic hence the reason they can be taught in primary school.
  Problem is most people don't follow grammar rules when writing or speaking.
* So in this document I focused on how can we add these rules also there are different kinf of rules for which we first need to focus on text that follows the rules.
* Based on this premise here is what I would do

a) First we input transcript of speech recognition system (in our case i use Google Speech Recognition service)

b) Convert paragraph transcipted into tokens.

c) Run NLTK POS Tagger on string (once we know the Parts of Speech we can code rules)

d) Identify tokens whose part of speech breaks the grammar rules of a sentence (sentences shouldn't end in a preposition)

e) Identify tokens that a sentence could end with based on grammar rules (Nouns are a great start)

f) Find a large well punctuated grammatically correct corpora of text and remove the punctuation.

g) Try your "new rules" out on adding punctuation to the corpora. Adjust your rules. Rinse and Repeat

h) We can add more rules like decontracted phrases like will not to won't etc 

* Check rules.py files in which i implement such rules.
