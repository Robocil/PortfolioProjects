#!/usr/bin/env python
# coding: utf-8

# In[25]:


name = input("Enter you name: ")

weight = int(input("Enter your weight in pounds: "))

height_feet = int(input("Enter your height(ft): "))

height_inches = int(input("Enter your height (in): "))

height = (height_feet * 12) + height_inches

BMI = (weight * 703) / (height * height)

BMI_str = str(BMI)

print ("BMI: " + BMI_str)

if BMI>0:
    if(BMI < 18.5):
        print(name +", you are Underweight.")
    elif(BMI <= 24.9):
        print (name +", you are normal weight.")
    elif(BMI <= 29.9):
        print (name + ", you are overweight.")
    elif(BMI <= 34.9):
        print (name + ", you are obese.")    
    elif(BMI <= 39.9):
        print (name + ", you are severely obese.")
    elif(BMI >= 40):
        print (name + ", you are morbidely obese")
    else:
        print("Enter valid inputs")


# In[24]:


#BMI = (weight in pounds x 703) / (height in inches x height in inches)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




