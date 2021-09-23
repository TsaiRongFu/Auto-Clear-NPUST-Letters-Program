# NPUST信箱自動清除器 

先決條件：
*   Windows&nbsp;&nbsp;x64&nbsp;&nbsp;(64位元系統)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;目前尚未開發32位元應用
*   Chrome網頁瀏覽器&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;目前尚未開發Firefox、Edge、Opera、IE、PhantomJS版本
*   ChromeDriver&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;專案Releases已經附上各版本

 
## 確認Chrome瀏覽器版本是否符合ChromeDriver

*   查看Chrome版本

    ![image](https://github.com/TsaiRongFu/Auto-Clear-NPUST-Letters-Program/blob/main/README_Picture/ChromeVersion.gif)
*   至Releases(發行版本)找到與您Chrome相符的版本下載                  

    * Auto-Clean-NPUST-Mail-Program.exe
    * chromedriver.exe
    
    或

    * 直接下載Auto-Clean-NPUST-Mail-Program.zip
解壓縮就有了

*   如果Releases(發行版本)中沒有符合您Chrome版本的ChromeDrive，請至下方連結下載符合您版本的ChromeDrive

    * https://chromedriver.chromium.org/

        舊版網站畫面![image](https://github.com/TsaiRongFu/Auto-Clear-NPUST-Letters-Program/blob/main/README_Picture/ChromeDriveWeb.png)

        
        新版網站畫面
        ![image](https://github.com/TsaiRongFu/Auto-Clear-NPUST-Letters-Program/blob/main/README_Picture/ChromeDriveWebNewPage.png)
## 操作範例(以發行版本中的v1.2為例)

<br>
下載zip後解壓縮結構如下：

```
Auto-Clean-NPUST-Mail-Program Folder
└────Auto-Clean-NPUST-Mail-Program.exe
└────chromedriver.exe
```
| 直接點擊運行Auto-Clean-NPUST-Mail-Program.exe即可 |

*   ### **登入分為兩種**
    * ### **第一種為手動登入**

        ![image](https://github.com/TsaiRongFu/Auto-Clear-NPUST-Letters-Program/blob/main/README_Picture/login.gif)

    * ### **第二種為自動登入**

        ![image](https://github.com/TsaiRongFu/Auto-Clear-NPUST-Letters-Program/blob/main/README_Picture/autoLogin.gif)

*   ### **基本功能-刪除所有信件**

    ![image](https://github.com/TsaiRongFu/Auto-Clear-NPUST-Letters-Program/blob/main/README_Picture/Delete.gif)

*   ### **基本功能-清空回收筒**

    ![image](https://github.com/TsaiRongFu/Auto-Clear-NPUST-Letters-Program/blob/main/README_Picture/Clean.gif)

*   ### **基本功能-重置網頁及按鈕**

    ![image](https://github.com/TsaiRongFu/Auto-Clear-NPUST-Letters-Program/blob/main/README_Picture/Reset.gif)

<br>

### 目前檔案會google會偵測不安全所屬正常現象！因為我沒有code signing
### 至於要不要使用就所屬個人了，這個專案就是無聊做著玩的性質！

---

### 有任何程式的問題或<label style = "color:red;">Bug</label>歡迎提出Issues！

![TsaiRongFu/Auto-Clear-NPUST-Letters-Program Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FTsaiRongFu%2FAuto-Clear-NPUST-Letters-Program&count_bg=%23F51DD0&title_bg=%234B4B4B&icon=linux.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)