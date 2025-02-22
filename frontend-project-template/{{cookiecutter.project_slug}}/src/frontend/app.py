from argparse import ArgumentParser
from common.logger import setup_logger
from common.yaml_parser import ConfigParser
import streamlit as st
from frontend.components.sidebar import SideBar
from frontend.misc.page_config import set_page_config
import common.config as config


def run(config_file: str):
    logger = setup_logger()

    if config.config is None:
        logger.info("Parsing app config")
        config_parser = ConfigParser(file_path=config_file)
        config.config = config_parser.parse()

    set_page_config()
    side_bar = SideBar()
    side_bar.render()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--config-file", type=str, default="./config/main.yaml")
    args = parser.parse_args()
    run(config_file=args.config_file)
