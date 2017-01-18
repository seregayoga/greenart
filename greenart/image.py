from typing import List
import datetime
from PIL import Image as PillowImage
from greenart import __version__


class Image:
    X = 52
    Y = 7

    """Image for drawing in github green panel"""
    def __init__(self, filename: str):
        image = PillowImage.open(filename)
        self.image = image.convert('L').resize((Image.X, Image.Y))

    def get_commands(self) -> List[str]:
        commands = [
            # clean history before drawing
            'git reset --hard {}'.format(__version__)
        ]
        days_ago = Image.__get_days_ago_when_was_first_sunday()
        for x in range(0, Image.X):
            for y in range(0, Image.Y):
                grey_color = self.image.getpixel((x, y))
                github_color = Image.__get_github_color_from_grey(grey_color)

                for index in range(0, github_color):
                    echo = 'echo {}{} > for_diff.txt'.format(days_ago, index)
                    add = 'git add for_diff.txt'
                    commit = self.__get_commit_from_past(days_ago)
                    commands.extend([echo, add, commit])
                days_ago -= 1

        commands.append('git push --force origin master')

        return commands

    @staticmethod
    def __get_days_ago_when_was_first_sunday() -> int:
        return 365 + datetime.datetime.now().weekday()

    @staticmethod
    def __get_commit_from_past(days_ago: int) -> str:
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=days_ago)
        past_date = now - delta
        return 'git commit -m "green art" --date "{}"'.format(past_date.isoformat())

    @staticmethod
    def __get_github_color_from_grey(grey_color: int) -> int:
        if 0 <= grey_color < 51:
            return 7
        if 51 <= grey_color < 102:
            return 5
        if 102 <= grey_color < 153:
            return 3
        if 153 <= grey_color < 204:
            return 1
        if 204 <= grey_color <= 255:
            return 0
