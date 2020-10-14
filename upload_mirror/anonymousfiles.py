import requests,json,os
from datetime import datetime

## This driver is only for: anonymousfiles.io
server = 'https://api.anonymousfiles.io/'

def uploadThisDir(usePath):
    #Check we got the right dir
    if not os.path.isdir(usePath):
        print("error upload, dir %s didnt found"%usePath)
        return

    #Open father's text output
    with open(usePath+'/anonymousfiles.txt','a+') as main_output:
        main_output.write("Start in: "+str(datetime.now())+"\n") #Understand what in text file
        count_files = len(os.listdir(usePath)) #We use that only for printing status

        #Run over the subdir (messages) of the chat
        for idx,(subdir, _, files) in enumerate(os.walk(usePath)):
            print(" Uploading "+str(idx+1)+" from "+ str(count_files), end='\r')
            if 'anonymousfiles.txt' in files: files.remove('anonymousfiles.txt') #Ignore the log file
            if(len(files)>0): #ONLY IF THERE IS FILES TO UPLOAD
                with open(subdir+'/anonymousfiles.txt','w+') as sub_output: #Build log for each message
                    main_output.write(subdir+'\n') #Add title to father

                    for file in files:
                        with open(subdir+'/'+file,'rb') as file_to_upload:
                            result = requests.post(server,files={'file':file_to_upload})
                            result_url = result.json()['url']
                            sub_output.write(file+': '+result_url+'\n')
                            main_output.write(result_url+'\n')

        main_output.close()
        print("All the files uploaded to: %s \n" % server)
        print("You can watch the link in every dir, or the main log file in: %s"% usePath)                            
 
            