# CSTHome

东华大学党员之家 APP 后端。

## 本地运行

确保已经配置好 docker。如果没有，其参考[这里](https://docs.docker.com/engine/installation/)。

```bash
$ docker-compose up --build
```

- 后台管理页面请访问 [http://localhost:12138/admin](http://localhost:12138/admin) 。

- API 文档请访问 [http://localhost:12138/docs](http://localhost:12138/docs) 。

## 远程部署

本项目使用的是 Fabric 进行自动化部署。先确保安装 Fabric (Python 2 的一个库），然后进入到项目根目录执行自动化任务。

```bash
$ pip install fabric
$ fab deploy
```

需要注意的是，如果没有云主机的私钥文件是无法进行远程登录的。
