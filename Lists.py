if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        user_input = input()
        user_input_split = user_input.split(' ')
        command = user_input_split[0]
        if command == "insert":
            pos = int(user_input_split[1])
            val = int(user_input_split[2])
            my_list.insert(pos,val)
        elif command == "append":
            val = int(user_input_split[1])
            my_list.append(val)
        elif command == "print":
            print(my_list)
        elif command == "remove":
            val = int(user_input_split[1])
            my_list.remove(val)
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.remove(my_list[-1])
        elif command == "reverse":
            my_list.reverse()
        else: print("Wrong, Command!\n")
