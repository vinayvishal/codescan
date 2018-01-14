#!/usr/bin/python3

# Copyright

class Copyright(object):

    def __init__(self,statement,holder):
        self.statement = statement
        self.holder = holder

    def __eq__(self,other):
      if isinstance(other, self.__class__):
        return self.holder == other.holder
      return False

    def __ne__(self, other):
      if not isinstance(other, self.__class__):
        return True
      return self.holder != other.holder

    def __hash__(self):
        return hash(self.holder)

    def __str__(self):
        return "Copyright:" + self.statement + "\n" + \
               "Holder:" + self.holder

    def get_copyright_statement(self):
        return self.statement

    def get_copyright_holder(self):
        return self.holder

# License


class License(object):

    def __init__(self,spdx_license_key):
      self.spdx_license_key = spdx_license_key

    def __eq__(self, other):
      if isinstance(other,self.__class__):
        return self.spdx_license_key == other.spdx_license_key
      return False

    def __ne__(self, other):
      if not isinstance(other, self.__class__):
        return True
      return self.spdx_license_key != other.spdx_license_key

    def __hash__(self):
        return hash(self.spdx_license_key)

    def __str__(self):
        return "License:" + str(self.spdx_license_key)

    def get_license(self):
        return self.spdx_license_key

# FileMetadata


class FileMetadata(object):

    def __init__(self, copyright, license):
        self.copyright = copyright
        self.license = license

    def __eq__(self, other):
      if isinstance(other, self.__class__):
        return self.copyright == other.copyright and self.license == other.license
      return False

    def __ne__(self, other):
      if not isinstance(other, self.__class__):
        return True
      return self.copyright != other.copyright and self.license != other.license

    def __hash__(self):
        return hash(self.copyright) + hash(self.license)

    def __str__(self):
        return str(self.copyright) + "\n" + str(self.license)

    def get_copyright(self):
        return self.copyright

    def get_license(self):
        return self.license
