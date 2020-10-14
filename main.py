from telethon import TelegramClient, events, sync
from conversation_backup import get_all_history
from cli_parse import get_args
from upload_manager import uploader
import os,json

# local variables
local_path = os.path.dirname(os.path.abspath(__file__))
data_path = local_path+'/data'

def get_setting():
    with open(local_path+'/setting/config.json') as setting_file:
        try:
            setting_data = json.load(setting_file)
            api_id = setting_data['api_id']
            api_hash = setting_data['api_hash']
            return api_id, api_hash

        except:
            print("Error loading ./setting/config.json")
            print("Please double check that file contain 'api_id' & 'api_hash'")
        

if __name__ == "__main__":
    api_id, api_hash = get_setting()
    conversation_id, limit, override, mirror, upload = get_args()
    conv_path = data_path +'/'+ conversation_id
    client = TelegramClient('new', api_id, api_hash)
    client.start()

    if not(os.path.isdir(data_path)):
        os.mkdir(data_path)

    get_all_history(client,conversation_id,conv_path,override,mirror)
    uploader(upload,conv_path)
    