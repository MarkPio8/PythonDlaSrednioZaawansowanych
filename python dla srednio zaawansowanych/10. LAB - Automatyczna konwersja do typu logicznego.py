# options = ['load data', 'export data', 'analyze & predict']
#
# while True:
#     for i in range(0, len(options)):
#         print('%d.%s' % (i+1, options[i]))
#     choice = input("Wich options would like you to choose, or PRESS ENTER TO QUIT: ")
#     if choice:
#         if int(choice):
#             if int(choice) > 0 and int(choice) < len(options)-1:
#                 for i in range(0, len(options)):
#                     if (i+1) == int(choice):
#                         print(options[i])
#             else:
#                  print('Number out of range')
#         else:
#             "This is not a number or it 0"
#     else:
#         break





options  = ['load data', 'export data', 'analyze & predict']

choice = 'x'

def DisplayOpitions(list):
    for i in range(len(list)):
        print('{} - {}'.format(i+1,list[i]))

    a = input('Select option above or press ENTER to exit: ')
    return a

while choice:
    choice = DisplayOpitions(options)
    if choice:
        try:
            choice_num = int(choice) -1
            if choice_num >=0 and choice_num<len(options):
                print(options[choice_num])
            else:
                print('number which you choose schould be visable on MENU!')
        except:
            print('Input should be a number!!!')
    else:
        print("THE END")
