import argparse,string,os

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i","--id", 
    help="User ID or chaneel ID, for: https://t.me/test, use only 'test'"
    )
parser.add_argument(
    "-l","--limit", 
    help="If you want to get only some of the history, how much count back ?",
    type=int)
parser.add_argument(
    "-o","--override", 
    help="If you already used the script, you can chose to override the data.\n"+
    "Default is True, use lower case", 
    choices=['true','false']
    )
parser.add_argument(
    "-m","--mirror", 
    help="Mirror to backup bot", 
    action='store_true'
    )
parser.add_argument(
    "-u","--upload", 
    help="Upload it to one of supported sites, select one. It can take a while...", 
    choices=['anonymousfiles']
    )

args = parser.parse_args()

def get_args():
    conv_id = ''
    limit = None
    override = True
    mirror = False
    upload = None

    if not(args.id):
        print("You must provide chaneel/user id !")
        exit()
    else:
        conv_id = args.id

    print("Configuration:")
    if not(args.limit):
        print("Limit: None (Take all history)")
    else:
        limit = args.limit
        print("Limit: %d"%limit)


    if not(args.override):
        print("Override: True")
    elif(args.override == 'false'):
        override = False
        print("Override: False")

    if (args.mirror):
        mirror=True
    
    if(args.upload):
        upload = args.upload

    return conv_id,limit,override,mirror,upload