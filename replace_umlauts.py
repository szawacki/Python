#!/usr/bin/env python

def replace_umlauts(text_string):
    """Replaces umlauts in a given string."""

    result = ''
    char_map = {}

    char_map['Ä'] = 'Ae'
    char_map['Ö'] = 'Oe' 
    char_map['Ü'] = 'Ue'
    char_map['ä'] = 'ae'
    char_map['ö'] = 'oe' 
    char_map['ü'] = 'ue'
    char_map['ß'] = 'ss'

    for char in text_string:
        if char in char_map:
            result += char_map[char]
        else:
            result += char
    
    return(result)

print(replace_umlauts("Übermäßig völlig Öl Ästhetik über"))
