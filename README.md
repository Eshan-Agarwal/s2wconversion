# Spoken English To Written English Conversion system (s2wconversion)

* This repository contain library which convert spoken english like "Triple A" to written English like AAA or "Double A" to AA.
* To use this library you have to simply install it using pip and write from conversion import conversion (See demo.py)

#### Installation

#### Dependencies
#### s2wconversion requires:

* Python (>= 3.5)
* NumPy (>= 1.11.0)
* speech_recognition

#### User installation

If you already have a working installation of numpy and speech_recognition, the easiest way to install s2wconversion is using pip

pip install s2w

#### Conversion 

* conversion directory contain converion.py file which have spoken to written funtion as per above rules
* run demo.py file to see how to convert trascript paragraph such as "I worked at Triple a" to "I worked at AAA". After run demo.py it    says "Say Something" then spoke anything you want then by using google speech recognition services it trascript paragraph spoken with abbrevations conversion rules.

#### conversion rules
* conversion rules directory contain rules.md file and rules.py file.
* In rules.md file i explained about adding some grammer rules such as Part of speech in a paragraph or decontracted phrases
* rules.py file contain some of these rules implemented
* We convert transcript speech into tokens then after apply nltk pos_tagg to detect pos for words and implement some rules
(See rules.md)

#### Future implementations and contributions
* This repo always open for open source contributions.
* We can add some more pos tagging rules and implement it to our library.
* Also we can use deep learning pos tagging for get better accuracy and add more grammer rules.
* Can add some more abbrevations such as we can add rules for "AAAA", "AAAAA" etc.I think of quad a, pent a etc.


#### LICENSE

GNU General Public License v3.0 (gplv3)
