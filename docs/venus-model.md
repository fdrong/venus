### venus表结构设计

####  1. 用户表（venus_user）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | Y | 自增 | 
用户名 | username | string | 20 | Y | |
姓名 | name | string | 20 | Y | |
密码  | password | string | 200 | Y | |
邮箱 | email | string | 100 | Y | |
手机号 | mobilephone | int | 20 | Y | |
所属单位 | company_id | int | 20 | Y | |
是否删除 | isdelete | int | 10 | 否 |
上次登录时间 | last\_login_time | datetime | | N | |
创建时间 | create_at | datetime | | Y | |
更新时间 | update_at | datetime | | Y | |


####  2. 权限表（venus_permission）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | Y | 自增 | 
权限名 | name | string | 100 | Y | |
权限编码 | codename | string | 100 | Y | |
权限描述 | desc | string | 200 | N | |
创建时间 | create_at | datetime | | Y | |
更新时间 | update_at | datetime | | Y | |


####  3. 角色表（venus_role）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | Y | 自增 | 
角色名 | name | string | 100 | Y | |
角色描述 | desc | string | 200 | N | |
创建时间 | create_at | datetime | | Y | |
更新时间 | update_at | datetime | | Y | |

####  4. 用户-角色表（venus\_user_role）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | Y | 自增 | 
用户ID | user_id | int | 10 | Y | |
角色ID | role_id | int | 10 | Y | |
创建时间 | create_at | datetime | | Y | |


####  5. 角色-权限表（venus\_role_permission）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | Y | 自增 | 
角色ID | role_id | int | 10 | Y | |
权限ID | permission_id | int | 10 | Y | |
创建时间 | create_at | datetime | | Y | |

####  6. 单位表（venus_company）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | Y | 自增 | 
单位名 | name | string | 500 | Y | |
单位编码 | code | string | 200 | Y | |
邮箱 | email | string | 100 | Y | |
电话号码 | telno | string | 200 | Y | |
单位地址 | address | string | 200 | Y | |
创建时间 | create_at | datetime | | Y | |
更新时间 | update_at | datetime | | Y | |

####  7. 试卷表（venus\_paper）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | 自增 | 
用户ID | user_id | int | 10 | 是 | |
试卷名 | name | string | 500 | 是 | |
试卷内容 | content | Text | | 否 | 试卷内容整个导入可能是富文本| 
创建时间 | create_at | datetime | | Y | |
更新时间 | update_at | datetime | | Y | |



####  8. 考试表（venus_exam）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | 自增 | |
试卷ID | paper_id | int | 200 | 是 | |
考试名称 | name | string | 500 | 否 | |
考试类型 | type | string | 200 | 否 | |
考试时长 | overdue | int | 20 | 否 | 单位是分钟 |
考试密码 | password | string | 100 | 否 | 
创建时间 | create_at | datetime | | 是 | |
更新时间 | update_at | datetime | | 是 | |


####  9. 考试-用户表（venus\_exam_user）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | 自增 | |
考试ID | exam_id | int | 20 | 是 |
用户ID | user_id | int | 20 | 是 | |
成绩分数 | grade | float | 20 | 否 | |
开始时间 | begin_at | datetime | | 否 |
提交时间 | commit_at | datetime | | 否 | |
创建时间 | create_at | datetime | | 是 | |
更新时间 | update_at | datetime | | 是 | |


####  10. 操作日志表（venus_log）

| 名称  | 字段  | 类型 | 长度 | 是否必填 | 描述 |
|:-------------:|:---------------:|:-------------:|:-------------:|:-------------:|:-------------:|
ID | id  | int | 20 | 自增 | |
操作者 | user_id | int | 20 | 是 | |
操作类型 | type | string | 200 | 是 | |
远程主机IP | ip | string | 100 | 是 | |
操作信息 | message | string | 500 | 是 | |
创建时间 | create_at | datetime | | 是 | |



