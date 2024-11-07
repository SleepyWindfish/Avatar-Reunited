#FIRE BENDER MOVE NAME CONFLAGRATION
#Move Name: The calm before the Storm
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import random
root=Tk()
root.title("Avatar Reunited")
root.geometry("700x800")
root.configure(bg="bisque3")

#Open Image
a_open=Image.open('AirBending.jpeg')
w_open=Image.open('WaterBending.webp')
e_open=Image.open('EarthBender.jpeg')
f_open=Image.open('FireBending.webp')
me_open=Image.open('Meelo.webp')
jin_open=Image.open('Jinora.jpeg')
zah_open=Image.open('Zaheer.webp')
cab_open=Image.open('Cabbage_merchant.webp')
sokka_open=Image.open('Sokka.jpeg')
pip_open=Image.open('PipSqueak.jpeg')
iroh_open=Image.open('Iroh.jpeg')
koopa_open=Image.open('Magikoopas.webp')

#Resize image
a_resize=a_open.resize((100,100),Image.ANTIALIAS)
w_resize=w_open.resize((100,100),Image.ANTIALIAS)
e_resize=e_open.resize((100,100),Image.ANTIALIAS)
f_resize=f_open.resize((100,100),Image.ANTIALIAS)
me_resize=me_open.resize((150,150),Image.ANTIALIAS)
me_battle=me_open.resize((75,75),Image.ANTIALIAS)
jin_resize=jin_open.resize((150,150),Image.ANTIALIAS)
zah_resize=zah_open.resize((150,150),Image.ANTIALIAS)
zah_battle=zah_open.resize((75,75),Image.ANTIALIAS)
cab_resize=cab_open.resize((120,120),Image.ANTIALIAS)
cab_battle=cab_open.resize((75,75),Image.ANTIALIAS)
pip_resize=pip_open.resize((120,120),Image.ANTIALIAS)
pip_battle=pip_open.resize((75,75),Image.ANTIALIAS)
iroh_resize=iroh_open.resize((120,120),Image.ANTIALIAS)
iroh_battle=iroh_open.resize((75,75),Image.ANTIALIAS)
sokka_resize=sokka_open.resize((120,120),Image.ANTIALIAS)
sokka_battle=sokka_open.resize((75,75),Image.ANTIALIAS)
koopa_battle=koopa_open.resize((75,75),Image.ANTIALIAS)

Air_symbol=ImageTk.PhotoImage(a_resize)
Water_symbol=ImageTk.PhotoImage(w_resize)
Earth_symbol=ImageTk.PhotoImage(e_resize)
Fire_symbol=ImageTk.PhotoImage(f_resize)
meelo_char=ImageTk.PhotoImage(me_resize)
meelo_fight=ImageTk.PhotoImage(me_battle)
jin_char=ImageTk.PhotoImage(jin_resize)
zan_char=ImageTk.PhotoImage(zah_resize)
zan_fight=ImageTk.PhotoImage(zah_battle)
cab_trainer=ImageTk.PhotoImage(cab_resize)
cab_fight=ImageTk.PhotoImage(cab_battle)
Pip_trainer=ImageTk.PhotoImage(pip_resize)
pip_fight=ImageTk.PhotoImage(pip_battle)
iroh_trainer=ImageTk.PhotoImage(iroh_resize)
iroh_fight=ImageTk.PhotoImage(iroh_battle)
sokka_trainer=ImageTk.PhotoImage(sokka_resize)
sokka_fight=ImageTk.PhotoImage(sokka_battle)
koopa_fight=ImageTk.PhotoImage(koopa_battle)

def reset():
  Air_bender.destroy()
  Atitle.destroy()
  Water_bender.destroy()
  wtitle.destroy()
  Earth_bender.destroy()
  etitle.destroy()
  Fire_bender.destroy()
  ftitle.destroy()
  intro.destroy()

def clear():
  Jinora.destroy()
  C2.destroy()
  Zaheer.destroy()
  C3.destroy()
  Meelo.destroy()
  C1.destroy()
  intro.destroy()
  ctitle.destroy()
  Sokka.destroy()
  ptitle.destroy()
  PipSqueak.destroy()
  utitle.destroy()
  Iroh.destroy()
  Power.destroy()
  info.destroy()
  

# Order of data is Charecter,ability,Type of ability,Trainer,Power,Spirit,Endurance,level 
User_Data=[]
Ev="False"
Entry_Into_stats=0
# Move name,move power,turn duration,number of uses
Meelo_Moveset=['Mini-Whirlwind',10,5,3,'Paint-Ball',5,1,5,'Lemur Attack',22,1,2]
Meelo_Moveinfo=['Meelo creates a small Whirl-wind that batters the enemy for 5 turns','Meelo uses the paint balls he collects to hit the enemy this may also reduce their accuracy','Meelo calls all his Lemur Friends to attack']
Meelo_Dice=[16,19,100000]

Zaheer_Moveset=['Air Acolyte',10,1,5,'Seeing Stars',32,1,3,'Fly',0,0,2]
Zaheer_Moveinfo=['Zaheer Meditates and patiently waits for the right moment to strike','Zaheer knocks the opponent with such a powerful force that the victom beggins seeing stars around their head. The victom will be confused','Zaheer is a Air Bending Prodigy who can fly away from a attack on command']
Zaheer_Dice=[12,5,17]

#Trainer: Move name,attack multiplyer,add or delete stat,stat name, healing,number of uses
Sokka_Moveset=['Space Sword',0.45,'none','none',0,2,'Cactus Juice',0,'Confuse','none',10,3]
Sokka_Moveinfo=['Sokka uses his meteorite sword to slice through his Enemys increasing attack by 45%','Sokka gives his enemy some seemingly innocent cactus juice. The hallucinagin increases the chance that they become confused hurting themselves. He also heals the player a little.']

Koopa_Moveset=['Heavy Stopper',-0.5,'none','none',0,50,'Sorcerers Stone',0,'none','none',-30,50]
Koopa_Moveinfo=['Your In REAL Trouble now! Koopa Reduces the Power of you Move by 50%','Its all DOWN hill from here! Koopa uses her powers to throw a massive stone in your direction. Their is no chance it Misses!']

Pipsqueak_Moveset=['Fire Encasing',0,'Add','Endurance',10,2,'Double Hammer',0.13,'Add','Endurance',0,1]
Pipsqueak_Moveinfo=['With the help of his friend Jet the freedom fighter create a fire encasing around you that helps you endure a hit and you gain a little health.','Pip Squeak and the Duke let loose their hammers making your enemys fall back and lose some endurance. Your attack is 13% stronger']

Iroh_Moveset=['Dragon Breath',0.50,'Add','Endurance',5,2,'A Cup Of Tea',0,'Add','Power',10,2]
Iroh_Moveinfo=['Uncle Iroh drinks a warm cup of tea and lets out a FURY of fire from his mouth.Your attack increases by 50% and you have more endurance. Your health is increased a tiny bit.','Uncle Iroh sits with the opponent and has a cup of tea. The opponent rethinks thier life choices and thier power is reduced. Your health is increased a little bit']




