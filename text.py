# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
  
def countword()->int:
    file= open("text.txt", "r")
    seq= file.read()
    text= seq.split ()
    word= text[0]
    count=1
    for cur in text[1:]:
        txt= revword(cur)
        if word==txt:
            count+=1
    return count
      
def revword(word:str) -> str:
    word = word.lower()
    return word[::-1]

