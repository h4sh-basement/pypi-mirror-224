import abc
from enum import Enum
from typing import List, Optional

class QueryOperator(Enum):
    AND = "AND"
    OR = "OR"

class DefType(abc.ABC):
    pass

class LuceneQueryBuilder(DefType):
    q_op: Optional[QueryOperator]
    df: Optional[str]
    sow: Optional[bool]

    """
    Create a Lucene query builder.
    
    :param q_op: Query operator.
    :param df: Default field
    :param sow: Split on whitespace
    """
    def __init__(
        self,
        q_op: Optional[QueryOperator] = None,
        df: Optional[str] = None,
        sow: Optional[bool] = None,
    ):
        pass

class DismaxQueryBuilder(DefType):
    q_alt: Optional[str]
    qf: Optional[str]
    mm: Optional[str]
    pf: Optional[str]
    ps: Optional[str]
    qs: Optional[str]
    tie: Optional[str]
    bq: Optional[List[str]]
    bf: Optional[List[str]]

    """
    Create a DisMax query builder.
    
    :param q_alt: Alternate query
    :param qf: Query fields
    :param mm: Minimum match
    :param pf: Phrase fields
    :param ps: Phrase slop
    :param qs: Query slop
    :param tie: Tie breaker
    :param bq: Boost query
    :param bf: Boost functions
    """
    def __init__(
        self,
        q_alt: Optional[str] = None,
        qf: Optional[str] = None,
        mm: Optional[str] = None,
        pf: Optional[str] = None,
        ps: Optional[str] = None,
        qs: Optional[str] = None,
        tie: Optional[str] = None,
        bq: Optional[List[str]] = None,
        bf: Optional[List[str]] = None,
    ):
        pass

class EdismaxQueryBuilder(DefType):
    q_alt: Optional[str]
    qf: Optional[str]
    mm: Optional[str]
    mm_auto_relax: Optional[bool]
    pf: Optional[str]
    pf2: Optional[str]
    pf3: Optional[str]
    ps: Optional[str]
    ps2: Optional[str]
    ps3: Optional[str]
    qs: Optional[str]
    tie: Optional[str]
    bq: Optional[List[str]]
    bf: Optional[List[str]]
    sow: Optional[bool]
    boost: Optional[List[str]]
    lowercase_operators: Optional[bool]
    stopwords: Optional[bool]
    uf: Optional[str]

    """
    Create an Edismax query builder.
    
    :param q_alt: Alternate query
    :param qf: Query fields
    :param mm: Minimum match
    :param mm_auto_relax: Automatically relax mm
    :param pf: Phrase fields
    :param pf2: Phrase fields 2
    :param pf3: Phrase fields 3
    :param ps: Phrase slop
    :param ps2: Phrase slop 2
    :param ps3: Phrase slop 3
    :param qs: Query slop
    :param tie: Tie breaker
    :param bq: Boost query
    :param bf: Boost functions
    :param sow: Split on whitespace
    :param boost: Boost
    :param lowercase_operators: Lowercase operators
    :param stopwords: Stopwords
    :param uf: User fields
    """
    def __init__(
        self,
        q_alt: Optional[str] = None,
        qf: Optional[str] = None,
        mm: Optional[str] = None,
        mm_auto_relax: Optional[bool] = None,
        pf: Optional[str] = None,
        pf2: Optional[str] = None,
        pf3: Optional[str] = None,
        ps: Optional[str] = None,
        ps2: Optional[str] = None,
        ps3: Optional[str] = None,
        qs: Optional[str] = None,
        tie: Optional[str] = None,
        bq: Optional[List[str]] = None,
        bf: Optional[List[str]] = None,
        sow: Optional[bool] = None,
        boost: Optional[List[str]] = None,
        lowercase_operators: Optional[bool] = None,
        stopwords: Optional[bool] = None,
        uf: Optional[str] = None,
    ):
        pass
