Marks = {

    "Normi" : "Naughty",
    "Kabul" : "Rampage",
    "Messi" : "Looser",
    "Romina":"Country",
    "Sona"  : "New" ,   
    "Rose"  : "Queen"
}
print(Marks["Messi"])   
print(type(Marks))      #type of the dict
print(Marks.items())    #all item of marks dict
print(Marks.keys())     #all keys of marks
print(Marks.values())   #all values of marks dict
Marks.update({"Rose": "Nona", "Sona": "Bitch" , "Luna" : "Mister"})  # we modify the dict and update the rose key and now it's value is NONA
                                                                     # Even we can add new key values to update the dict like we have added the luna one
print (Marks.get("Rose") , ("Sona"), ("Rin"))
