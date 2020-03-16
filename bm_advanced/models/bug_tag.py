# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugTag(models.Model):
    _name = 'bm.bug_tag'
    _description = "bug标识"

    name = fields.Char('名称')
    '''
    以下划线（_）开头的属性不是普通的属性，我们称之为模型属性。
    也就是说这些属性的作用不是用于描述记录，而是描述整个模型。
    常用三模型属性:
    _name：这是Odoo内模型的内部标示，如果我们创建的是一个新模型，则必须填写该属性。
    _description：是展示给用户看时该模型的一个标题，不是必需的，但推荐最好是使用该模型属性。
    _order：该属性设置的是该模型的记录集展示时默认的排序字段，
    类似于我们编写SQL语句时的order by后面的字段。
    
    _rec_name：该模型属性是record name的缩写，可用来指定一个字段作为该记录的描述。
    一般来讲，Odoo默认使用name字段作为一条记录的描述，我们可以通过这个字段指定其他的字段。
    _table：是在模型里面制定后台存储数据的数据库表名，通常，该数据库表名是更改模型的名称，
    把点（.）换成下划线，但是通过这个模型属性制定后，Odoo会根据该属性创建数据库表。
    用于继承的_inherit和_inherits两个模型属性
    '''
    '''
    Odoo模型被统一保存在中央记录处，
    在老的API中则是缓存池。
    中央记录处是一个字典，
    保存了指向所有模型实例的引用，
    我们可以通过模型的名字获取这个模型的引用，
    在代码中就是self.env[‘x’]。这样就会返回模型x的引用。
    '''
    '''
    瞬态模型和抽象模型
    瞬态模型：该类模型是基于models.TransientModel类的，
        一般可用于向导式用户交互，其数据也是存储于数据库表的，
        只不过是临时存储，会有作业定期从这些表中删除老数据。
    抽象模型：该类模型是基于models.AbstractModel类的，
        没有数据库表为其存储数据。
        抽象模型往往仅仅是为了方便子类复用其字段或方法，
        自己本身并不需要存储数据。
    '''