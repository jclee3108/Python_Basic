arr = [1,1,3,3,0,1,1]

new_arr = []
new_arr.append(arr[0])

index = len(arr)

main_i = 0
sub_i = 1

while main_i < index:
    
    print(main_i)

    while sub_i < index:
        if arr[main_i] == arr[sub_i]:
            sub_i += 1
        else:
            new_arr.append(arr[sub_i])
            main_i = sub_i
            sub_i = main_i + 1 
    
    main_i += 1


print(new_arr)

