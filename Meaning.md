ChatGPT did a lot of the work here, but it was super useful, so don't worry I actually learned these things.

_______________________________________________________________________________________________________________________
1. colou?r  
--> color or colour

    3. colo: This part of the pattern simply matches the characters "colo" in sequence.

    2. u?: This is a quantifier that specifies that the character "u" is optional. The question mark ? means that the preceding character "u" 
        may appear zero or one time in the matched text.

    3. r: This part of the pattern matches the character "r" literally.



_______________________________________________________________________________________________________________________
2. (\W|^)[\w.\-]{0,25}@(gmail|deliveryhero)\.com(\W|$)  
--> emails with TLD gmail.com or deliveryhero.com

     1. (\W|^): This part matches a non-word character \W or the start of the string ^. It's a boundary condition to ensure that the email address starts 
        at the beginning of the string or after a non-word character.

    2. [\w.\-]{0,25}: This part matches the local part of the email address. It allows for a sequence of up to 25 characters that can be alphanumeric 
        (\w), dot (.), or hyphen (-). The square brackets [] denote a character class, and the curly braces {} specify the minimum and maximum number of occurrences.

    3. @: This matches the "@" symbol, which separates the local part from the domain part of the email address.
    
    4. (gmail|deliveryhero): This part matches either "gmail" or "deliveryhero".

    5. \.: This matches the dot character "." in the domain part of the email address.

    6. com: This matches the literal string "com".

    7. (\W|$): This part matches a non-word character \W or the end of the string $. It's a boundary condition to ensure that 
        the email address ends at the end of the string or before a non-word character.



_______________________________________________________________________________________________________________________
3. ^(?=.\*[a-z])(?=.\*[A-Z])(?=.\*\d).{6,12}$  
--> PW  
6 to 12 characters in length  
Must have at least one uppercase letter  
Must have at least one lower case letter  
Must have at least one digit  
Should contain other characters  

        1. ^: Asserts the start of the string.
    
        2. (?=.*[a-z]): This is a positive lookahead assertion. It asserts that the string contains at least one lowercase letter ([a-z]) 
            somewhere ahead in the string.
    
        3. (?=.*[A-Z]): Another positive lookahead assertion, ensuring that the string contains at least one uppercase letter ([A-Z]) 
            somewhere ahead in the string.
    
        4. (?=.*\d): Yet another positive lookahead assertion, ensuring that the string contains at least one digit (\d) somewhere ahead in the string.
    
        5. .{6,12}: Matches any character (.) between 6 and 12 times ({6,12}). This ensures that the string length is between 6 and 12 characters.
    
        6. $: Asserts the end of the string.


_______________________________________________________________________________________________________________________
4. ^\#?([a-f0-9]{6}|[a-f0-9]{3})$  
--> hex color code  

    1. : Asserts the start of the string.
    
    2. \#?: Matches an optional # character. The ? quantifier means that the # character may appear zero or one time.
    
    3. ([a-f0-9]{6}|[a-f0-9]{3}): This is a capturing group denoted by (...). It matches either of the following two patterns:

            [a-f0-9]{6}: Matches exactly six characters, where each character is a hexadecimal digit (a through f or 0 through 9).
            [a-f0-9]{3}: Matches exactly three characters, where each character is a hexadecimal digit (a through f or 0 through 9).
            
            The capturing group ([a-f0-9]{6}|[a-f0-9]{3}) captures either a six-character or three-character sequence of hexadecimal digits, 
            representing the RGB (or RGBA) color values.

    4. $: Asserts the end of the string.
    
    


_______________________________________________________________________________________________________________________
5. done$  
$ is looking for anything that ends with that specific string. 

Example: Mastodone
