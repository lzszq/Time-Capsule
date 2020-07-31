# 7/21

###### 前端开发流程图

```flow
start=>start: Open TimeCapsule Website
end=>end: Close TimeCapsule Website

index.html=>operation: index.html
put.html=>operation: put.html
open.html=>operation: open.html

POST_put_form=>operation: POST data of TimeCapsule
POST_open_form=>operation: POST data of TimeCapsule

Put=>condition: Go to put TimeCapsule?
Open=>condition: Go to open TimeCapsule?

Back_put.html=>condition: Go back to put.html?
Back_open.html=>condition: Go back to open.html?
Back_index.html=>condition: Go back to index.html?

start->index.html->Put

Put(yes)->put.html->POST_put_form->Back_put.html
Back_put.html(yes)->put.html
Back_put.html(no)->Back_index.html
Back_index.html(yes)->index.html
Back_index.html(no)->end

Put(no)->Open

Open(yes)->open.html->POST_open_form->Back_open.html
Back_open.html(yes)->open.html
Back_open.html(no)->Back_index.html
Back_index.html(yes)->index.html
Back_index.html(no)->end

Open(no)->end
```

###### 后端交互

flask实现数据接收和发送

###### 项目标志

“Starliner”飞船外形类似Capsule，故将其作为本次项目的标志。

//其实是作者喜欢飞船:stuck_out_tongue:

###### 数据安全问题

由于Time Capsule装的数据可能涉及隐私，故决定采用AES(Advanced Encryption Standard)，又称Rijndael算法。利用对称加密算法对数据进行加密，以保证用户对该功能的信任。

~~利用python在后端对数据进行加密。~~

//本来打算只在后端对数据进行加密处理，但对于用户而言，manager仍有权限看到其数据，故决定在前端，即用户的本地端利用javascript进行加密（要不是有crypto.js现成的库，其实作者都懒得写js:sweat_smile:)，key由用户自己管理，由于有的用户不在意是否进行加密也懒得记key，故在前端采取optional方式。

利用crypto.js对数据进行加密。

对MySQL该项目相关database的privilege进行限制，保证数据在server的安全。

# 7/22

##### 后端开发流程

###### put

```flow
start_put.html=>start: Open put.html 
end_put.html=>end: Close put.html

GET_put.html=>condition: GET?
POST_put.html=>condition: POST?
is_put_done=>condition: Put done?

render_put_after_GET=>operation: Return render html
put_done=>operation: Return successful html
non_put_done=>operation: Return non-finished html with data that you filled
record_put_data=>operation: Record data from POST

start_put.html->GET_put.html

GET_put.html(yes)->render_put_after_GET->POST_put.html
POST_put.html(yes)->is_put_done
is_put_done(yes)->record_put_data->put_done->end_put.html
is_put_done(no)->non_put_done->POST_put.html
POST_put.html(no)->end_put.html

GET_put.html(no)->end_put.html
```

###### open

```flow
start_open.html=>start: Open open.html 
end_open.html=>end: Close open.html

GET_open.html=>condition: GET?
POST_open.html=>condition: POST?
is_open_done=>condition: Open done?

render_open_after_GET=>operation: Return render html
open_done=>operation: Return successful html
non_open_done=>operation: Return Not Found or others
record_open_data=>operation: Record data from POST

start_open.html->GET_open.html

GET_open.html(yes)->render_open_after_GET->POST_open.html
POST_open.html(yes)->is_open_done
is_open_done(yes)->record_open_data->open_done->end_open.html
is_open_done(no)->non_open_done->POST_open.html
POST_open.html(no)->end_open.html

GET_open.html(no)->end_open.html
```

##### put页面

为方便用户填充更改到期时间，采取自动填充使用时的时间。

利用js的alert函数对用户进行提醒，保留encryptkey。

##### 关于Capsule的管理

生成secret-key，根据secret-key对Capsule进行索引。组成元素有(0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ )共62个字符。由于生成的secret-key长度为16，则其生成的个数为(n个元素，长度为m)
$$
key = {n^{m}} = {62^{16}}
$$
故足够支撑Capsule的管理，而每生成一个key会与原先生成的key进行查重，若重复则重新生成，虽然概率较小，为保险起见，决定牺牲查询损耗的时间来保证不会出错。

##### 数据的存储

由于还处于测试阶段，未使用MySQL进行数据存储。

# 7/23

###### 数据处理

在服务器新建一个用户TimeCapsule专门处理这个项目，在Mysql新建一个用户TimeCapsule，并且privileges限制为create, insert, select。

采用mysql-connector对MySQL进行读，写及建表的操作。

###### 项目试部署

使用virtualenv构建一个虚拟环境。

采用gunicorn+flask+gevent对项目进行迅速部署，并使用nginx对其进行反向代理。

编写gunicorn.conf.py文件。//gunicorn需在虚拟环境中使用。

使用命令如下：

```
gunicorn -c gunicorn.conf.py start:app
```

进行部署。

# 7/25

###### Capsule开启限制

未到时间，则显示unexpired reminder。

###### 到时间，发送邮件提醒功能

本意是想在服务器上通过postfix，用python3使用smtp协议发送邮件，但鉴于各云服务器ban掉了25端口，也不建议在服务器本地直接发送邮件，故使用465端口的想法也否决掉，直接采用第三方smtp服务器，比如~~网易~~，QQ等，为什么不用阿里云的邮件推送？虽然有免费额度，但是超了还是要钱的嘛，当然是选择白嫖:sweat_smile:。

千万不要选163邮箱，千万不要选163邮箱！！！！血泪教训，一直554，查了百度才知道。。。。。。

# 7/27

给表新增一个判断是否发送提醒邮件的参数。

实现并完善邮件提醒功能。

计划使用crontab实现发送到期capsule。

# 7/28

使用docker部署项目主体

