from django.db import models


class Visit(models.Model):
    ip_address = models.IPAddressField()
    visit_time = models.DateTimeField(auto_now=True)

    def save(self, headers, *args, **kwargs):
        self.ip_address = self._get_client_ip(headers)
        super().save(*args, **kwargs)

    def _get_client_ip(self, headers):
        x_forwarded_for = headers.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else headers.get('REMOTE_ADDR')
        return ip
