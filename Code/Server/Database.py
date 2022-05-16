"""
class to represent Database
    attributes:
    VideoArray
    UserArray
    VideoCount
    UserCount
    methods:
    GetVideoById
    GetUserById
    GetVideoCount
    GetUserCount
    InsertVideo
    InsertUser
    UpdateVideo
    UpdateUser
    DeleteVideo
    DeleteUser
"""
import UserData
import VideoData

class Database:
    
    
    def __init__(self) -> None:
        self.VideoArray = []
        self.UserArray = []
        self.UserCount = 0
        self.VideoCount = 0
    
    def getVideoById(self,Id):
        return self.VideoArray[Id]
    
    def getUserById(self,Id):
        return self.UserArray[Id]
    
    def getVideoCount(self):
        return self.VideoCount

    def getUserCount(self):
        return self.UserCount
    
    def insertVideo(self,video):
        self.VideoArray.append(video)
        self.VideoCount += 1
    
    def insertUser(self,user):
        self.UserArray.append(user)
        self.UserCount += 1
    
    def updateVideo(self,Id,video):
        self.VideoArray[Id] = video
    
    def updateUser(self,Id,user):
        self.UserArray[Id] = user
        
    def deleteVideo(self,Id):
        pass
    
    def deleteUser(self,Id):
        pass
        
    
    