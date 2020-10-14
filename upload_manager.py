from upload_mirror.anonymousfiles import uploadThisDir

def uploader(upload_func,path):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if(upload_func == 'anonymousfiles'):
        print("Starting to upload files....")
        uploadThisDir(path)
        print("Done !")