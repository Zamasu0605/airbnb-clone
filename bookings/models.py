from django.db import models
from common.models import CommonModel


class Booking(CommonModel):
    """Booking Model Definition"""

    # one booking model for experiences or rooms
    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )

    # user는 많은 예약을 가지지만, 많은 예약은 하나의 user를 가진다.
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bookings",
    )

    # booking은 하나의 room을 가지고, room은 다수의 bookings를 가질 수 있다.
    room = models.ForeignKey(
        "rooms.Room",
        # Experiences or Rooms 에 따라 각 NULL이 될 수도 있으니
        null=True,
        # blank는 장고 어드민 폼을 위한 것이다.
        # 반드시 채울 필요가 없도록 해준다.
        blank=True,
        # room이 지워져도, 예약을 지우는 건 좀 그렇다.
        # 그리고, 예약 내역을 기록해두고 싶을 지도 모르니.
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

    # Room have check_in and check_out. but experience isn't
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )

    # This is for experience.
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    guests = models.PositiveIntegerField()

    # title is method.
    def __str__(self) -> str:
        return f"{self.kind.title()} booking for : {self.user}"
