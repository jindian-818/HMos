from django.db import models


class Evaluate(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    parent_phone = models.CharField(max_length=25, blank=True, null=True)
    teacher_phone = models.CharField(max_length=25, blank=True, null=True)
    subject = models.CharField(max_length=25, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    time_info = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate'


class ParMoney(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    parent_phone = models.CharField(max_length=25, blank=True, null=True)
    account_money = models.CharField(max_length=25, blank=True, null=True)
    balance = models.CharField(max_length=25, blank=True, null=True)
    points = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'par_money'


class ParOrder(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    parent_phone = models.CharField(max_length=25, blank=True, null=True)
    book_name = models.CharField(max_length=25, blank=True, null=True)
    quantity = models.CharField(max_length=25, blank=True, null=True)
    price = models.CharField(max_length=25, blank=True, null=True)
    is_received = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'par_order'


class ParReward(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    parent_phone = models.CharField(max_length=25, blank=True, null=True)
    voucher_value = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'par_reward'


class Parent(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    address_info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parent'


class Plant(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    parent_phone = models.CharField(max_length=25, blank=True, null=True)
    plan_content = models.CharField(max_length=255, blank=True, null=True)
    plan_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plant'


class Reserve(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    parent_phone = models.CharField(max_length=25, blank=True, null=True)
    teacher_phone = models.CharField(max_length=25, blank=True, null=True)
    teacher_name = models.CharField(max_length=25, blank=True, null=True)
    subject = models.CharField(max_length=25, blank=True, null=True)
    reserve_time = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserve'


class Teacher(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    teaching_experience = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'