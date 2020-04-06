from __future__ import unicode_literals
from datetime import date


class OurStory(object):
    IMAGE_SET_SIZE = 5
    TIMELINE_SIZE = 5

    def __init__(self):
        self._ourStoryInfo = {}
        self._defaultImageSet = []
        self._defaultTimelineSet = []

        self._initDefaultImageSet()
        self._initDefaultTimelineSet()
        self._initOurStoryInfo()

    @property
    def OurStorySet(self):
        return self._ourStoryInfo

    def _initDefaultImageSet(self):
        IMAGE_PATH = "/static/bigday/images/{imageName}.jpg"
        imgs = ["bikes-edited", "chapmans-peak-view", "lions-head-medium", "twelve-apostles", "wedding-selfie",
                "A", "A", "A", "A", "A",
                "A", "A", "A", "A", "A",
                "A", "A", "A", "A", "A",
                "A", "A", "A", "A", "A"]

        alts = ["A", "A", "A", "A", "A",
                "A", "A", "A", "A", "A",
                "A", "A", "A", "A", "A",
                "A", "A", "A", "A", "A",
                "A", "A", "A", "A", "A"]

        titles = ["A", "A", "A", "A", "A",
                  "A", "A", "A", "A", "A",
                  "A", "A", "A", "A", "A",
                  "A", "A", "A", "A", "A",
                  "A", "A", "A", "A", "A"]

        descriptions = ["A", "A", "A", "A", "A",
                        "A", "A", "A", "A", "A",
                        "A", "A", "A", "A", "A",
                        "A", "A", "A", "A", "A",
                        "A", "A", "A", "A", "A"]

        for row in range(0, self.TIMELINE_SIZE):
            startIndex = row if row == 0 else row * self.IMAGE_SET_SIZE
            for col in range(startIndex, startIndex + self.IMAGE_SET_SIZE):
                self._defaultImageSet.append({"selection": "item active" if col % self.IMAGE_SET_SIZE == 0 else "item",
                                              "img_url": IMAGE_PATH.format(imageName=imgs[col]),
                                              "alt": alts[col],
                                              "title": titles[col],
                                              "description": descriptions[col]})

    def _initDefaultTimelineSet(self):
        dateSet = ["2012-6-20",
                   "2014-7-21",
                   "2015-9-22",
                   "2017-10-23",
                   "2019-11-24"]

        event_title = ["sas",
                       "dasdad",
                       "asdcc",
                       "casfas",
                       "sfhhgdrhcvb"]

        for index in range(0, self.TIMELINE_SIZE):
            self._defaultTimelineSet.append({"date": dateSet[index],
                                             "event_title": event_title[index],
                                             "selection": True if index == 0 else False,
                                             "images_id": index})

    def _initOurStoryInfo(self):
        row = 0
        timelineSet = []
        timelineEventSet = []
        for timeline in self._defaultTimelineSet:
            dates = timeline.get("date").split("-")
            year = int(dates[0])
            month = int(dates[1])
            day = int(dates[2])
            timelineSet.append(Timeline(date=date(year, month, day),
                                        time=date(year, month, day),
                                        selection=timeline.get("selection")))
            imageInfoSet = []
            startPoint = row if row == 0 else row * self.IMAGE_SET_SIZE
            for img_index in range(startPoint, startPoint + self.IMAGE_SET_SIZE):
                imageInfoSet.append(ImageInfo(selection=self._defaultImageSet[img_index].get("selection"),
                                              img_url=self._defaultImageSet[img_index].get("img_url"),
                                              alt=self._defaultImageSet[img_index].get("alt"),
                                              title=self._defaultImageSet[img_index].get("title"),
                                              description=self._defaultImageSet[img_index].get("description")))

            timelineEventSet.append(TimelineEvent(event_title=timeline.get("event_title"),
                                                  event_date=date(year, month, day),
                                                  image_info_set=imageInfoSet))
            row += 1

        self._ourStoryInfo.setdefault("timelineSet", timelineSet)
        self._ourStoryInfo.setdefault("timelineEventSet", timelineEventSet)

        # Create your models here.


class Timeline(object):
    def __init__(self, date: date, time: date, selection: bool):
        self.date = date.strftime("%d/%m/%Y")
        self.time = time.strftime("%d %b")
        self.selection = selection


class TimelineEvent(object):
    def __init__(self, event_title: str, event_date: date, image_info_set: list):
        self.event_title = event_title
        self.event_date = event_date.isoformat()
        self.imageInfoS = image_info_set


class ImageInfo(object):
    def __init__(self, selection: bool, img_url: str, alt: str, title: str, description: str):
        self.selection = selection
        self.img_url = img_url
        self.alt = alt
        self.title = title
        self.description = description


if __name__ == '__main__':
    ourStory = OurStory()
    print(ourStory.OurStorySet)
