from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50, help_text="Item name")
    description = models.CharField(max_length=250, help_text="Full description of item")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    date_found = models.DateField(auto_now_add=True)
    claimed_status = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, through="ItemTag")

    def __str__(self):
        return self.name

class ItemTag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} - {self.tag.name}"
