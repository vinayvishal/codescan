#!/usr/bin/python3

from configparser import ConfigParser


class ScancodeToolkitConfig:

  @staticmethod
  def get_path():
    config = ConfigParser()
    config.read("codescan.ini")
    return str(config['CODESCAN_TOOLKIT']['PATH'])

  @staticmethod
  def get_version():
    config = ConfigParser()
    config.read("codescan.ini")
    return str(config['CODESCAN_TOOLKIT']['VERSION'])


class CopyrightPluginConfig:

  @staticmethod
  def get_path():
    config = ConfigParser()
    config.read("codescan.ini")
    return str(config['COPYRIGHT_PLUGIN']['PATH'])

  @staticmethod
  def get_version():
    config = ConfigParser()
    config.read("codescan.ini")
    return str(config['COPYRIGHT_PLUGIN']['VERSION'])


class TargetRepoConfig:

  @staticmethod
  def get_path():
    config = ConfigParser()
    config.read("codescan.ini")
    return str(config['TARGET_REPO']['PATH'])

  @staticmethod
  def get_repo():
    config = ConfigParser()
    config.read("codescan.ini")
    return str(config['TARGET_REPO']['REPO'])

  @staticmethod
  def get_repo_name():
    config = ConfigParser()
    config.read("codescan.ini")
    return str(config['TARGET_REPO']['PATH']).split("/")[-1]
