from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    distributor = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    retailPrice = models.DecimalField(max_digits=10, decimal_places=2)
    quantityLeft = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    entryDate = models.DateTimeField("Entry Date")
    nameOfTransaction = models.CharField(max_length=200)

    def __str__(self):
        return self.nameOfTransaction


class PurchasedItem(models.Model):
    date = models.DateField("Document Date")
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    documentNumber = models.PositiveIntegerField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    soldTo = models.CharField(max_length=100)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name+" "+str(self.quantity)


class ReturnedItem(models.Model):
    purchasedItem = models.ForeignKey(PurchasedItem, on_delete=models.PROTECT)
    dateReturned = models.DateField("Date Returned")
    remark = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name+" "+str(self.quantity)


class DefectiveItem(models.Model):
    date = models.DateTimeField("Entry Date")
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)

    def __str__(self):
        return self.item.name+" "+str(self.quantity)


class ImportedStocks(models.Model):
    date = models.DateField("Document Date")
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    documentNumber = models.PositiveIntegerField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name+" "+str(self.quantity)