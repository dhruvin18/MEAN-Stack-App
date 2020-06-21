#excel read and write imports and re for regular expression
import xlrd
import xlwt
import re

#create a new excel sheet 
newwb=xlwt.Workbook()
newws=newwb.add_sheet('Labelled_Dataset')
sentence=[]
#keywords list curated manually identified for labelling
#postive list
tempposwords=['In the event of the arrest of the applicants in the territory of this state each of the applicants be released on bail','applicant-accused be released on bail','Accused be released on bail','present appellants be released on bail in the event of their arrest','Criminal Appeal stands allowed','bail is quashed and set aside','The petition is accordingly allowed','satisfied that the accused-applicant deserves granting of bail','Trial Court should lay off the hands from taking any action against these applicants for arresting them','The appeal is allowed','must be quashed and set aside','THE Revision is partly allowed','applications under consideration deserves to succeed','applicant shall be released forthwith on the same bail','Petitions allowed','PRAYER for cancellation of bail made by the prosecution against all other respondents is hereby allowed','we allow this petition','we allow this petition; quash and set aside the impugned detention order','Application for anticipatory bail is allowed','The petitioners be released on bail','Applicant\'s interim bail granted','find the impugned order of detention unsustainable','I find this to be a fit case in which the petitioner deserves to be grant anticipatory bail','APPLICATION allowed','at the commencement of this order that I have granted bail','In the event of the arrest of the Applicants, the Applicants shall be released on bail','petition is hereby allowed','it is a case to protect the applicants/accused by granting pre-arrest bail','this is a fit case for grant of bail to applicant-petitioner','In the event of the arrest of the Applicant, the Applicant shall be released on bail','Applicant shall be released on bail','All these three petitions are allowed','application succeeds','It is directed that the Applicant be released on bail','Applicant be released on bail','Criminal Application for cancellation of bail is allowed','I direct that the applicant be enlarged on bail','applicant/accused shall be released on bail','application is partly allowed','appellant will be relcased on bail','petitioner is directed to be released on bail','Application succeed','petitioner is ordered to be released on bail','bail granted by the Magistrate is also hereby set aside','anticipatory bail granted to the respondents is cancelled','Applicant shall be enlarged on bail','detenus are directed to be released forthwith','Petition is allowed','Prayer for cancellation of bail made by the prosecution against all other respondents is hereby allowed','allow the above application','allow both these applications','detenu shall be set at liberty','accused be enlarged on bail','Petition allowed','petition is allowed','petition partly succeeds','Application allowed','detenu is directed to be released forthwith','detenu be released forthwith','appellants be ordered to be enlarged on bail','application is allowed','detenu be released','Application is allowed','Applications are allowed','application for cancellation of bail is allowed','For the aforesaid reasons, accused be released','Applicants in both the applications shall be released on bail','applications are allowed','applicant is granted bail','Applications filed by the Customs Department/State are accordingly allowed','detention order is unsustainable and the petition succeeds','Applicant is ordered to be released on bail','applicant is ordered to be released on bail','applicant shall be enlarged on bail','bail is granted subject to condition','against the petitioner is quashed and set aside','the applicants are granted bail']
#negative list
tempnegwords=['the Revision Applications are dismissed','appeal fails and stands dismissed','Application, therefore, is hereby dismissed','cannot be a ground to entertain subsequent application for grant of anticipatory bail','see no reason to entertain this second application for anticipatory bail','application is concerned, it stands dismissed','petitioner shall continue to be on bail unless the said bail is cancelled','the application is hereby dismissed','The application is, therefore, rejected','The petition, therfore, fails','This application is devoid of material particulars, and, therefore, not maintainable','we have taken the petitions will have to be dismissed and are dismissed','Accordingly, this Application stands rejected','these applications cannot be granted','I do not think that it would be proper to reduce the bail amount','WE, therefore, dispose of this petition','order disposes of the two applications for cancellation of bail','I find no merit in this petition','their remand is valid and legal, and, therefore the applicants are not entitled to bail','this is not a case where the petitioner should be readmitted to bail','this repeated bail application stands dismissed','applicant stands rejected','the bail application made by the accused/petitioner has to be rejected and is accordingly rejected','the objections raised to the detention order are not convincing','Writ Petition, being devoid of substance, stands dismissed','I reject all the above applications','I find there is no merit in this application and consequently the same is hereby dismissed','no case is made out by the petitioner for quashing and setting aside the order of detention','application is required to be and accordingly rejected','the applicant cannot be admitted to bail','applications are, therefore, rejected','directed not to release the convicted accused on bail','application fails and dismissed accordingly','prayer for suspending the operation of this order is rejected','Petition is devoid of merits, hence rule stands discharged','order putting the petitioner in police custody is hereby quashed','Interim relief stands vacated','the appeal is rejected','no case made out for interference in the impugned order of detention of the detenu','petition fails and is hereby dismissed','application for anticipatory bail/ pre-arrest bail order stands rejected','application deserves to be rejected and accordingly same is rejected','application, therefore, stands rejected','present application therefore deserves to be rejected and is hereby rejected','reject this application for anticipatory bail','applicant-accused for bail stands dismissed','application for cancellation of bail is rejected','application is not maintainable and consequently the same is rejected','application is dismissed','Application is dismissed','application is rejected','Application is rejected','application is disposed of accordingly','Application for bail is rejected','application for bail is rejected','Writ Petition is disposed off','applications stand dismissed','bail application is accordingly rejected','Application is accordingly rejected','application is hence rejected','Application rejected','application fails and it is dismissed','petition will stand rejected','appeals are dismissed','applications are hereby dismissed as not maintainable','applications stand rejected','application stands rejected','petition is dismissed','Petition is dismissed','Application is accordingly disposed of','Application dismissed','applications stand adjourned','criminal applications is accordingly rejected','application for anticipatory bail is rejected']

