from palindrome_list import palindrome

def test_palindrome_true():
    assert palindrome(["hannah"]) == True

def test_palindrome_false():
    assert palindrome(["boy"]) == False

def test_palindrome_num_true():
    assert palindrome(["12321"]) == True

def test_palindrome_num_false():
    assert palindrome(["123421"]) == False

def test_palindrome_sentence_true():
    assert palindrome(["Doc, note: I dissent. A fast never prevents a fatness. I diet on cod"]) == True

def test_palindrome_sentence_false():
    assert palindrome(["Naomi, did I moan, today?"]) == False
