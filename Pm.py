import pprint,sys,pyperclip
def passCopy():
    if(len(sys.argv)<2):
        print("NO account name found.\n Command format: python3 Pm.py [account name]")
        sys.exit()
    else:
        accountName = sys.argv[1]
        accountName = sys.argv[1].lower()
        print(accountName)
        if accountName in passwords:
            pyperclip.copy(passwords[accountName]["password"])
            print("copied to clipboard")
        else:
            print("account not found!\n Care to add?")        
            
def accDetails():
    if(len(sys.argv)<2):
        print("NO account name found.\n Command format: python3 Pm.py [account name]")
        sys.exit()
    else:
        accountName = sys.argv[1].lower()
        print(accountName)
        if accountName in passwords:
            print(passwords[accountName])
        else:
            print("account not found!\n Care to add?")        
    
passwords ={"facebook":{"username":"nos835","password":"12345"},"quora":{"username":"xsel","password":"454a8"}}
accDetails()
passCopy()
