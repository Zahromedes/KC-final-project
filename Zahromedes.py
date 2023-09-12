import tkinter as tk
from PIL import Image, ImageTk

def open_image_a():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter A.jpg"
    open_image(file_path)

def open_image_b():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter B.jpg"
    open_image(file_path)

def open_image_c():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter C.jpg"
    open_image(file_path)

def open_image_d():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter D.jpg"
    open_image(file_path)

def open_image_e():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter E.jpg"
    open_image(file_path)

def open_image_f():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter F.jpg"
    open_image(file_path)  

def open_image_g():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter G.jpg"
    open_image(file_path) 

def open_image_h():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter H.jpg"
    open_image(file_path)

def open_image_i():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter I.jpg"
    open_image(file_path)   

def open_image_j():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter J.jpg"
    open_image(file_path)           

def open_image_k():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter K.jpg"
    open_image(file_path)

def open_image_l():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter L.jpg"
    open_image(file_path)

def open_image_m():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter M.jpg"
    open_image(file_path)

def open_image_n():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter N.jpg"
    open_image(file_path)

def open_image_o():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter O.jpg"
    open_image(file_path) 

def open_image_p():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter P.jpg"
    open_image(file_path)

def open_image_q():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter Q.jpg"
    open_image(file_path)   

def open_image_r():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter R.jpg"
    open_image(file_path)

def open_image_s():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter S.jpg"
    open_image(file_path)   

def open_image_t():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter T.jpg"
    open_image(file_path)

def open_image_u():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter U.jpg"
    open_image(file_path)   

def open_image_v():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter V.jpg"
    open_image(file_path)

def open_image_w():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter W.jpg"
    open_image(file_path)

def open_image_x():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter X.jpg"
    open_image(file_path)

def open_image_y():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter Y.jpg"
    open_image(file_path)

def open_image_z():
    file_path = "C:/Users/zahro/OneDrive/Desktop/Zoasl/pics/Letter Z.jpeg"
    open_image(file_path)   
      
def open_image(file_path):
    try:
        img = Image.open(file_path)
        img.show()
    except FileNotFoundError:
        print(f"File not found: {file_path}")


window = tk.Tk()
window.title("Asl")


button_a = tk.Button(window, text="Letter A", command=open_image_a)
button_a.pack(pady=10)
button_a.place(x=0, y=0)

button_b = tk.Button(window, text="Letter B", command=open_image_b)
button_b.pack(pady=10)
button_b.place(x=100, y=0)

button_c = tk.Button(window, text="Letter C", command=open_image_c)
button_c.pack(pady=10)
button_c.place(x=200, y=0)

button_d = tk.Button(window, text="Letter D", command=open_image_d)
button_d.pack(pady=10)
button_d.place(x=300, y=0)

button_e = tk.Button(window, text="Letter E", command=open_image_e)
button_e.pack(pady=10)
button_e.place(x=400, y=0)

button_f = tk.Button(window, text="Letter F", command=open_image_f)
button_f.pack(pady=10)
button_f.place(x=0, y=50)

button_g = tk.Button(window, text="Letter G", command=open_image_g)
button_g.pack(pady=10)
button_g.place(x=100, y=50)

button_h = tk.Button(window, text="Letter H", command=open_image_h)
button_h.pack(pady=10)
button_h.place(x=200, y=50)

button_i = tk.Button(window, text="Letter I", command=open_image_i)
button_i.pack(pady=10)
button_i.place(x=300, y=50)

button_j = tk.Button(window, text="Letter J", command=open_image_j)
button_j.pack(pady=10)
button_j.place(x=400, y=50)

button_k = tk.Button(window, text="Letter K", command=open_image_k)
button_k.pack(pady=10)
button_k.place(x=0, y=100)

button_l = tk.Button(window, text="Letter L", command=open_image_l)
button_l.pack(pady=10)
button_l.place(x=100, y=100)

button_m = tk.Button(window, text="Letter M", command=open_image_m)
button_m.pack(pady=10)
button_m.place(x=200, y=100)

button_n = tk.Button(window, text="Letter N", command=open_image_n)
button_n.pack(pady=10)
button_n.place(x=300, y=100)

button_o = tk.Button(window, text="Letter O", command=open_image_o)
button_o.pack(pady=10)
button_o.place(x=400, y=100)

button_p = tk.Button(window, text="Letter P", command=open_image_p)
button_p.pack(pady=10)
button_p.place(x=0, y=150)

button_q = tk.Button(window, text="Letter Q", command=open_image_q)
button_q.pack(pady=10)
button_q.place(x=100, y=150)

button_r = tk.Button(window, text="Letter R", command=open_image_r)
button_r.pack(pady=10)
button_r.place(x=200, y=150)

button_s = tk.Button(window, text="Letter S", command=open_image_s)
button_s.pack(pady=10)
button_s.place(x=300, y=150)

button_t = tk.Button(window, text="Letter T", command=open_image_t)
button_t.pack(pady=10)
button_t.place(x=400, y=150)

button_u = tk.Button(window, text="Letter U", command=open_image_u)
button_u.pack(pady=10)
button_u.place(x=0, y=200)

button_v = tk.Button(window, text="Letter V", command=open_image_v)
button_v.pack(pady=10)
button_v.place(x=100, y=200)

button_w = tk.Button(window, text="Letter W", command=open_image_w)
button_w.pack(pady=10)
button_w.place(x=200, y=200)

button_x = tk.Button(window, text="Letter X", command=open_image_x)
button_x.pack(pady=10)
button_x.place(x=300, y=200)

button_y = tk.Button(window, text="Letter Y", command=open_image_y)
button_y.pack(pady=10)
button_y.place(x=400, y=200)

button_z = tk.Button(window, text="Letter Z", command=open_image_z)
button_z.pack(pady=10)
button_z.place(x=250, y=250)
window.mainloop()

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
            img = img.resize((150, 150))  
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(window, image=img)
            img_label.image = img  
            img_label.grid(row=i + 3, column=0, columnspan=2)



window.mainloop()



