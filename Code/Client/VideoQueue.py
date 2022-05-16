"""
Class simulating Video Queue Cache
in user device
"""
import Server.VideoData
class VideoQueue:
    
    
    def __init__(self,Capacity) -> None:
        self.Capacity = Capacity
        self.Queue = []
        
    def getQueueSize(self):
        return len(self.Queue)
    
    def pop(self):
        if len(self.Queue) != 0:
            return self.Queue.pop(0)
        else:
            return None
    
    def push(self,VideoArray):
        self.Queue.append(VideoArray)
        
        
        