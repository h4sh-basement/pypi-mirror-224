import os
from kevin_toolbox.data_flow.file import json_
from kevin_toolbox.nested_dict_list.serializer.backends import Backend_Base
from kevin_toolbox.nested_dict_list.serializer.variable import SERIALIZER_BACKEND


@SERIALIZER_BACKEND.register()
class Json_(Backend_Base):
    name = ":json"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.w_cache = None
        self.w_cache_id = None

    def write(self, name, var, **kwargs):
        if id(var) != self.w_cache_id:
            assert self.writable(var=var)

        with open(os.path.join(self.paras["folder"], f'{name}.json'), "w") as f:
            f.write(self.w_cache)

        self.w_cache = None
        self.w_cache_id = None
        return dict(backend=Json_.name, name=name)

    def read(self, name, **kwargs):
        assert self.readable(name=name)

        var = json_.read(file_path=os.path.join(self.paras["folder"], f'{name}.json'), b_use_suggested_converter=True)
        return var

    def writable(self, var, **kwargs):
        """
            是否可以写
        """
        try:
            self.w_cache = json_.write(content=var, file_path=None, sort_keys=False, b_use_suggested_converter=True)
            self.w_cache_id = id(var)
            return True
        except:
            return False

    def readable(self, name, **kwargs):
        """
            是否可以写
        """
        return os.path.isfile(os.path.join(self.paras["folder"], f'{name}.json'))


if __name__ == '__main__':
    backend = Json_(folder=os.path.join(os.path.dirname(__file__), "temp"))

    var_ = [{123: 123, None: None, "<eval>233": 233, "foo": (2, 3, 4)}, 233]
    # backend.writable(var=var_)
    print(backend.write(name=":inst", var=var_))

    b = backend.read(name=":inst")
    print(b)
