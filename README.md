#Telegram Channel Backup

## About
This is a small program in Python3 that download channel massages and save it in your local machine. It can be used for mirroring or backup when you afraid to lose data or information.

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install telethon.

```bash
pip3 install telethon
```

Before starting, update API id & hash, in *setting/config.json* , get it from [https://my.telegram.org/](https://my.telegram.org/) -> 'API development tools'-> App api_id & App api_hash

## Usage

```
python3 main.py -i ChannelID -l LIMIT -o OVERRIDE
```
Using `-i` is short of `--id`, provide an ID of the channel, for example, https://t.me/*test* provide only *test*. By the way.. It's MUST parameter.

Using `-l` is short of `--limit`, set a limit of history, how long you want to search back, if you didn't use it, will take the whole chat (take some time..). INT ONLY

Using `-o` is short of `--override`, is *true* or *false* in lower case sensitive. True(Default) will re-create the folder, False - Will continue and fix what missing.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
Use at your own risk !
