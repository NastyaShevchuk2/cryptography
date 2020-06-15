test = "quatre jutges dun jutjat mengen fetge dun penjat"


def create_dictionary2(txt):
    dictionary = {}
    for x in set(txt):
        dictionary[x] = txt.count(x)/len(txt)
    return dictionary

import matplotlib.pyplot as plt
test_dict = create_dictionary2(test)
plt.bar(test_dict.keys(), test_dict.values(), width=0.5, color='g')

plt.show()