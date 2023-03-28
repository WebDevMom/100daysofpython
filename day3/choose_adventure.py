print('''
*******************************************************************************
     o   o
      )-(
     (O O)
      \=/
     .-"-.
    //\ /\\
  _// / \ \\_
 =./ {,-.} \.=
     || ||
     || ||    
   __|| ||__  
  `---" "---'
*******************************************************************************
''')
print("Welcome to Space.")
print("Your mission is to explore space and find the alien life.") 
print("Your ship approaches a small moon!")
moon_land = input("Do you land on the moon and explore? Y or N?\n").lower()
if moon_land == "y":
    print("You exit the ship and are immediately abliterated by aliens. You are dead! GAME OVER")
elif moon_land == "n":
    print("You travel further into space searhing for aliens!")
    print('''
 *********************************************************************************************
                   |||
                  +++++
               __/ (_) \__
          ____/_ ======= _\____
 ________/ _ \(_)_______(_)/ _ \________
<___+____ (_) | /   _   \ | (_) ____+___>
  O O O  \___/ |   (_)   | \___/  O O O
             \__\_______/__/

***************************************************************************************
''')
    print("You travel to a distant star and hear transmissions coming from the surface.")
    distant_star = input("Do you approach and make contact? Y or N?\n").lower()
    if distant_star == "y":
        print("Lets make contact! You decide to land on the planet. You have discovered a friendly alien race.")
    elif distant_star == "n":
        print("The civilization on the star takes your lack of communication as a threat and destroys your ship.Your dead! GAME OVER.")
    print("You meet a beatiful alien female on the star.")
    home = input("Do you stay on the star and make it your home? stay or go?\n")
    if home == "stay":
            print("You go native and live happily ever after with your alien bride.")
    elif home == "go":
            print("You leave the star and return to earth to a meagar existance.")