#!/usr/bin/env python
# coding: utf-8

# In[3]:


record = {1001 : {"Name" : "5-Star", "Price" : 20, "Qn" : 100},
         1002 :  {"Name" : "Cranberry", "Price" : 10, "Qn" :200},
         1003 :  {"Name" : "Alpenliebe", "Price" : 30, "Qn" : 50},
         1004 :  {"Name" : "Milka", "Price" : 40, "Qn" : 150},
         1005 :  {"Name" : "Dairy Milk", "Price" : 50, "Qn" :60}}
        


# In[4]:


print(record[1001]["Name"])
print(record[1001]["Price"])
print(record[1001]["Qn"])


# In[5]:


for key in record.keys():
    print(key,":",record[key]["Name"],"|",record[key]["Price"],"|",record[key]["Qn"])


# In[68]:


import json
import time
sale = ""
fd = open("Records.json", "r")
js = fd.read()
fd.close()
record = json.loads(js)
print("----------------------------- \n")
user_name = str(input("Enter your name:"))
user_mail = str(input("Enter your email:"))
user_phoneno = str(input("Enter your phone number:"))
user_id = str(input("Enter a user input id:"))
user_q  = int(input("Enter a quantity:"))
print("-----------------------------")

if(record[user_id]["Qn"] >= user_q):
    print("              BILL        \n")
    print("Name of the product          :", record[user_id]["Name"])
    print("Price of the product (Rs)    :", record[user_id]["Price"])
    print("Quantity of the product      :", user_q)
    print("---------------------------------------------------")
    print("Billing price                :", user_q * record[user_id]["Price"], "Rs")
    print("---------------------------------------------------")
    record[user_id]["Qn"] = record[user_id]["Qn"] - user_q
    print("--------------------------------\n")
    if(user_q * record[user_id]["Price"] > 99):
        print("There is going to be a 10% discount")
        discounted_price = (10/100 * user_q * record[user_id]["Price"])
        Final_price = user_q * record[user_id]["Price"] - discounted_price
        print(Final_price)
        print("---------------------------------------------------")
        print("Billing price after discount                :", Final_price, "Rs")
        print("---------------------------------------------------")
        print("-----------------\n")
    
    
    sale = user_name+ ","+ user_mail+ ","+user_phoneno+","+user_id+","+str(user_q)+","+str(user_q * record[user_id]["Price"])+ "," + time.ctime()+ "\n"
else:
    print("Sorry, There are no products in the inventory")
    print("There are only", record[user_id]["Qn"])
    print("Would you like to purchase it?")
    ch = str(input("Enter Y/y?"))
    if (ch == "Y" or ch == "y"):
        print("              BILL        \n")
        print("Name of the product          :", record[user_id]["Name"])
        print("Price of the product (Rs)    :", record[user_id]["Price"])
        print("Quantity of the product      :", record[user_id]["Qn"])
        print("---------------------------------------------------")
        print("Billing price                :", record[user_id]["Qn"] * record[user_id]["Price"], "Rs")
        print("---------------------------------------------------")
        record[user_id]["Qn"] = 0
        if(record[user_id]["Qn"] * record[user_id]["Price"] > 99):
            print("There is going to be a 10% discount")
            discounted_price = (10/100 * record[user_id]["Qn"]  * record[user_id]["Price"])
            Final_price = record[user_id]["Qn"] * record[user_id]["Price"] - discounted_price
            print(Final_price)
            print("---------------------------------------------------")
            print("Billing price after discount                :", Final_price, "Rs")
            print("---------------------------------------------------")
            print("-----------------\n")
        sale = user_name+ ","+ user_mail+ ","+user_phoneno+","+user_id+","+str(user_q)+","+str(record[user_id]["Qn"] * record[user_id]["Price"])+ "," + time.ctime()+ "\n"
    else:
        print("Thanks")
        


js = json.dumps(record)
fd = open("Records.json", "w")
fd.write(js)
fd.close()

fd = open("Sales_json.csv","a")
fd.write(sale)
fd.close()


# In[65]:


record


# In[7]:


record


# In[45]:


sale = user_name+ ","+ user_mail+ ","+user_phoneno+","+user_id+","+str(user_q)+","+str(record[user_id]["Qn"] * record[user_id]["Price"])+ "," + time.ctime()+"\n"


# In[46]:


sale


# In[54]:


if(user_q * record[user_id]["Price"] > 99):
    print("There is going to be a 10% discount")
    discounted_price = (10/100 * user_q * record[user_id]["Price"])
    Final_price = user_q * record[user_id]["Price"] - discounted_price
    print(Final_price)


# In[56]:


if(record[user_id]["Qn"] * record[user_id]["Price"] > 99):
    print("There is going to be a 10% discount")
    discounted_price = (10/100 * record[user_id]["Qn"]  * record[user_id]["Price"])
    Final_price = record[user_id]["Qn"] * record[user_id]["Price"] - discounted_price
    print(Final_price)


# In[ ]:




