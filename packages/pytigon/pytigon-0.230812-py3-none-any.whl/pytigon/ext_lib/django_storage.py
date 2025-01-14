import os

from django.conf import settings
from django.core.files.storage import Storage
from django.core.files import File

from fs.path import abspath, dirname
from fs.errors import ResourceNotFound as ResourceNotFoundError
from fs.error_tools import unwrap_errors


class FSStorage(Storage):
    def __init__(self, fs=None, base_url=None):
        if fs is None:
            fs = settings.DEFAULT_FILE_STORAGE_FS()
        self.fs = fs
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = ""

    def save(self, name, content, max_length=None):
        if name is None:
            name = content.name

        if not hasattr(content, "chunks"):
            content = File(content, name)
        name = self.get_available_name(name, max_length=max_length)
        name = self._save(name, content)
        return name

    def validate_file_name(name, allow_relative_path=True):
        return True

    def get_available_name(self, name, max_length=None):
        name = str(name).replace("\\", "/")
        dir_name, file_name = os.path.split(name)
        file_root, file_ext = os.path.splitext(file_name)
        while self.exists(name) or (max_length and len(name) > max_length):
            name = dir_name + "/" + self.get_alternative_name(file_root, file_ext)
            if max_length is None:
                continue
            truncation = len(name) - max_length
            if truncation > 0:
                file_root = file_root[:-truncation]
                name = dir_name + "/" + self.get_alternative_name(file_root, file_ext)
        return name

    def exists(self, name):
        return self.fs.isfile(name) or self.fs.isdir(name)

    def isdir(self, name):
        return self.fs.isdir(name)

    def listdir(self, name):
        x = list(self.fs.scandir(name))
        dirs = [pos.name for pos in x if pos.isdir]
        files = [pos.name for pos in x if not pos.isdir]
        return (dirs, files)

    def path(self, name):
        path = self.fs.getsyspath(name)
        if path is None:
            raise NotImplementedError
        return path

    def size(self, name):
        with unwrap_errors(name):
            size = self.fs.getsize(name)
        return size

    def url(self, name):
        with unwrap_errors(name):
            ret = self.base_url + abspath(name)[1:]
        return ret

    def _open(self, name, mode):
        with unwrap_errors(name):
            f = self.fs.open(name, mode)
        return File(f)

    def _save(self, name, content):
        with unwrap_errors(name):
            self.fs.makedirs(dirname(name), recreate=True)
            self.fs.setbinfile(name, content)
        return name

    def delete(self, name):
        with unwrap_errors(name):
            try:
                self.fs.remove(name)
            except ResourceNotFoundError:
                pass

    def get_accessed_time(self, name):
        info = self.fs.getinfo(name, namespaces=["details"])
        return info.accessed

    def get_created_time(self, name):
        info = self.fs.getinfo(name, namespaces=["details"])
        return info.created

    def get_modified_time(self, name):
        info = self.fs.getinfo(name, namespaces=["details"])
        return info.modified

    def generate_filename(self, filename):
        return "/" + filename


class StaticFSStorage(FSStorage):
    def __init__(self, fs=None, base_url=None):
        if fs is None:
            fs = settings.STATIC_FILE_STORAGE_FS()
        self.fs = fs
        super().__init__(fs, settings.STATIC_URL)

    def generate_filename(self, filename):
        return "/static/" + filename

    def url(self, *argi, **argv):
        ret = super().url(*argi, **argv)
        return ret


class MediaFSStorage(FSStorage):
    def __init__(self, fs=None, base_url=None):
        super().__init__(fs, settings.MEDIA_URL)

    def generate_filename(self, filename):
        return "/media/" + filename
