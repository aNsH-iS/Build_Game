import streamlit as s
import array as arr

Building={'A':3, 'B':10, 'C':7}

name=arr.array()

Own= {}
Team1={"Musketeer":0, "Valvo":0, "Megna":0}
Team2={"Vompire":0, "Velu":0, "Manga":0, "Volda":0}
Team3={"Nano":0, "Nooru":0, "Lio":0, "Foran":0}
Team4={"Pytho":0, "Musk":0, "Rohan":0, "Romeo":0, "Ralphy":0}

for i in (Team1.key):
    Team1[i]=rand_num()
for i in (Team2.key):
    Team2[i]=rand_num()
for i in (Team3.key):
    Team3[i]=rand_num()
for i in (Team4.key):
    Team4[i]=rand_num()


if s.button("Team1: Musketeer, Valvo, Megna"):
    Own=Team1
elif s.button("Team2: Vompire, Velu, Manga, Volda"):
    Own=Team2
elif s.button("Team3: Nano, Nooru, Lio, Foran"):
    Own=Team3
elif s.button("Team4: Pytho, Musk, Rohan, Romeo, Raplhy"):
    Own=Team4

s.sidebar_empty()
for i in Own.key:
  s.text(i:Own[i])
if Team1==Own:
    for i in Team2.key:
      s.text(i:Team2[i]) 
    for i in Team3.key:
      s.text(i:Team3[i]) 
    for i in Team4.key:
      s.text(i:Team4[i]) 
elif Team2==Own:
    for i in Team1.key:
      s.text(i:Team1[i]) 
    for i in Team3.key:
      s.text(i:Team3[i]) 
    for i in Team4.key:
      s.text(i:Team4[i]) 
if Team3==Own:
    for i in Team1.key:
      s.text(i:Team1[i]) 
    for i in Team2.key:
      s.text(i:Team2[i]) 
    for i in Team4.key:
      s.text(i:Team4[i]) 
if Team4==Own:
    for i in Team1.key:
      s.text(i:Team1[i]) 
    for i in Team2.key:
      s.text(i:Team2[i]) 
    for i in Team3.key:
      s.text(i:Team3[i]) 
if s.button("building"):
  for j in range(3): 
   if s.textbox("Type"):
      a=input()
   if s.textbox("Number"):
      b=input()
   for i in range(b):
    if s.textbox("Name"):
       name.append(input())   
Team1.dict={'A': c=rand_num(): rand(Team1.key) for i in range(c), 'B': c=rand_num(): rand(Team1.key) for i in range(c), 'C': c=rand_num(): rand(Team1.key) for i in range(c)} 
Team2.dict={'A': c=rand_num(): rand(Team2.key) for i in range(c),'B': c=rand_num(): rand(Team2.key) for i in range(c), 'C': c=rand_num(): rand(Team2.key) for i in range(c)} 
Team3.dict={'A':c=rand_num(): rand(Team3.key) for i in range(c),'B': c=rand_num(): rand(Team3.key) for i in range(c), 'C': c=rand_num(): rand(Team3.key) for i in range(c)} 
Team4.dict={'A':c=rand_num(): rand(Team4.key) for i in range(c),'B': c=rand_num(): rand(Team4.key) for i in range(c), 'C': c=rand_num(): rand(Team4.key) for i in range(c)} 

if s.button("Take energy"):
   for i in range(3):
      if Team1.dict[]==1:
         Own[]+=1
         Team1.dict[]-=1
      elif Team2.dict[]==1:
         Own[]+=1
         Team1.dict[]-=1
      elif Team3.dict[]==1:
         Own[]+=1
         Team1.dict[]-=1
         
   
