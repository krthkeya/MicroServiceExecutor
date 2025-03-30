from task_template import generic_task

class service_a(generic_task):
    def __init__(self, dependencies = [], outgoing = []):
        super().__init__(dependencies, outgoing)
    def execute(self):
        return {"a_out" : "a"}
    
class service_b(generic_task):
    def __init__(self, dependencies = [], outgoing = []):
        super().__init__(dependencies, outgoing)
    def execute(self):
        return {"b_out" : "b" + self.inputs["a_out"]}

class service_c(generic_task):
    def __init__(self, dependencies = [], outgoing = []):
        super().__init__(dependencies, outgoing)
    def execute(self):
        return {"c_out" : "c" + self.inputs["a_out"]}

class service_d(generic_task):
    def __init__(self, dependencies = [], outgoing = []):
        super().__init__(dependencies, outgoing)
    def execute(self):
        return {"d_out" : "d" + self.inputs["b_out"] + self.inputs["c_out"]}