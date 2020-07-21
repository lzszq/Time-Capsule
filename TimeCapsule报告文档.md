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

//本来打算只在后端对数据进行加密处理，但对于用户而言，manager仍有权限看到其数据，故决定在前端，即用户的本地端利用javascript进行加密（要不是有crypto.js现成的库，其实作者懒得写js:sweat_smile:)，key由用户自己管理，由于有的用户不在意是否进行加密也懒得记key，故在前端采取optional方式。

利用crypto.js对数据进行加密。

对MySQL该项目相关database的privilege进行限制，保证数据在server的安全

# 7/22