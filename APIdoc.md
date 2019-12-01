#DEMO 文档

## 1.获取学生列表
 + URL:/api/students
 + METHOD:GET
 + RETURN
    ```json
    {
    "data": [
        {
            "clazz": "string",
            "description": "string",
            "id": 2,
            "id_card": "string",
            "name": "string"
        },
        {
            "clazz": "string",
            "description": "string",
            "id": 5,
            "id_card": "string",
            "name": "string"
        },
         ...
    ],
    "message": "获取成功",
    "status": 1
    }
    ```
    
## 2.获取指定学生
 + URL:/api/students/\<int\>
 + METHOD:GET
 + RETURN
    ```json
    {
    "data": {
        "clazz": "垃圾回收181班",
        "description": "这是一条神奇的描述",
        "id": 2,
        "id_card": "1234",
        "name": "还行"
    },
    "message": "获取成功",
    "status": 1
    }
    ```
    或者
    
    ```json
    {
     
            "status": 0,
            "message": "没有该学生",
            "data": ""
    }

    ```
    
## 3.添加学生
 + URL:/api/students/append
 + METHOD:POST
 + PARAMS
   ```json
   {
        "name": str,
        "clazz": str,
        "description": str,
        "id_card": str
    }
    ```
 + RETURN
 ```json
    {
        "status": 1,
        "message": "操作成功",
        "data": ""
    }
 ```
 
## 4.删除学生

 + URL:/api/students
 + METHOD: DELETE
 + PARAMS
   ```json
   {
        "id": int
    }
    ```
 + RETURN
 ```json
    {
        "status": 1,
        "message": "操作成功",
        "data": ""
    }
 ```
 
 
 ## 5.修改学生描述

 + URL:/api/students
 + METHOD: DELETE
 + PARAMS
   ```json
   {
        "id": int,
        "description" : "你很棒"
    }
    ```
 + RETURN
 ```json
    {
        "status": 1,
        "message": "操作成功",
        "data": ""
    }
 ```
 或者
 ```json

    {
            "status": 0,
            "message": "没有该学生",
            "data": ""
    }
  ```
 



    
    