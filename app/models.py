from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin","Admin"),
        ("user", "User"),
        ("mechanic", "Mechanic"),
        ("car_renter","Car Renter")
    ]
    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default="user")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    name=models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to="userprofile",default='static/images/profile/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.user.username


class MechanicProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mechanic_profile")
    name=models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="mechanic_location")
    phone = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    skills = models.TextField()
    experience = models.CharField(max_length=200)
    STATUS_CHOICES = [
        ("approved", "Approved"),
        ("pending", "Pending"),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="pending")
    SPECIALIZATION_CHOICES = [
        ("two_wheeler", "Two Wheeler"),
        ("four_wheeler", "Four Wheeler"),
        ("heavy_vehicle", "Heavy Vehicle"),
    ]
    specialized_in = models.CharField(max_length=200, choices=SPECIALIZATION_CHOICES)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="mech_pics",default='static/images/profile/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.user.username


class ReqToMechanic(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="req_profile")
    mechanic=models.ForeignKey(MechanicProfile,on_delete=models.CASCADE,related_name="req_profile")
    discription=models.CharField(max_length=200)
    phone=models.IntegerField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name="req_location")
    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("pending", "Pending"),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="pending")


class Bill(models.Model):
    customer=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    mechanic=models.ForeignKey(MechanicProfile,on_delete=models.CASCADE)
    req=models.ForeignKey(ReqToMechanic,on_delete=models.CASCADE)
    payment=models.PositiveBigIntegerField()
    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("pending", "Pending"),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="pending")


class FeedBack(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="feedback_userprofile")
    request=models.ForeignKey(ReqToMechanic,on_delete=models.CASCADE,related_name="feedback_req",null=True)
    mechanic=models.ForeignKey(MechanicProfile,on_delete=models.CASCADE,related_name="feedback_mechanicprofile")
    text=models.CharField(max_length=200)
    options=(
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )
    rating=models.CharField(max_length=200,choices=options,default="5")
    date=models.DateTimeField(auto_now_add=True)

class CarRenterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="carrental_profile")
    name=models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="pic_pics",default='static/images/profile/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.user.username

class RentCar(models.Model):
    owner=models.ForeignKey(CarRenterProfile,on_delete=models.CASCADE,related_name="carrental_profile")
    name=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    car_img=models.ImageField(upload_to="car_pics",default='static/images/car/default.jpg', blank=True, null=True)
    discription=models.CharField(max_length=200)
    STATUS_CHOICES = [
        ("available", "Available"),
        ("not_available", "Not Available"),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="available")
    def __str__(self):
        return self.name

class CarReserve(models.Model):
    customer=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    car=models.ForeignKey(RentCar,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    checked_out = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        ordering = ['-created_on']



