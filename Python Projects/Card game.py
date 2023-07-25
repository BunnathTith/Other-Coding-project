import random
def deal():
    num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    shape = ['D', 'C', 'H', 'S']
    card = []
    for i in range(13):
        for j in range(4):
            card.append(num[i]+shape[j])
    random.shuffle(card)
    #print (len(card))
    return card

def points(lst):
    point = 0
    holder_lst = []
    for ele in lst:
        if ele[0] == 'A':
            ele = '1'+ele[1]
            
        if ele[0] in ['J', 'Q', 'K']:
            if ele[0] in holder_lst:
                point += 10
                holder_lst.remove(ele[0])
            else:
                holder_lst.append(ele[0])        
        elif ele[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if '10' in ele: #'10X' can also pass the condition as i only checl ele[0], so it sees it as a '1X'
                n_ele = 10
            else:
                n_ele = int(ele[0])
                
            if 10-n_ele in holder_lst:
                point += 5
                holder_lst.remove(10-n_ele)
            else:
                holder_lst.append(n_ele)
                
    #print (holder_lst)
    point -= len(holder_lst)
    return point

lst = deal()
lst1 = lst[:(len(lst)//2)]
lst2 = lst[(len(lst)//2):]
p1 = points(lst1)
p2 = points(lst2)
print("Player 1 has {} points".format(p1))
print("Player 2 has {} points".format(p2))
if p1 > p2:
    print ("Player 1 Wins")
elif p1 < p2:
    print ("Player 2 Wins")
else:
    print ("It's a tie")
    
    
        
