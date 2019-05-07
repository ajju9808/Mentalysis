from tkinter import *
import MentalysisMainAlgo

print("Designing UI")
root = Tk()
root.wm_title('Sentiment Analysis Application')

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

l1 = Label(top_frame, text='Enter a review:')
l1.pack(side=LEFT)

w = Text(top_frame, height=3 )
w.pack(side=LEFT)

"""Making Object of Mentalysis Class"""
print("UI COMPLETE")
clf = MentalysisMainAlgo.Mentalsis()

def main_op():
    review_spirit = w.get('1.0',END)

    d = ("The Sentiment value of the Review is ", clf.calculatingSentiment(review_spirit))
    l2 = Label(bottom_frame, text=d)
    l2.pack()

button = Button(bottom_frame, text='Analyse', command=main_op )
button.pack(side=BOTTOM)

root.mainloop()