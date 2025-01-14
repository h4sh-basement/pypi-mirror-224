from kevin_toolbox.nested_dict_list.serializer.backends import Backend_Base
from kevin_toolbox.nested_dict_list.serializer.variable import SERIALIZER_BACKEND


@SERIALIZER_BACKEND.register(name=":skip:simple")
class Skip_Simple(Backend_Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.w_cache = None
        self.w_cache_id = None

    def write(self, name, var, **kwargs):
        if id(var) != self.w_cache_id:
            assert self.writable(var=var)
        return var

    def read(self, name, **kwargs):
        raise Exception(f'calling skip.read() is prohibited')

    def writable(self, var, **kwargs):
        """
            是否可以写
        """
        self.w_cache = False
        if isinstance(var, (int, float, str)):
            self.w_cache = True
        elif isinstance(var, (tuple,)):
            self.w_cache = all(isinstance(i, (int, float, str)) for i in var)
        self.w_cache_id = id(var)
        return self.w_cache

    def readable(self, name, **kwargs):
        """
            是否可以写
        """
        return False


if __name__ == '__main__':
    import os

    backend = Skip_Simple(folder=os.path.join(os.path.dirname(__file__), "temp"))

    a = 100
    print(backend.write(name=":a:b", var=a))

    b = backend.read(name=":a:b")
    print(b)
