import psutil as ps
from database.db import log_network_event
import socket

def get_network_connections():
    connections = []

    for conn in ps.net_connections(kind="inet"):
        if conn.raddr and conn.pid:
            try:
                process = ps.Process(conn.pid)
                process_name = process.name()
                remote_ip = conn.raddr.ip
                remote_port = conn.raddr.port
                connections.append(
                    (process_name, conn.pid, remote_ip, remote_port)
                )
            except (ps.NoSuchProcess, ps.AccessDenied):
                pass

    return connections



def monitor_network():
    connections = get_network_connections()
    for process_name, pid, ip, port in connections:
        print(f"{process_name} (PID {pid}) -> {ip}:{port}")
        log_network_event(process_name, pid, ip, port)


def get_connections_by_process_name(target):
    connections = []
    for conn in ps.net_connections(kind="inet"):
        if conn.raddr and conn.pid:
            try:
                proc = ps.Process(conn.pid)
                name = proc.name()

                if target.lower() in name.lower():
                    connections.append({
                        "ip": conn.raddr.ip,
                        "port": conn.raddr.port,
                        "pid": conn.pid
                    })
            except (ps.NoSuchProcess, ps.AccessDenied):
                pass
        return connections