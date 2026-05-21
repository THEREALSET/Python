with open('senha.txt', 'r') as f:
    lines = f.readlines()

    for senha in lines:
        for x in range(0, 2, 1):
            if x % 2 == 0:
                print('wiener:peter')
            else:
                print('carlos:' + senha.strip('\n'))
    
#    for x in range(0, 100, 1):
#        print('wiener:')
#        print('carlos:')
#    print(lines)

#for x in range(0, 100, 2):



