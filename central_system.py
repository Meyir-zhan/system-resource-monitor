import psutil
import time
from plyer import notification

class Brain:
    def __init__(self, cpu_limit, memory_limit, disk_limit, network_limit):
        self.sensor = SystemSensor()
        self.CPU = self.sensor.check_cpu()
        self.Memory = self.sensor.check_memory()
        self.Disk = self.sensor.check_disk()
        self.Network = self.sensor.check_network()
        self.cpu_limit = cpu_limit
        self.memory_limit = memory_limit
        self.disk_limit = disk_limit
        self.network_limit = network_limit
        self.active_alerts = {}

    def think(self, cpu, memory, disk, network):
        thresholds = {
            'CPU': (cpu, self.cpu_limit),
            'Memory': (memory, self.memory_limit),
            'Disk': (disk, self.disk_limit),
            'Network': (network, self.network_limit)
        }

        

        for name, (current, limit) in thresholds.items():
            if current > limit:
                current_time = time.time()
                if not (name in self.active_alerts) or (current_time - self.active_alerts[name]) > 60:
                    print(f'[ALERT]: {name} usage is too high!')
                    notification.notify(title = "System Monitor Alert", message = f'[ALERT]: {name} usage is too high!')
                    self.active_alerts[name] = current_time
                
            else:
                if name in self.active_alerts:
                    del self.active_alerts[name]
                

        if not self.active_alerts:
            print('All systems clear')
            
        
    def run(self):
        while True:
            cpu = self.sensor.check_cpu()
            memory = self.sensor.check_memory()
            disk = self.sensor.check_disk()
            network = (10 * (self.sensor.check_network())) / 1048576

            self.think(cpu,memory,disk,network)
            time.sleep(2)
        

        
class SystemSensor:
    def check_cpu(self):
        return psutil.cpu_percent(interval=None)
    def check_memory(self):
        return psutil.virtual_memory().percent
    def check_disk(self):
        return psutil.disk_usage("/").percent
    def check_network(self):
        stats = psutil.net_io_counters()
        start_bytes = stats.bytes_sent + stats.bytes_recv
        time.sleep(0.1)
        stats2 = psutil.net_io_counters()
        end_bytes = stats2.bytes_sent + stats2.bytes_recv
        return end_bytes - start_bytes
    

butler = Brain(85,85,85,5)
butler.run()



