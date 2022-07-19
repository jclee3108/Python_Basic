# array	commands	return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
commands_sub = []

#print(commands[0][0])

#print(array[1:3])

start = 0 
end = 0 
sel = 0
count = 0 
main_count = 0
result = []


for main_i in commands: 
    main_count += 1

    commands_sub = main_i

    #print(commands_sub)
       
    count = 0
    for i in commands_sub:

        count += 1
        if count == 1:
            start = i
        elif count == 2:
            end = i    
        elif count == 3:
            sel = i
        end

    else:

        array2 = sorted(array[start-1:end])

        result.append(array2[sel-1])
else:
        print(result)




