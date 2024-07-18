# Importing Necessory Modules
import backend as bs
from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as msg

# Define a class for animals
classes=['Bear','Cat','Dog','Lion']

#Loading artifects from backend
bs.load_saved_artifects()

# define mainclass | Tkinter Graphical User Interface
class Main:
    def __init__(self,root):
        self.root=root
        self.root.title("Animal Classification Software")
        self.root.geometry("1360x690+0+0")
        self.root.resizable(0,0)

        # MainFrame
        self.main_framee=Frame(self.root,bg='white')
        self.main_framee.pack(fill=BOTH,expand=True)
        
        # Border1
        self.border1=Label(self.main_framee,bg="lightgreen",fg="black",bd=10,relief=RIDGE,text="Animal Classification",font=("times new roman",40,'bold'))
        self.border1.pack(side=TOP,fill=X)
        
        # Border2
        self.border2=Label(self.main_framee,bg="lightgreen",fg="black",bd=10,relief=RIDGE,font=("times new roman",40,'bold'),text="Convolutional Neural Network")
        self.border2.pack(side=BOTTOM,fill=X)
        
        # MainLabel
        self.main_label=Label(self.main_framee,text="Enter Path : ",background="white",fg="black",font=('times new roman',30,'bold'))
        self.main_label.place(x=10,y=130)

        # MainEntry
        self.path=StringVar()
        self.main_entry=Entry(self.main_framee,font=('times new roman',20,'bold'),bd=10,relief=RIDGE,textvariable=self.path)
        self.main_entry.place(x=250,y=130,width=750)
        
        # ButtonForClassifyingImages
        self.classify_btn=Button(self.main_framee,text="Classify",bd=10,relief=GROOVE,font=("times new roman",17,'bold'),bg="lightgreen",fg="black",activebackground="lightgreen",command=self.classify)
        self.classify_btn.place(x=1010,y=125,width=300)
        
        # Button For Clear the fields
        self.clear_btn=Button(self.main_framee,text="Clear",bd=10,relief=GROOVE,font=("times new roman",17,'bold'),bg="lightgreen",fg="black",activebackground="lightgreen",command=self.clear)
        self.clear_btn.place(x=1010,y=200,width=300)
        
        # Text area for animal Information
        self.txt=Text(self.main_framee,bd=5,relief=GROOVE,bg="#7CB9E8",fg="black",font=("times new roman",10,'bold'))
        self.txt.place(x=510,y=290,height=300,width=830)

    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''functionality'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def classify(self):
        
        #Error Handling
        if self.path.get()=='':
           msg.showerror("Empty Error","Please input right path")
           self.main_entry.delete(0,END)

        else:
           try:
              #Getting image path
              path=self.path.get()
              #TypeCasting
              path=str(path)
              #ClassifyingImageUsingCNNModel
              value=bs.classify_image(path)
              #Deletetextfromentry
              self.main_entry.delete(0,END)
              #ExtractingNameFromList
              name=classes[value]
              #OpeningImageUsingPillow
              img=Image.open(path)
              #ResizeImage
              img1=img.resize((500,400))
              self.photo_1=ImageTk.PhotoImage(img1)
              #DisplayingImageUsingLabel
              self.lb2=Label(self.main_framee,image=self.photo_1)
              self.lb2.place(x=0,y=200,width=500,height=400)

              #BearInfo
              if value==0:
                self.lbl1=Label(self.main_framee,text=f"{name}:",font=("times new roman",50,'bold'),background="white")
                self.lbl1.place(x=510,y=200)
                text="Bears are carnivoran mammals of the family Ursidae. They are classified as caniforms, or doglike carnivorans. Although only eight species of bears are extant, they are widespread, appearing in a wide variety of habitats throughout most of the Northern Hemisphere and partially in the Southern Hemisphere \n\nSpeed : 48 km/h (Maximum, Adult)\nScientific name: Ursidae\nTerm for young: Cub\nClass: Mamalia\n\nBears are carnivoran mammals of the family Ursidae (/ˈɜːrsɪdiː, -daɪ/). They are classified as caniforms, or doglike carnivorans. Although only eight species of bears are extant, they are widespread, appearing in a wide variety of habitats throughout most of the Northern Hemisphere and partially in the Southern Hemisphere. Bears are found on the continents of North America, South America, and Eurasia. Common characteristics of modern bears include large bodies with stocky legs, long snouts, small rounded ears, shaggy hair, plantigrade paws with five nonretractile claws, and short tails."
                self.txt.delete(1.0,END)
                self.txt.insert(1.0,text)
              #CatInfo  
              elif value==1:
                self.lbl1=Label(self.main_framee,text=f"{name}:",font=("times new roman",50,'bold'),background="white")
                self.lbl1.place(x=510,y=200)
                text="A cat is a small, domesticated carnivorous mammal belonging to the species Felis catus. Here are some key points about cats:\nBreeds: There are many different cat breeds, each with unique characteristics and traits. Breeds vary in size, coat length, color patterns, and temperament.Physical Characteristics: Cats have a flexible body, sharp retractable claws, and keen senses of sight, hearing, and smell. They are known for their agility and ability to jump great distances.Behavior: Cats are known for their independence, curiosity, and playful behavior. They communicate through vocalizations (like meowing and purring), body language, and scent marking.Care: Responsible cat ownership includes providing proper nutrition, regular veterinary care, grooming (especially for long-haired breeds), and a stimulating environment. Cats benefit from interactive play and opportunities to engage in natural behaviors like scratching and climbing.Lifespan: The average lifespan of a cat is around 12 to 15 years, although many cats live well into their late teens or early twenties with proper care"
                self.txt.delete(1.0,END)
                self.txt.insert(1.0,text)
              #DogInfo  
              elif value==2:
                self.lbl1=Label(self.main_framee,text=f"{name}:",font=("times new roman",50,'bold'),background="white")
                self.lbl1.place(x=510,y=200)
                text="A dog is a domesticated mammal belonging to the species Canis lupus familiaris. Here are some key points about dogs\nOrigins and Evolution: Dogs are descendants of wolves and have been domesticated by humans for thousands of years. They were likely the first animals to be domesticated.\nRoles and Uses: Throughout history, dogs have been bred for various purposes such as hunting, herding, guarding, companionship, and as working animals (e.g., service dogs, police dogs, therapy dogs).\nBreeds: There are hundreds of dog breeds, each with unique characteristics and traits. Breeds vary widely in size, appearance, temperament, and purpose.Physical Characteristics: Dogs typically have a keen sense of smell, good hearing, and a wide range of physical abilities. They come in various sizes, from tiny breeds like Chihuahuas to large breeds like Great Danes\nBehavior: Dogs are known for their loyalty, social nature, and ability to form strong bonds with humans. They communicate through body language, vocalizations, and behavior.\nCare: Responsible dog ownership includes providing proper nutrition, regular exercise, veterinary care, and training. Socialization and mental stimulation are also important for a dog's well-being.\nLifespan: The average lifespan of a dog varies by breed and size but generally ranges from 10 to 15 years. Some small breeds can live longer, while larger breeds may have shorter lifespans."
                self.txt.delete(1.0,END)
                self.txt.insert(1.0,text)
              #LionInfo
              else:
                self.lbl1=Label(self.main_framee,text=f"{name}:",font=("times new roman",50,'bold'),background="white")
                self.lbl1.place(x=510,y=200)
                text="The lion is a large cat of the genus Panthera, native to Africa and India. It has a muscular, broad-chested body; a short, rounded head; round ears; and a dark, hairy tuft at the tip of its tail. It is sexually dimorphic; adult male lions are larger than females and have a prominent mane\n\nMass: 190kg\nSpeed: 74km/h\nScientific Name:Panthera leo\n\nThe lion inhabits grasslands, savannahs, and shrublands. It is usually more diurnal than other wild cats, but when persecuted, it adapts to being active at night and at twilight. During the Neolithic period, the lion ranged throughout Africa and Eurasia, from Southeast Europe to India, but it has been reduced to fragmented populations in sub-Saharan Africa and one population in western India. It has been listed as Vulnerable on the IUCN Red List since 1996 because populations in African countries have declined by about 43% since the early 1990s. Lion populations are untenable outside designated protected areas. Although the cause of the decline is not fully understood, habitat loss and conflicts with humans are the greatest causes for concern."
                self.txt.delete(1.0,END)
                self.txt.insert(1.0,text)
           except:
               ValueError
    #FunctionForClearFields           
    def  clear(self):
       self.txt.delete(1.0,END)
       self.lbl1.destroy() 
       self.lb2.destroy()  

if __name__ == "__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()

    