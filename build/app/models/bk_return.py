# #!/usr/bin/python3

# import enum

# from . issued import Issued
# from common.base import Base, myql_session
# from sqlalchemy import Column, DateTime, ForeignKey, Integer
# from sqlalchemy import Enum, Integer
# from sqlalchemy.orm import relationship, backref
# from sqlalchemy.sql import func


# class YesNoChoice(enum.Enum):
#     YES = 'Yes'
#     NO = 'No'

# class BK_Return(Base, object):
#     __tablename__ = 'bk_return'
#     return_id =  Column(Integer, primary_key = True)
#     issue_id = Column(Integer, ForeignKey('issued.issued_id'), nullable=False)
#     issued = relationship(Issued)
#     is_returned = Column(Enum(YesNoChoice, values_callable=lambda x: [str(return_choice.value) for return_choice in YesNoChoice]))
#     created_at = Column(DateTime(timezone=True), default=func.now())

#     def __init__(self, issued_id, isreturned='No'):
#         self.issue_id = issued_id
#         self.is_returned = isreturned

#     def __repr__(self):
#         return f"Is the book returned {self.is_returned}"
    
#     def create_bk_return(self):
#         bk_returned = BK_Return(self.issue_id, self.is_returned)
#         myql_session.add(bk_returned)
#         myql_session.commit()
#         myql_session.close()
