class MirrorListeners:
    def __init__(self, message):
        self.message = message
        self.uid = self.message.id


    def onDownloadStarted(self):
        raise NotImplementedError

    def onDownloadProgress(self):
        raise NotImplementedError
    
    def onDownloadComplete(self):
        raise NotImplementedError

    def onDownloadError(self, error: str):
        raise NotImplementedError

    def onUploadStarted(self):
        raise NotImplementedError

    def onUploadProgress(self):
        raise NotImplementedError

    def onUploadComplete(self, link: str):
        raise NotImplementedError

    def onUploadError(self, error: str):
        raise NotImplementedError