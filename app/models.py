from django.db import models

# ၁။ Project များကို သိမ်းဆည်းမည့် Model
class Project(models.Model):
    # Category ရွေးချယ်စရာများ
    CATEGORY_CHOICES = [
        ('web', 'Web Design'),
        ('php', 'PHP Projects'),
        ('python', 'Python Projects'),
        ('mobile', 'Mobile App'),
    ]

    title = models.CharField(max_length=200, verbose_name="ပရောဂျက်အမည်")
    description = models.TextField(verbose_name="အသေးစိတ်ဖော်ပြချက်")
    technology = models.CharField(max_length=200, verbose_name="အသုံးပြုထားသော နည်းပညာများ") # e.g. Django, React, MySQL
    image = models.ImageField(upload_to='project_images/', verbose_name="ပရောဂျက်ပုံ")
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='web',
        verbose_name="အမျိုးအစား"
    )
    github_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="GitHub လင့်ခ်")
    vercel_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Vercel လင့်ခ်")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ဖန်တီးသည့်ရက်စွဲ")

    # Admin Panel မှာ နာမည်အတိုင်း ပေါ်နေစေရန်
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at'] # အသစ်ဆုံးတင်တဲ့ project ကို အပေါ်ဆုံးကပြမယ်


# ၂။ Contact Form မှ Message များကို သိမ်းဆည်းမည့် Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="အမည်")
    email = models.EmailField(verbose_name="အီးမေးလ်")
    subject = models.CharField(max_length=200, verbose_name="အကြောင်းအရာ")
    message = models.TextField(verbose_name="ပေးပို့စာ")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="ပေးပို့သည့်အချိန်")

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"