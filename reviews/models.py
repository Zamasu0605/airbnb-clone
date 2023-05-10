from django.db import models
from common.models import CommonModel
from django.core.validators import MaxValueValidator


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    room = models.ForeignKey(
        # Review can sent room or experience.
        # 둘 중 하나만 가능하며 둘 다 보내는건 불가능하다.
        # Review가 Experience로 보내지면 Room은 NULL값이 되니 NULL = True로 하고
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        # Review는 하나의 Room을 가진다!
        # Room은 많은 Reviews를 가진다!
        related_name="reviews",
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    payload = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"
