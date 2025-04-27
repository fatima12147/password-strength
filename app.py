import re
import streamlit as st

# page styling   : step no 1


st.set_page_config(page_title="password strenght generator created by syeda sehar" ,layout="centered")

# page title and description : step no 2

st.title("password strenght generator")
st.write ("enter your password below to its security level ")

# function to check password strenght:  step no 3

def check_password_strenght(password):
    score = 0
    feedback= []

    if len(password) >= 8:
        score += 1 # increase by score 1 
    else :
        feedback.append("password should be ** at least 8 characters long **.")
    
    if re.search(r"[A-Z]", password)and re.search("r[a-z]",password):
        score+= 1
    
    else:
        feedback.append("password should include ** both upper case [ A-Z ] and lower case [ a-z ] letters**.")

    if re.search(r"\d", password):
        score +=1

    else:
        feedback.append("password should include ** atleast one number (0-9)**.")

# special character  : step no 4 

    if re.search(r"[!@$%^&*]", password):
        score +=1

    else:
        feedback.append("include ** atleast one special character [ !@#$%^&*]**.")

# display password strenght result:  step no 5 


    if score == 4:
      st.success("**strong password**: your password is secure .")

    elif score == 3:
        st.info("**moderate password**: consider improving security by adding more features.")
    
    else:
        st.error("**weak password ** :follow the suggestion below to strenght it .")


    # feedback :  step no 6 

    if feedback:
        with st.expander("**improve your password**"):
            for items in feedback:
                st.write(items)
password = st.text_input("enter your password", type ="password", help = "ensure your password is strong ")


   # button working   : step no 7 



if st.button("check strength"):
       if password:
        check_password_strenght(password)
       else:
        st.warning("please enter your password first !")
import re
import streamlit as st

# page styling   : step no 1


st.set_page_config(page_title="password strenght generator created by syeda sehar" ,layout="centered")

# page title and description : step no 2

st.title("password strenght generator")
st.write ("enter your password below to its security level ")

# function to check password strenght:  step no 3

def check_password_strenght(password):
    score = 0
    feedback= []

    if len(password) >= 8:
        score += 1 # increase by score 1 
    else :
        feedback.append("password should be ** at least 8 characters long **.")
    
    if re.search(r"[A-Z]", password)and re.search("r[a-z]",password):
        score+= 1
    
    else:
        feedback.append("password should include ** both upper case [ A-Z ] and lower case [ a-z ] letters**.")

    if re.search(r"\d", password):
        score +=1

    else:
        feedback.append("password should include ** atleast one number (0-9)**.")

# special character  : step no 4 

    if re.search(r"[!@$%^&*]", password):
        score +=1

    else:
        feedback.append("include ** atleast one special character [ !@#$%^&*]**.")

# display password strenght result:  step no 5 


    if score == 4:
      st.success("**strong password**: your password is secure .")

    elif score == 3:
        st.info("**moderate password**: consider improving security by adding more features.")
    
    else:
        st.error("**weak password ** :follow the suggestion below to strenght it .")


    # feedback :  step no 6 

    if feedback:
        with st.expander("**improve your password**"):
            for items in feedback:
                st.write(items)
password = st.text_input("enter your password", type ="password", help = "ensure your password is strong ")


   # button working   : step no 7 



if st.button("check strength"):
       if password:
        check_password_strenght(password)
       else:
        st.warning("please enter your password first !")
import re
import streamlit as st

# page styling   : step no 1


st.set_page_config(page_title="password strenght generator created by syeda sehar" ,layout="centered")

# page title and description : step no 2

st.title("password strenght generator")
st.write ("enter your password below to its security level ")

# function to check password strenght:  step no 3

def check_password_strenght(password):
    score = 0
    feedback= []

    if len(password) >= 8:
        score += 1 # increase by score 1 
    else :
        feedback.append("password should be ** at least 8 characters long **.")
    
    if re.search(r"[A-Z]", password)and re.search("r[a-z]",password):
        score+= 1
    
    else:
        feedback.append("password should include ** both upper case [ A-Z ] and lower case [ a-z ] letters**.")

    if re.search(r"\d", password):
        score +=1

    else:
        feedback.append("password should include ** atleast one number (0-9)**.")

# special character  : step no 4 

    if re.search(r"[!@$%^&*]", password):
        score +=1

    else:
        feedback.append("include ** atleast one special character [ !@#$%^&*]**.")

# display password strenght result:  step no 5 


    if score == 4:
      st.success("**strong password**: your password is secure .")

    elif score == 3:
        st.info("**moderate password**: consider improving security by adding more features.")
    
    else:
        st.error("**weak password ** :follow the suggestion below to strenght it .")


    # feedback :  step no 6 

    if feedback:
        with st.expander("**improve your password**"):
            for items in feedback:
                st.write(items)
password = st.text_input("enter your password", type ="password", help = "ensure your password is strong ")


   # button working   : step no 7 



if st.button("check strength"):
       if password:
        check_password_strenght(password)
       else:
        st.warning("please enter your password first !")
    