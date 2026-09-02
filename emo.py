emotonic = "v.v"  #global variable
emoticon= "v_v"

def main ():
    global emotonic                   #here we are calling global variable... reaching out the global variable so can change the value inside the function..
    global emoticon                   #we can reach for multiple var
    say("Somebody there?")

    emotonic = ">.<"                  #local variable more like a secrect container that's just limited to this funtion..
    say("Oh, Hi!!")

    emoticon = ":)"                   #also local that stay in function only no connection with global var
    say("Sup!")

def say (phrase):
    print(phrase + " " + emotonic and emoticon)
    
    
main()
                    #but don't ever use global var in your function it'll fuck your code will cause
                    #that bugs that won't be easy to chase so avoide and use only Return funtion