
<h1 align="center">GetDanmuSender</h1>
<div align="center">

<p align="center">
    <h3>一个基于Python3.7开发的bilibili弹幕发送者查询工具</h3>
    <p align="center">
      <a href="https://t.me/tkdifferent">
        <a href="http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=SQ2EDC77_dObl8QOdmwMVxw39H8Ur1Ax&authKey=OD1jf7NyaNkZu0HpXuhjnFPTA9hWdxcmiU72rteVclsIWSziS1bjThC8OJaK36sV&noverify=0&group_code=893018099">
<img alt="加入QQ交流群" src="https://img.shields.io/badge/QQGroup-893018099-blue" />
</a>
      <p>
查询范围<br />
普通视频 / 分P视频 / 番剧...<br />
<br />
    </p>
    <p align="center">
      <img alt="GIF" src="https://i.postimg.cc/SRzfqCxh/show.gif" />
    </p>
  </p>
</div>



# 快速上手🔨
### 源码部署 
若您的计算机中安装了git，可通过以下命令部署
```cmd
git clone https://github.com/cwuom/GetDanmuSender.git
cd GetDanmuSender
pip install -r requirements.txt
python main.py
```
若您的计算机无法使用git，您可以[直接下载](https://github.com/cwuom/GetDanmuSender/archive/refs/heads/main.zip)源码来部署它

### 直接部署（无需环境）
前往[releases](https://github.com/cwuom/GetDanmuSender/releases)下载最新的打包版本。

# 使用方式🪄

## 您提供的
 1. 你的B站cookies [(如何获取?)](https://cn.bing.com/search?q=%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96b%E7%AB%99cookies&qs=n&form=QBRE&sp=-1&lq=0&pq=%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96b%E7%AB%99cookies)
2. 视频、分P视频/番剧链接
3. 若为分p视频则需要在回车后输入想要查询的page。程序会自动识别视频类型
4. 需要查询的弹幕内容


#### 视频、分P视频/番剧链接输入示例
```
视频链接: https://www.bilibili.com/video/BV1ED4y1Y7dc/?spm_id_from=333.999.0.0
分P视频链接: https://www.bilibili.com/video/BV17F411T7Ao/?spm_id_from=333.337.search-card.all.click
番剧链接(三体第一集): https://www.bilibili.com/bangumi/play/ep704473?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0

总结：想解析什么直接把头顶上的URL复制以后粘贴到程序里就行了
```

## 程序返回给您的 
### 控制台输出

#### 基本信息
```
[CID] 917705395
[标题] 【4月】间谍过家家 03
[弹幕库(?)] 144838
[描述] 正片

[视频时长] 1451s
[发布时间] 2022-05-14
```
当您输入视频链接后程序会自动解析，解析成功后会返回给您视频的基本数据来供您确认。

#### 检索结果
  

a. 关键字检索

1.  单个检索结果
> input: https://www.bilibili.com/bangumi/play/ep508406?from_spmid=666.25.episode.0&spm_id_from=333.337.0.0 
```
全部弹幕信息已构造完成，请输入关键字(你想要搜索的弹幕内容)来检索弹幕。 若要搜索全部弹幕，请先回车后再输入all来搜索
搜索弹幕> 别再回忆了，好水
检索到弹幕 -> 别再回忆了，好水 ...
按下回车进行midHash逆向操作(UID反推)。这可能需要一点时间.. 'n'取消
cracking -> 40357a2c

==========================
弹幕内容: 别再回忆了，好水
发送时间: 2022-11-25 17:35:33
字体大小: 18
弹幕类型: 普通弹幕
发送者UID: 503147312
发送者主页连接: https://space.bilibili.com/503147312
==========================
所有UID反推成功，耗时1.03秒
```
2. 多个检索结果
> input: https://www.bilibili.com/bangumi/play/ep508404?from_spmid=666.25.episode.0&spm_id_from=333.337.0.0

<details>  
<summary>output:</summary>

```
全部弹幕信息已构造完成，请输入关键字(你想要搜索的弹幕内容)来检索弹幕。 若要搜索全部弹幕，请先回车后再输入all来搜索
搜索弹幕> 66
检索到弹幕 -> 666国家孕动员 ...
检索到弹幕 -> 我直呼666 ...
检索到弹幕 -> [】666 ...
检索到弹幕 -> 一秒变声666！ ...
检索到弹幕 -> 精神医生666太可了 ...
检索到弹幕 -> 读心术啊我的宝子666 ...
检索到弹幕 -> 666有点像我啊 ...
检索到弹幕 -> 树枝666 ...
检索到弹幕 -> 树枝666 ...
检索到弹幕 -> 666 自己暴露 ...
检索到弹幕 -> 366+ ...
检索到弹幕 -> 666好厉害！ ...
检索到弹幕 -> 666，身上有多少颗痘都知道 ...
检索到弹幕 -> 香翅捞饭食不食一阿尼亚树枝666 ...
检索到弹幕 -> 666哇 ...
检索到弹幕 -> 鸡？阿尼亚树枝666 ...
检索到弹幕 -> 找个杀过666个人的单身女士 ...
检索到弹幕 -> 你没逝吧你没逝吧 吃点66梅 ...
检索到弹幕 -> ji?什么意思一可爱女娃树脂666 ...
检索到弹幕 -> 6666扬雾运动 ...
按下回车进行midHash逆向操作(UID反推)。这可能需要一点时间.. 'n'取消
cracking -> 9ec53f79
cracking -> 6d92fb62
cracking -> ac90fae2
cracking -> 12bb5acb
cracking -> 2f35b4bf
cracking -> df8646b3
cracking -> 41b73f9f
cracking -> e7be572a
cracking -> b8aaa332
cracking -> 692eaaf3
cracking -> a3c2c61e
cracking -> 3b21b818
cracking -> 8d8fc457
cracking -> c774eb4a
cracking -> 87813946
cracking -> 23baa12e
cracking -> fae5fa89
cracking -> 6497db1c
cracking -> f927b6a0
cracking -> 489157d9

==========================
弹幕内容: 读心术啊我的宝子666
发送时间: 2022-07-24 17:40:33
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 288670918
发送者主页连接: https://space.bilibili.com/288670918
==========================

==========================
弹幕内容: 366+
发送时间: 2022-05-09 20:06:45
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 157243520
发送者主页连接: https://space.bilibili.com/157243520
==========================

==========================
弹幕内容: 香翅捞饭食不食一阿尼亚树枝666
发送时间: 2022-06-26 07:21:08
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 84167133
发送者主页连接: https://space.bilibili.com/84167133
==========================

==========================
弹幕内容: 666 自己暴露
发送时间: 2022-05-03 01:26:39
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 29257067
发送者主页连接: https://space.bilibili.com/29257067
==========================

==========================
弹幕内容: 精神医生666太可了
发送时间: 2022-07-31 17:16:36
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 447472526
发送者主页连接: https://space.bilibili.com/447472526
==========================

==========================
弹幕内容: 一秒变声666！
发送时间: 2022-05-04 01:10:45
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 518925195
发送者主页连接: https://space.bilibili.com/518925195
==========================

==========================
弹幕内容: 666哇
发送时间: 2022-06-19 10:49:37
字体大小: 18
弹幕类型: 顶部弹幕
发送者UID: 126088187
发送者主页连接: https://space.bilibili.com/126088187
==========================

==========================
弹幕内容: 找个杀过666个人的单身女士
发送时间: 2022-05-06 01:00:52
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 250620582
发送者主页连接: https://space.bilibili.com/250620582
==========================

==========================
弹幕内容: [】666
发送时间: 2022-06-26 22:36:22
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 648890053
发送者主页连接: https://space.bilibili.com/648890053
==========================

==========================
弹幕内容: 666好厉害！
发送时间: 2022-09-22 19:43:18
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 519153783
发送者主页连接: https://space.bilibili.com/519153783
==========================

==========================
弹幕内容: ji?什么意思一可爱女娃树脂666
发送时间: 2022-05-15 17:08:15
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 383422259
发送者主页连接: https://space.bilibili.com/383422259
==========================

==========================
弹幕内容: 666，身上有多少颗痘都知道
发送时间: 2022-07-07 11:45:19
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 618368642
发送者主页连接: https://space.bilibili.com/618368642
==========================

==========================
弹幕内容: 6666扬雾运动
发送时间: 2023-02-19 12:50:52
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 582621618
发送者主页连接: https://space.bilibili.com/582621618
==========================

==========================
弹幕内容: 鸡？阿尼亚树枝666
发送时间: 2022-06-09 22:08:17
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 399698342
发送者主页连接: https://space.bilibili.com/399698342
==========================

==========================
弹幕内容: 树枝666
发送时间: 2022-07-11 08:36:54
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 737896911
发送者主页连接: https://space.bilibili.com/737896911
==========================

==========================
弹幕内容: 我直呼666
发送时间: 2022-07-02 20:40:27
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 1541956582
发送者主页连接: https://space.bilibili.com/1541956582
==========================

==========================
弹幕内容: 666有点像我啊
发送时间: 2022-07-14 14:33:18
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 1403556754
发送者主页连接: https://space.bilibili.com/1403556754
==========================

==========================
弹幕内容: 树枝666
发送时间: 2022-06-06 20:48:33
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 1470353839
发送者主页连接: https://space.bilibili.com/1470353839
==========================

==========================
弹幕内容: 你没逝吧你没逝吧 吃点66梅
发送时间: 2022-05-02 11:55:45
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 2004989581
发送者主页连接: https://space.bilibili.com/2004989581
==========================

==========================
弹幕内容: 666国家孕动员
发送时间: 2022-07-05 17:13:40
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 1837817767
发送者主页连接: https://space.bilibili.com/1837817767
==========================
所有UID反推成功，耗时30.35秒
```


</details>

----

b. 全部检索
> input: https://www.bilibili.com/video/BV1dR4y117QN/?spm_id_from=333.999.0.0

<details>  
<summary>output:</summary>

```
全部弹幕信息已构造完成，请输入关键字(你想要搜索的弹幕内容)来检索弹幕。 若要搜索全部弹幕，请先回车后再输入all来搜索
搜索弹幕>
你没有输入任何关键词，请输入关键词后检索！
若需要检索全部弹幕，请输入'all'
all
检索到弹幕 -> 线插紧 ...
检索到弹幕 -> 笑死了 ...
检索到弹幕 -> 有没有可能接口没插好 ...
检索到弹幕 -> 大聪明，截图给别人看屏幕 ...
检索到弹幕 -> 《你截图我怎么看》 ...
检索到弹幕 -> 省流：评论置顶 ...
检索到弹幕 -> TN屏吧？卓威也是这样 ...
检索到弹幕 -> tn屏是这样的 ...
检索到弹幕 -> 小米，合理 ...
检索到弹幕 -> 尬黑 ...
检索到弹幕 -> 是正品 ...
检索到弹幕 -> 跟学校机房的差不多 ...
检索到弹幕 -> 米狗，这也是尬黑？？？ ...
检索到弹幕 -> 这是线问题吧。 ...
检索到弹幕 -> 1080p就这样 ...
检索到弹幕 -> 不爱小米不爱国 ...
检索到弹幕 -> 冬天 ...
检索到弹幕 -> 看不清，不予评价 ...
检索到弹幕 -> 看不清 ...
检索到弹幕 -> 看不清 ...
检索到弹幕 -> 这能看的？不要付费？ ...
检索到弹幕 -> 为了黑而黑 ...
检索到弹幕 -> 省流:看评论区 ...
检索到弹幕 -> 小呆唯不是很友善啊 ...
检索到弹幕 -> 起码他会截图 ...
检索到弹幕 -> 啥软 ...
检索到弹幕 -> 粗粮 凑合吃吧 ...
检索到弹幕 -> 要么是分辨率太低。要么是显卡没设置好 ...
检索到弹幕 -> Windows的问题 ...
检索到弹幕 -> 肯定是OPPO派来的黑子 ...
检索到弹幕 -> Win11显示有问题 ...
检索到弹幕 -> 有妖气 ...
检索到弹幕 -> 1080p ...
检索到弹幕 -> 你非要买小米的垃圾，那能怎么办。以后长记性， 他们家没什么好玩意。早买早退坑。 ...
检索到弹幕 -> 拍的什么玩意，生怕我们看懂 ...
检索到弹幕 -> 呆唯攻击性满昏 ...
检索到弹幕 -> 省流：小米真好用，小米是我爹 ...
检索到弹幕 -> 呆唯 ...
检索到弹幕 -> 是不是720分辨率的 ...
检索到弹幕 -> 你就1 ...
检索到弹幕 -> 写轮眼 ...
检索到弹幕 -> 我现在听都听不清了 ...
按下回车进行midHash逆向操作(UID反推)。这可能需要一点时间.. 'n'取消
cracking -> be11b671
cracking -> 5752f9a2
cracking -> c9c88631
cracking -> f3f34316
cracking -> 43170c75
cracking -> 13b70c3
cracking -> 41b45af7
cracking -> 9bb71977
cracking -> 8d033d39
cracking -> e5215bea
cracking -> da79cca1
cracking -> bb84a88e
cracking -> 9db58c87
cracking -> d596a4ba
cracking -> fbe690ad
cracking -> 7000fea0
cracking -> 64c6773a
cracking -> 8e1ce468
cracking -> 33c99ccc
cracking -> 33c99ccc
cracking -> 5d8a17c0
cracking -> 72bbbec7
cracking -> 3364964
cracking -> 2c31b493
cracking -> bc1573e
cracking -> 433faf84
cracking -> c507b069
cracking -> 231876
cracking -> 1a169259
cracking -> c037c943
cracking -> 4a28ffe7
cracking -> a79ac605
cracking -> c350d91
cracking -> c43f9d2f
cracking -> c734b966
cracking -> 10d610c9
cracking -> 9895cc74
cracking -> 9895cc74
cracking -> a25936ec
cracking -> b17e0809
cracking -> 794a2f82
cracking -> 6b8046d1

==========================
弹幕内容: 线插紧
发送时间: 2023-01-11 20:26:10
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 11047709
发送者主页连接: https://space.bilibili.com/11047709
==========================

==========================
弹幕内容: 大聪明，截图给别人看屏幕
发送时间: 2023-01-13 14:23:56
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 17312669
发送者主页连接: https://space.bilibili.com/17312669
==========================

==========================
弹幕内容: 有没有可能接口没插好
发送时间: 2023-01-12 11:54:43
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 69580924
发送者主页连接: https://space.bilibili.com/69580924
==========================

==========================
弹幕内容: TN屏吧？卓威也是这样
发送时间: 2023-01-14 18:30:15
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 8156402
发送者主页连接: https://space.bilibili.com/8156402
==========================

==========================
弹幕内容: 是正品
发送时间: 2023-01-16 13:18:27
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 813738
发送者主页连接: https://space.bilibili.com/813738
==========================

==========================
弹幕内容: 1080p就这样
发送时间: 2023-01-17 16:37:40
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 40307795
发送者主页连接: https://space.bilibili.com/40307795
==========================

==========================
弹幕内容: tn屏是这样的
发送时间: 2023-01-15 02:27:51
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 221789548
发送者主页连接: https://space.bilibili.com/221789548
==========================

==========================
弹幕内容: 笑死了
发送时间: 2023-01-11 20:55:14
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 363914344
发送者主页连接: https://space.bilibili.com/363914344
==========================

==========================
弹幕内容: 尬黑
发送时间: 2023-01-16 08:05:59
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 282813465
发送者主页连接: https://space.bilibili.com/282813465
==========================

==========================
弹幕内容: 小米，合理
发送时间: 2023-01-16 00:57:29
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 316353938
发送者主页连接: https://space.bilibili.com/316353938
==========================

==========================
弹幕内容: 啥软
发送时间: 2023-01-20 09:50:29
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 8079393
发送者主页连接: https://space.bilibili.com/8079393
==========================

==========================
弹幕内容: 粗粮 凑合吃吧
发送时间: 2023-01-22 10:37:00
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 14517274
发送者主页连接: https://space.bilibili.com/14517274
==========================

==========================
弹幕内容: Windows的问题
发送时间: 2023-01-22 20:36:37
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 2298840
发送者主页连接: https://space.bilibili.com/2298840
==========================

==========================
弹幕内容: 肯定是OPPO派来的黑子
发送时间: 2023-01-23 09:27:34
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 3880807
发送者主页连接: https://space.bilibili.com/3880807
==========================

==========================
弹幕内容: 《你截图我怎么看》
发送时间: 2023-01-13 16:25:01
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 436638784
发送者主页连接: https://space.bilibili.com/436638784
==========================

==========================
弹幕内容: 这能看的？不要付费？
发送时间: 2023-01-17 23:38:44
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 234931266
发送者主页连接: https://space.bilibili.com/234931266
==========================

==========================
弹幕内容: 看不清
发送时间: 2023-01-17 22:33:09
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 410478782
发送者主页连接: https://space.bilibili.com/410478782
==========================

==========================
弹幕内容: 省流：评论置顶
发送时间: 2023-01-13 19:34:07
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 330120048
发送者主页连接: https://space.bilibili.com/330120048
==========================

==========================
弹幕内容: 你非要买小米的垃圾，那能怎么办。以后长记性， 他们家没什么好玩意。早买早退坑。
发送时间: 2023-01-24 05:09:47
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 13251233
发送者主页连接: https://space.bilibili.com/13251233
==========================

==========================
弹幕内容: 看不清，不予评价
发送时间: 2023-01-17 20:29:46
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 503884832
发送者主页连接: https://space.bilibili.com/503884832
==========================

==========================
弹幕内容: 你就1
发送时间: 2023-02-07 18:37:02
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 65405244
发送者主页连接: https://space.bilibili.com/65405244
==========================

==========================
弹幕内容: 写轮眼
发送时间: 2023-02-07 18:37:13
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 65405244
发送者主页连接: https://space.bilibili.com/65405244
==========================

==========================
弹幕内容: 为了黑而黑
发送时间: 2023-01-17 23:52:07
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 297991801
发送者主页连接: https://space.bilibili.com/297991801
==========================

==========================
弹幕内容: 1080p
发送时间: 2023-01-23 18:14:36
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 9332775
发送者主页连接: https://space.bilibili.com/9332775
==========================

==========================
弹幕内容: 不爱小米不爱国
发送时间: 2023-01-17 17:11:58
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 439310802
发送者主页连接: https://space.bilibili.com/439310802
==========================

==========================
弹幕内容: 起码他会截图
发送时间: 2023-01-19 02:52:46
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 202299927
发送者主页连接: https://space.bilibili.com/202299927
==========================

==========================
弹幕内容: 我现在听都听不清了
发送时间: 2023-03-24 11:08:37
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 13221994
发送者主页连接: https://space.bilibili.com/13221994
==========================

==========================
弹幕内容: 看不清
发送时间: 2023-01-17 22:33:16
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 410478782
发送者主页连接: https://space.bilibili.com/410478782
==========================

==========================
弹幕内容: 米狗，这也是尬黑？？？
发送时间: 2023-01-16 14:13:58
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 535816556
发送者主页连接: https://space.bilibili.com/535816556
==========================

==========================
弹幕内容: 省流:看评论区
发送时间: 2023-01-18 02:51:56
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 302561191
发送者主页连接: https://space.bilibili.com/302561191
==========================

==========================
弹幕内容: 要么是分辨率太低。要么是显卡没设置好
发送时间: 2023-01-22 16:31:37
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 338857393
发送者主页连接: https://space.bilibili.com/338857393
==========================

==========================
弹幕内容: Win11显示有问题
发送时间: 2023-01-23 11:08:25
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 290260403
发送者主页连接: https://space.bilibili.com/290260403
==========================

==========================
弹幕内容: 拍的什么玩意，生怕我们看懂
发送时间: 2023-01-28 12:55:18
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 403033778
发送者主页连接: https://space.bilibili.com/403033778
==========================

==========================
弹幕内容: 小呆唯不是很友善啊
发送时间: 2023-01-18 10:46:40
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 628718076
发送者主页连接: https://space.bilibili.com/628718076
==========================

==========================
弹幕内容: 呆唯攻击性满昏
发送时间: 2023-01-29 09:52:55
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 454069305
发送者主页连接: https://space.bilibili.com/454069305
==========================

==========================
弹幕内容: 有妖气
发送时间: 2023-01-23 16:54:31
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 490744102
发送者主页连接: https://space.bilibili.com/490744102
==========================

==========================
弹幕内容: 跟学校机房的差不多
发送时间: 2023-01-16 13:34:59
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 916430804
发送者主页连接: https://space.bilibili.com/916430804
==========================

==========================
弹幕内容: 呆唯
发送时间: 2023-01-29 13:14:42
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 475672344
发送者主页连接: https://space.bilibili.com/475672344
==========================

==========================
弹幕内容: 冬天
发送时间: 2023-01-17 18:53:46
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 1473133205
发送者主页连接: https://space.bilibili.com/1473133205
==========================

==========================
弹幕内容: 省流：小米真好用，小米是我爹
发送时间: 2023-01-29 10:07:05
字体大小: 25
弹幕类型: 顶部弹幕
发送者UID: 1417391693
发送者主页连接: https://space.bilibili.com/1417391693
==========================

==========================
弹幕内容: 是不是720分辨率的
发送时间: 2023-02-05 05:00:38
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 1139513571
发送者主页连接: https://space.bilibili.com/1139513571
==========================

==========================
弹幕内容: 这是线问题吧。
发送时间: 2023-01-16 23:01:02
字体大小: 25
弹幕类型: 普通弹幕
发送者UID: 3706386123
发送者主页连接: https://space.bilibili.com/3706386123
==========================
所有UID反推成功，耗时37.06秒
回车继续检索，输入q退出...
```

----

</details>

### 文件输出

#### 全部弹幕.json
##### 所处文件夹
> 运行目录\DanmuJSON
##### 文件名格式
> danmu_list_{**bvid**}.json

----

#### 弹幕检索结果.txt
##### 所处文件夹
> 运行目录\outputs
##### 文件名格式
> {**检索内容**}_{**bvid**}

---
# 运行效率🏃‍♂️
#### 弹幕爬取
经过测试 57854 条弹幕仅需**4.26秒**即可爬取完成。

#### UID反推
mid_hash破解效率随着原mid的长度或大小的增大而减小。

---

# 注意事项👀
### 使用代理
#### 若您在打开代理的环境下使用本程序，您需要注意以下几点（这里用Clash for Windows举例）
- 关闭**系统代理模式(System Proxy)**，这可能会导致程序无法访问API
- 若您关闭了系统代理模式(System Proxy)无法正常上网，请尝试**点亮小地球(Service Mode)**
- 若还是无法正常联网，请通过[Issues](https://github.com/cwuom/GetDanmuSender/issues)来阐述具体情况（除程序外的软件、网站访问情况或是代理规则等）

### 报错、闪退
- 若遇到这些问题，**请先将程序闲置几个小时来排除风控的可能**。若在闲置后问题依旧复发，请通过[Issues](https://github.com/cwuom/GetDanmuSender/issues)告诉我复现方式（视频链接、网络环境、运行环境、操作系统等）。
- 若您用的是打包版本（exe），您可以通过在运行目录打开命令窗口后输入{软件名称}.exe来运行。在此环境下，报错后不会直接闪退而是会出现具体的报错内容。**请将报错内容截图或以文字形式提供给我我才能更好的解决问题。**

### 返回UID一定正确吗？
- 因为弹幕文件的mid是通过**crc32校验得到的结果转为16进制数**，一般无法逆向。但在查询后得知还是有类似的反推算法的，此算法作者也在文档中说明“**Sometimes the results are inaccurate**”，经过核实B站最新的16位mid以及超过10位以上的mid被加密后都无法正常反推出原有数据。但8、9位UID的返回结果基本正确。因为不同mid有一定几率计算成同一个哈希值，数据越大撞库的可能性就越大，**所以此程序只能保证大部分用户发送的弹幕中mid_hash逆向结果是正确的。若真的要查成分也需进一步核实，若因为此程序造成的误伤后果自负！**

# 声明

 - 一切开发皆在学习，请勿用于非法用途
