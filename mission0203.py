def a(list):
    temp =sorted(list, key=lambda list:list[1], reverse=True)    
    temp.node()
    return temp

if __name__=="__main__":
    poke_list = [["wierdo", 20], ["pika", 35], ["lubdo", 60], ["firero", 120], ["kka", 200]]
    print(poke_list)
    poke_name = input("name?")
    poke_hp = int(input("hp?"))
    poke_list.append([poke_name,poke_hp])
    print(a(poke_list))
    