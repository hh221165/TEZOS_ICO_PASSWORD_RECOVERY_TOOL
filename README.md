# TEZOS_ICO_PASSWORD_RECOVERY_TOOL
Tool to recover Tezos ICO password if parts of the password are known or guessable 

The methods how passwords are created vary from person to person. Never the less in discussions with colleagues, friends and family, I found that everyone has a typical way to create password. Although everyone also thinks his method is unique, I found that there is for most persons a similar pattern how passwords are created. As I could not find any wordlist generator which reflected this way of creating passwords, I tied to create a wordlist generator on my own. The primary goal of this program is to create a wordlist which is as short as possible to minimize brute-force attempts to recover passwords. This program is not brute-forcing itself, it is simply a tool which creates a wordlist which can be provided to brute forcing programs such a “John The Ripper”.

How are passwords created:
Usually each Password has a core word or phrase which has a meaning to the owner. To make it difficult to crack but as easy as possible to remember most persons intend to “salt” the password in different ways. Here are a view examples how passwords are created.

Keyword or phrase with replacement of characters:
“haveaniceday” will be altered to h@ve@niced@y” => substitution of characters 

Leading and/or ending special characters:
“haveaniceday” will be altered into “!haveaniceday!” => leading and ending salt

Adding additional components like year dates or birthdays:
“haveaniceday” will be altered into “haveaniceday2018”   or
“haveaniceday” will be altered into “haveaniceday2018today” => multiple components

Combinations of the above:
$$Ch@rles%%1990ETC!
This example consists of 6 components
•	Leading Salt: $$
•	A keyword with altered characters; Ch@rles
•	A birthyear: 1990
•	Variable salt%%
•	An additional component like initials of family members: ETC
•	Ending salt: !

The GUI of the program allows you to specify multiple components which will be combined together to create a password which follows one ore multiple of these patterns. It allows to have up to 6 components which will be combined in different ways. An explanation for each component is displayed once you move the mouse over the individual input field.

Leading salt: you have the possibility to create a leading salt with individual characters which will be altered.   If you usually use for example the characters “@!?$&” but you know that you never use more than 2 at the same time you will be able to address this. If you never use a leading character salt just leave it blank.

4 Components: here you can enter a list of keywords separated by a whitespace which you can think of that might have been used. An automatic alteration of characters is not implemented at the moment. You would have to add both keywords into the list (e.g. “…. Charles Ch@rles ....”)

Ending salt: equivalent to leading salt
Variable salt: some altering characters which might be in any position between the components. In the above example I have added family member initials as a component. If you are not sure of the correct order that you might have used, you can simply add the initials as characters to the list of salt characters.

Combinations:
The 4 Components and the variable salts can be combined in nearly any order. If you have for example only 3 components just leave one blank. Component 1 will stay on its defined position. This means you can have this component either on first position if leading salt is left empty or you select “leading salt null possible” or on second position if a leading salt is applied.

If you can identify one ore more of the methods similar to how you are creating your passwords, and you have an idea of the individual components, you have a fair chance to recover your password.

If you cannot narrow down the way you create your password into one of the described models you might be better off with a wordlist creator such as “Crunch”, which you can find in the Kali Linux distribution.
