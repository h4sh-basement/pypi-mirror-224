# 调试模块

#### 介绍

一个用于消息整理和打印输出的模块，主要功能包括 文本对齐，表格整理对方，文本修饰等。

#### 软件架构

调试模块.py # 主功能代码
效果测试.py # 用于测试主功能代码的使用效果

#### 安装教程

安装 DebugInfo 模块
```bash
pip install DebugInfo
```

在脚本中使用 DebugInfo 模块
```python
# region 引入 调试模块
from DebugInfo.DebugInfo import *
# endregion
```

#### 使用说明

测试代码可以见 **效果测试.py** 文档内的代码

文本处理效果的演示代码如下：

```python
from DebugInfo.DebugInfo import *

if __name__ == '__main__':
    # 对象实例化时,可以指定调试模式,也可以指定其它参数
    虫子 = 调试模板(True)

    # 如果调试模式打开, 这里可以打印执行位置消息
    虫子.执行位置(os.path.basename(__file__) + '[这个信息应该被显示]')

    # 可以关闭调试模式
    虫子.关闭调试()
    # 关闭调试模式后,执行位置信息不再打印
    虫子.执行位置(os.path.basename(__file__) + '[这个提示不应该被显示]')

    # 调试信息只有在调试状态才会打印输出
    虫子.关闭调试()
    虫子.调试消息('这是一个调试状态才会输出的消息, 这是1号消息')
    虫子.打开调试()
    虫子.调试消息('这是一个调试状态才会输出的消息, 这是2号消息, 你应该看不到1号消息的')

    # 可以进行缩进处理, 默认缩进一个空格符
    虫子.消息('这是缩进前')
    虫子.缩进()
    虫子.消息('这是缩进后')
    # 你也可以指定缩进的字符,例如可以指定缩进两个空格
    虫子.缩进('  ')
    虫子.消息('注意,这一行相对上一行,缩进了两个空格')

    # 注意,缩进功能没有提供回退方法,推荐的方法是如果你需要临时缩进,你可以通过创建副本的方法来进行,对副本的操作不会影响原对象
    小虫子: 调试模板 = 虫子.副本.缩进()
    小虫子.消息('这是新对象的打印,应该有一个缩进效果')
    虫子.消息('这还是原对象的打印')

    # 你可以级联进行多个操作,例如 创建副本, 缩进, 打开调试
    虫卵: 调试模板 = 虫子.副本.关闭调试().设置打印头('@')
    虫卵.消息('这是一个卵宝宝,请注意打印头符号')

    # 你可以打印一个错误消息,错误消息将标记为红色背景
    虫子.提示错误('天啊,这里有一个致命错误')

    # 可以生成并打印一个分隔线
    虫子.分隔线.修饰符('~').提示内容('这是一个黄色背景的分隔线').修饰方法(黄底).总长度(50).展示()
    虫子.分隔线.修饰符('*').提示内容('这是一个黄色字体的分隔线').修饰方法(黄字).总长度(60).展示()
    虫子.消息('下面是一个不加修饰的分隔线')
    虫子.分隔线.展示()

    # 可以很方便的整理并打印一个表格
    虫子.准备表格()  # 每次使用表格功能前,你需要手动准备一下表格
    虫子.添加一行('列1', '列2', '列3')  # 你可以把第一行的内容视做表头
    虫子.添加一行('行1', '天下', '太平')
    虫子.添加一行('行2', '和', '谐', '社', '会')
    虫子.添加一行('', '', '', '这一行前面的列没有内容', '这一列没有表头哈')

    # 你可以添加一行只有在调试模式才显示的内容
    虫子.添加一调试行('行5', '这一行只有调试状态下才显示')

    # 也可以通过list添加一行
    虫子.添加一行(['行6', '', '', '行6列4'])

    # 也可以添加多行
    虫子.添加多行([['行7', '行7列2'], ['行8', '', '行8列3']])
    虫子.展示表格()

    虫子.分隔线.提示内容('这是一个绿色的分隔线').修饰方法(绿字).展示()

    # 你可以在表格,或者其它需要的地方,使用颜色修饰你的字符
    虫子.准备表格()
    虫子.添加一行('彩字效果', '编码展示')
    彩字 = 蓝字('蓝字')
    虫子.添加一行(彩字, 彩字.encode())
    彩字 = 红底(彩字 + '红底')
    虫子.添加一行(彩字, 彩字.encode())
    彩字 = 黄底(彩字 + '黄底')
    虫子.添加一行(彩字, 彩字.encode())
    彩字 = 绿字(彩字 + '绿字')
    虫子.添加一行(彩字, 彩字.encode())
    虫子.展示表格()
```

以上代码的运行效果如下：  
![文本处理效果演示](image0.png)

语义日期效果的演示代码如下：

