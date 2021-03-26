●使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。
INSERT INTO user(id,name,username,password) VALUES (0, "user", "ply", "ply");</br>
INSERT INTO user(id,name,username,password) VALUES (0, "cat1", "cute", "12345");</br>
INSERT INTO user(id,name,username,password) VALUES (0, "cat2", "adorable", "54321");</br>
INSERT INTO user(id,name,username,password) VALUES (0, "cat3", "funny", "11111");</br>
INSERT INTO user(id,name,username,password) VALUES (0, "cat4", "black", "00000");</br>

<img src="https://user-images.githubusercontent.com/64306646/112638631-6c5b2900-8e7a-11eb-9e23-15716b4b6fd1.png" width="300" height="150">

● 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。
select * from user;</br>
<img src="https://user-images.githubusercontent.com/64306646/112637291-f1ddd980-8e78-11eb-82f2-6783d7b8cffd.png" width="300" height="150">

● 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。
select count(1) as count from user;
<img src="https://user-images.githubusercontent.com/64306646/112639685-82b5b480-8e7b-11eb-8090-271aa530e8a4.png" width="300" height="150">

● 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近到遠排序。
select * from user order by time desc;
<img src=https://user-images.githubusercontent.com/64306646/112646518-87ca3200-8e82-11eb-88a0-3e67b423da0f.png" width="300" height="150">


● 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
select * from user order by time limit 3 offset 1;
<img src=https://user-images.githubusercontent.com/64306646/112646637-ab8d7800-8e82-11eb-9d3a-c05c8ba4e95d.png" width="300" height="150">


● 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。
select * from user where username='ply';
<img src=https://user-images.githubusercontent.com/64306646/112648216-4044a580-8e84-11eb-987f-9eb125f87082.png" width="300" height="150">


● 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。
select * from user where username='ply' and password='ply';
<img src=https://user-images.githubusercontent.com/64306646/112648313-5f433780-8e84-11eb-8677-c2b9f0311971.png" width="300" height="150">


● 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位改成【丁滿】。
update user set name='丁滿' where username='ply';
<img src=https://user-images.githubusercontent.com/64306646/112648447-80a42380-8e84-11eb-8611-ec3967ce03dc.png)


● 使用 DELETE 指令刪除所有在 user 資料表中的資料。
