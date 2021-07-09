from appJar import gui

# these variables are arrays with the alphabet stored so we can shift them
letterArr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]  # lowercase array
upperArr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  # uppercase array

choice = ""  # global choice array which stores either "Encrypt" or "Decrypt"
kill = 0  # stops the encryption incase of an error if set to 1

# this function executes on button press
def whatHappens(choices):
    global choice  # calls in the global variable choice
    # sets choice to choices (either "Encrypt" or "Decrypt") depending on the button clicked
    choice = choices
    encryption()  # executes the encryption function

# this is a custom length function
def length(string):
    num = 0  # sets a local variable to 0
    for letter in string:  # for each letter that is in the string
        num += 1  # add a number to the local variable
    return num  # returns the length after completion

# Function Encryptkey, returns the encryption array
def encryptKey():
    global kill #calls in the global kill function
    key = app.getEntry("key")  # gets the entry for the key
    if key: #checking if key exists
        #executes if key exists and isnt empty
        kill = 0 # sets kill to 0
        i = 0 #sets i to 0
        encryptionKey = [] #defines an empty array
        for letter in key: #for each letter that exists in the key
            i = 0 # sets i to 0
            while i <= 25: #while i is less than or equals to 25
                if letter == letterArr[i]: #if the letter equals to the letter array
                    encryptionKey = encryptionKey + [i] #adds the number to the array

                i += 1 # adds 1 to i each time the letter doesnt exist in the array
        return encryptionKey # returns the encryrption key
    else: #if key doesnt exist
        kill = 1 #sets kill to 1
        app.errorBox("Error", "Please insert a key") # sends an error box 
#function for the "Back" button
def goBack():
    app.hideButton("Back") #hides the button "Back"
    app.clearTextArea("response") #clears the text area of "Response"
    app.clearEntry("key") # Clears the entry in the input "Key"
    app.clearEntry("strings") # Clears the entry in the input "Strings"
    app.hideLabel("responses") # hides the lavel responses
    app.hideTextArea("response") #"Hides the text area "Response"
    app.showLabelFrame("Encryption") #Shows the label frame "Encryption"

#Encryption/Decryption Function
def encryption():
    global kill #calls in the kill variable
    i2 = 0 #local variable for encryption
    i3 = 0 #local variable for encryption
    number = 0 #local variable for encryption
    newStr = "" #local string for storing the encrypted string
    strEncrypt = app.getEntry("strings") #gets the value inserted into the string insert

    keyArr = encryptKey() #gets the encryption key from the function "encryptKey"
    if strEncrypt: #checks if the string returned from the insert exists and isnt null
        #if it exists
        if kill == 0: #if kill is set to 0 executes below
            for letter in strEncrypt: # for each letter that exists in the "strEncrypt" variable
                i2 = 0 # sets i2 to 0
                number = 0 # sets number to 0
                if letter in letterArr: # if the letter exists in the array "letterArr" execute below
                    while i2 < 26: # while i2 is less than 26 execute below
                        if letter == letterArr[i2]: # if the letter is equal to the array that its currently set to through i2 execute below
                            if choice == "Encrypt": #if the choice equals to "Encrypt" execute below
                                number = i2 + keyArr[i3] #sets the number to encrypt the string

                            else: #if the choice doesnt equal to "Encrypt"
                                number = i2 - keyArr[i3] #sets the number to decrypt the string

                            if number >= 25: # if number is greater than or equal to 25 execute below
                                number = number - 26 # minus's 26 from the number so it doesnt get higher than the array length

                            if length(keyArr)-1 == i3: #if the length of the keyArr minus 1 is equal to the variable i3 execute below
                                i3 = 0 # sets i3 to 0
                            else: # if it isnt equal to i3 execute below
                                i3 += 1 # adds 1 to i3

                            newStr = newStr + letterArr[number] # adds the encrypted/decrypted key to the string
                        i2 += 1 # adds 1 to i2 if letter doesnt equal to the current letter array
                elif letter in upperArr: # if letter is in the array "upperArr" execute below
                    while i2 < 26: # executes below while i2 is less than 26
                        if letter == upperArr[i2]: # if letter is equal to the array that is currently set to through 12 execute below
                            if choice == "Encrypt": #if the choice equals to "Encrypt" execute below
                                number = i2 + keyArr[i3] #sets number to Encrypt the string
                            else: #if the choice does not equal to "Encrypt"
                                number = i2 - keyArr[i3] #sets number to Decrypt the string

                            if length(keyArr)-1 == i3: #if the length of the keyArr minus 1 is equal to the variable i3 execute below
                                i3 = 0 # sets i3 to 0
                            else: # if the length of the keyArr -1 does not equal to i3 execute below
                                i3 += 1 # adds 1 to i3

                            if number >= 25: # if number is equal to or greater than 25 execute below
                                number = number - 26 # minus's 26 from the number so it doesnt get higher than the array length

                            newStr = newStr + upperArr[number] #adds the encrypted/decrypted key to the string
                        i2 += 1 # adds 1 to i2 eaceh time letter doesnt equal to the array
                else: # executes if the letter doesnt exist in either of the encryption arrays execute below
                    newStr = newStr + letter # adds letter to the string as it is punctuation
            
            app.hideLabelFrame("Encryption") #hides the label frame "Encryption"
            app.showTextArea("response") #shows the text area "Response"
            app.setTextArea("response", newStr) #sets the text area to the encrypted string
            app.showButton("Back") #shows the "Back" button
            app.showLabel("responses") # shows the label "Responses"
            newStr = "" #sets the encrypted string to an empty string
    else: # if the string returned is null execute below
        app.errorBox("Error", "Please insert a string to encrypt") # sends an error box 

# appjar designs
app = gui("Encryption/Decryption") #creates the app with the name "Encryption/Decryption"
app.setSize("400x300") # sets the size of the application to 400px by 300px
app.setLocation("CENTER") #sets location of the application to the center of your screen
app.setBg("light blue") # sets the background colour to light blue
app.addButton("Back", goBack) # adds a "Back" button
app.hideButton("Back") #hides the "Back" button
app.addLabel("responses", "Here is your response:") # Adds a label 
app.hideLabel("responses") # hides the label "responses"    
app.addScrolledTextArea("response") # Adds a text area called "Response"
app.disableTextArea("response") # Sets the text area "Response" so users cant input into it
app.hideTextArea("response") # Hides the text area "Response"

app.startLabelFrame("Encryption") #starting a label frame called "Encryption"

app.setPadding([90, 10]) #sets the padding for the label frame
app.addLabel("keys", "Please insert the key") #adds a label called "keys"
app.addEntry("key") #adds an entry to store the encryption key
app.addLabel("words", "Please insert the String") # adds a label called "words"
app.addEntry("strings") #adds an entry to store the the string to encrypt/decrypt
app.addLabel("Choose", "What would you like to do?") # adds a label called "Choose"
app.addButtons(["Encrypt", "Decrypt"], whatHappens)#adds 2 buttons, Encrypt and Decrypt
app.setEntryTooltip("key", "Must be a string with no spaces.") #adds a tooltip for the entry "key"
app.setEntryTooltip("strings", "You can insert anything into this.") # adds a tooltip for the entry "strings"

app.stopLabelFrame()

app.go()
