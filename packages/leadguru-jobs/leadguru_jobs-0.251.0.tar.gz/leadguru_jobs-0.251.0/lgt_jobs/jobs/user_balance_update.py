import datetime
from typing import Optional

from lgt_data.engine import UserCreditStatementDocument
from lgt_data.enums import UserAccountState
from lgt_data.model import UserModel
from lgt_data.mongo_repository import UserMongoRepository, to_object_id
from pydantic import BaseModel

from ..basejobs import BaseBackgroundJobData, BaseBackgroundJob

"""
User balance handling
"""


class UpdateUserBalanceJobData(BaseBackgroundJobData, BaseModel):
    user_id: Optional[str]


class UpdateUserBalanceJob(BaseBackgroundJob):
    @property
    def job_data_type(self) -> type:
        return UpdateUserBalanceJobData

    @staticmethod
    def __update_processed(user: UserModel):
        pipeline = [
            {
                "$match": {
                    "user_id": to_object_id(user.id),
                    "balance": {"$lte": 0},
                    "action": {"$nin": ["admin-creds-added", "admin-creds-set"]}
                }
            },
            {
                '$group': {
                    '_id': "$user_id",
                    'count': {'$sum': {"$multiply": [-1, "$balance"]}}
                }
            }
        ]

        results = list(UserCreditStatementDocument.objects.aggregate(*pipeline))
        if not results:
            return

        count = results[0]["count"]
        if count >= user.leads_limit:
            # suspend account
            if user.state != UserAccountState.Suspended.value:
                UserMongoRepository().set(user.id, leads_proceeded=count,
                                          credits_exceeded_at=datetime.datetime.utcnow(),
                                          state=UserAccountState.Suspended.value)
                return

        if user.state == UserAccountState.Suspended.value:
            # unsuspend account
            UserMongoRepository().set(user.id, leads_proceeded=count,
                                      credits_exceeded_at=None,
                                      state=UserAccountState.Operational.value)
            return

        UserMongoRepository().set(user.id, leads_proceeded=count)

    def exec(self, data: UpdateUserBalanceJobData):
        user = UserMongoRepository().get(data.user_id)
        if not user:
            return

        self.__update_processed(user=user)
