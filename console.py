import cmd
from models.base_model import BaseModel, SimpleStorage

class Shell(cmd.Cmd):
    prompt = '(hbnb) > '
    storage = SimpleStorage()
    objects = {}

    def do_create(self, args):
        obj = BaseModel()
        serialized = self.storage.serialize(obj)
        self.objects[obj.id] = serialized
        print(obj.id)

    def do_show(self, args):
        if not args:
            print("** please enter id **")
            return
        obj_id = args.strip()
        if obj_id in self.objects:
            obj = self.storage.deserialize(self.objects[obj_id], BaseModel)
            print(vars(obj))
        else:
            print("** id not found **")

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

if __name__ == '__main__':
    Shell().cmdloop()