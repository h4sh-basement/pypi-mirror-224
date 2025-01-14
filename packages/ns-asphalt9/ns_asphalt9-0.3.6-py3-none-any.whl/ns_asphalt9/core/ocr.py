import os
import re

import pytesseract
from PIL import Image, ImageFilter

from . import consts
from .page_factory import factory
from .screenshot import screenshot
from .utils.log import logger
from .utils.track_data import track_data


class LogManager:
    log_texts = None
    log_text_index = 0

    @classmethod
    def get_text(cls):
        if not cls.log_texts:
            cls.log_texts = []
            with open("logs/race.log") as file:
                lines = file.readlines()
            for line in lines:
                match = re.search(r"'text':\s*'(.*?)'", line)
                match1 = re.search(r"'text':\s*\"(.*?)\"", line)
                if match:
                    text = match.group(1)
                    cls.log_texts.append(text)
                elif match1:
                    text = match1.group(1)
                    cls.log_texts.append(text)
        text = cls.log_texts[cls.log_text_index]
        cls.log_text_index += 1
        return text


class OCR:
    filename = "output.jpg"
    ticket = -1

    @classmethod
    def get_text(cls):
        debug = os.environ.get("A9_DEBUG", 0)
        if debug:
            text = LogManager.get_text()
        else:
            text = cls._get_text(config="--psm 11", replace=True)
        return text

    @classmethod
    def get_page(cls):
        """获取匹配页面"""
        screenshot()
        text = cls.get_text()
        page = factory.create_page(text)
        logger.info(f"ocr page dict = {page.dict}")
        return page

    @classmethod
    def get_track(cls):
        """识别赛道"""
        text = cls._get_text(crop=(0, 0, 600, 300), replace=True)
        logger.info(f"ocr page map result = {text}")
        for track in track_data:
            if track["tracken"] in text:
                logger.info(f"Get track = {track}")
                return track

    @classmethod
    def get_progress(cls, image_path):
        """识别进度"""
        text = cls._get_text(
            crop=(150, 80, 400, 140), replace=True, image_path=image_path
        )
        pattern = r"\b\d{1,3}\b"
        match = re.search(pattern, text)
        if match:
            return int(match.group())
        return -1

    @classmethod
    def has_play(cls, mode):
        """是否有PLAY按钮"""
        if mode in [consts.car_hunt_zh, consts.legendary_hunt_zh]:
            crop = (1550, 900, 1675, 1080)
        else:
            crop = (1600, 900, 1750, 1080)
        text = cls._get_text(
            crop=crop,
            filter=ImageFilter.SHARPEN,
            convert="L",
            replace=True,
        )
        return "PLAY" in text

    @classmethod
    def has_next(cls, image_path=""):
        """是否有NEXT按钮"""
        text = cls._get_text(
            crop=(1460, 900, 1750, 1040),
            filter=ImageFilter.SHARPEN,
            replace=True,
            image_path=image_path,
        )
        return "NEXT" in text

    @classmethod
    def get_ticket(cls):
        """获取票数"""
        text = cls._get_text(
            crop=(1620, 250, 1755, 300),
            filter=ImageFilter.SHARPEN,
            convert="L",
            replace=True,
        )
        r = re.findall("(\d+)/10", text)
        if r:
            cls.ticket = int(r[0])
        else:
            cls.ticket = cls.ticket - 1
        return cls.ticket

    @classmethod
    def is_car_hunt(cls):
        """每日carhunt页面"""
        screenshot()
        text = cls._get_text(
            crop=(100, 280, 1000, 430),
            replace=True,
        )
        if re.findall("CAR HUNT(?!\sRIOT)", text):
            return True
        return False

    @classmethod
    def is_legendary_hunt(cls):
        screenshot()
        """每日lengedd hunt页面"""
        text = cls._get_text(
            crop=(100, 280, 1000, 430),
            replace=True,
            config=None
        )
        if re.findall("LEGENDARY HUNT(?!\sRIOT)", text):
            return True
        return False

    @classmethod
    def _get_text(
        cls,
        crop=None,
        filter=None,
        convert=None,
        replace=None,
        config="--dpi 72",
        image_path="",
    ):
        if not image_path:
            image_path = cls.filename
        img = Image.open(image_path)

        if crop:
            width, height = img.size
            if width != 1920:
                x_scale = width / 1920
                y_scale = height / 1080
                crop = (int(crop[0] * x_scale), int(crop[1] * y_scale),
                        int(crop[2] * x_scale), int(crop[3] * y_scale))
            img = img.crop(crop)
        if filter:
            img = img.filter(filter)
        if convert:
            img = img.convert(convert)
        text: str = pytesseract.image_to_string(img, lang="eng", config=config)
        img.close()
        if replace:
            text = text.replace("\n", " ")
        logger.info(f"Get text from page, text = {text}")
        return text


if __name__ == "__main__":
    OCR.get_text()
