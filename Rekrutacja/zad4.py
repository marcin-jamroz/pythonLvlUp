triangle = list()
depth = 0

with open("zadanie_4_triangle_big.txt", "r") as file:    
    for line in file:
        sline = line.strip().split(" ")
        if depth == 0:
            triangle.append([int(sline[0]),])
            depth = depth + 1
            continue
        
        tmp_num_list = [int(0) for x in range(len(sline))]
        for enum, snum in enumerate(triangle[depth - 1]):
            num = int(snum)
            tmp_sum = num + int(sline[enum])
            if tmp_sum > tmp_num_list[enum]:
                tmp_num_list[enum] = tmp_sum
            
            tmp_sum = num + int(sline[enum + 1])
            if tmp_sum > tmp_num_list[enum + 1]:
                tmp_num_list[enum + 1] = tmp_sum
        
        triangle.append(tmp_num_list)
        depth = depth + 1
            

            


print(max(triangle[len(triangle) - 1]))