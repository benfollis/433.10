# a socket which contains other sockets that are switched on and off as a group
# this can be used void concurrency problems when different sockets
# share the same bit driver, and the bit driver is not thread safe.
# it's also useful when you want to present multiple sockets as the same
# logical socket
class SocketGroup:

    # the group members are the _names_ of the sockets
    # and we take the sockets array, as we want to reference
    # the name after config binding is complete
    def __init__(self, group_members, sockets):
        self.group_members = group_members
        self.sockets = sockets


    def switch_socket(self, state):
        for socket_name in self.group_members:
            socket = self.sockets[socket_name]
            socket.switch_socket(state)
