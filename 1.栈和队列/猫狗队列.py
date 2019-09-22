"""
    实现一个队列存储dog和cat类的对象
    有以下功能：
        1,用户可以调用add方法将cat类或者dog类的实例放入到队列中
        2,用户可以调用pollAll方法，将队列中所有的实例按照队列的先后顺序依次弹出
        3,用户可以调用pollCat方法，将队列中cat类的实例按照队列顺序依次弹出
        4,调用isEmpty方法，检查队列中是否还有dog和cat
        5,调用isDogEmpty检查队列中是否有dog类的实例
        6,调用isCatEmpty检查队列中是否有cat类的实例

    实现方法：
        1,定义cat和dog类并拥有类属性count表示添加时的顺序
        2,定义PetQueue类其中拥有dog队列和cat队列每次add时按照类型和count添加
"""
class Dog(object):
    def __init__(self):
        self.type = 'Dog'

class Cat(object):
    def __init__(self):
        self.type = 'Cat'

class PetEnterQueue(object):
    def __init__(self,obj,count=None):
        self.pet = obj
        self.count = count

    def get_pet(self):
        return self.pet

    def get_count(self):
        return self.count

    def get_type(self):
        return self.type

class PetQueue(object):
    def __init__(self):
        self.count = 0
        self.cat_queue = []
        self.dog_queue = []

    def add(self,obj):
        assert isinstance(obj,(Cat,Dog))
        if isinstance(obj,Cat):
            self.cat_queue.append(PetEnterQueue(obj,self.count))
        elif isinstance(obj,Dog):
            self.dog_queue.append(PetEnterQueue(obj,self.count))
        self.count += 1

    def is_empty(self):
        return not self.dog_queue and not self.cat_queue

    def is_dog_empey(self):
        return not self.dog_queue

    def is_cat_empty(self):
        return not self.cat_queue

    def poll_all(self):
        if self.is_empty():
            raise Exception('queue is empty')
        if self.cat_queue and self.dog_queue:
            if self.cat_queue[0].count < self.dog_queue[0].count:
                return self.cat_queue.pop(0)
            else:
                return self.dog_queue.pop(0)
        elif self.cat_queue:
            return self.cat_queue.pop(0)
        elif self.dog_queue:
            return self.dog_queue.pop(0)

    def poll_dog(self):
        if not self.dog_queue:
            raise Exception('dog is empty')
        return self.dog_queue.pop(0)

    def poll_cat(self):
        if not self.cat_queue:
            raise Exception('cat is empty')
        return self.cat_queue.pop(0)






















