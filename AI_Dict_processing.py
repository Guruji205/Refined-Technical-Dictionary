
# coding: utf-8

# In[2]:


import os
f=open("/home/nupur/internship/Refined-Technical-Dictionary/Computer_Science_Glossary_(English-Hindi)","r")
final=open("/home/nupur/internship/Refined-Technical-Dictionary/Final_Computer_Science_Glossary_English-Hindi","w+")
AIdict=f.read().split("\n")
#print(AIdict)

#wx=open("/home/nupur/Convert_utf_wx/wx_tmp","w")
wx_list=[]
E_words=[]
os.chdir("/home/nupur/Convert_utf_wx/")
for i in AIdict :
    eng_temp=i.split("\t")[::2]
    eng="".join(eng_temp)
    E_words.append(eng)
    hin=open("/home/nupur/Convert_utf_wx/hin_tmp","w")
    temp=i.split("\t")[1::2]
    hindi="".join(temp)
    #print(hindi,"#####")
    hin.write(hindi)
    os.system("sh utf8_to_wx.sh hin_tmp wx_tmp")
    wx=open("wx_tmp","r")
    wx_word=wx.read()
    #print(wx_word)
    if wx_word != "" :
        wx_list.append(wx_word)
for i,j in zip(E_words,wx_list) :
    str1=i+" <> "+j
    print(str1)
    final.write(str1+"\n")    

