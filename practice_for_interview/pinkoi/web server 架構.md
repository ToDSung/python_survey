# web server 架構
這是我去 pinkoi 面試時面對的問題，完全把我給考倒了
問題敘述是這樣子，當一個使用者點下了 pinkoi 網站，從頭到尾的流程應該是什麼

## 閱讀導覽
白色部分是我的原話，以及聽完面試官的講解後自己打字的內容

```
這裡面是查到的內容
```

![](https://i.imgur.com/hOKnbJz.png)


我僅提出了
client 發出 request 到 server
server 根據 request 從 db 取出資料，然後發回 response

面試官從頭講解了一遍
當使用者 發出 request 後 這是一個 http request 
裡面包含了 
request 裡的網址 要轉成 ip 透過 DNS
header 是什麼可以說明清楚
body 是什麼

## http 協議
```
第一部分
request line 請求行
（例如GET /images/logo.gif HTTP/1.1，表示從/images目錄下請求logo.gif這個檔案）
第二部分
header（例如Accept-Language: en）
第三部分 空行 
第四部分 請求數據
```

每個 http request 下屬於 tcp 協定 拆成了許多 packet 

就 常見舉例而言而言 request 抵達 webserver 後 
通常交給 nginx or apache 等網頁伺服器程式，可以用來處理 load balance 等等架設多個網頁伺服器，然後傳給 uWsgi 為了溝通 django

## Nginx 
![](https://i.imgur.com/wYZDRl1.png)

### 網頁伺服器程式:
```
每一個網頁伺服器程式都需要從網路接受HTTP請求，然後提供HTTP回覆給請求者。
HTTP回覆一般包含一個HTML檔案，有時也可以包含純文字檔案、圖像或其他類型的檔案。

Nginx是一個高性能的HTTP和反向代理服務器，也是一個IMAP/POP3/SMTP代理服務器。

反向代理是代理伺服器的一種。伺服器根據用戶端的請求，從其關聯的一組或多組後端伺服器
（如Web伺服器）上取得資源，然後再將這些資源返回給用戶端，用戶端只會得知反向代理的IP位址，
而不知道在代理伺服器後面的伺服器叢集的存在。
```
### 我的理解:
前端畫面 是由第一次 Nginx 傳 靜態檔案過去完成的

### 查到的說法:
```
瀏覽器向 Nginx 發起一個請求，如果匹配到 Nginx 的靜態 URL，
比如 /static 目錄下的 js、css、404.html 等文件，那麼 Nginx 直接返回文件。
其他請求 URL，通過 uwsgi_pass 配置轉給 uWSGI 處理。
```

## uWSGI
![](https://i.imgur.com/OKzhaCB.png)

### 為什麼需要 uWSGI
![](https://i.imgur.com/XdLKWCh.png)


### uWSGI的作用:
```
一句話: uWSGI 是一個全功能的 HTTP 服務器，
他要做的就是把 HTTP 協議轉化成語言支持的網絡協議。
比如把 HTTP 協議轉化成 WSGI 協議，讓 Python 可以直接使用。

WSGI協議主要包括服務器和應用程序兩部分：

WSGI服務器負責從客戶端接收請求，請求轉發給應用程序，將應用程序返回的響應返回給客戶端;

WSGI application 接收由 server 轉發的 request，處理 request，並將處理結果返回給server. 
application 中可以包括多個 middlewares，middleware需要同時實現服務器與應用程序，
因此可以在WSGI服務器與WSGI應用之間起調節作用：
對 server 來說，middleware 扮演應用程序，
對 application 來說， middleware 扮演 server。
```
## django
![](https://i.imgur.com/LSexIGt.png)

用 django 解釋
這些process 都是 django 程式，他會根據 
route 找到對應的方法執行 
view 執行正確的 function
model 去從 db 取得資料再回傳 response 給使用者
而從 db 取資料這件事情來說 如果有很常出現的動態資料，也可以考慮使用快取
```
控制器 Controller - 負責轉發請求，對請求進行處理。
視圖 View - 介面設計人員進行圖形介面設計。
模型 Model - 程式設計師編寫程式應有的功能（實作演算法等等）、
            資料庫專家進行資料管理和資料庫設計（可以實作具體的功能）。
```
