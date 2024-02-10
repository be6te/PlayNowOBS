# PlayNow-OBS 
NowPlayOBS Share and show your audience in real time what you are listening to at that moment.

#### Preview Example: 
![preview](https://i.imgur.com/5izGe4J.gif)


## Installation
- Install Python 3.10+ [(Download)](https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe)
#### Install Requirements:

```text
$ pip install -r requirements.txt
```
#### Run CMD / Powershell:
```text
$ py main.py
```
## How to use

 Log in to `https://developer.spotify.com/dashboard` and create an application once inside you fill in everything but `important in the Redirect URI section enter the following address http://localhost:7777/callback` and `activate the WEB API option` once created enter your app you created and go to the `Settings` option once in `Settings copy the CLIENT ID and SECRET ID`

![oauth](https://i.imgur.com/UaM0E3v.png)

Once you have those two in the `NowPlayOBS folder` you will have a file called `Credentials.json` and it will ask you to `enter the CLIENT_ID and SECRET_ID` and it should look like this

![set](https://i.imgur.com/QcULDdp.png)

With that done, you can go ahead and run the script using `py main.py` or `python3 main.py`
In CMD or powershell console

#### Localhost / Port

```txt
http://localhost:7777/
```
#### The server is started on a local host on port `7777` and must be started here `http://localhost:7777/` to authenticate with [OAuth](https://developer.spotify.com/documentation/web-api/concepts/authorization) and make use of NowPlayOBS.
#### OBS / Streamlabs

```txt
http://localhost:7777/playing
```

#### If everything works you will see the song you are listening to on spotify and to display it on OBS or Streamlabs is as simple as copying the URL and pasting it as follows
#### Preview (Browser):
![page](https://i.imgur.com/J1TGBdF.png)

#### Create a new font and add it as browser

![obs](https://i.imgur.com/g6b83Rv.png)

#### If you did the rest, it should look like this

![obss](https://i.imgur.com/eZocc46.png)

 `The preview does not appear when you enter the URL`, it will be `ready when you click OK and it will be displayed normally`

## Read
#### If you find bugs open [Issue](https://github.com/beeteo/PlayNowOBS/issues) and tell me about your bug so I can fix it further in the future. 
#### This is being worked on by a single person and will soon be available for more platforms.

#### If you encounter lag when displaying the song or pausing it is normal for now, but I will fix it soon.

### This is intended for use on `Windows only`, not on other operating systems.