```python
from DebugInfo.DebugInfo import *

if __name__ == '__main__':
    虫子: 调试模板 = 调试模板()
    虫子.消息(分隔线模板().提示内容('语义日期演示').修饰方法(红字))
    虫子.准备表格()
    虫子.添加一行('日期', '日期语义')
    虫子.添加一行(datetime.now().date() + timedelta(days=-365 * 5), 语义日期模板(datetime.now() + timedelta(days=-365 * 5)))
    虫子.添加一行(datetime.now().date() + timedelta(days=-365), 语义日期模板(datetime.now() + timedelta(days=-365)))
    虫子.添加一行(datetime.now().date() + timedelta(days=-180), 语义日期模板(datetime.now() + timedelta(days=-180)))
    虫子.添加一行(datetime.now().date() + timedelta(days=-40), 语义日期模板(datetime.now() + timedelta(days=-40)))
    虫子.添加一行(datetime.now().date() + timedelta(days=-20), 语义日期模板(datetime.now() + timedelta(days=-20)))
    虫子.添加一行(datetime.now().date() + timedelta(days=-8), 语义日期模板(datetime.now() + timedelta(days=-8)))
    虫子.添加一行(datetime.now().date() + timedelta(days=-2), 语义日期模板(datetime.now() + timedelta(days=-2)))
    虫子.添加一行(datetime.now().date() + timedelta(days=-1), 语义日期模板(datetime.now() + timedelta(days=-1)))
    虫子.添加一行(datetime.now().date() + timedelta(days=-0), 语义日期模板(datetime.now() + timedelta(days=-0)))
    虫子.添加一行(datetime.now().date() + timedelta(days=1), 语义日期模板(datetime.now() + timedelta(days=1)))
    虫子.添加一行(datetime.now().date() + timedelta(days=2), 语义日期模板(datetime.now() + timedelta(days=2)))
    虫子.添加一行(datetime.now().date() + timedelta(days=3), 语义日期模板(datetime.now() + timedelta(days=3)))
    虫子.添加一行(datetime.now().date() + timedelta(days=9), 语义日期模板(datetime.now() + timedelta(days=9)))
    虫子.添加一行(datetime.now().date() + timedelta(days=18), 语义日期模板(datetime.now() + timedelta(days=18)))
    虫子.添加一行(datetime.now().date() + timedelta(days=40), 语义日期模板(datetime.now() + timedelta(days=40)))
    虫子.添加一行(datetime.now().date() + timedelta(days=180), 语义日期模板(datetime.now() + timedelta(days=180)))
    虫子.添加一行(datetime.now().date() + timedelta(days=365), 语义日期模板(datetime.now() + timedelta(days=365)))
    虫子.添加一行(datetime.now().date() + timedelta(days=365 * 4), 语义日期模板(datetime.now() + timedelta(days=365 * 4)))

    虫子.展示表格()
```

以上代码的运行效果如下：  
![语义日期效果演示](image.png)

使用乘法表演示表格对齐打印效果的代码如下：

```python
from DebugInfo.DebugInfo import *

if __name__ == '__main__':
    # 对象实例化时,可以指定调试模式,也可以指定其它参数
    虫子 = 调试模板(True)

    # 打印乘法表
    虫子.准备表格()
    虫子.添加多行([[f'{被乘数}・{乘数} = {被乘数 * 乘数}' for 被乘数 in range(1, 乘数 + 1)] for 乘数 in range(1, 15)])

    虫子.分隔线.提示内容('展示乘法表').修饰方法(红字).展示()
    虫子.展示表格()

    虫子.分隔线.提示内容('左右巅倒乘法表').修饰方法(红字).展示()
    虫子.副本.左右巅倒表格().展示表格()

    虫子.分隔线.提示内容('上下巅倒乘法表').修饰方法(红字).展示()
    虫子.副本.上下巅倒表格().展示表格()

    虫子.分隔线.提示内容('上下左右巅倒乘法表').修饰方法(红字).展示()
    虫子.副本.上下巅倒表格().左右巅倒表格().展示表格()
```
以上代码的运行效果如下：  
![乘法表打印效果](image3.png)


#### 待办事项

- [x] 调试模块中,所有的方法都使用了中文命名,这是在尝试所谓的"中文编程"概念,通过母语理解代码的逻辑还是有帮助和有意义的.
- [ ] 代码中对于 python 原生关键字,依然使用的英文名字,例如 def, for..in, while,这部分希望可以有大神进行汉化支持,例如

```python
if 条件 > 10:
    return True
elif 条件 > 5:
    return True
else:
    return False
# 汉化语法如下
如果 条件 > 10:
    返回 真
再如 条件 > 5:
    返回 真
其它:
    返回 假

for itm in itmList:
    print(itm)
# 汉化语法可以如下
循环 列表 中的 项:
    打印(项)


def funName():
    return True


# 汉化语法可以如下:
定义 函数名():
    返回 真

# 以上汉化仅仅是举例,如何定义中文关键字,才能更贴合这些关键字的本意,并非天生的,是需要思考和探索的.
# 以上举例中,所展示的关键字和语法结构未必合理,但如果没有人思考和探索,则永远也不会突然出现合理的中文关键字和合理的中文语法结构.
# 以上抛砖引玉,希望可以引起大牛的兴趣,引起大家对中文是否应该在编程领域可以占一席之地的思考.
```

#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

#### 特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5. Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