#initialization
tempcount=0
poscount=0
negcount=0
totalcount=0
ambi=0
poswords=[]
negwords=[]
#list converted to lower cases and made unique
for t in tempposwords:
    if str(t).lower() not in poswords:
        poswords.append(str(t).lower())

for t in tempnegwords:
    if str(t).lower() not in negwords:
        negwords.append(str(t).lower())
#labelling method
#filename is excel sheet with all names, file folder is where all the text files are stored and max cases is the number of cases for the highcourt

def labelling(filename,file_folder,max_cases):
    location=filename
    #read the excel sheet
    workbook=xlrd.open_workbook(location)
    worksheet=workbook.sheet_by_index(0)
    global totalcount
    global tempcount
    global poscount
    global negcount
    global ambi
    #iterate for each case
    for i in range(1,max_cases):
        positive=0
        hit=0
        lastflag=False
        print(worksheet.cell_value(i,1))
        filename=file_folder+worksheet.cell_value(i,2)
        #read file from the folder
        f=open(filename,'r')
        casefacts=f.read()
        #split on new line
        sentence=casefacts.split('\n')
        for s in sentence:
            #s=s.strip()
            #print(s)
            if not s:
                continue
            elif len(s)<5:
                continue
            else:
                for k in poswords:
                    #regular expression search ignoring cases for positive tags
                    if re.search(k,s,re.IGNORECASE):
                        print(k)
                        positive+=1
                        lastflag=True
                        hit+=1
                #regular expression search ignoring cases for negative tags
                for k in negwords:
                    if re.search(k,s,re.IGNORECASE):
                        print("- "+k)
                        positive-=1
                        lastflag=False
                        hit+=1
                #combination of keywords in same sentence
                if 'Criminal Application' in s or 'Criminal Bail Application Nos' in s or 'Anticipatory Bail Applications' in s:
                    if 'is allowed' in s:
                        positive+=1
                        hit+=1
                        lastflag=True
                elif 'stands rejected' in s:
                    positive-=1
                    hit+=1
                    lastflag=False
                elif 'are allowed' in s:
                    positive+=1
                    hit+=1
                    lastflag=True
                elif 'is partly allowed' in s:
                    positive+=1
                    hit+=1
                    lastflag=True
                elif 'shall be released on bail' in s:
                    positive+=1
                    hit+=1
                    lastflag=True
                elif 'are rejected' in s:
                    positive-=1
                    hit+=1
                    lastflag=False
                if 'Criminal Revision Application' in s or 'Criminal Application' in s:
                    if 'succeeds' in s:
                        positive+=1
                        hit+=1
                        lastflag=True
                if 'event of the arrest of the applicants' in s:
                    if 'shall be released on bail' in s:
                        positive+=1
                        hit+=1
                        lastflag=True
                if 'Criminal Application Nos' in s or 'Criminal Applications Nos' in s or 'Criminal Miscellaneous Application' in s or 'petition' in s:
                    if 'stand rejected' in s:
                        positive-=1
                        hit+=1
                        lastflag=False
                elif 'stands rejected' in s:
                    positive-=1
                    hit+=1
                    lastflag=False
                elif 'are allowed' in s:
                    positive+=1
                    hit+=1
                    lastflag=True
                elif 'is dismissed' in s:
                    positive-=1
                    hit+=1
                    lastflag=False
                elif 'stands dismissed' in s or 'stand dismissed' in s:
                    positive-=1
                    hit+=1
                    lastflag=False
                elif 'is allowed' in s:
                    positive+=1
                    hit+=1
                    lastflag=True
                if 'Criminal Application' in s:
                    if 'is, therefore, rejected' in s:
                        positive-=1
                        hit+=1
                        lastflag=False
                elif 'is rejected' in s:
                    positive-=1
                    hit+=1
                    lastflag=False
                if 'Petitioner / Detenu' in s or 'Petitioner' in s:
                    if 'be set at liberty forthwith' in s:
                        positive+=1
                        hit+=1
                        lastflag=True
                if 'order of detention passed against the detenu' in s:
                    if 'cannot be sustained' in s:
                        positive+=1
                        hit+=1
                        lastflag=True
                if 'detenu' in s or 'Detenu' in s:
                    if 'is ordered to be released forthwith' in s:
                        positive+=1
                        hit+=1
                        lastflag=True
        print(positive)
        #postive value> 0 Label 1 else Label 0
        if positive>0:
            newws.write(totalcount,1,worksheet.cell_value(i,2))
            newws.write(totalcount,0,worksheet.cell_value(i,1))
            newws.write(totalcount,2,'yes')
            totalcount+=1
            poscount+=1 
        if positive<0:
            newws.write(totalcount,1,worksheet.cell_value(i,2))
            newws.write(totalcount,0,worksheet.cell_value(i,1))
            newws.write(totalcount,2,'no')
            totalcount+=1
            negcount+=1
        #if positive value is 0 check for the last tag, if tag is +ve Label 1 else 0 , if hit =0 dont label remove from dataset
        if positive==0:
            if hit>0:
                if lastflag==True:
                    newws.write(totalcount,1,worksheet.cell_value(i,2))
                    newws.write(totalcount,0,worksheet.cell_value(i,1))
                    newws.write(totalcount,2,'yes')
                    poscount+=1
                    totalcount+=1
                else:
                    newws.write(totalcount,1,worksheet.cell_value(i,2))
                    newws.write(totalcount,0,worksheet.cell_value(i,1))
                    newws.write(totalcount,2,'no')
                    negcount+=1
                    totalcount+=1
            else:
                ambi+=1
                # newws.write(tempcount,1,worksheet.cell_value(i,1))
                # tempcount+=1
                print(worksheet.cell_value(i,1))
   
