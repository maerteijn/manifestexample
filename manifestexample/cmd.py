class ManifestCommmand(object):
    def __call__(self, *args, **kwargs):
        print(
            "I'm an example command to show MANIFEST.in is not always "
            "excluding files"
        )


command = ManifestCommmand()
