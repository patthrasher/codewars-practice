# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.

def move_zeros(array) :
    new_list = []
    zero_count = 0
    for each in array :

        if each != 0 and each != 0.0 :
            new_list.append(each)

        else :
            st = str(each)

            if st == '0' or st == '0.0':
                zero_count = zero_count + 1
            else :
                new_list.append(each)

    while zero_count > 0 :
        new_list.append(0)
        zero_count = zero_count - 1

    return new_list

print(move_zeros(['a',0,0,'b',None,'c','d',0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
