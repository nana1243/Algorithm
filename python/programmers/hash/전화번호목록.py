def solution(phone_book):
    phone_book.sort(key=len)
    idx=0
    
    while idx<=len(phone_book)-1:
        for element in phone_book:
            if element.startswith(phone_book[idx])and element !=phone_book[idx]:
                return False
        idx+=1
        
    return True