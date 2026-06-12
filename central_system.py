import psutil
import time

class Brain:
    def __init__(self):
        self.sensor = SystemSensor()
        self.CPU = self.sensor.check_cpu()
        self.Memory = self.sensor.check_memory()
        self.Disk = self.sensor.check_disk()
        self.Network = self.sensor.check_network()
    
    def think(self):
        thresholds = {
            'CPU': (self.CPU, 80),
            'Memory': (self.Memory, 80),
            'Disk': (self.Disk, 80),
            'Network': (self.Network, 5)
        }

        alert_triggered = False

        for name, (current, limit) in thresholds.items():
            if current > limit:
                print(f'[ALERT]: {name} usage is too high!')
                alert_triggered = True

        if not alert_triggered:
            print('All systems clear')
        
    def run(self):
        while True:
            self.CPU = self.sensor.check_cpu()
            self.Memory = self.sensor.check_memory()
            self.Disk = self.sensor.check_disk()
            self.Network = (10 * (self.sensor.check_network())) / 1048576

            self.think()
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
    

butler = Brain()
butler.run()



