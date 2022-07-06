# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import itertools as it
CONST_SIZE_MIN = 3
CONST_CUT_PRIORITY = 7

'''def add_rail(lst):
    print("\nInsert the size and the quantity : size,quantity")
    txt = input()
    if txt == "STOP":
        return 0
    lst_txt = txt.split(",")
    size = int(lst_txt[0])
    quantity = int(lst_txt[1])
    for i in range(len(lst[0])):
        if lst[0][i]==size:
            lst[1][i] += quantity
            return 1
    position = 0
    for i in lst[0]:
        if int(i)<int(lst_txt[0]):
            position+=1
        else:
            break
    lst[0].insert(position,size)
    lst[1].insert(position,quantity)
    return 1'''

def add_rail(lst):
    print("\nInsert the size and the quantity : size,quantity")
    txt = input()
    if txt == "STOP":
        return 0
    lst_txt = txt.split(",")
    size = int(lst_txt[0])
    quantity = int(lst_txt[1])
    lst.extend([size]*quantity)
    return 1


#lst_rail_build[rail_take,cut_rail,rail_to_bin,[rail_build_in_store]]

def element_in_list(rail_build,lst_rail_store,lst_rail_build):

    for i in range(len(lst_rail_store)):
        temp_lst_rail_store = lst_rail_store.copy()
        if rail_build==lst_rail_store[i]:
            if i == len(lst_rail_store) - 1:
                temp_lst_rail_store = temp_lst_rail_store[:-1:]
            else:
                temp_lst_rail_store = temp_lst_rail_store[:i:] + temp_lst_rail_store[i + 1::]
            lst_rail_build.append([[lst_rail_store[i]],[[],[],0],0,temp_lst_rail_store])
        if rail_build<lst_rail_store[i]:
            if lst_rail_store[i]-rail_build <=CONST_SIZE_MIN:
                if i == len(lst_rail_store)-1:
                    temp_lst_rail_store = temp_lst_rail_store[:-1:]
                else:
                    temp_lst_rail_store = temp_lst_rail_store[:i:] + temp_lst_rail_store[i+1::]
                lst_rail_build.append([[lst_rail_store[i]],[[lst_rail_store[i]],[lst_rail_store[i]-rail_build],1],lst_rail_store[i]-rail_build , temp_lst_rail_store])
            else:
                if i == len(lst_rail_store) - 1:
                    temp_lst_rail_store = temp_lst_rail_store[:-1:] + [temp_lst_rail_store[-1]-rail_build]
                else:
                    temp_lst_rail_store = temp_lst_rail_store[:i:] + [temp_lst_rail_store[i]-rail_build] + temp_lst_rail_store[i + 1::]
                lst_rail_build.append([[lst_rail_store[i]], [[lst_rail_store[i]],[lst_rail_store[i]-rail_build],1], 0, temp_lst_rail_store])

def all_elemets_of_list(lst_rail_store,lst_need_build):
    lst_rail_build = []
    element_in_list(lst_need_build[0],lst_rail_store,lst_rail_build)
    for i in range(1,len(lst_need_build)):
        temp = []
        for h in range(len(lst_rail_build)):
            lst_test = []
            element_in_list(lst_need_build[i], lst_rail_build[h][3], lst_test)
            for j in range(len(lst_test)):
                lst_test[j][0].extend(lst_rail_build[h][0])
                lst_test[j][1][2]+=lst_rail_build[h][1][2]
                lst_test[j][1][0].extend(lst_rail_build[h][1][0])
                lst_test[j][1][1].extend(lst_rail_build[h][1][1])
                lst_test[j][2] += lst_rail_build[h][2]
            temp.extend(lst_test)
        lst_rail_build = temp.copy()
    return lst_rail_build

'''def do_all_possibility(lst_rail_store,lst_need_build):
    #tupple_rail_all_possibility = list(it.permutations(lst_rail_store,len(lst_rail_store)))
    #lst_rail_all_possibility = []
    lst_rail_all_possibility = lst_rail_store.copy()
    for i in tupple_rail_all_possibility:
        temp = []
        for j in i:
            temp.append(j)
        lst_rail_all_possibility.append(temp)
    all_result =[]
    for k in lst_rail_all_possibility:
        print(k)
        all_result.extend(all_elemets_of_list(k,lst_need_build))
    return all_result'''

def find_best_possibility(lst_rail_store,lst_need_build):
    all_possibility = all_elemets_of_list(lst_rail_store,lst_need_build)
    position = [0]
    best_situation = all_possibility[0][1][2]*CONST_CUT_PRIORITY + all_possibility[0][2]
    for i in range(1,len(all_possibility)):
        temp_situation = all_possibility[i][1][2]*CONST_CUT_PRIORITY + all_possibility[i][2]
        if temp_situation == best_situation:
            position.append(i)
        if temp_situation<best_situation:
            best_situation = temp_situation
            position =[i]
    best_lst = []
    lst_number = []
    for k in position:
        if all_possibility[k][0] not in lst_number:
            best_lst.append(all_possibility[k])
            lst_number.append(all_possibility[k][0])
    return best_lst

def print_solution(lst_solution,lst_need):
    counteur = 1
    print("The best solution(s) are : ")
    for solution in lst_solution:
        print("\tSolution number: ",counteur)
        for i in range(len(lst_need)):
            print(f'\t\t- Take the rail : {solution[0][(-1)*(i+1)]} meter, for the {lst_need[i]} meter section')
        print("\tCut Section : ", counteur)
        for j in range(len(solution[1][0])):
            print(f'\t\t- Cut the rail : {solution[1][0][(-1)*(j+1)]} meter, still {solution[1][1][(-1)*(j+1)]} meter')
        counteur+=1
        print("\n")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    menu = 6
    rail = []
    zone = []
    while (menu):
        print(" 0 - Exit\n", "1 - Add one rail\n", "2 - Add some rails\n", "3 - Add one zone\n", "4 - Add some zone\n", "5 - Calculate\n")
        menu = int(input())
        if menu == 1:
            add_rail(rail)
            print(rail)
        if menu == 2:
            print("Insert some rail, for stop write \"STOP\"")
            loop_continue = True
            while (loop_continue):
                loop_continue = add_rail(rail)
            print(rail)
        if menu == 3:
            add_rail(zone)
            print(zone)
        if menu == 4:
            print("Insert some rail, for stop write \"STOP\"")
            loop_continue = True
            while (loop_continue):
                loop_continue = add_rail(zone)
            print(zone)
        if menu == 5:
            best = find_best_possibility(rail,zone)
            print_solution(best,zone)


'''    a = [1,2,3,4,5,6,7]
    d = [3.2,4]
    c = find_best_possibility(a,d)
    print_solution(c,d)'''


    #c = all_elemets_of_list(a,d)
    #print(c)
    #print(list(it.permutations(a,7)))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
