def LongestWord(sen): 

  # first we remove non alphanumeric characters from the string
  # using the translate function which deletes the specified characters
  sen = sen.translate(None, "~!@#$%^&*()-_+={}[]:;'<>?/,.|`")

  # now we separate the string into a list of words
  arr = sen.split(" ")

  # the list max function will return the element in arr
  # with the longest length because we specify key=len
  return max(arr, key=len)
    
print LongestWord("the $$$longestasdfasdf# word is coderbyte")  
