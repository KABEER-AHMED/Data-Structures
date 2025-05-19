class Deque():
    def __init__ (self):
        self.deque = []
    def addFront(self,item):
        self.deque.insert(0,item)
    def addRear(self,item):
        self.deque.append(item)
    def removeFront(self):
        return self.deque.pop(0)
    def removeRear(self):
        return self.deque.pop()
    def isEmpty(self):
        return not bool(self.deque)
    def Size(self):
        return len(self.deque)
    
# creating the logic for the program
def Palindrome_checker(word):
    deque = Deque()
    for letter in word:
        deque.addRear(letter)
    same = True
    while deque.Size()>1 and same:
        first_letter = deque.removeFront()
        last_letter = deque.removeRear()
        if first_letter != last_letter :
            same = False
    return same

# Main program
print("Hello there !, i see you want to check whether you word is a palindrome or not! ")
word = input("enter the word please: ")
result = Palindrome_checker(word)
if result:
    print(f"Congratulations! , the word {word} is a palindrome")
else:
    print(f"Sorry, the word {word} is not a palindrome")