---
title: "Google Drive 命令行上传/下载文件"
date: 2023-05-14T10:37:48+08:00
draft: False
categories:
    - 教程
tags:
    - linux
    - docker
    - tar
    - 传输文件
enableTocContent: true
---

> 需求：内网服务器没有图形界面时，Google Drive作为中转站传输数据使用，使用scp等工具特别慢

## 上传文件

### Google OAuth 客户端凭据 (Client Credentials)

> Thanks gdrive !
> https://github.com/glotlabs/gdrive/blob/main/docs/create_google_api_credentials.md

Create Google API credentials in **50 easy steps**

Google has made it really easy to create api credentials for own use, just follow these few steps:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)

2. Create a new project (or select an existing) from the menu 
   
   ![screenshot](https://user-images.githubusercontent.com/720405/210136984-7ed0eb00-f940-47c2-a1b7-95147e0f6ed8.png)

3. Search for `drive api` in the search bar and select `Google drive api` under the marketplace section ![screenshot](https://user-images.githubusercontent.com/720405/210137041-57633760-eb57-4c87-bacf-a9850c363a63.png)

4. Click to enable `Google Drive API` button ![screenshot](https://user-images.githubusercontent.com/720405/210137243-3f7c1ea6-519b-4c50-afea-577e19fe543d.png)

5. Click on the `Credentials` menu item

6. Click on the `Configure Consent Screen` button ![screenshot](https://user-images.githubusercontent.com/720405/210137298-9c9eb3d1-9420-4bdb-bd98-4e6e778c8ed5.png)

7. Select `External` user type (Internal is only available for workspace subscribers) ![screenshot](https://user-images.githubusercontent.com/720405/210137317-de4b8bea-235d-498d-b78d-b0c37dd96717.png)

8. Click on the `Create` button

9.  Fill out the fields `App name`, `User support email`, `Developer contact information` with your information; you will need to put the Project ID into the app name (keep the other fields empty) ![screenshot](https://user-images.githubusercontent.com/720405/210137365-09aa2294-8984-45ef-9a29-7f485cfbe7ac.png)

10. Click the `Save and continue` button. If you get `An error saving your app has occurred` try changing the project name to something unique

11. Click the `Add or remove scopes` button

12. Search for `google drive api`

13. Select the scopes `.../auth/drive` and `.../auth/drive.metadata.readonly` ![screenshot](https://user-images.githubusercontent.com/720405/210137392-f851aa1e-ea59-4c19-885e-d246992c4dd7.png)

14. Click the `Update` button

15. Click the `Save and continue` button ![screenshot](https://user-images.githubusercontent.com/720405/210137425-44cab632-c885-495d-bb10-3b6e842ed79a.png)

16. Click the `Add users` button

17. Add the email of the user you will use with gdrive ![screenshot](https://user-images.githubusercontent.com/720405/210137458-ec6a6fb3-ea0c-47e8-a8ec-fe230841ba3b.png)

18. Click the `Add` button until the sidebar disappears

19. Click the `Save and continue` button ![screenshot](https://user-images.githubusercontent.com/720405/210137468-9c1fc03e-cb18-4798-a17c-1a6c912f07a8.png)

20. Click on the `Credentials` menu item again

21. Click on the `Create credentials` button in the top bar and select `OAuth client ID` ![screenshot](https://user-images.githubusercontent.com/720405/210137498-dc9102c4-2720-466d-809a-4d8947dbb0a0.png)

22. Select application type `Desktop app` and give a name ![screenshot](https://user-images.githubusercontent.com/720405/210137673-d3a387ab-3bbe-4af3-81c8-7c744aed8bd5.png)

23. Click on the `Create` button

24. You should be presented with a Cliend Id and Client Secret ![screenshot](https://user-images.githubusercontent.com/720405/210137709-587edb53-4703-4ad3-8941-6130f47d0547.png)

25. Click on `OAuth consent screen`

26. Click on `Publish app` (to prevent the token from expiring after 7 days) ![screenshot](https://user-images.githubusercontent.com/720405/216276113-18356d78-c81c-42c1-be2b-49c9b6a6cafe.png)

27. Click `Confirm` in the dialog

Thats it!

Gdrive will ask for your Client Id and Client Secret when using the `gdrive account add` command.

### 使用curl上传文件

> https://towardsdatascience.com/uploading-files-to-google-drive-directly-from-the-terminal-using-curl-2b89db28bb06

1. 之前创建的OAuth是桌面应用，这里需要更改成TV和其他限制输入设备

2. 验证设备

    ```bash
    curl -d "client_id=<client_id>&scope=https://www.googleapis.com/auth/drive.file" https://oauth2.googleapis.com/device/code
    ```

    得到如下的回复：

    ```json
    {
        "device_code": "<long string>",
        "user_code": "xxx-xxx-xxx",
        "expires_in": 1800,
        "interval": 5,
        "verification_url": "https://www.google.com/device"
    }
    ```

    这里我们需要访问网址（https://www.google.com/device）并提供用户代码来完成我们的验证。我们现在继续选择我们的谷歌账户并授予相关权限。执行此操作时，请务必记下下一步的设备代码。

3. 得到Bearer code

    当我们开始上传时，这是我们需要用来识别我们帐户的代码。我们通过使用以下方法获得它：

    ```bash
    curl -d client_id=<client id> -d client_secret=<client secret> -d device_code=<device code> -d grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Adevice_code https://accounts.google.com/o/oauth2/token
    ```

    client id 和 secret 是从第一步保存的，以及上一节中的设备代码。输出应采用以下格式：

    ```json
    {
        "access_token": ".....",
        "expires_in": 3599,
        "refresh_token": "....",
        "scope": "https://www.googleapis.com/auth/drive.file",
        "token_type": "Bearer"
    }
    ```

    记下上传阶段需要的 access_token

4. 上传文件

    ```bash
    curl -X POST -L \
    -H "Authorization: Bearer <enter access token here>" \
    -F "metadata={name :'<our.zip>'};type=application/json;charset=UTF-8" \
    -F "file=@<our.zip>;type=application/zip" \
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
    ```

### 使用Python

现在我们知道我们的命令有效，我们可以创建一个可执行脚本来为我们完成所有工作。在这里我们可以提供一组文件，它将它们压缩，然后将它们发送到谷歌驱动器。 

我们首先使用 nano curlgoogle 创建一个新文件；并输入以下代码——记得添加您自己的个人身份验证令牌！已选择 Python 2.7，因为这仍然是旧系统上的默认 python 版本，但是下面的脚本也应该适用于 python 3。 如果系统上已经存在 curl，它应该不需要新的依赖项。

```python
#!/usr/bin/python
'''
A quick python script to automate curl->googledrive interfacing
This should require nothing more than the system python version and curl. Written for python2.7 (with 3 in mind).
Dan Ellis 2020
'''
import os,sys,json
if sys.version[0]=='3':
  raw_input = lambda x: input(x)
##############################
#Owner information goes here!#
##############################

client_id= sys.argv[1]     # '<enter your client id>'
client_secret=sys.argv[2]  # '<enter your client secret>'
##############################

cmd1 = json.loads(os.popen('curl -d "client_id=%s&scope=https://www.googleapis.com/auth/drive.file" https://oauth2.googleapis.com/device/code'%client_id).read())
str(raw_input('\n Enter %(user_code)s\n\n at %(verification_url)s \n\n Then hit Enter to continue.'%cmd1))
str(raw_input('(twice)'))
cmd2 = json.loads(os.popen(('curl -d client_id=%s -d client_secret=%s -d device_code=%s -d grant_type=urn~~3Aietf~~3Aparams~~3Aoauth~~3Agrant-type~~3Adevice_code https://accounts.google.com/o/oauth2/token'%(client_id,client_secret,cmd1['device_code'])).replace('~~','%')).read())
print(cmd2)

for name in sys.argv[3:]:
    # zip files
    cmd4 = os.popen('''
    curl -X POST -L \
        -H "Authorization: Bearer %s" \
        -F "metadata={name :\'%s\'};type=application/json;charset=UTF-8" \
        -F "file=@%s;type=application/zip" \
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
        '''%(cmd2["access_token"],name,name)).read()
    print(cmd4)
    print('end')
```

```bash
./curlgoogle =client-id client-secret file1 file2.txt file3.jpg etc... 
```


## 下载文件

在 Google Drive 将文件设置为共享，得到如下链接

https://drive.google.com/file/d/1Cy_MpY452A------------xkIRWJhPwz/view?usp=sharing

需要设置下面的文件id和下载的文件名：

```
import gdown

url = 'https://drive.google.com/uc?id=1Cy_MpY452A------------xkIRWJhPwz'
output = <name>
gdown.download(url, output, quiet=False)
```