from ansible.errors import AnsibleActionFail

class Response(object):
    def __init__(self, response):
        self.response = response

class FakeISE(object):
    def __init__(self, family):
        self.objects = []
        self.family = family

    def add(self, obj):
        self.objects.append(obj)
        id = len(self.objects) - 1
        self.objects[id].update(dict(id=id))

    def get(self, name):
        result = dict()
        for obj in self.objects:
            if obj["name"] == name:
                result.update(obj)
                break
        return result

    def get_by_id(self, **params):
        id = params.get("id")
        response = dict(response=None)
        result = []
        for obj in self.objects:
            if obj["id"] == id:
                result.append(obj)
                break
        return response.update({family:result})

    def get_by_name(self, **params):
        name = params.get("name")
        result = None
        for obj in self.objects:
            if obj["name"] == name:
                result = obj
                break
        return Response({self.family: result})

    def update_by_id(self, **params):
        id = params.get("id")
        found = False
        for obj in self.objects:
            if obj["id"] == id:
                obj.update(params)
                found = True
        if not found:
            raise Exception("Error 404: Object not found")
        return Response(None)

    def create(self, **params):
        self.add(params)
        return Response(None)


class FakeISESDK(object):
    def __init__(self, family):
        self.result = dict(changed=False,result="")
        self.api = FakeISE(family)

    def add_object(self, obj):
        self.api.add(obj)

    def get_object(self):
        return self.api.objects[0]

    def changed(self):
        self.result["changed"] = True

    def object_created(self):
        self.changed()
        self.result["result"] = "Object created"

    def object_updated(self):
        self.changed()
        self.result["result"] = "Object updated"

    def object_deleted(self):
        self.changed()
        self.result["result"] = "Object deleted"

    def object_already_absent(self):
        self.result["result"] = "Object already absent"

    def exec(self, family, function, params=None):
        name_parts = function.split("_")
        if name_parts[0] == "create":
            function = "create"
        else:
            function = "_".join((name_parts[0], name_parts[-2], name_parts[-1]))
        try:
            func = getattr(self.api, function)
        except Exception as e:
            self.fail_json(msg=e)
        try:
            if params:
                response = func(**params)
            else:
                response = func()
        except Exception as e:
            self.fail_json(
                msg=(
                    "An error occured when executing operation."
                    " The error was: {error}"
                ).format(error=e)
            )
        return response


    def fail_json(self, msg, **kwargs):
        self.result.update(**kwargs)
        raise AnsibleActionFail(msg, kwargs)

    def exit_json(self):
        return self.result