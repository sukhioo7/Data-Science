import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import ImageTk, Image

# Loading the dataset
athelete = pd.read_csv('athlete_events.csv')

def show_img(image):
    global img  # Declare img as global to keep a reference to it
    img = ImageTk.PhotoImage(Image.open(image))
    panel.config(image=img)
    panel.image = img  # Keep a reference to the image to prevent it from being garbage collected

def button1():
    india_data=athelete[athelete.eq("India").any(axis=1)]
    india_medal_count=india_data.groupby("Sport")["Medal"].count().reset_index()
    india_medal_count=india_medal_count.sort_values(by="Medal", ascending=False).head(10)

    plt.figure(figsize=(7,5))
    sns.barplot(data=india_medal_count, x="Sport", y="Medal",palette='mako')
    plt.xticks(rotation=20)
    plt.title('Top 10 Medal winning sports by India',size=17)
    plt.xlabel('Name Of Sport')
    plt.ylabel('Number of Medals')
    plt.savefig('graph_img.jpg')
    show_img('graph_img.jpg')

def button2():
    gender_counts=athelete["Sex"].value_counts()
    gender_counts
    plt.figure(figsize=(7,5))
    arr=[0,0.2]
    colors = ['#006989','#E88D67']
    plt.pie(gender_counts, labels= ['Male','Female'],colors=colors,radius=1.1, shadow=True, explode=arr,autopct='%0.2f%%')
    plt.title("Male VS Female Participants", size=17)
    plt.savefig('graph_img.jpg')
    show_img('graph_img.jpg')

def button3():
    female_participants= athelete[(athelete.Sex=="F") & (athelete.Season=="Summer")][["Sex", "Year"]]
    female_participants= female_participants.groupby("Year").count().reset_index()

    plt.figure(figsize=(7,5))
    sns.barplot(data=female_participants, x="Year", y="Sex",palette='icefire')
    plt.xticks(rotation=90)
    plt.title("Total no. of female in summer olympic", size=17)
    plt.xlabel("")
    plt.ylabel("No. of female")
    plt.savefig('graph_img.jpg')
    show_img('graph_img.jpg')

def button4():
    medal_count=athelete.pivot_table(index='Team', columns='Medal', aggfunc='size', fill_value=0)
    medal_count['Total'] = medal_count.sum(axis=1)
    medal_count = medal_count.sort_values(by='Total', ascending=False)
    medal_count
    medal_count = medal_count.drop(columns='Total').head(10)
    medal_count
    medal_count = medal_count.reset_index().melt(id_vars='Team', var_name='Medal', value_name='Count')

    plt.figure(figsize=(7,5))
    sns.barplot(x='Team', y='Count', hue='Medal', data=medal_count, palette=['#EE4E4E', '#F6EEC9', '#A1DD70'])
    plt.title('Top 10 Countries by Medal in Olympics',size=17)
    plt.xlabel('')
    plt.ylabel('Number of Medals')
    plt.legend(title='Medal Type')
    plt.xticks(rotation=20)
    plt.savefig('graph_img.jpg')
    show_img('graph_img.jpg')

def button5():
    gold_medals=athelete.query('Medal=="Gold"')
    top5=gold_medals.groupby("Team")["Medal"].count().reset_index().sort_values(by="Medal", ascending=False).head()

    plt.figure(figsize=(7,5))
    sns.barplot(data=top5, x="Team", y="Medal", palette="vlag")
    plt.title("Top 5 Countries who won most Gold Medal", size=17)
    plt.xlabel("Top 5 Countries")
    plt.ylabel("Number of 5 Medal")
    plt.savefig('graph_img.jpg')
    show_img('graph_img.jpg')

def button6():
    gold_medals=athelete.query('Medal=="Gold"')
    abve_60=gold_medals[(gold_medals["Age"]>60) & (gold_medals["Medal"]=="Gold") ]

    plt.figure(figsize=(7,5))
    sns.countplot(data=abve_60, x="Sport", palette="crest")
    plt.title("Gold Medals winning Sports by above 60 years old", size=17)
    plt.savefig('graph_img.jpg')
    show_img('graph_img.jpg')

def button7():
    injpch= athelete[((athelete.Team=="India") | (athelete.Team=="Japan") | (athelete.Team=="China"))& ((athelete.Year==2006)|(athelete.Year==2008)|(athelete.Year==2010)|(athelete.Year==2012)|(athelete.Year==2014)|(athelete.Year==2016))]
    injpch=injpch.query('Medal==["Gold", "Bronze", "Silver"]')
    medals_over_time =injpch[injpch['Medal'].notnull()].groupby(['Year', 'NOC']).size().reset_index(name='Medal Count')

    plt.figure(figsize=(7,5))
    sns.lineplot(data=medals_over_time, x='Year', y='Medal Count', hue='NOC', marker='o')
    plt.title('Past 10 year Performance of India, China, and Japan',size=17)
    plt.xlabel('Year')
    plt.ylabel('Number of Medals')
    plt.legend(title='Country')
    plt.grid(alpha=0.3)
    plt.savefig('graph_img.jpg')
    show_img('graph_img.jpg')



root = tk.Tk()
root.title('Athlete Events')
root.geometry('1200x650')
root.config(bg='white')

heading = tk.Label(text='Olympic Athlete Events',font=('Impact',45),bg='white')
heading.grid(row=1,column=1,columnspan=3,pady=15)

sub_heading = tk.Label(text="Event's Findings",font=('Impact',25),bg='white')
sub_heading.grid(row=2,column=1,columnspan=2,pady=15)

btn1 = tk.Button(text="India's Top 10",font=('Harlow Solid Italic',16),bg='#FCDC94',relief='solid',width=15,command=button1)
btn1.grid(row=3,column=1,padx=15,pady=5)

btn2 = tk.Button(text='Male VS Female',font=('Harlow Solid Italic',16),bg='#78ABA8',relief='solid',width=15,command=button2)
btn2.grid(row=3,column=2,padx=15,pady=5)

btn3 = tk.Button(text='Female in Olympics',font=('Harlow Solid Italic',16),bg='#5A72A0',relief='solid',width=15,command=button3)
btn3.grid(row=4,column=1,padx=15,pady=5)

btn4 = tk.Button(text='Top 10 Contries',font=('Harlow Solid Italic',16),bg='#FF6969',relief='solid',width=15,command=button4)
btn4.grid(row=4,column=2,padx=15,pady=5)

btn5 = tk.Button(text='Top 5 Nations',font=('Harlow Solid Italic',16),bg='#FFF5E1',relief='solid',width=15,command=button5)
btn5.grid(row=5,column=1,padx=15,pady=5)

btn6 = tk.Button(text='Over 60',font=('Harlow Solid Italic',16),bg='#95D2B3',relief='solid',width=15,command=button6)
btn6.grid(row=5,column=2,padx=15,pady=5)

btn7 = tk.Button(text='Past 10 Year Performance',font=('Harlow Solid Italic',15),bg='#83B4FF',relief='solid',width=33,command=button7)
btn7.grid(row=6,column=1,columnspan=2)


panel = tk.Label(root,relief='solid')
panel.grid(row=2,column=3,rowspan=6)
show_img('logo.bin')

root.mainloop()