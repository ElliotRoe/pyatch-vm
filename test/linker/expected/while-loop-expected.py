async def thread_id_0(vm_proxy):
    move = vm_proxy.move
    while True:
        move(10)
        move(10)

