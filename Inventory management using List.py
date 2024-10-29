#!/usr/bin/env python
# coding: utf-8

# In[1]:


fd = open("Inventory.txt", "w")
fd.close()


# In[2]:


ls


# # Mark down of data
# 1. Product ID
# 2. Product name
# 3. Product price
# 4. Quantity

# In[19]:


fd = open("Inventory.txt", "r")
products = fd.read().split("\n")
fd.close()


# In[22]:


products


# In[59]:


for product in products:
    print(product)


# In[89]:


user_1 = input("Enter a product_id:")
user_q = input("Enter a quantity needed :")
for product in products:
    indices = product.split(",")
    print(indices)
    if indices[0] == user_1:
        print("---------------------")
        print("Product ID", indices[0])
        print("Product Name", indices[1])
        print("Product Price", indices[2])
        print("Billing price" , int(user_q) * int(indices[2]))
        print("----------------------")
        print(indices)
    
        


# In[269]:


fd = open("Inventory.txt", "r")
products = fd.read().split("\n")
fd.close()
    



# In[270]:


products


# In[235]:


for i in updated_prod_indices:
    print(i)


# In[216]:


for i in products:
    print(i)


# In[259]:


updated_prod_indices


# In[262]:


updated_prod_indices[-1] = updated_prod_indices[-1][:-1]
print(updated_prod_indices)


# In[265]:


updated_prod_indices


# In[271]:


ls


# In[379]:


fd = open("Inventory.txt", "w")
fd.close()


# In[451]:


fd = open("Inventory.txt", "r")


# In[452]:


print(items)


# In[450]:


type(items)


# In[437]:


splitted = items.split("\n")


# In[438]:


splitted


# In[439]:


print(len(splitted))


# In[429]:


splitted[0]


# In[430]:


type(splitted)


# In[448]:


import time
user_name = input("Enter your name:")
user_phone_no = input("Enter your phone no:")
user_mail = input("Enter your e-mail:")
user_1 = input("Enter a product ID:")
user_q = input("Enter a quantity:")
updated_env_lst = []
for spl in splitted:
    products = spl.split(",")
    if products[0] == user_1:
        if int(user_q) <= int(products[3]):
            print("--------")
            print("Product ID" , products[0])
            print("Product Name" , products[1])
            print("Product Price" , products[2])
            print("Billing Price" , int(user_q) * int(products[2]))
            print("--------")
            products[3] = str(int(products[3]) - int(user_q))

            fd = open("Sales.txt", "a")
            sales_info = user_name + "," + user_phone_no + "," + user_mail + "," + user_1 + "," + user_q + "," + str(int(user_q) * int(products[2])) + "," + time.ctime() + "\n"
            fd.write(sales_info)
            fd.close()
        else:
            print("Sorry.We are not having enough quantity")
            print("We 're having only", products[3], "quantity")
            print("Would you like to purchase it?")
            
            ch = input("Y/N?")
            if ch == "Y" or ch == "y":
                print("--------")
                print("Product ID" , products[0])
                print("Product Name" , products[1])
                print("Product Price" , products[2])
                print("Billing Price" , int(products[3]) * int(products[2]))
                print("--------")
                fd = open("Sales.txt", "a")
                sales_info = user_name + "," + user_phone_no + "," + user_mail + "," + user_1 + "," + user_q + "," + str(int(products[3]) * int(products[2])) + "," + time.ctime() + "\n"
                fd.write(sales_info)
                fd.close()
                products[3] = "0"
                

                
            
    updated_env_lst.append(products)
    print(updated_env_lst)
    print(products)
lst = []
for i in updated_env_lst:
    prod = i[0] + "," + i[1] + "," + i[2] + "," + i[3] + "\n"
    lst.append(prod)
lst[-1] = lst[-1][:-1]
print(lst)
fd = open("Inventory.txt", "w")
for i in lst:
    fd.write(i)
fd.close()

    


# In[340]:


spl


# In[350]:


products


# In[449]:


lst = []
for i in updated_env_lst:
    print(i)
    prod = i[0] + "," + i[1] + "," + i[2] + "," + i[3] + "\n"
    lst.append(prod)
    print(lst)


# In[396]:


lst[-1] = lst[-1][:-1]


# In[358]:


for i in products:
    print(i)


# In[ ]:




