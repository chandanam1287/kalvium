def spell_out_number(num):
    
    if num == 0:
        return "zero"

    
    number_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                    19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
                    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
                    90: 'ninety', 100: 'hundred', 1000: 'thousand'}

    
    if num in number_words:
        return number_words[num]

    
    if num < 100:
        tens = (num // 10) * 10
        ones = num % 10
        return f"{number_words[tens]}-{number_words[ones]}"

    
    if num < 1000:
        hundreds = num // 100
        tens = num % 100
        if tens == 0:
            return f"{number_words[hundreds]} {number_words[100]}"
        else:
            return f"{number_words[hundreds]} {number_words[100]} {spell_out_number(tens)}"

    
    if num < 10000:
        thousands = num // 1000
        hundreds = num % 1000
        if hundreds == 0:
            return f"{number_words[thousands]} {number_words[1000]}"
        else:
            return f"{spell_out_number(thousands)} {number_words[1000]} {spell_out_number(hundreds)}"

    
    return "number out of range"


number = int(input("Enter a number: "))
print(spell_out_number(number))
