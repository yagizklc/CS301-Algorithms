A = ["BATURAY", "GORKEM", "GIRAY", "TAHIR", "BARIS"]

def longest(A:list) -> str:
    """
    returns the longest string in list
    """
    longest = ""
    for i in A:
        if len(i) > len(longest):
            longest = i
    return longest

def fill_name(A:list, longest_name_len: int) -> dict:
    """
    adds 'A' at the end of names until 
    they are as long as the longest string in list
    """

    for i in range(len(A)):
        diff = longest_name_len - len(A[i])
        if diff > 0:
            for k in range(diff): 
                A[i] += 'A'  


def convert_ascii(A:list) -> None:
    """
    converts each str into lists of int
    which are ascii values deducted by 'A'
    """
    for i in range(len(A)):
        ascii_list = []
        for k in range(len(A[i])):
            ascii_list.append( ord(A[i][k]) - ord('A') )
        A[i] = ascii_list

def convert_str(A:list):
    """
    converts each ascii_list into str
    which is composed of corresponding chars of ints
    """
    for i in range(len(A)):
        name = []
        for k in range(len(A[i])):
            name.append( chr( (A[i][k]) + ord('A') ) )
        A[i] = ''.join(name)

def name_map(A:list, original_names:list) -> dict:
    """
    maps enhanced names to original names
    """
    return {A[i]: original_names[i] for i in range(len(original_names))}

