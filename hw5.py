def read_single_digit(digit):
    if digit == 1 :
        return '일'
    elif digit == 2 :
        return '이'
    elif digit == 3 :
        return '삼'
    elif digit == 4 :
        return '사'
    elif digit == 5 :
        return '오'
    elif digit == 6 :
        return '육'
    elif digit == 7 :
        return '칠'
    elif digit == 8 :
        return '팔'
    elif digit == 9 :
        return '구'
    else :
        return '영'
    
def read_number(number):
    if number == 0 :
        return '영'
    elif number < 10 :
        return read_single_digit(number)
    elif number < 100 :
        ten_digits = number // 10
        one_digits = number % 10
        if ten_digits == 1 :
            if one_digits == 0 :
                return '십'
            else :
                return '십' + read_single_digit(one_digits)
        else :
            if one_digits == 0 :
                return read_single_digit(ten_digits) + '십'
            else :
                return read_single_digit(ten_digits) + '십' + read_single_digit(one_digits)
    else : 
        hundred_digits = number // 100
        ten_digits = (number % 100) // 10
        one_digits = number % 10
        if number == 100 :
            return '백'
        elif ten_digits == 0 and one_digits == 0 :
            return read_single_digit(hundred_digits) + '백'
        elif ten_digits == 0 :
            return read_single_digit(hundred_digits) + '백' + read_single_digit(one_digits)
        elif one_digits == 0 :
            return read_single_digit(hundred_digits) + '백' + read_single_digit(ten_digits) + '십'
        else :
            return read_single_digit(hundred_digits) + '백' + read_single_digit(ten_digits) + '십' + read_single_digit(one_digits)
number = int(input('세 자리 정수 입력:'))
print(read_number(number))