def Irohadd():
  cheack=Power.get()
  if(Legend==0):
    messagebox.showerror("Legend Error","You Already have a Legendary.")
  else:
    User_Data.append('Iroh')
    Main_Menu()
    

def Sokkaadd():
  if(Legend==0):
    messagebox.showerror("Legend Error","You Already have a Legendary.")
  else:
    User_Data.append('Sokka')
    Main_Menu()

def PipSqueakadd():
  User_Data.append('PipSqueak')
  Main_Menu()

def Stats_Clear():
  opening.destroy()
  tPower.destroy()
  Power.destroy()
  tSpiritual.destroy()
  Spiritual.destroy()
  tEndurance.destroy()
  Endurance.destroy()
  tmode.destroy()
  mode.destroy()
  back.destroy()
  Main_Menu()
  
def Menu_Clear():
  intro.destroy()
  Single.destroy()
  Multi.destroy()
  Train.destroy()
  Shop.destroy()
  stats.destroy() 
  credits.destroy() 

def Move_info(charecter,value):
  if(charecter=='Meelo'):
    messagebox.showinfo('i',Meelo_Moveinfo[value])
  if(charecter=='Zaheer'):
    messagebox.showinfo('i',Zaheer_Moveinfo[value])
  if(charecter=='Sokka'):
    messagebox.showinfo('i',Sokka_Moveinfo[value])
  if(charecter=='PipSqueak'):
    messagebox.showinfo('i',Pipsqueak_Moveinfo[value])
  if(charecter=='Iroh'):
    messagebox.showinfo('i',Iroh_Moveinfo[value])
  if(charecter=='Cursed'):
    messagebox.showinfo('i',Koopa_Moveinfo[value])

def Curse_Trainer():
  global Trainer_naming,Single_Trainer,cursed1,cursed2,detail3,detail4 
  Trainer_naming.config(text="Trainer: Cursed Witch")
  Single_Trainer.config(image=koopa_fight)
  detail3.config(command=lambda: Move_info('Cursed',0))
  detail4.config(command=lambda: Move_info('Cursed',1))
  cursed1=Button(root,text=Koopa_Moveset[0],height=3,width=15,bg='steel blue',command=lambda: Waiting("#",Koopa_Moveset[0],"-","-",Koopa_Moveset[5],"-",[Koopa_Moveset[0],Koopa_Moveset[1],Koopa_Moveset[2],Koopa_Moveset[3],Koopa_Moveset[4]],"four"))
  cursed2=Button(root,text=Koopa_Moveset[6],height=3,width=15,bg='steel blue',command=lambda: Waiting("#",Koopa_Moveset[6],"-","-",Koopa_Moveset[11],"-",[Koopa_Moveset[6],Koopa_Moveset[7],Koopa_Moveset[8],Koopa_Moveset[9],Koopa_Moveset[10]],"five"))
  cursed1.grid(row=9,column=1)
  cursed2.grid(row=10,column=1)

verify=[]
func_storage=[]
Trainer_In_Use=[]
All_Move_Duration=[["one",0],["two",0],["three",0]]
Trainer_Move_Duration=[["four",0],["five",0]]
Attackability=[0,1,2,3,4,5,6,7,8,9,10]
Nerfed_Attackability=[1,2,3,4]

