import os,shutil

def get_all_history(client,conv_id,data_path,override=False,mirror=False):
    conv_path = data_path+'/'+conv_id
    err_list = []
    exists_ids = []


    #Each covertsation need to manage her own data in folder
    if not(os.path.isdir(conv_path)):
        os.mkdir(conv_path)
    else:
        if(override):
            override_count = 0
        else:
            exists_ids = get_exists_id_list(conv_path)

    #None limit since we want all the history
    messages = client.get_messages(conv_id,None)

    #User console
    print("---------------------------------")
    print("Start to get history of "+conv_id)
    print("Starting download messages")

    for idx,message in enumerate(messages):
        print(" Downloading "+str(idx+1)+" from "+ str(len(messages)), end='\r')

        #Skip when massage already exists
        if (override is False) and (message.id in exists_ids):
            continue

        #Each message contain it's own data, seperate folder
        message_path = conv_path+'/'+str(message.id)+'/'

        #If path exists an need to override - re create
        if(os.path.isdir(message_path) & override):
            shutil.rmtree(message_path)
            override_count += 1
        elif(os.path.isdir(message_path)):
            continue

        os.mkdir(message_path)
        
        #Save text from the message
        if(message.message):
            with open(message_path+'/text.txt','w') as textfile:
                try:
                    textfile.write(message.message)
                except:
                    textfile.close()
                    err_list.append(err_detail(
                        "Error saving text from the massage",
                        message.id,
                        message.date
                    ))
        # Save media attached
        if(message.media) is not None:
            try:
                message.download_media(file=message_path)
            except:
                err_list.append(err_detail(
                "Error saving text from the massage",
                message.id,
                message.d
                ))
            
        
        if(mirror):
            try:
                message.forward_to('BackupMyDataBot')
            except:
                continue
        
        clear_empty(message_path)

    #User summary
    print('\n')
    print("---------------------------------")

    if(len(err_list)>0):
        print("We found %d errors while saving" % len(err_list))
        for err in err_list:
            print(err)
        
    if(override):
        print("%d messages override" % override_count)     

    print("Downloaded data can be found at: '"+conv_path+"'")
    print("Complete!")

#----------------- Sub functions -----------------#
def get_exists_id_list(conv_path):
    dir_list = os.listdir(conv_path)
    if(len(dir_list)<1):
        clear_empty(conv_path)
    else:
        return dir_list

def clear_empty(path_to_check):
    if len(os.listdir(path_to_check) ) == 0:
        os.rmdir(path_to_check)

class err_detail: 
    def __init__(self, details, message_id,message_time):  
        self.details = details  
        self.message_id = message_id
        self.message_time = message_time 
    
    def __str__(self):
        return self.details + " in massage "+ str(self.message_id) +", time: "+ str(self.message_time)
