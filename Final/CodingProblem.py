#problem 3
def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    sum = 0
    digit = False
    for i in s:
        if i in '0123456789':
            sum += int(i)
            digit = True
    if digit == True:
        return sum
    else:
        raise ValueError('there are no digits in s')

#problem 4
def longestRun(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return 1
    else:
        long = []
        point_start = 0
        point_end = 0
        for i in range(len(L)-1):
            if L[i+1] >= L[i]:
                point_end = i + 1
                long.append(point_end - point_start + 1)
            else:
                long.append(point_end - point_start + 1)
                point_start = i + 1
                point_end = i + 1
    return max(long)

#problem 7
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here  
    dict = {}
    for i in range(len(map_from)):
        dict[map_from[i]] = map_to[i]
    decoded = ''
    for j in code:
        decoded += dict[j]
    return (dict, decoded)
        
#problem 6
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + self.name + ' says: ' + stuff      
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff
       
#problem 7  
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            pass

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)      

        
  
                
        
    
    