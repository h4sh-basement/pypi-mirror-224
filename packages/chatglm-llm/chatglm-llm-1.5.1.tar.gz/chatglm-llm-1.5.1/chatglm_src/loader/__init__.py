from langchain.document_loaders.word_document import UnstructuredWordDocumentLoader
from langchain.document_loaders.pdf import PyPDFLoader
from langchain.document_loaders import DirectoryLoader, TextLoader


from langchain.text_splitter import CharacterTextSplitter
import re
from typing import List


class ChineseTextSplitter(CharacterTextSplitter):
    def __init__(self, pdf: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.pdf = pdf

    def split_text(self, text: str) -> List[str]:
        if self.pdf:
            text = re.sub(r"\n{3,}", "\n", text)
            text = re.sub('\s', ' ', text)
            text = text.replace("\n\n", "")
        sent_sep_pattern = re.compile('([﹒﹔﹖﹗．。！？]["’”」』]{0,2}|(?=["‘“「『]{1,2}|$))')  # del ：；
        sent_list = []
        for ele in sent_sep_pattern.split(text):
            if sent_sep_pattern.match(ele) and sent_list:
                sent_list[-1] += ele
            elif ele:
                sent_list.append(ele)
        return sent_list


def scan_docx(root):

    ds = DirectoryLoader(root, glob="**/*.docx", loader_cls=UnstructuredWordDocumentLoader)
    return ds.load_and_split(ChineseTextSplitter(pdf=False))

def scan_pdf(root):
    ds = DirectoryLoader(root, glob="**/*.pdf", loader_cls=PyPDFLoader, silent_errors=True)
    return ds.load_and_split(ChineseTextSplitter(pdf=True))