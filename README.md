# 如何开启开发服务器

进入项目主目录，依次运行如下命令。

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python manage.py runserver
```

如果需要退出虚拟环境，输入 `deactivate` 命令即可。

# 进入后台管理界面

开启开发服务器后，输入 [localhost:8000/admin/](localhost:8000/admin/) 即可进入后台管理系统。管理员账号是 `admin` ，密码是 `tomismyson` 。

# 查看API文档

打开Swagger Editor在线编辑器 [http://editor.swagger.io/#](http://editor.swagger.io/#)。

然后将 docs 中的 `api-docs.yaml` 复制进在线编辑器中，即可查看渲染后的文档。

所有的 `Response` 返回结果（`JSON` 格式）均在 docs/responseExamples 中。