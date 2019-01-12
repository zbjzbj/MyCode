import hashlib
from django.db import models


class UserInfo(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField("密码", max_length=64)
    uid = models.CharField(verbose_name='个人唯一ID',max_length=64, unique=True)
    wx_id = models.CharField(verbose_name="微信ID", max_length=128, blank=True, null=True, db_index=True)

    def save(self, *args, **kwargs):
        # 创建用户时，为用户自动生成个人唯一ID
        if not self.pk:
            m = hashlib.md5()
            m.update(self.username.encode(encoding="utf-8"))
            self.uid = m.hexdigest()
        super(UserInfo, self).save(*args, **kwargs)

"""
如果用户只是关注我的公众号不授权给我，
那么他可以看我的文章，我不能给他推送消息，
因此我们要诱导用户授权给我们，wx_id就是存用户授权后的wx账号id
"""

