class TrieNode1:

    def __init__(self):
        self.children = [0] * 58                            # number of child nodes for alphabets

        self.end = False                                    # to know the end of the word
        self.index_list1 = []                               # index list to store the index


class TrieNode2:

    def __init__(self):
        self.children = [0] * 10                            # number of child nodes for numbers

        self.end = False                                    # to know the end of the word
        self.index_list2 = []                               # index list to store the index


class Trie:

    def __init__(self):
        self.root1 = TrieNode1()                            # first root used for alphabets
        self.root2 = TrieNode2()                            # second root used for numbers

    def get(self, ch):
        return ord(ch) % 65                                 # function to mod the characters to index

    def get2(self, ch):                                     # function to get the index
        return ord(ch) - 48

    def add(self, word, id, index):  # k+l

        """
        Algorithm: This add function takes in 3 parameters which are the word, id and the index of the record, the function adds the record to the trie, it uses two loops, one to add the words and the second to add the numbers,
        the loops checks for the position of the character to append it to the respective index list. The if condition is used to create a new node if the character is also present. Then it sets the end of the wordd and appends the index
        to the respective index lists.
        :param word: the word that is passed through
        :param id:   the id that is passed through
        :param index: the record index
        precondition: word, id and the index
        Time Complexity:  Worst Case: O(k+l), Best Case: O(1) where k is the length of the id and l is the length of the word
        Space Complexity: O(1)
        :return: no return
        """

        current = self.root1                                # the current node for characters
        for letter in word:
            current.index_list1.append(index)               # append to the index list
            position = self.get(letter)                     # the position of the character
            if current.children[position]:                  # checks the character if present
                current = current.children[position]
            else:
                new_trie = TrieNode1()                      # if character not present makes a new node
                current.children[position] = new_trie
                current = current.children[position]

        current.end = True
        current.index_list1.append(index)                   # append the index to the index list

        # numbers
        current = self.root2                                # the current node for numbers
        for number in id:
            current.index_list2.append(index)               # append the to the index list
            position = self.get2(number)                    # the position of the number
            if current.children[position]:
                current = current.children[position]
            else:
                new_trie = TrieNode2()                      # if number not present makes a new node
                current.children[position] = new_trie
                current = current.children[position]

        current.end = True
        current.index_list2.append(index)                   # append the index to the index list

    def search(self, word, id):

        """
        Algorithm: This add function takes in 2 parameters which are the word and the id, the function searches for the word and id, it uses two loops to search, the first loop gets the position of the character and checks for the current node
        it then returns the current word using the index list of the words. The second loop gets the position of the character and checks for the current node it then returns the current id using the index list of the words.
        :param word: the word that is passed through
        :param id:   the id that is passed through
        precondition: word and id
        post-condition: reutrn list of indexes
        Time Complexity:  Worst Case: O(k+l), Best Case: O(1) where k is the length of the id and l is the length of the word
        Space Complexity: O(1)
        :return: list of indexes
        """

        current = self.root1                                # current node for alphabets
        for letter in word:
            position = self.get(letter)                     # getting the position
            stored_letter = current.children[position]
            if not stored_letter:                           # if found return the letter else return empty list
                return []
            current = stored_letter

        return1 = current.index_list1

        current = self.root2                                # current node for numbers
        for number in id:
            position = self.get2(number)                    # getting the position
            stored_letter = current.children[position]
            if not stored_letter:                           # if found return the number else return empty list
                return []
            current = stored_letter

        return2 = current.index_list2

        return return1, return2

# general idea of implementing a trie taken from https://www.geeksforgeeks.org/trie-insert-and-search/


def query(filename, id_prefix, last_name_prefix):
    """
    Algorithm: Open the file and read through the lines, initialise 2 empty strings one to store the characters the other for temporary storage. Concatenating the lines of the file and then starting a for loop to check
    te character only between A to Z, a to z and 0 to 9. Then the space is checked and if there is a space it check the column by the column counter, if its the first column then set the string as id, and if its on the
    third column set it as word(last_name) and increment the columns in the end. Then if there is a new line, add the word, id and the index to the trie and increment the index to the next record and set the column back
    to zero. A trie object is created and trie search takes place to find the respective prefix_id and prefix_last_name. Two lists are returned as I have one trie using two different nodes, one for the alphabets and one
    for the id. Overlaps are searched in the end to find the matching records and the final list is returned.
    :param filename: the file that is passed for the function
    :param id_prefix: the id that is entered to find a match
    :param last_name_prefix: the name that is entered to find a match
    precondition: word and id
    post-condition: list of indexes
    Time Complexity: O(k+l+n_k+n_l) where k is the length of id_prefix, l is the length of last_name_prefix, nk is the number of records matching the id_prefix and nl the number of records matching the last_name_prefix
    Space Complexity: O(T+NM) T is the number of characters in all identification numbers and all last names and NM is reading the input
    :return: list of indexes
    """
    with open(filename, 'r') as myFile:                     # opening the file using a "with" command so the file gets automatically closed
        test = myFile.read()

    mainString = ''                                         # empty string to store the characters from the file
    newString = ''                                          # temporary empty string
    trie = Trie()

    for line in test:                                       # concatenating the lines of the file. O(N)
        mainString += line

    column = 0                                              # counter to check columns
    index = 0                                               # counter to check index
    id = ''                                                 # empty string to store id
    word = ''                                               # empty string to store word

    for character in range(len(mainString)):                # looping through the main string

        if 97 <= ord(mainString[character]) <= 122 or 65 <= ord(mainString[character]) <= 90 or 48 <= ord(
                mainString[character]) <= 57:
            newString += mainString[character]              # concatenating to a temp string
        elif ord(mainString[character]) == 32:              # checking for empty space
            if column == 1:                                 # if its the first column
                id = newString                              # then set it as id
            if column == 3:                                 # if its the third column
                word = newString                            # then set it as last name
            column += 1                                     # increment the columns
            newString = ''                                  # empty the temp string
        elif ord(mainString[character]) == 10:              # if there is a new line found
            trie.add(word, id, index)                       # then add the word, id and the index to Trie
            index += 1                                      # and increment index for the next record
            column = 0
            newString = ''                                  # initialise the string to empty

    a = trie.search(last_name_prefix, id_prefix)            # searching the id and the last name

    result = []
    for element in a[0]:                                    # finding the intersection to get the final id
        if element in a[1]:
            result.append(element)

    return result


if __name__ == "__main__":

    input_file = input("Enter the file name of the query database:  ")
    id_no = input("Enter the prefix of the identification number: ")
    last_name = input("Enter the prefix of the last name : ")
    filename = query(input_file, id_no, last_name)
    print("---------------------------------------------------------------------")
    obj = Trie()
    my = obj.search(id_no, last_name)

    records = len(filename)
    print(str(records) + " record found")

    for i in filename:
        print("Index number: " + str(i))
    print("---------------------------------------------------------------------")
    print("Program end")
