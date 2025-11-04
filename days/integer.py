numbers = list(map(int, input("Enter integers seperated by spaces ").split()))

total = sum(numbers)
average = total/len(numbers)

with open ("numbers_data.txt", "w")as file:
    file.write(f'numbers:{numbers}\n')
    file.write(f'sum:{total}\n')
    file.write(f'average:{average}\n')
    
    print('\nnumbers_data.txt')

    print('\nreading from file:')
    with open ("numbers_fata.txt","r")as file:
        content = file.read()
        print(content)