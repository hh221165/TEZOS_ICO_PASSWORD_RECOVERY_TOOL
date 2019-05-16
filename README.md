# TEZOS_ICO_PASSWORD_RECOVERY_TOOL
Tool to recover Tezos ICO password if parts of the password are known or guessable 

Donations welcome: tz1dBY6SeETnveGf9H2ThvYscV4RtzvAvaUf

When I first heard that people forgot their ICO Password in 2017, I had to chuckle as I could not imagine how that can happen. After the mainnet launch the smile certainly drained my face after I tried several passwords without success. In the following several months I made multiple attempts to find a solution to recover my password. I have played with John The Ripper in combination with Crunch, Andrea Pizzato solution from Github and several others without success. 
I was absolutely sure I created the password in a pattern that I usually use to create my passwords but I just couldn’t find a tool which was reflecting this pattern.
Although the invested amount was not a dramatic loss, I got so annoyed about my stupidity, that I decided to learn how to program good enough, to being able to create a tool on my own which reflects the pattern of password creation that I usually use. So, several months ago I started to learn programming in Python and created a tool which did the trick for me. As I am a lazy guy, I decided to do it in a way to have a user interface to enter the Data needed. I just didn’t want to fiddle around with command line entries. Although the tool is not fully finished and has several limitations, I could not believe my eyes last Sunday when it suddenly displayed “Your password is – “…………………”. The password is 20 characters and consists of 5 different components where each component could have been multiple different options. Due to the advice on the wallet creation page during ICO to use an absolute unique password, I obviously decided to vary one of the components, and did not write it down. With the tool I created I checked several hundred million different combinations before I succeeded. On My computer which is a Windows Six Core machine with 32 GB of RAM, I could check about 1.700 different passwords per second using multiprocessing. 
My funds are meanwhile recovered and transferred to a Trezor Hardware wallet.
Although I know that my code is far from perfect, could be improved a lot and could also be extended with features, I decided to put it on Github for download. Maybe it helps someone else as well. Maybe someone even knows how to get the code running on the GPU (I tried but failed miserably) which should increase the hash -rate significantly. In this case the brute forcing of parts of the password might get much better and stable. In this case I even would consider to put some more efforts in, just for fun.  
If you are successful with it, I would be happy if you let me know. And of course, feel free to donate to my TEZOS donation wallet if you recovered your password successfully and think that I deserve some gratitude for my efforts.
Wallet Address: tz1dBY6SeETnveGf9H2ThvYscV4RtzvAvaUf

If you think my code is crap, that is fine too. As said, I learned how to code because of a need for it. Although I am a technician, the last time I programmed something seriously is about 30 years ago in Commodore Basic and Assembler on a C64. 

######################################

The methods how passwords are created vary from person to person. Never the less in discussions with colleagues, friends and family, I found that everyone has a typical way to create password. Although everyone also thinks his method is unique, I found that there is for most persons a similar pattern how passwords are created. As I could not find any wordlist generator which reflected this way of creating passwords, I tied to create a wordlist generator on my own. The primary goal of this program is to create a wordlist which is as short as possible to minimize brute-force attempts to recover passwords. This program was originally started as a tool to create wordlists, but finally I skiped that and decided to implemented the brute-forcing as well. 

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
