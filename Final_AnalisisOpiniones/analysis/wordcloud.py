from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image

def mostrar_wordcloud(texto):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)
    
    root = tk.Tk()
    root.title("Wordcloud de Estadísticas")
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('wordcloud.png')
    
    img = Image.open("wordcloud.png")
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    
    root.mainloop()
