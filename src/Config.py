# 사용자의 input을 받으면서 설정을 진행한다.
import datetime

class Config():

    def __init__(self, title, image, summary, linefeed, days, noinfo):
        self.is_title_only_crawl = title
        self.is_image_crawl = image
        self.is_summary_crawl = summary
        self.is_lf = linefeed
        self.days = days
        self.noinfo =noinfo

    def get_days_list(self):
        days_list = []
        day = datetime.date.today()
        for i in range(0, self.days):
            day = day - datetime.timedelta(days=1)
            days_list.append(day.isoformat())
        return days_list
        # for debug
        # print(self.days_list)
        # print(type(self.days_list[1]))

    def get_config(self):
        setting= {'title': self.is_title_only_crawl,
                  'image': self.is_image_crawl,
                  'summary':self.is_summary_crawl,
                  'lf': self.is_lf,
                  'noinfo': self.noinfo}
        return setting





if __name__=="__main__":
    a = Config(1,2,3,4,5)
    print(a.get_config())

