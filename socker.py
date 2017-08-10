import socket,socks

def socker(address,port):
    SOCKS5_PROXY_HOST = address
    SOCKS5_PROXY_PORT = port 
    default_socket = socket.socket
    socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT) 
    socket.socket = socks.socksocket