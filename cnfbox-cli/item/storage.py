import item.base


class Storage(item.base.Base):
    __BOOTLOADER_LIST: tuple = ('none', 'mbr', 'uefi', 'kernel')

    def __init__(
            self,
            bootloader: str = 'mbr',
            auto_partition: bool = True,
            clear_partition: bool = False):
        assert bootloader in self.__BOOTLOADER_LIST, "Invalid Bootloader Location given."
        self.bootloader = bootloader
        self.auto_partition = auto_partition
        self.clear_partition = clear_partition

    def __repr__(self):
        return super().__repr__()
