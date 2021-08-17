#!/usr/bin/env python
# coding: utf-8

# In[13]:


#for the Apache tika to work set up the enviornment with latest jdk version
#!pip install nltk
#!pip install glob
#!pip install tika==1.23    


# In[14]:



import pandas as pd
from .temp import *
import os
import glob
import re
import json
import nltk
from tika import parser
from nltk.tokenize import word_tokenize
nltk.download('punkt')

############global file declarations#############
info = {}
edu = {}
skill_set = []
path=''

finalData=[]
#################################################

# <h3>Cleaning of the raw resume</h3>

# <ol>Step 1 : Raw data from the resume is parsed using apache parser</ol>

# <ol>Step 2 : Conversion of data to upper and spliting them new line vise</ol>

# <ol>Step 3 : Removing the blank and empty lines from the splited lines and storing them in list</ol>

# In[15]:

def motherFunc(path):


    def clean_resume(data):
        df = data['content'].upper().splitlines()
        df2 = [x.strip() for x in df]
        df3 = [x for x in df2 if x != '']
        return df3


# In[16]:
    print('Already Started')

    raw_data = parser.from_file(path)

    cdf = clean_resume(raw_data)
    # In[17]:


    #for line in cdf:
        #print(line)


    # In[18]:


    #initializing the diction info for section division, edu dictionary for education division, and skill_set list for skils extraction


    # <h2>Section Division</h2>

    # In[19]:


    #For the matching the particular keys of info dictionary
    def match_line(line):
        if re.match(r'(?=.*\bOBJECTIVE\b)', line):
            return True
        if re.match(r'(?=.*\bSUMMARY\b)', line):
            return True
        if re.match(r'(?=.*\bRESEARCH\b)', line):
            return True
        if re.match(r'(?=.*\bEDUCATION\b)', line):
            return True
        if re.match(r'(?=.*\bINTEREST\b)', line):
            return True
        if re.match(r'(?=.*\bINDUSTRY\b)', line):
            return True
        if re.match(r'(?=.*\bDEVELOPMENT\b)', line):
            return True
        if re.match(r'(?=.*\bSKILL\b)', line):
            return True
        if re.match(r'(?=.*\bPROJECT\b)', line):
            return True
        if re.match(r'(?=.*\bPROFILE\b)', line):
            return True
        if re.match(r'(?=.*\bAWARD\b)', line):
            return True
        if re.match(r'(?=.*\bEXPERIENCE\b)', line):
            return True
        if re.match(r'(?=.*\bPUBLICATION\b)', line):
            return True
        if re.match(r'(?=.*\bPROFESSIONAL\b)', line):
            return True
        if re.match(r'(?=.*\bCONFERENCE\b)', line):
            return True
        if re.match(r'(?=.*\bFEST\b)', line):
            return True
        if re.match(r'(?=.*\bEXAM\b)', line):
            return True
        if re.match(r'(?=.*\bCULTURAL\b)', line):
            return True
        if re.match(r'(?=.*\bEXTRA\b)', line):
            return True
        if re.match(r'(?=.*\bPERSONAL\b)', line):
            return True
        if re.match(r'(?=.*\bREFERENCE\b)', line):
            return True
        if re.match(r'(?=.*\bDECLARATION\b)', line):
            return True


    # In[20]:


    #extracting the particular key for the dictionary
    def extract_key(line):
        if re.match(r'(?=.*\bOBJECTIVE\b)', line):
            return "OBJECTIVE"
        if re.match(r'(?=.*\bSUMMARY\b)', line):
            return "SUMMARY"
        if re.match(r'(?=.*\bRESEARCH\b)', line):
            return "RESEARCH"
        if re.match(r'(?=.*\bEDUCATION\b)', line):
            return "EDUCATION"
        if re.match(r'(?=.*\bINTEREST\b)', line):
            return "INTEREST"
        if re.match(r'(?=.*\bINDUSTRY\b)', line):
            return "INDUSTRY"
        if re.match(r'(?=.*\bDEVELOPMENT\b)', line):
            return "DEVELOPMENT"
        if re.match(r'(?=.*\bSKILL\b)', line):
            return "SKILL"
        if re.match(r'(?=.*\bPROJECT\b)', line):
            return "PROJECT"
        if re.match(r'(?=.*\bPROFILE\b)', line):
            return "PROFILE"
        if re.match(r'(?=.*\bAWARD\b)', line):
            return "AWARD"
        if re.match(r'(?=.*\bEXPERIENCE\b)', line):
            return "EXPERIENCE"
        if re.match(r'(?=.*\bPUBLICATION\b)', line):
            return "PUBLICATION"
        if re.match(r'(?=.*\bPROFESSIONAL\b)', line):
            return "PROFESSIONAL"
        if re.match(r'(?=.*\bCONFERENCE\b)', line):
            return "CONFERENCE"
        if re.match(r'(?=.*\bFEST\b)', line):
            return "FEST"
        if re.match(r'(?=.*\bEXAM\b)', line):
            return "EXAM"
        if re.match(r'(?=.*\bCULTURAL\b)', line):
            return "CULTURAL"
        if re.match(r'(?=.*\bEXTRA\b)', line):
            return "EXTRA"
        if re.match(r'(?=.*\bPERSONAL\b)', line):
            return "PERSONAL"
        if re.match(r'(?=.*\bREFERENCE\b)', line):
            return "REFERENCE"
        if re.match(r'(?=.*\bDECLARATION\b)', line):
            return "DECLARATION"


    # In[21]:


    #using the current line to produce key and con-current lines to produce the section & store in the value of the key 
    def formdict(key, line_num):
        key = extract_key(key)
        s = []
        while line_num < len(cdf):
            if match_line(cdf[line_num]):
                info[key] = s; 
                break
            else :
                s.append(cdf[line_num])
                line_num = line_num + 1
        return line_num


    # In[22]:


    #call for the dictionary with particular line to form the key
    for i in range(0, len(cdf)):
        if match_line(cdf[i]):
            i = formdict(cdf[i], i+1)


    # <h2>Extracting the Educational Details</h2>

    # In[23]:


    # Education Degrees

    edu_key = ['PH.D']
    edu_key1 = [ 'BE','B.E.', 'B.E', 'BS', 'B.SC','B.COM', 'B. TECH','BA']
    edu_key2 = ['CBSE', 'SECONDARY','ICSE', 'XII','HSC']
    edu_key3 = ['X','CBSE','ICSE','SSC']
    edu_key4 = ['ME', 'M.E', 'M.E.', 'MS', 'M.SC', 'M.TECH', 'MTECH','M.COM']


    # In[24]:


    #extracting the nearest floating number but if any other key is present it return none
    def extract_marks(i, l2):
        ekey = [
                'BE','B.E.', 'B.E', 'BS', 'B.SC', 
                'ME', 'M.E', 'M.E.', 'MS', 'M.SC', 
                'B.COM', 'B. TECH', 'M.TECH', 'MTECH',
                'PH.D', 'M.COM', 'BA', 'ICSE', 'X', 'XII', 
                'SSC', 'HSC', 'CBSE', 'SECONDARY'
            ]
        for ele in range(i, len(l2)):
            if re.match(rf'\d+\.\d+', l2[ele]):
                return l2[ele]
            if l2[ele] in ekey:
                return None



    # In[25]:
    def extract(education):
        edu = {}
        l1 = word_tokenize(' '.join(education))
        l2 = [x for x in l1 if x != ',' if x!= '%' if x != '(' if x != ')' if x != '&' if x != '.']

    #Calling the eductaion text
    #Tokenizing the text in words tokens and cleaning of special characters
    #Matching the educational keys from the edu_key list
    def extract_education(education):
        edu = {'secondary':'',
                'sr.secondary':'',
                'bachelors':'',
                'masters':'',
                'phd':''}
        
        l1 = word_tokenize(' '.join(education))
        l2 = [x for x in l1 if x != ',' if x!= '%' if x != '(' if x != ')' if x != '&' if x != '.']
        for i in range(0, len(l2)):
            for a in range(0, len(edu_key)):
                if re.match(rf'(?=.*\b{edu_key[a]}\b)', l2[i]):
                    marks = extract_marks(i+1, l2)
                    if marks is None:
                        edu['phd'] = ''
                    else:
                        edu['phd'] = marks+','+l2[i]
            for b in range(0, len(edu_key1)):
                if re.match(rf'(?=.*\b{edu_key1[b]}\b)', l2[i]):
                    marks = extract_marks(i+1, l2)
                    if marks is None:
                        edu['bachelors'] = ''
                    else:
                        edu['bachelors'] = marks+','+l2[i]
            for c in range(0, len(edu_key2)):
                if re.match(rf'(?=.*\b{edu_key2[c]}\b)', l2[i]):
                    marks = extract_marks(i+1, l2)
                    if marks is None:
                        edu['sr.secondary'] = ''
                    else:
                        edu['sr.secondary'] = marks
            for d in range(0, len(edu_key3)):
                if re.match(rf'(?=.*\b{edu_key3[d]}\b)', l2[i]):
                    marks = extract_marks(i+1, l2)
                    if marks is None:
                        edu['secondary'] = ''
                    else:
                        edu['secondary'] = marks
            for e in range(0, len(edu_key4)):
                if re.match(rf'(?=.*\b{edu_key4[e]}\b)', l2[i]):
                    marks = extract_marks(i+1, l2)
                    if marks is None:
                        edu['masters'] = ''
                    else:
                        edu['masters'] = marks+','+l2[i]
        return edu


    # In[28]:
    info.keys()

    edu = extract_education(info['EDUCATION'])
    #print(edu)

    finalData.append(edu)



    # <h2>Extracting the Skills</h2>

    # In[10]:


    #getting the pre-defined dataset of skills
    #converting them all to upper case for easier processing
    skill_df = pd.read_csv(r"C://django//resume//skillset.csv")
    skill_df = skill_df.applymap(lambda s:s.upper() if type(s) == str else s)


    # In[11]:


    #converting all the text to token and cleaning the special characters
    #checking if the token is present in the dataset then appending
    def extract_skill(txt):
        l1 = word_tokenize(' '.join(txt))
        l2 = [x for x in l1 if x != ',' if x!= '%' if x != '(' if x != ')' if x != '&' if x != '.' if x!= ':']
        skill_set = []
        for i in range(0, len(l2)):
            if l2[i] in skill_df.values:
                ##print(l2[i])
                skill_set.append(l2[i])

        return skill_set


    # In[12]:


    skill_set = extract_skill(info['SKILL'])
    #print(skill_set)
    finalData.append(skill_set)



    # In[21]:

    final=[]
    for key in info.keys():
        for i in range(len(info[key])):
            final.append(info[key][i].replace('\uf0b7',''))


    finalData.append(info)
    print(finalData)
    return finalData


    




