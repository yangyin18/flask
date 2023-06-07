from flask import Flask
#给Flask一个实例化对象,其中__name__入参是你的模块名或者包名，Flask应用会根据这个来确定你的应用路径以及静态文件和模板文件夹的路径
app = Flask(__name__)
#路由
@app.route('/')
def hello_world():
   return 'Hello World!'
#运行
if __name__ == '__main__':
    app.run()