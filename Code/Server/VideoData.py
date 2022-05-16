"""class to represent video
attributes:
    Id,Embedding,Tags

"""

class VideoData:
    def __init__(self,Id,Embedding,Tags) -> None:
        self.Id = Id
        self.Embedding = Embedding
        self.Tags = Tags