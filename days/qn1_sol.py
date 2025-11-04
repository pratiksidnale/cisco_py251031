words_seq = input('words (seperated by space):')
print(words_seq)
words = words_seq.split() #''
print(words, type(words))
words_tuple = tuple(words)
print(words_tuple, type(words_tuple))

'''
output_file = open()





'''
with open('qn01_data.text' , 'w') as output_files:
    output_files.write(f'list:{words}\n')
    output_files.write(f'tuple:{words_tuple}\n')

    with open ('qn01_data.txt', 'r')as input_file:
        file_words_list = input_file.readline()
        file_words_list = input_file.readline()
        print(file_words_list_line)
        