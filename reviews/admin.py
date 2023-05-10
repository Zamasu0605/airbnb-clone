from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by ratings!"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good(>3)"),
            ("bad", "Bad(<3)"),
            ("neutral", "Neutral(=3)"),
        ]

    def queryset(self, request, reviews):
        param = self.value()
        match = {
            "good": reviews.filter(rating__gt=3),
            "bad": reviews.filter(rating__lt=3),
            "neutral": reviews.filter(rating__exact=3),
        }
        return match.get(param, reviews)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
    )
