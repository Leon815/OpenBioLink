from graph_creation import utils
from graph_creation.types.infileType import InfileType
from graph_creation.types.readerType import ReaderType
from graph_creation.file_processor.fileProcessor import FileProcessor
from graph_creation.metadata_infile import InMetaEdgeStringBinding


class EdgeStringBindingProcessor(FileProcessor):

    IN_META_CLASS = InMetaEdgeStringBinding

    def __init__(self):
        self.use_cols = self.IN_META_CLASS.USE_COLS
        super().__init__(self.use_cols, readerType=ReaderType.READER_EDGE_STRING_ACTION,
                         infileType=InfileType.IN_EDGE_STRING_BINDING, mapping_sep=self.IN_META_CLASS.MAPPING_SEP)


    def individual_preprocessing(self, data):
        #binding is an undirectional link --> take only the undirectional cases and only in one direction
        #data = data[data['action'].isnull()]
        data = data[data['mode'] == 'binding']
        data = data[data['is_directional']=='f']
        return data

    def individual_postprocessing(self, data):
        return utils.remove_bidir_edges_from_df(data)
