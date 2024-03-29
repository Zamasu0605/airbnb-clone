from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """Room Model Definition"""

    # participants = 참가자들
    # 한 개의 채팅방은 많은 참가자를 가진다.
    # 한 명의 참가자는 많은 채팅방에 가입할 수 있다.
    participants = models.ManyToManyField(
        "users.User",
        related_name="chattingrooms",
    )

    def __str__(self) -> str:
        return "Chatting Room"


class Message(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages",
    )

    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"