player_curse=0
#Waiting for user to choose both a trainer move and a charecter move.Then applying spirituality before attacking. 
def Waiting(key,name,store1,store2,store3,flash,All_Trainer_Info,Move_ID):
  global Add_Power,Add_Spirit,Add_Endurance,Confuse,player_curse,cursed1,cursed2
  Add_Power=False
  Add_Spirit=False
  Add_Endurance=False
  Confuse=False
  if(key=="#"):
    #The Move ID is used to decrease durability of specific move[for trainer]
    if(Move_ID=="four"):
        Trainer_Move_Duration[0].insert(1,Trainer_Move_Duration[0][1]+1)
        usability2=Trainer_Move_Duration[0][1]
        display_usability=store3-usability2
        if(player_curse>=2):
          cursed1.config(text=name+" "+str(display_usability))
        else:
          Option4.config(text=name+" "+str(display_usability))
    if(Move_ID=="five"):
      Trainer_Move_Duration[1].insert(1,Trainer_Move_Duration[1][1]+1)
      usability2=Trainer_Move_Duration[1][1]
      display_usability=store3-usability2
      if(player_curse>=2):
          cursed2.config(text=name+" "+str(display_usability))
      else:
        Option5.config(text=name+" "+str(display_usability))
      

    #Now destroy button if the player clicked more times then allowed.   
    if(store3<=usability2):
        if(Move_ID=="four"):
          Option4.destroy()
          player_curse+=1
        if(Move_ID=="five"):
          Option5.destroy()
          player_curse+=1
    if(len(Trainer_In_Use)==0):
      for i in All_Trainer_Info:
        Trainer_In_Use.append(i)
    else:
      Trainer_In_Use.clear()
      for i in All_Trainer_Info:
        Trainer_In_Use.append(i)
  if(key=="^"):
    key="#"
    Trainer_In_Use.clear()
  #Appending the Key AFTER the skip Button is take into consideration  
  verify.append(key)
  print(verify)
  if(key=="$"):
    #The Move ID is used to decrease durability of specific move[for charecter]
    if(Move_ID=="one"):
        All_Move_Duration[0].insert(1,All_Move_Duration[0][1]+1)
        usability=All_Move_Duration[0][1]
        display_usability=store3-usability
        Option1.config(text=name+" "+str(display_usability))
    if(Move_ID=="two"):
      All_Move_Duration[1].insert(1,All_Move_Duration[1][1]+1)
      usability=All_Move_Duration[1][1]
      display_usability=store3-usability
      Option2.config(text=name+" "+str(display_usability))
    if(Move_ID=="three"):
      All_Move_Duration[2].insert(1,All_Move_Duration[2][1]+1)
      usability=All_Move_Duration[2][1]
      display_usability=store3-usability
      Option3.config(text=name+" "+str(display_usability))
    if(len(func_storage)==0):
      func_storage.append(store1)
      func_storage.append(store2)
      
      if(flash==1):
        for i in range(0,2):
          Option1.flash()
          continue
      if(flash==2):
        for i in range(0,2):
          Option2.flash()
          continue
      if(flash==3):
        for i in range(0,2):
          Option3.flash()
          continue
      if(store3<=usability):
        if(Move_ID=="one"):
          Option1.destroy()
        if(Move_ID=="two"):
          Option2.destroy()
        if(Move_ID=="three"):
          Option3.destroy()
    else:
      func_storage.clear()
      func_storage.append(store1)
      func_storage.append(store2)
      if(flash==1):
        for i in range(0,2):
          Option1.flash()
          continue
      if(flash==2):
        for i in range(0,2):
          Option2.flash()
          continue
      if(flash==3):
        for i in range(0,2):
          Option3.flash()
          continue
      if(store3<=usability):
        if(Move_ID=="one"):
          Option1.destroy()
        if(Move_ID=="two"):
          Option2.destroy()
        if(Move_ID=="three"):
          Option3.destroy()
    print(verify[len(verify)-2])
  if(len(verify)%2==0):
    if(verify[len(verify)-2]=="$"):
      if(verify[len(verify)-1]=="#"):
        print("In function Waiting 1")
        opportunity=random.choice(Attackability)
        opportunity2=random.choice(Nerfed_Attackability)
        if(comp_spirit//10>opportunity):
          if(opportunity2==1):
            messagebox.showinfo("Too bad","Your opponents Spirituality Has Disconnected you from your Attack")
            comp_attacked()
          else:
            user_attacked(func_storage[0],func_storage[1])
            return
        else:
          user_attacked(func_storage[0],func_storage[1])
          return
    if(verify[len(verify)-2]=="#"):
      if(verify[len(verify)-1]=="$"):
        print("In function Waiting 2")
        opportunity=random.choice(Attackability)
        opportunity2=random.choice(Nerfed_Attackability)
        if(comp_spirit//10>opportunity):
          if(opportunity2==1):
            messagebox.showinfo("Too bad","Your opponents Spirituality Has Disconnected you from your Attack")
            comp_attacked()
          else:
            user_attacked(func_storage[0],func_storage[1])
            return
        else:
          user_attacked(func_storage[0],func_storage[1])

  #Lets See If the Trainer Needs to be Cursed.
  print("The Player Curse ",player_curse)
  if(player_curse>=2):
    Curse_Trainer()
    

#Stores the Previous moves attack duration
pre_duration=0
stored_power=0
attackable=True
comp_attackable=True

def user_attacked(power,duration):
  global comp_health,pre_duration,attackable,Round,stored_power,Add_Power,Add_Spirit,Confuse,Add_Endurance,comp_Endur
  #Move name,move power,duration
  original=200+User_Data[7]
  comp_original=200+(User_Data[7]+5)

  #Cheack if the computer is hittable
  if(comp_attackable==False):
    messagebox.showinfo("Your Attack","You can't attack this round!")
    comp_attacked()
    return

  #Cheak for a move that repeats more than once
  if(duration>1):
    power=User_Data[4]+power
    power=power-comp_Endur
    stored_power=(power*(duration-1))
    pre_duration=duration

  pre_round=Round-1
  if(duration==0):
    attackable=False
    pre_round=Round
  #Remove invinsibility next Round
  if(pre_round<Round):
    attackable=True
  #Adding Power Spirit or Endurance based on the Trainer used.
  if(len(Trainer_In_Use)>0):
    if(Trainer_In_Use[2]=="Add"):
      if(Trainer_In_Use[3]=="Endurance"):
        Add_Endurance=True
      if(Trainer_In_Use[3]=="Power"):
        Add_Power=True
      if(Trainer_In_Use[3]=="Spirit"):
        Add_Spirit=True
    if(Trainer_In_Use[2]=="Confuse"):
      confuse_chance=["yes","both","both","yes","no","no","no","no","no","no"]
      confuse_choose=random.choice(confuse_chance)
      if(confuse_choose=="yes"):
        Confuse=True
      if(confuse_choose=="both"):
        Confuse="both"
      else:
        Confuse=False
      print("Confuse:",Confuse)
  
  if(power>0 and comp_attackable==True):
    #Add Beacause of the Trainer
    if(Add_Power==True):
      Addition1=User_Data[4]+(User_Data[4]*0.2)
      messagebox.showinfo("Trainer attack","Brilliant! Your Trainer did "+str(Addition1)+" damage in Power!")
    else:
      Addition1=User_Data[4]
    power=Addition1+power
    if(len(Trainer_In_Use)>0):
      power=power+(power*Trainer_In_Use[1])
    power=power-comp_Endur
    comp_health=comp_health-power
    if(pre_duration>1):
      messagebox.showinfo("Additional attack","Your attack did "+str(power)+" damage but your repeating attack will now be added.")
      comp_health=comp_health-(stored_power/pre_duration)
      stored_power=stored_power-(stored_power/pre_duration)
      pre_duration=pre_duration-1
    
    Comp_health_label.config(text="Computer Health:"+str(comp_health))
    
    #Calculating bar reduction
    bar_reduction=power/original
    bar_reduction2=bar_reduction*100
    Comp_health['value']-=bar_reduction2

    
    Round+=0.5
    Round_naming.config(text="Round: "+str(Round))
  comp_attacked()
  return
#Sometimes the computer will attack twice hopefully booleans will fix this.
Comp_Done=False
def comp_attacked():
  global char_health,comp_health,Round,comp_attackable,Add_Spirit,Add_Endurance,Comp_Done
  comp_attackable=True
  Comp_Done=False
  original=200+User_Data[7]
  comp_original=200+(User_Data[7]+5)
  if(Comp_choice=='Zaheer'):
    max_hit=Zaheer_Moveset[5]
    name1=Zaheer_Moveset[4]
    intro_hit=Zaheer_Moveset[9]
    name2=Zaheer_Moveset[8]
    special_hit=Zaheer_Moveset[5]
    name3=Zaheer_Moveset[4]
  if(Comp_choice=='Meelo'):
    max_hit=Meelo_Moveset[9]
    name1=Meelo_Moveset[8]
    intro_hit=Meelo_Moveset[1]
    name2=Meelo_Moveset[0]
    special_hit=Meelo_Moveset[5]
    name3=Meelo_Moveset[4]
    
#Can the Computer Attack this Round?  
  if(attackable==False):
    messagebox.showinfo("Counter Attack",str(Comp_choice)+" was unable to attack this round")
    return
    
  opportunity3=random.choice(Attackability)
  opportunity4=random.choice(Nerfed_Attackability)
  if(Add_Spirit==True):
    Addition3=User_Data[5]+(User_Data[5]*0.2)
  else:
    Addition3=User_Data[5] 
  if(Addition3//10>opportunity3):
    if(opportunity4==1):
      messagebox.showinfo("Nice","Lucky You!! Your Spirituality Has Disconnected your opponent from his Attack.")
      return

  #Add the Health The Trainer Restored
  if(Round>1):
    if(len(Trainer_In_Use)>0):
      if(Trainer_In_Use[4]>0):
        char_health=char_health+Trainer_In_Use[4]
        #Calculating bar Increase
        bar_reduction=Trainer_In_Use[4]/original
        bar_reduction2=bar_reduction*100
        User_health['value']+=bar_reduction2
      
  
  if(comp_health>(comp_original-10) and Comp_Done==False):
    pick=[intro_hit,intro_hit,intro_hit,intro_hit,max_hit]
    strategy=random.choice(pick)
    if(strategy==intro_hit):
      title=name2
    elif(strategy==max_hit):
      title=name1
    if(title=='Fly'):
      comp_attackable=False
    power=strategy+comp_power
    if(Add_Endurance==True):
      Addition2=User_Data[6]+(User_Data[6]*0.2)
      messagebox.showinfo("Trainer attack","Brilliant! Your Trainer helped Endured the hit by "+str(Addition2))
    else:
      Addition2=User_Data[6]
    power=power-Addition2
    if(Confuse==True or Confuse=="both"):
      comp_health=comp_health-power
      Comp_health_label.config(text="Computer Health:"+str(comp_health))
      bar_reduction=power/original
      bar_reduction2=bar_reduction*100
      Comp_health['value']-=bar_reduction2
      if(Confuse==True):
        messagebox.showinfo("Computer Confused",str(Comp_choice)+" choose the attack "+str(title)+" but "+str(Comp_choice)+" became CONFUSED and hurt Himself Only!!")
        return
        
    char_health=char_health-power
    health_label.config(text="Your Health:"+str(char_health))
    if(Confuse=="both"):
      messagebox.showinfo("Computer Confused",str(Comp_choice)+" choose the attack "+str(title)+" but "+str(Comp_choice)+" became CONFUSED and hurt both Himself and You!")
    else:
      messagebox.showinfo("Counter Attack info",str(Comp_choice)+" choose the attack "+str(title)+" it was succesful")
    #Calculating bar reduction
    bar_reduction=power/original
    bar_reduction2=bar_reduction*100
    User_health['value']-=bar_reduction2
    Comp_Done=True
    
  if(comp_health>(comp_original/2) and comp_health<(comp_original-10) and Comp_Done==False):
    pick=[special_hit,max_hit,max_hit,max_hit]
    strategy=random.choice(pick)
    if(strategy==special_hit):
      title=name3
    elif(strategy==max_hit):
      title=name1
    if(title=='Fly'):
      comp_attackable=False
    power=strategy+comp_power
    if(Add_Endurance==True):
      Addition2=User_Data[6]+(User_Data[6]*0.2)
      messagebox.showinfo("Trainer attack","Brilliant! Your Trainer helped Endured the hit by "+str(Addition2))
    else:
      Addition2=User_Data[6]
    power=power-Addition2
    if(Confuse==True or Confuse=="both"):
      comp_health=comp_health-power
      Comp_health_label.config(text="Computer Health:"+str(comp_health))
      bar_reduction=power/original
      bar_reduction2=bar_reduction*100
      Comp_health['value']-=bar_reduction2
      if(Confuse==True):
        messagebox.showinfo("Computer Confused",str(Comp_choice)+" choose the attack "+str(title)+" but "+str(Comp_choice)+" became CONFUSED and hurt Himself Only!!")
        return
        
    char_health=char_health-power
    health_label.config(text="Your Health:"+str(char_health))
    if(Confuse=="both"):
      messagebox.showinfo("Computer Confused",str(Comp_choice)+" choose the attack "+str(title)+" but "+str(Comp_choice)+" became CONFUSED and hurt both Himself and You!")
    else:
      messagebox.showinfo("Counter Attack info",str(Comp_choice)+" choose the attack "+str(title)+" it was succesful")
    #Calculating bar reduction
    bar_reduction=power/original
    bar_reduction2=bar_reduction*100
    User_health['value']-=bar_reduction2
    Comp_Done=True

  if(comp_health<(comp_original/2) and char_health>(original/2) and Comp_Done==False):
    pick=[special_hit,special_hit,max_hit]
    strategy=random.choice(pick)
    if(strategy==special_hit):
      title=name3
    elif(strategy==max_hit):
      title=name1
    if(title=='Fly'):
      comp_attackable=False
    power=strategy+comp_power
    if(Add_Endurance==True):
      Addition2=User_Data[6]+(User_Data[6]*0.2)
      messagebox.showinfo("Trainer attack","Brilliant! Your Trainer helped Endured the hit by "+str(Addition2))
    else:
      Addition2=User_Data[6]
    power=power-Addition2
    if(Confuse==True or Confuse=="both"):
      comp_health=comp_health-power
      Comp_health_label.config(text="Computer Health:"+str(comp_health))
      bar_reduction=power/original
      bar_reduction2=bar_reduction*100
      Comp_health['value']-=bar_reduction2
      if(Confuse==True):
        messagebox.showinfo("Computer Confused",str(Comp_choice)+" choose the attack "+str(title)+" but "+str(Comp_choice)+" became CONFUSED and hurt Himself Only!!")
        return
        
    char_health=char_health-power
    health_label.config(text="Your Health:"+str(char_health))
    if(Confuse=="both"):
      messagebox.showinfo("Computer Confused",str(Comp_choice)+" choose the attack "+str(title)+" but "+str(Comp_choice)+" became CONFUSED and hurt both Himself and You!")
    else:
      messagebox.showinfo("Counter Attack info",str(Comp_choice)+" choose the attack "+str(title)+" it was succesful")
    #Calculating bar reduction
    bar_reduction=power/original
    bar_reduction2=bar_reduction*100
    User_health['value']-=bar_reduction2
    Comp_Done=True
    
  if(comp_health<(comp_original/2) and char_health<(original/2) and Comp_Done==False):
    pick=[max_hit,special_hit,max_hit]
    strategy=random.choice(pick)
    if(strategy==special_hit):
      title=name3
    elif(strategy==max_hit):
      title=name1
    if(title=='Fly'):
      comp_attackable=False
    power=strategy+comp_power
    if(Add_Endurance==True):
      Addition2=User_Data[6]+(User_Data[6]*0.2)
      messagebox.showinfo("Trainer attack","Brilliant! Your Trainer helped Endured the hit by "+str(Addition2))
    else:
      Addition2=User_Data[6]
    power=power-Addition2
    if(Confuse==True or Confuse=="both"):
      comp_health=comp_health-power
      Comp_health_label.config(text="Computer Health:"+str(comp_health))
      bar_reduction=power/original
      bar_reduction2=bar_reduction*100
      Comp_health['value']-=bar_reduction2
      if(Confuse==True):
        messagebox.showinfo("Computer Confused",str(Comp_choice)+" choose the attack "+str(title)+" but "+str(Comp_choice)+" became CONFUSED and hurt Himself Only!!")
        return
        
    char_health=char_health-power
    health_label.config(text="Your Health:"+str(char_health))
    if(Confuse=="both"):
      messagebox.showinfo("Computer Confused",str(Comp_choice)+" choose the attack "+str(title)+" but "+str(Comp_choice)+" became CONFUSED and hurt both Himself and You!")
    else:
      messagebox.showinfo("Counter Attack info",str(Comp_choice)+" choose the attack "+str(title)+" it was succesful")
    #Calculating bar reduction
    bar_reduction=power/original
    bar_reduction2=bar_reduction*100
    User_health['value']-=bar_reduction2
    Comp_Done=True
  

  
    Round+=0.5
    Round_naming.config(text="Round: "+str(Round))
      
      
def Single_Player():
  Menu_Clear()
  global char_health,comp_health,Comp_health_label,comp_power,comp_spirit,comp_Endur,health_label,User_health,Comp_health,Comp_choice,Round,Round_naming,Option1,Option2,Option3,Option4,Option5,Add_Power,Add_Spirit,Add_Endurance,Confuse,Trainer_naming,Single_Trainer,detail3,detail4
  char_health=200+User_Data[7]
  Round=1
  Add_Power=False
  Add_Spirit=False
  Add_Endurance=False
  Confuse=False
  
  #Calculate Multiplyer for bot stats
  #Gradualy get harder until 1.666 times more
  print(difficulty)
  Choose_Strength=[1,1,1,1,2,2,2,3,3,3]
  Strength=random.choice(Choose_Strength)
  Substractor=0.5
  if(User_Data[7]<=20):
    multiplyer=User_Data[7]/12
  if(User_Data[7]<=30 and User_Data[7]>20):
    multiplyer=User_Data[7]/18 
  if(User_Data[7]<=43 and User_Data[7]>30):
    multiplyer=User_Data[7]/24
  if(User_Data[7]<=50 and User_Data[7]>43):
    multiplyer=User_Data[7]/30
  if(User_Data[7]>=51):
    multiplyer=(User_Data[7]/((User_Data[7]/10)*5))-0.48
    
#Calculate Additional difficulty for bot stats      
  if(difficulty==1):
    if(User_Data[7]<=12):
      adder=10
    else:
      adder=0
  if(difficulty==2):
    if(User_Data[7]<=20):
      if(User_Data[7]<=12):
        adder=10
      else:
        adder=5
    if(User_Data[7]<=30 and User_Data[7]>20):
      adder=4
      Substractor=0.4
    if(User_Data[7]<=43 and User_Data[7]>30):
      adder=7
      Substractor=0.35
    if(User_Data[7]>=51):
      adder=11
      Substractor=0.25
#The Bot will have strength in either Power, Spirit, or Endurance to make the game more intresting. 
  if(Strength==1):
    comp_power=(User_Data[4]*multiplyer)+adder
    comp_spirit=(User_Data[5]*(multiplyer-Substractor))
    comp_Endur=(User_Data[6]*(multiplyer-Substractor))+adder
  if(Strength==2):
    comp_power=(User_Data[4]*(multiplyer-Substractor))+adder
    comp_spirit=(User_Data[5]*multiplyer)+adder
    comp_Endur=(User_Data[6]*(multiplyer-Substractor))
  if(Strength==3):
    comp_power=(User_Data[4]*(multiplyer-Substractor))+adder
    comp_spirit=(User_Data[5]*(multiplyer-Substractor))
    comp_Endur=(User_Data[6]*multiplyer)+adder
  print("Strength",Strength)  
    
  comp_health=200+(User_Data[7]+5)
  Single_intro=Label(root,text="FIGHT",bg="red")
  Single_intro.config(font=('Helvatical bold',20))
  Single_intro2=Label(root,text="VS",bg="red")
  Single_intro2.config(font=('Helvatical bold',20))
  Comp_char=['Meelo','Zaheer']
  Comp_trai=['Sokka','PipSqueak','Iroh']
  Comp_trai2=['Sokka','PipSqueak']
  Comp_choice=random.choice(Comp_char)
  if(Comp_choice=='Zaheer'):
    Comp_choice2=random.choice(Comp_trai2)
  else:
    Comp_choice2=random.choice(Comp_trai)
  

  
  if(User_Data[0]=='Meelo'):
    #Roll the Dice
    Player_Dice=random.choice(Meelo_Dice)
    #Draw from moves of Player
    Single_image=Button(root,image=meelo_fight)
    Option1=Button(root,text=Meelo_Moveset[0],height=3,width=15,bg='steel blue',activebackground='medium blue',activeforeground='LightYellow2',command=lambda: Waiting("$",Meelo_Moveset[0],Meelo_Moveset[1],Meelo_Moveset[2],Meelo_Moveset[3],1,"No","one"))
    Option2=Button(root,text=Meelo_Moveset[4],height=3,width=15,bg='steel blue',activebackground='medium blue',activeforeground='LightYellow2',command=lambda: Waiting("$",Meelo_Moveset[4],Meelo_Moveset[5],Meelo_Moveset[6],Meelo_Moveset[7],2,"No","two"))
    Option3=Button(root,text=Meelo_Moveset[8],height=3,width=15,bg='steel blue',activebackground='medium blue',activeforeground='LightYellow2',command=lambda: Waiting("$",Meelo_Moveset[8],Meelo_Moveset[9],Meelo_Moveset[10],Meelo_Moveset[11],3,"No","three"))


  if(User_Data[0]=='Zaheer'):
    #Roll the Dice
    Player_Dice=random.choice(Zaheer_Dice)
    #Draw from moves of Player
    Single_image=Button(root,image=zan_fight)
    Option1=Button(root,text=Zaheer_Moveset[0],height=3,width=15,bg='steel blue',activebackground='medium blue',activeforeground='LightYellow2',command=lambda: Waiting("$",Zaheer_Moveset[0],Zaheer_Moveset[1],Zaheer_Moveset[2],Zaheer_Moveset[3],1,"No","one"))
    Option2=Button(root,text=Zaheer_Moveset[4],height=3,width=15,bg='steel blue',activebackground='medium blue',activeforeground='LightYellow2',command=lambda: Waiting("$",Zaheer_Moveset[4],Zaheer_Moveset[5],Zaheer_Moveset[6],Zaheer_Moveset[7],2,"No","two"))
    Option3=Button(root,text=Zaheer_Moveset[8],height=3,width=15,bg='steel blue',activebackground='medium blue',activeforeground='LightYellow2',command=lambda: Waiting("$",Zaheer_Moveset[8],Zaheer_Moveset[9],Zaheer_Moveset[10],Zaheer_Moveset[11],3,"No","three"))


  if(Comp_choice=='Zaheer'):
    #Roll the Dice
    Comp_Dice=random.choice(Zaheer_Dice)
    #Draw from moves of Player
    Single_cimage=Button(root,image=zan_fight)
    
#The Following is the move Labels for the Computers:    
    Option7=Button(root,text=Zaheer_Moveset[0],height=3,width=15,bg='steel blue')
    Option8=Button(root,text=Zaheer_Moveset[4],height=3,width=15,bg='steel blue')
    Option9=Button(root,text=Zaheer_Moveset[8],height=3,width=15,bg='steel blue')

  
  if(Comp_choice=='Meelo'):
    #Roll the Dice
    Comp_Dice=random.choice(Meelo_Dice)
    #Draw from moves of Player
    Single_cimage=Button(root,image=meelo_fight)
    Option7=Button(root,text=Meelo_Moveset[0],height=3,width=15,bg='steel blue')
    Option8=Button(root,text=Meelo_Moveset[4],height=3,width=15,bg='steel blue')
    Option9=Button(root,text=Meelo_Moveset[8],height=3,width=15,bg='steel blue')  


    
  #Charecter Label 
  Single_naming=Label(root,text=User_Data[0],bg="alice blue")
  Single_cnaming=Label(root,text="Computer Choice: "+Comp_choice,bg="alice blue")
  Round_naming=Label(root,text="Round: "+str(Round),bg="PaleTurquoise1")
  Trainer_naming=Label(root,text="Trainer:"+User_Data[3],bg="alice blue")

  health_label=Label(root,text="Your Health:"+str(char_health),bg="papaya whip")
  User_health=ttk.Progressbar(root,orient=HORIZONTAL,length=150,mode='determinate')
  User_health['value']=100
  Comp_health_label=Label(root,text="Computer Health:"+str(comp_health),bg="papaya whip")
  Comp_health=ttk.Progressbar(root,orient=HORIZONTAL,length=150,mode='determinate')
  Comp_health['value']=100

  #Check whose Dice rolled higher
  if(Comp_Dice>Player_Dice):
    messagebox.showinfo('Order',str(User_Data[0])+" Rolled a "+str(Player_Dice)+" While Computer rolled "+str(Comp_Dice)+". Computer goes first.")
    comp_attacked()
  elif(Comp_Dice==Player_Dice):
    coin=[1,2]
    flip=random.choice(coin)
    if(flip==1):
      messagebox.showinfo("Equal","You both rolled "+str(Comp_Dice)+". Computer won the coin toss. Computer goes first.")
      comp_attacked()
    else:
      messagebox.showinfo("Equal","You both rolled "+str(Comp_Dice)+". You won the coin toss! You go first.")
  elif(Player_Dice>Comp_Dice):
    messagebox.showinfo('Order',str(User_Data[0])+" Rolled a "+str(Player_Dice)+" While Computer rolled "+str(Comp_Dice)+". Player goes first.")








  
  #Move Info
  detail0=Button(root,text="Info",bg='OliveDrab2',command=lambda: Move_info(User_Data[0],0))
  detail1=Button(root,text="Info",bg='OliveDrab2',command=lambda: Move_info(User_Data[0],1))
  detail2=Button(root,text="Info",bg='OliveDrab2',command=lambda: Move_info(User_Data[0],2))
  detail3=Button(root,text="Info",bg='OliveDrab2',command=lambda: Move_info(User_Data[3],0))
  detail4=Button(root,text="Info",bg='OliveDrab2',command=lambda: Move_info(User_Data[3],1))
  
    # Moveset of the Trainer
  if(User_Data[3]=='Sokka'):
    Single_Trainer=Button(root,image=sokka_fight)
    Option4=Button(root,text=Sokka_Moveset[0],height=3,width=15,bg='steel blue',command=lambda: Waiting("#",Sokka_Moveset[0],"-","-",Sokka_Moveset[5],"-",[Sokka_Moveset[0],Sokka_Moveset[1],Sokka_Moveset[2],Sokka_Moveset[3],Sokka_Moveset[4]],"four"))
    Option5=Button(root,text=Sokka_Moveset[6],height=3,width=15,bg='steel blue',command=lambda: Waiting("#",Sokka_Moveset[6],"-","-",Sokka_Moveset[11],"-",[Sokka_Moveset[6],Sokka_Moveset[7],Sokka_Moveset[8],Sokka_Moveset[9],Sokka_Moveset[10]],"five"))
  
  if(User_Data[3]=='PipSqueak'):
    Single_Trainer=Button(root,image=pip_fight)
    Option4=Button(root,text=Pipsqueak_Moveset[0],height=3,width=15,bg='steel blue',command=lambda: Waiting("#",Pipsqueak_Moveset[0],"-","-",Pipsqueak_Moveset[5],"-",[Pipsqueak_Moveset[0],Pipsqueak_Moveset[1],Pipsqueak_Moveset[2],Pipsqueak_Moveset[3],Pipsqueak_Moveset[4]],"four"))
    Option5=Button(root,text=Pipsqueak_Moveset[6],height=3,width=15,bg='steel blue',command=lambda: Waiting("#",Pipsqueak_Moveset[6],"-","-",Pipsqueak_Moveset[11],"-",[Pipsqueak_Moveset[6],Pipsqueak_Moveset[7],Pipsqueak_Moveset[8],Pipsqueak_Moveset[9],Pipsqueak_Moveset[10]],"five"))

  if(User_Data[3]=='Iroh'):
    Single_Trainer=Button(root,image=iroh_fight)
    Option4=Button(root,text=Iroh_Moveset[0],height=3,width=15,bg='steel blue',command=lambda: Waiting("#",Iroh_Moveset[0],"-","-",Iroh_Moveset[5],"-",[Iroh_Moveset[0],Iroh_Moveset[1],Iroh_Moveset[2],Iroh_Moveset[3],Iroh_Moveset[4]],"four"))
    Option5=Button(root,text=Iroh_Moveset[6],height=3,width=15,bg='steel blue',command=lambda: Waiting("#",Iroh_Moveset[6],"-","-",Iroh_Moveset[11],"-",[Iroh_Moveset[6],Iroh_Moveset[7],Iroh_Moveset[8],Iroh_Moveset[9],Iroh_Moveset[10]],"five"))

  Skip=Button(root,text="Skip",bg="light slate blue",command=lambda: Waiting("^","-","-","-","-","-""-","-","abc"))


  #Now Computer Choses a Trainer

  if(Comp_choice2=='Sokka'):
    Single_Trainer2=Button(root,image=sokka_fight)
    Option10=Button(root,text=Sokka_Moveset[0],height=3,width=15,bg='steel blue')
    Option11=Button(root,text=Sokka_Moveset[6],height=3,width=15,bg='steel blue')
  
  if(Comp_choice2=='PipSqueak'):
    Single_Trainer2=Button(root,image=pip_fight)
    Option10=Button(root,text=Pipsqueak_Moveset[0],height=3,width=15,bg='steel blue')
    Option11=Button(root,text=Pipsqueak_Moveset[6],height=3,width=15,bg='steel blue')

  if(Comp_choice2=='Iroh'):
    Single_Trainer2=Button(root,image=iroh_fight)
    Option10=Button(root,text=Iroh_Moveset[0],height=3,width=15,bg='steel blue')
    Option11=Button(root,text=Iroh_Moveset[6],height=3,width=15,bg='steel blue')
  
  
  Single_intro.grid(row=1,column=3)
  Single_intro2.grid(row=3,column=3)
  Single_naming.grid(row=2,column=1)
  Single_cnaming.grid(row=2,column=7)
  Single_image.grid(row=3,column=1)
  Single_cimage.grid(row=3,column=7)
  Option1.grid(row=4,column=1)
  Option7.grid(row=4,column=7)
  detail0.grid(row=4,column=2)
  Option2.grid(row=5,column=1)
  Option8.grid(row=5,column=7)
  detail1.grid(row=5,column=2)
  Option3.grid(row=6,column=1)
  Option9.grid(row=6,column=7)
  detail2.grid(row=6,column=2)
  Trainer_naming.grid(row=7,column=1)
  Single_Trainer.grid(row=8,column=1)
  Single_Trainer2.grid(row=8,column=7)
  Skip.grid(row=7,column=2)
  Option4.grid(row=9,column=1)
  Option10.grid(row=9,column=7)
  detail3.grid(row=9,column=2)
  Option5.grid(row=10,column=1)
  Option11.grid(row=10,column=7)
  detail4.grid(row=10,column=2)
  health_label.grid(row=11,column=1)
  User_health.grid(row=12,column=1)
  Comp_health_label.grid(row=11,column=7)
  Comp_health.grid(row=12,column=7)
  Round_naming.grid(row=12,column=4)

#The Difficulty will be used for computer stats
def mode_change():
  global difficulty,mode
  if(difficulty==2):
    mode.config(text="Medium",bg="khaki2",activebackground="khaki2")
    difficulty=1
  elif(difficulty==1):
    mode.config(text="Hard",bg="brown1",activebackground="brown1")
    difficulty=2
difficulty=1

def user_stats():
  Menu_Clear()
  global opening,tPower,Power,tSpiritual,Spiritual,tEndurance,Endurance,back,Ev,Entry_Into_stats,mode,tmode 
  Entry_Into_stats=Entry_Into_stats+1
  opening=Label(root,text="Your Characters Stats",bg="red")
  opening.config(font=('Helvatical bold',20))
  opening.grid(row=1,column=2)
  
  if(User_Data[2]=='Power'):
    tPower=Label(root,text="Your Power:")
    Power=Label(root,text=User_Data[1])
    po=User_Data[1]
    if(Legend==0):
      Spirit=(110-User_Data[1])//2
      tSpiritual=Label(root,text="Your Spirituality:")
      Spiritual=Label(root,text=Spirit)
      Endur=110-(Spirit+User_Data[1])
      tEndurance=Label(root,text="Your Endurance:")
      Endurance=Label(root,text=Endur)
    else:
      Spirit=(90-User_Data[1])//2
      tSpiritual=Label(root,text="Your Spirituality:")
      Spiritual=Label(root,text=Spirit)
      Endur=90-(Spirit+User_Data[1])
      tEndurance=Label(root,text="Your Endurance:")
      Endurance=Label(root,text=Endur)
    tmode=Label(root,text="Your Difficulty(click to change):",bg="yellow3")
    mode=Button(root,text="Medium",bg="khaki2",command=mode_change)
    back=Button(root,text="Back",bg="blue",activebackground="light blue",command=Stats_Clear)

    
    tPower.grid(row=2,column=1)
    Power.grid(row=2,column=2)
    tSpiritual.grid(row=3,column=1)
    Spiritual.grid(row=3,column=2)
    tEndurance.grid(row=4,column=1)
    Endurance.grid(row=4,column=2)
    tmode.grid(row=5,column=1)
    mode.grid(row=5,column=2)
    back.grid(row=6,column=3)
    
  elif(User_Data[2]=='Spirituality'):
    tSpiritual=Label(root,text="Your Spirituality:")
    Spiritual=Label(root,text=User_Data[1])
    Spirit=User_Data[1]
    if(Legend==0):
      po=(-2*User_Data[1])+110
      tPower=Label(root,text="Your Power:")
      Power=Label(root,text=po)
      Edur=110-(po+User_Data[1])
      tEndurance=Label(root,text="Your Endurance:")
      Endurance=Label(root,text=Edur)
    else:
      po=(-2*User_Data[1])+90
      tPower=Label(root,text="Your Power:")
      Power=Label(root,text=po)
      Edur=90-(po+User_Data[1])
      tEndurance=Label(root,text="Your Endurance:")
      Endurance=Label(root,text=Edur)
      
    back=Button(root,text="Back",bg="blue",activebackground="light blue",command=Stats_Clear)

    tSpiritual.grid(row=2,column=1)
    Spiritual.grid(row=2,column=2)
    tPower.grid(row=3,column=1)
    Power.grid(row=3,column=2)
    tEndurance.grid(row=4,column=1)
    Endurance.grid(row=4,column=2)
    back.grid(row=6,column=3)
    
  elif(User_Data[2]=='Endurance'):
    tEndurance=Label(root,text="Your Endurance:")
    Endurance=Label(root,text=User_Data[1])
    Endur=User_Data[1]
    tEndurance.grid(row=2,column=1)
    Endurance.grid(row=2,column=2)
    if(Legend==0):
      Spirit=-User_Data[1]+110
      tSpiritual=Label(root,text="Your Spirituality:")
      Spiritual=Label(root,text=Spirit)
      po=User_Data[1]-Spirit
      tPower=Label(root,text="Your Power:")
      Power=Label(root,text=po)
    else:
      Spirit=-User_Data[1]+90
      tSpiritual=Label(root,text="Your Spirituality:")
      Spiritual=Label(root,text=Spirit)
      po=User_Data[1]-Spirit
      tPower=Label(root,text="Your Power:")
      Power=Label(root,text=po)
    back=Button(root,text="Back",bg="blue",activebackground="light blue",command=Stats_Clear)

    
    tSpiritual.grid(row=2,column=1)
    Spiritual.grid(row=2,column=2)
    tPower.grid(row=3,column=1)
    Power.grid(row=3,column=2)
    tEndurance.grid(row=4,column=1)
    Endurance.grid(row=4,column=2)
    back.grid(row=6,column=3)
    
  #Finaly we need to append the stats ONCE into the Program  
  if(Entry_Into_stats==1):  
    User_Data.append(po)  
    User_Data.append(Spirit)
    User_Data.append(Endur)
    if(Legend==0):
      User_Data.append((po+Spirit+Endur)/11)
    else:
      User_Data.append((po+Spirit+Endur)/9)
  Ev="True"
  print(User_Data)  


def reroute(destination):
  if(Ev=="True"):
    if(destination=="Single"):
      Single_Player()
  else:
    messagebox.showerror("Ev-Falure","Hey, Before you begain the Program needs to calculate your Effort Value stats. Please Click the View Stats button to allow the program to do so.")





Choosing_is_done="True"

def Main_Menu():
  global Choosing_is_done
  if(Choosing_is_done=="True"):
    clear()
    Choosing_is_done=="False"
  global intro,Single,Multi,Train,Shop,stats,credits
  intro=Label(root,text="Main Menu",bg="red")
  intro.config(font=('Helvatical bold',20))
  Single=Button(root,text="Single Player",bg="SteelBlue1",height=5,width=20,command=lambda: reroute("Single"))
  Multi=Button(root,text="MultiPlayer",bg="salmon",height=5,width=20)
  Train=Button(root,text="Train Your Effort Value Points",bg="SeaGreen1",height=2)
  Shop=Button(root,text="Shop",bg='DarkGoldenrod1',height=2,width=10)
  
  stats=Button(root,text="View Stats",bg="lemon chiffon",command=user_stats)
  credits=Button(root,text="View Credits",bg="lemon chiffon")

  intro.grid(row=1,column=2)
  Single.grid(row=3,column=3)
  Multi.grid(row=3,column=1)
  Train.grid(row=4,column=2)
  Shop.grid(row=5,column=2)
  stats.grid(row=6,column=2)
  credits.grid(row=7,column=2)
  





def Trainer(Power,Spirituality,Endurance):
  Continue.destroy()
  global intro,ctitle,Sokka,ptitle,PipSqueak,utitle,Iroh
  if(Spirituality==0 and Endurance==0):
    User_Data.append(Power)
    User_Data.append('Power')
  elif(Power==0 and Endurance==0):
    User_Data.append(Spirituality)
    User_Data.append('Spirituality')
  elif(Spirituality==0 and Power==0):
    User_Data.append(Endurance)
    User_Data.append('Endurance')
  
    
  intro=Label(root,text="Choose Your Trainer",bg="red")
  intro.config(font=('Helvatical bold',20))
  ctitle=Label(root,text="Sokka LEGENDARY",bg="pink")
  ctitle.config(font=('Helvatical bold',10))
  Sokka=Button(root,image=sokka_trainer,bg="blue",command=Sokkaadd)
  ptitle=Label(root,text="PipSqueak and The Duke",bg="Pink")
  ptitle.config(font=('Helvatical bold',10))
  PipSqueak=Button(root,image=Pip_trainer,bg="blue",command=PipSqueakadd)
  utitle=Label(root,text="Uncle Iroh LEGENDARY",bg="pink")
  utitle.config(font=('Helvatical bold',10))
  Iroh=Button(root,image=iroh_trainer,bg="blue",command=Irohadd)
  

  
  intro.grid(row=3,column=1)
  ctitle.grid(row=4,column=1)
  Sokka.grid(row=4,column=2)
  ptitle.grid(row=5,column=1)
  PipSqueak.grid(row=5,column=2)
  utitle.grid(row=6,column=1)
  Iroh.grid(row=6,column=2)



def Zah_stats():
  global Legend
  ans=messagebox.askokcancel("Legend Status","You are choosing to have a Legendary charecter instead of a Legendary Trainer is that okay?")
  print(ans)
  if(ans==1):
    global info,Power,Continue 
    Legend=0
    C1.destroy()
    Meelo.destroy()
    C2.destroy()
    Jinora.destroy()
    Meelo_info.destroy()
    Jinora_info.destroy()
    Zaheer_info.destroy()
    Power=Scale(root,from_=50, to=105,orient=HORIZONTAL)
    info=Label(root,text="Power Slider[Adding more Power will reduce your other stats]",bg="pink")
    info.config(font=('Helvatical bold',10))
    Continue=Button(root,text="Continue",bg="IndianRed1",activebackground="OrangeRed3",command=lambda: Trainer(Power.get(),0,0))
    
    Power.grid(row=2,column=2)
    info.grid(row=2,column=3)
    User_Data.append('Zaheer')
    Zaheer.grid(row=1,column=1)
    Continue.grid(row=3,column=3)
    
  
    


    
def Meelo_Special():
  global info,Power,Continue
  Jinora.destroy()
  C2.destroy()
  Zaheer.destroy()
  C3.destroy()
  Meelo_info.destroy()
  Jinora_info.destroy()
  Zaheer_info.destroy()
  Power=Scale(root,from_=40, to=85, orient=HORIZONTAL)
  info=Label(root,text="Power Slider[Adding more Power will reduce your other stats]",bg="pink")
  info.config(font=('Helvatical bold',10))
  Continue=Button(root,text="Continue",bg="IndianRed1",activebackground="OrangeRed3",command=lambda: Trainer(Power.get(),0,0))
  
  Power.grid(row=2,column=2)
  info.grid(row=2,column=3)
  Continue.grid(row=3,column=3)
  User_Data.append('Meelo')
  
  
def Me_info():
  messagebox.showinfo("Meelo Info","Originaly from Legend of Korra Meelo is a power charecter. He takes huge inspiration from his Uncle Boomi and always finds the most creative solutions to a problem.He has one of the best dices in the game. Dice:16,19,Rolls higher than opponent")

def Ji_info():
  messagebox.showinfo("Jinora Info","Originaly from Legend of Korra Jinora has a very powerful connection with spirits. She can eaisly doge and evade attacks. Dice:10,8,14")

def Za_info():
  messagebox.showinfo("Zaheer Info","Originaly from Legend of Korra Zaheer has extreme Power and will easily one shot enemys when fully trained. Dice:12,5,17")
def Air():
  reset()
  global Jinora,C2,C1,Meelo,C3,Zaheer,Meelo_info,Jinora_info,Zaheer_info
  C1=Label(root,text="Meelo",bg="pink")
  C1.config(font=('Helvatical bold',10))
  Meelo=Button(root,image=meelo_char,bg="blue",command=Meelo_Special)
  Meelo_info=Button(root,text="View Info",bg="NavajoWhite2",activebackground="NavajoWhite3",command=Me_info)

  C2=Label(root,text="Jinora",bg="pink")
  C2.config(font=('Helvatical bold',10))
  Jinora=Button(root,image=jin_char,bg="blue")
  Jinora_info=Button(root,text="View Info",bg="NavajoWhite2",activebackground="NavajoWhite3",command=Ji_info)
 
  C3=Label(root,text="Zaheer LEGENDARY",bg="pink")
  C3.config(font=('Helvatical bold',10))
  Zaheer=Button(root,image=zan_char,bg="blue",command=Zah_stats)
  Zaheer_info=Button(root,text="View Info",bg="NavajoWhite2",activebackground="NavajoWhite3",command=Za_info)
  
  C1.grid(row=1,column=1)
  Meelo.grid(row=1,column=2)
  Meelo_info.grid(row=1,column=3)
  C2.grid(row=3,column=1)
  Jinora.grid(row=3,column=2)
  Jinora_info.grid(row=3,column=3)
  C3.grid(row=5,column=1)
  Zaheer.grid(row=5,column=2)
  Zaheer_info.grid(row=5,column=3)
  






#Opening options
Legend=1

intro=Label(root,text="Choose Your Element",bg="red")
intro.config(font=('Helvatical bold',20))

Atitle=Label(root,text="Air Bending",bg="pink")
Atitle.config(font=('Helvatical bold',10))
Air_bender=Button(root,image=Air_symbol,bg="blue",command=Air)


wtitle=Label(root,text="Water Bending",bg="pink")
wtitle.config(font=('Helvatical bold',10))
Water_bender=Button(root,image=Water_symbol,bg="blue")


etitle=Label(root,text="Earth Bending",bg="pink")
etitle.config(font=('Helvatical bold',10))
Earth_bender=Button(root,image=Earth_symbol,bg="blue")

ftitle=Label(root,text="Fire Bending",bg="pink")
ftitle.config(font=('Helvatical bold',10))
Fire_bender=Button(root,image=Fire_symbol ,bg="blue")





intro.grid(row=0,column=2)
Atitle.grid(row=1,column=1)
Air_bender.grid(row=1,column=2)
wtitle.grid(row=3,column=1)
Water_bender.grid(row=3,column=2)
etitle.grid(row=5,column=1)
Earth_bender.grid(row=5,column=2)
ftitle.grid(row=7,column=1)
Fire_bender.grid(row=7,column=2)
root.mainloop()



