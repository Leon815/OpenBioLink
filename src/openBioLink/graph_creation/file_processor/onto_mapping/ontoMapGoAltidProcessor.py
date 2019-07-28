from ...file_processor.fileProcessor import FileProcessor
from ...types.readerType import ReaderType
from ...types.infileType import InfileType
from ...metadata_infile.mapping.inMetaMapOntoGoAltid import InMetaMapOntoGoAltid



class OntoMapGoAltidProcessor(FileProcessor):
    IN_META_CLASS = InMetaMapOntoGoAltid

    def __init__(self):
        self.use_cols = self.IN_META_CLASS.USE_COLS
        super().__init__(self.use_cols, readerType=ReaderType.READER_ONTO_GO,
                         infileType=InfileType.IN_MAP_ONTO_GO_ALT_ID, mapping_sep=self.IN_META_CLASS.MAPPING_SEP)