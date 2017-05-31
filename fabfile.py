from fabric.api import local
from fabric.decorators import task


@task
def install(requirements_env="dev"):
    """安装所有的依赖包
    默认参数是dev，开发环境下安装依赖包；可选参数prod（fab install:prod ）则是在生产环境安装"""
    local("pip3 install -r requirements/%s.txt" % requirements_env)


@task
def runser():
    """运行本地服务器"""
    local("./manage.py runserver")


@task
def migrate():
    """创建、迁移、修改数据库"""
    local("./manage.py migrate")
    local("./manage.py makemigrations")


@task
def freeze():
    """生成含有项目所需依赖包的requirements.txt文件"""
    local("pip3 freeze > requirements.txt")


@task
def pep():
    """用pep8检查Python代码风格"""
    local("pep8 .")


@task
def lint():
    """用pylint检查Python代码风格"""
    local("pylint .")


@task
def tag(version):
    """使用git标签记录版本，再发到GitHub。需要版本号作为参数，格式：v0.0.x"""
    local("git tag %s" % version)
    local("git push origin %s" % version)


@task
def fetch_tag(version):
    """从GitHub下载已发布的包。参数为版本号，格式：v0.0.x"""
    local('wget https: // codeload.github.com / Bryanthelol / my_second_blog / tar.gz / %s ' % version)


@task
def gitall(message):
    """git一键add和commit"""
    local("git add .")
    local('git commit -m "%s"' % message)


@task
def sta():
    """git status的简化命令，从码status的痛苦中解放"""
    local("git status")


@task
def test():
    """运行测试"""
    local("./manage.py test")
