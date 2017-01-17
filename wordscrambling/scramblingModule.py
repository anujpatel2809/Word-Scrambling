'''
Created on Dec 26, 2016

@author: Anuj
'''

import random

class WordScrambling:
    def scrambleFile(self,ip_file_name) :
        new_list = []
        try :
            ip_file = open(ip_file_name,'r')
            ip_file.seek(0)
            ip_string = ip_file.read()
            word_list = ip_string.split()
            
            for word in word_list :
                length = len(word)
                if length <= 3 :
                    new_list.append(word)
            
                else :
                    flag = False
                    if(word[-1] in ',?.;!') :
                        length -= 1
                        flag = True
                    scramble_word = self.scramble(word[0:length])
                    if(flag == True) :
                        scramble_word = scramble_word + word[-1]
                    new_list.append(scramble_word)
            
            op_string = ' '.join(new_list) 
            ip_file_name_list = ip_file_name.split('.')
            op_file_name = ip_file_name_list[0] + 'Scrambled.' + ip_file_name_list[-1]
            op_file = open(op_file_name,'w+')
            op_file.write(op_string)
            op_file.close()
            ip_file.close()
            return(op_file_name)
        
        except FileNotFoundError :
            raise FileNotFoundError('File does not exist')
        
        except ValueError :
            raise ValueError('Value is out of bound')
        
        except BufferError :
            raise BufferError('Buffer is Full')
        
        except EOFError :
            raise EOFError('File is Empty')
        
        except :
            raise Exception("Something Wrong happend, Please try aganin later")
             
    def scramble(self,word):
        
        length = len(word)
        if length > 3 :
            word_list = list(word)
            for i in range(length - 2) :
                index1 = random.randint(1, length - 2)
                index2 = random.randint(1, length - 2)
                while index1 == index2:
                    index2 = random.randint(1, length - 2)
        
                temp = word_list[index1]
                word_list[index1] = word_list[index2]
                word_list[index2] = temp 
                  
            return ''.join(word_list)
        else:
            return word

