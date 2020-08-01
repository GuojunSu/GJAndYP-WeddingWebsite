class ImageInfo(object):
    def __init__(self, selection: bool, img_url: str, description: str):
        self.selection = selection
        self.img_url = img_url
        self.description = description

    def ToDict(self):
        return {
            "selection": self.selection,
            "url": self.img_url,
            "des": self.description
        }


class OurStory(object):
    _ourStoryInfo = None
    _instance = None
    _events = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._events = ["College", "JapanTour", "Honeymoon", "PreWeddingPhoto"]
            cls._instance._ourStoryInfo = {}
        return cls._instance

    def __init__(self):
        self._ourStoryInfo.setdefault("Events", self._events)
        for event in self._events:
            self._ourStoryInfo.setdefault(event, self.init_event_images(period=event))

    def __del__(self):
        del self._ourStoryInfo

    @property
    def StoryEvents(self):
        return self._ourStoryInfo

    @staticmethod
    def create_images(image_info_list: list) -> list:
        images = []
        for index, imgInfo in enumerate(image_info_list):
            name, des = imgInfo
            images.append(ImageInfo(selection=True if index == 0 else False,
                                    img_url=f"/static/bigday/images/{name}.jpg",
                                    description=des).ToDict())
        return images

    @staticmethod
    def init_event_images(period: str = "College"):
        return {"College": OurStory.create_images([("bikes-edited", "sss"),
                                                   ("bikes-edited", "sa"),
                                                   ("bikes-edited", "sa"),
                                                   ("bikes-edited", "dd"),
                                                   ("bikes-edited", "dd")]),

                "JapanTour": OurStory.create_images([("chapmans-peak-view", "hsdhk"),
                                                     ("chapmans-peak-view", "fdfs"),
                                                     ("chapmans-peak-view", "fsdf"),
                                                     ("chapmans-peak-view", "seee"),
                                                     ("chapmans-peak-view", "ssdf")]),

                "Honeymoon": OurStory.create_images([("prince-of-wales-hotel-nav", "dfs "),
                                                     ("prince-of-wales-hotel-nav", "ff"),
                                                     ("prince-of-wales-hotel-nav", "dsfsd"),
                                                     ("prince-of-wales-hotel-nav", "xcvxv"),
                                                     ("prince-of-wales-hotel-nav", "vsdgh")]),

                "PreWeddingPhoto": OurStory.create_images([("wedding-selfie", "wcsd"),
                                                           ("wedding-selfie", "wefew"),
                                                           ("wedding-selfie", "2ddc "),
                                                           ("wedding-selfie", "42fff"),
                                                           ("wedding-selfie", "dsvv")])}[period]


# if __name__ == '__main__':
#     import sys
#     ourStory = OurStory()
#     print(ourStory.StoryEvents)
#     print(f"{sys.getsizeof(ourStory.StoryEvents)} bytes")
#     print(id(ourStory.StoryEvents))
