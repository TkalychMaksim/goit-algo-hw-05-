import re
from typing import Generator
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str)-> Generator[float, None, None]:
    """
    Number generator from text.
    
    Accepts a string and uses regular expressions to search for numbers in the text and
    returns them as a generator
    
    """
    pattern = r'(?<=\s)-?\d+(\.\d+)?(?=\s)'
    matches = re.finditer(pattern, text)
    for match in matches:
        yield float(match.group())
        
        
def sum_profit(text: str, func: callable):
    """
    Calculates the total sum of the numbers found in the text.
    
    This function uses the passed function to generate numbers from text, 
    then calculates and returns their sum.
    
    """
    result = 0
    for number in func(text):
        result += number
        print(number)
    return result

    