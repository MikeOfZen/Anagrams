import collections

class Anagrams:
    def __init__(self):

        self.sorted_dict=collections.defaultdict(list)
        with open("./words_alpha.txt","r") as f:
            for line in f:
                line=line.rstrip()
                key=self.sort(line)
                self.sorted_dict[key].append(line)


    @staticmethod
    def sort(word):
        return ''.join(sorted(word))

    def search(self,word):
        return self.sorted_dict[self.sort(word)]

    def search_allsubsets(self,word,smallest_size=2):
        matches=[]
        lengths=list(range(smallest_size, len(word) + 1))
        lengths.reverse()
        for length in lengths:
            matches_for_length=set()
            for comb in find_combinations(word,length):
                matches_for_length.update(self.search(comb))
            matches.append((length,matches_for_length))
        return matches


def find_combinations(input, length, trunk=''):
    if length == 0:
        return [trunk]
    length -=1

    result=[]
    for i in range(len(input)):
        new_trunk=trunk+input[i]
        residue = input[i+1:]
        result += find_combinations(residue,length,new_trunk)
    return result

if __name__ == "__main__":
    app=Anagrams()
    while True:
        word=input("Enter a word to find all anagrams: ")
        word=word.rstrip()
        if not word.isalpha():
            print("Only alphabetic characters allowed")
            continue
        word=word.lower()
        results=app.search_allsubsets(word)
        for length_list in results:
            print(f"Length {length_list[0]} words - {length_list[1]}")