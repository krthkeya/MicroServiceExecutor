import asyncio
class generic_task:
    def __init__(self, dependencies : list = [], outgoing : list = []):
        """
        The generic task class, inherit this in your task class.
        This class helps you execute a DAG like task pipeline with concurrency.
        Args:
            dependencies (list) : a list of strings, the inputs needed to the specific task
            outgoing (list) : a list of objects also inherting the same generic_task class, that depend on this task in the DAG.
        """
        self.dependencies = dependencies
        self.outgoing = outgoing
        self.inputs = {key : None for key in self.dependencies}
        self.ready = False
        # the output will be stored as a dict under self.output for all tasks
        self.output = {}
    def update_readiness(self):
        """
        checks if task is ready for execution based on if all inputs received, and updates the self.ready
        """
        self.ready = all(value != None for value in self.inputs.values())
        return self.ready
    def execute(self) -> dict:
        """
        The custom execute method, override this to write custom logic, just return a dict that will be updated into self.output
        Returns:
            dict : a dict with all outputs that will be updated into self.output
        """
        raise NotImplementedError
    async def execute_broadcast_trigger(self):
        """
        A concurrent executor of the DAG.
        Handles calling the execute function as well as broadcasting outputs to dependents and triggering all ready dependents.
        """
        self.output.update(self.execute())
        tasks = []
        for dependent in self.outgoing:
            dependent.inputs.update(self.output)
            if dependent.ready == True or dependent.update_readiness() == True:
                tasks.append(asyncio.create_task(dependent.execute_broadcast_trigger()))
        if len(tasks) >= 1:
            await asyncio.gather(*tasks)
        

    