from tasks import service_a, service_b, service_c, service_d
import asyncio

d_instance_1 = service_d(
dependencies=["c_out", "d_out"],
outgoing=[]
)

c_instance_1 = service_c(
dependencies=["a_out"],
outgoing=[d_instance_1]
)

b_instance_1 = service_b(
dependencies=["a_out"],
outgoing=[d_instance_1]
)

a_instance_1 = service_a(
    dependencies=[],
    outgoing=[b_instance_1, c_instance_1]
)

asyncio.run(a_instance_1.execute_broadcast_trigger())
print(d_instance_1.output)