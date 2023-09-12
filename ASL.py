import tkinter as tk
import string
from PIL import Image, ImageTk


def convert_to_int_and_display_images():
    input_text = entry.get().lower()  
    integer_list = [str(letter_to_number[char]) for char in input_text if char in letter_to_number]
    result_label.config(text="Converted Numbers: " + " ".join(integer_list))

    
    for img_label in image_labels:
        img_label.config(image=None)

    
    for i, num in enumerate(integer_list):
        image_path = image_paths.get(num)
        if image_path:
            img = Image.open(image_path)
            img = img.resize((80, 80))  
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(window, image=img)
            img_label.image = img  
            img_label.grid(row=10, column=i+5, columnspan=1)


window = tk.Tk()
window.title("Letter to Number Converter with Images")


start_number = 1
end_number = 26


letter_to_number = {char: num for char, num in zip(string.ascii_lowercase, range(start_number, end_number + 1))}


image_paths = {"1":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter A.jpg" ,
    "2":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter B.jpg",
    "3":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter C.jpg" ,
    "4":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter D.jpg" ,
    "5":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter E.jpg" ,
    "6":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter F.jpg" ,
    "7":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter G.jpg" ,
    "8":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter H.jpg" ,
    "9":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter I.jpg" ,
    "10":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter J.jpg" ,
    "11":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter K.jpg" ,
    "12":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter L.jpg" ,
    "13":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter M.jpg" ,
    "14":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter N.jpg" ,
    "15":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter O.jpg" ,
    "16":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter P.jpg" ,
    "17":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter Q.jpg" ,
    "18":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter R.jpg" ,
    "19":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter S.jpg" ,
    "20":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter T.jpg" ,
    "21":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter U.jpg" ,
    "22":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter V.jpg" ,
    "23":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter W.jpg" ,
    "24":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter X.jpg" ,
    "25":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter Y.jpg" ,
    "26":"C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter Z.jpeg" ,
}

    
    



label = tk.Label(window, text="Enter your the word in lowercase:")
entry = tk.Entry(window)
convert_button = tk.Button(window, text="Translate into ASL", command=convert_to_int_and_display_images)
result_label = tk.Label(window, text="Converted Numbers: ")


label.grid(row=0, column=0, columnspan=2)
entry.grid(row=0, column=2, columnspan=2)
convert_button.grid(row=1, column=0, columnspan=4)
result_label.grid(row=2, column=0, columnspan=4)


image_labels = []


window.mainloop()




label = tk.Label(window, text="Enter your name:")
entry = tk.Entry(window)
convert_button = tk.Button(window, text="Translate into ASL", command=convert_to_int_and_display_images)
result_label = tk.Label(window, text="Converted Numbers: ")


label.grid(row=0, column=0, columnspan=2)
entry.grid(row=0, column=2, columnspan=2)
convert_button.grid(row=1, column=0, columnspan=4)
result_label.grid(row=2, column=0, columnspan=4)


image_labels = []


window.mainloop()




label = tk.Label(window, text="Enter your name in lowercase:")
entry = tk.Entry(window)
convert_button = tk.Button(window, text="Translate into ASL", command=convert_to_int_and_display_images)
result_label = tk.Label(window, text="Converted Numbers: ")


label.grid(row=0, column=0, columnspan=2)
entry.grid(row=0, column=2, columnspan=2)
convert_button.grid(row=1, column=0, columnspan=4)
result_label.grid(row=2, column=0, columnspan=4)


image_labels = []


window.mainloop()




label = tk.Label(window, text="Enter your name:")
entry = tk.Entry(window)
convert_button = tk.Button(window, text="Translate into ASL", command=convert_to_int_and_display_images)
result_label = tk.Label(window, text="Converted Numbers: ")


label.grid(row=0, column=0, columnspan=2)
entry.grid(row=0, column=2, columnspan=2)
convert_button.grid(row=1, column=0, columnspan=4)
result_label.grid(row=2, column=0, columnspan=4)


image_labels = []



