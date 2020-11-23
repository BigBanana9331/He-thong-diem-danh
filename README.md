# faceRecognition
He thong diem Danh

# B1: Train Model
```
    #: python ./trainSave.py
```

Ta duoc model train.pkl

# B3: Tao file constant

Voi noi dung:
    ```
    dbInfor = {
	    "host":"localhost",
        "user":"user1",
        "password":"mypass",
        "database":"diemdanh"
    }
    ```

# B2: Tren Jetson Nano chay:
```
    #: python ./faceRecognition-jetson.py
```

Neu tren Windows chay:
```
    #: python ./faceRecognition-windows.py
```

# Stack
MySQL
OpenCV2

