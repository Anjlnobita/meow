import json
import os

YOUTUBE = {
    "access_token": "ya29.a0ARW5m74cyvv5Z01VehfySSbSodSMQAePHXgTvXd0lPzzVlAxj_ezdHGpxGCd9El1knK1bFxEhLqS0JVLGKUmmOybMqzRVfcsRDG1K0fRhpl4hezRTc0TfPj9BlogRS4GqSnffrMlLWTixqFCXHhF3k7hLvKzXAYrLZ4HtCW1nMsDgyV9uO0uaCgYKAf4SARESFQHGX2Miuas8DiP6cuIRh_EPecHH2Q0187",
    "expires": 1736677423.241441,
    "refresh_token": "1//03XLKunT7JHVkCgYIARAAGAMSNwF-L9IrHGEA1Dl6BhwoSYJjJBJHvSMJW0W86U3wqlyFlUXxacXh6fR1-rUQfFp9NMDw1rqP2r8",
    "token_type": "Bearer"
}


def vipboy():
    TOKEN_DATA = os.getenv("TOKEN_DATA")
    if not TOKEN_DATA:
        os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