labelling(r'C:\Users\Dhruvin\Desktop\Dataset\legal_cases_textfiles_karnataka.xlsx', r'C:\Users\Dhruvin\Desktop\Dataset\dataset_karnataka\\', 761)
labelling(r'C:\Users\Dhruvin\Desktop\Dataset\legal_cases_textfiles_bombay.xlsx', r'C:\Users\Dhruvin\Desktop\Dataset\dataset_bombay\\', 756 )
labelling(r'C:\Users\Dhruvin\Desktop\Dataset\legal_cases_textfiles_calcutta.xlsx', r'C:\Users\Dhruvin\Desktop\Dataset\dataset_calcutta\\', 764 )
labelling(r'C:\Users\Dhruvin\Desktop\Dataset\legal_cases_textfiles_delhi.xlsx', r'C:\Users\Dhruvin\Desktop\Dataset\dataset_delhi\\', 717 )
labelling(r'C:\Users\Dhruvin\Desktop\Dataset\legal_cases_textfiles_allahabad.xlsx', r'C:\Users\Dhruvin\Desktop\Dataset\dataset_allahabad\\', 743 )
labelling(r'C:\Users\Dhruvin\Desktop\Dataset\legal_cases_textfiles_lucknow.xlsx', r'C:\Users\Dhruvin\Desktop\Dataset\dataset_lucknow\\', 328 )

print('positive '+str(poscount))
print('negative '+str(negcount))
print("0cases: "+str(ambi))
newwb.save('LabelledDataset.xls')

