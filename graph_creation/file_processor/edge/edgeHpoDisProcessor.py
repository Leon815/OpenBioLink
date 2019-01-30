from graph_creation.file_processor.fileProcessor import FileProcessor
from graph_creation.Types.readerType import ReaderType
from graph_creation.Types.infileType import InfileType
from graph_creation.metadata_infile.edge.inMetaEdgeHpoDis import InMetaEdgeHpoDis


class EdgeHpoDisProcessor(FileProcessor):

    def __init__(self):
        self.use_cols = InMetaEdgeHpoDis.USE_COLS
        super().__init__( self.use_cols, readerType=ReaderType.READER_EDGE_HPO_DIS,
                          infileType=InfileType.IN_EDGE_HPO_DIS, mapping_sep=InMetaEdgeHpoDis.MAPPING_SEP)